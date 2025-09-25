import cv2
import os
import time

base_dir = "captured_sessions"
os.makedirs(base_dir, exist_ok=True)
frames_per_second = 3
delay = 1 / frames_per_second

print("Face Capture Program")

while True:
    # Get user input for person's name
    person_name = input("\nEnter the name of the known person: ").strip()
    if not person_name:
        print("Name cannot be empty. Try again.")
        continue

    # Ensure unique folder by checking existing sessions with the same name
    existing_sessions = [d for d in os.listdir(base_dir) if d.startswith(person_name)]
    session_folder_name = f"{person_name}"
    session_folder = os.path.join(base_dir, session_folder_name)
    os.makedirs(session_folder, exist_ok=True)

    # Start capturing
    video_capture = cv2.VideoCapture(0)
    if not video_capture.isOpened():
        print("Error: Could not access the camera.")
        break

    frame_count = 0
    print(f"\nStarting capture for: {session_folder_name}")
    print("Capturing at 3 FPS. Press 'q' in the video window to stop...")

    while True:
        start_time = time.time()
        ret, frame = video_capture.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        filename = os.path.join(session_folder, f"frame_{frame_count + 1}.jpg")
        cv2.imwrite(filename, gray)
        frame_count += 1

        cv2.imshow(f"Capturing {session_folder_name}", gray)

        # Wait and check for key press
        if cv2.waitKey(10) & 0xFF == ord('q'):
            print("Detected 'q' key press. Stopping capture...")
            break

        elapsed_time = time.time() - start_time
        if elapsed_time < delay:
            time.sleep(delay - elapsed_time)

    video_capture.release()
    cv2.destroyAllWindows()

    print(f"Capture for {session_folder_name} completed with {frame_count} frames.")

    another = input("Do you want to capture another person? (y/n): ").strip().lower()
    if another != 'y':
        print("Exiting program.")
        break
