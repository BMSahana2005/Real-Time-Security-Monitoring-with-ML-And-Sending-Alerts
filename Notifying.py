import face_recognition
import cv2
import pickle
from twilio.rest import Client
import os
import time
import yagmail
import threading
from datetime import datetime

# === Load Trained Encodings ===
known_faces_dir = "known_faces"
with open(os.path.join(known_faces_dir, "known_faces.pkl"), "rb") as f:
    known_encodings, known_labels = pickle.load(f)

# === Twilio Setup ===
twilio_sid = "<Enter Your Twilio Sid>""
twilio_auth_token = "<Enter Twilio Authorization Token>"
twilio_from_number = "<Twilio Alloted Mobile Number>"
admin_to_number = "<Admin Mobile Number>"
twilio_client = Client(twilio_sid, twilio_auth_token)

# === Email Setup ===
sender_email = "<Sender's Email ID (FROM)>"
app_password = "Enter App Password"
receiver_email = "<Admin's (Receiver) Email ID (TO)>"

# === Function to send email asynchronously ===
def send_email_in_background(snapshot_path):
    yag = yagmail.SMTP(sender_email, app_password)
    yag.send(
        to=receiver_email,
        subject="Unknown Person Detected",
        contents="An unknown person was detected by the camera. Snapshot attached.",
        attachments=snapshot_path
    )
    print("Email sent!")

# === Live Camera Detection ===
video = cv2.VideoCapture(0)
unknown_alerted = False  # Ensure email is sent only once
email_sent = False  # Flag to check if email has been sent

print("Scanning for unknown faces. Press 'q' to quit.")
while True:
    ret, frame = video.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for encoding, location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_encodings, encoding, tolerance=0.5)

        if True not in matches and not unknown_alerted and not email_sent:
            print("Unknown face detected! Sending alerts...")

            # Draw Red Box around the face
            top, right, bottom, left = location
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)  # Red box

            # Label as "Unknown"
            label = "Unknown"
            cv2.putText(frame, label, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

            # Save snapshot with the red box and label
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            snapshot_path = f"unknown_{timestamp}.jpg"
            cv2.imwrite(snapshot_path, frame)

            # Send SMS
            twilio_client.messages.create(
                body="Unknown face detected on camera!",
                from_=twilio_from_number,
                to=admin_to_number
            )

            # Send Email in background
            email_thread = threading.Thread(target=send_email_in_background, args=(snapshot_path,))
            email_thread.start()

            unknown_alerted = True  # Set this to prevent further SMS
            email_sent = True  # Email is now sent, avoid sending again
            time.sleep(2)

        # Draw rectangle and label for known faces as well (optional)
        top, right, bottom, left = location
        label = "Unknown" if True not in matches else "Known"
        color = (0, 0, 255) if label == "Unknown" else (0, 255, 0)
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(frame, label, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    cv2.imshow("Live Camera - Press 'q' to quit", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
