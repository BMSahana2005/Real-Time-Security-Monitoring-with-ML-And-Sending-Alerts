import face_recognition
import os
import pickle

frame_folder = "captured_sessions"
known_faces_dir = "known_faces"
os.makedirs(known_faces_dir, exist_ok=True)

pkl_path = os.path.join(known_faces_dir, "known_faces.pkl")

# Load previously saved encodings if available
if os.path.exists(pkl_path):
    with open(pkl_path, "rb") as f:
        known_face_encodings, known_face_names = pickle.load(f)
    print(f"Loaded {len(known_face_names)} previously known faces.")
else:
    known_face_encodings = []
    known_face_names = []

# Keep track of already trained names
already_trained_names = set(known_face_names)

total_frames = 0
rejected_frames = 0
new_faces_trained = 0

# Traverse each person's folder
for person_name in os.listdir(frame_folder):
    person_path = os.path.join(frame_folder, person_name)
    if not os.path.isdir(person_path):
        continue

    if person_name in already_trained_names:
        print(f"Skipping {person_name} (already trained).")
        continue

    print(f"Training new person: {person_name}")

    for frame_file in os.listdir(person_path):
        if frame_file.endswith(".jpg"):
            total_frames += 1
            image_path = os.path.join(person_path, frame_file)
            image = face_recognition.load_image_file(image_path)
            face_locations = face_recognition.face_locations(image)
            face_encodings = face_recognition.face_encodings(image, face_locations)

            if not face_encodings:
                rejected_frames += 1
            else:
                for encoding in face_encodings:
                    known_face_encodings.append(encoding)
                    known_face_names.append(person_name)
                    new_faces_trained += 1

# Save updated encodings
with open(pkl_path, "wb") as f:
    pickle.dump((known_face_encodings, known_face_names), f)

print("\nTraining complete and updated data saved.")
print(f"Total frames processed: {total_frames}")
print(f"Frames rejected (no face found): {rejected_frames}")
print(f"Frames accepted: {total_frames - rejected_frames}")
print(f"New faces trained: {new_faces_trained}")
