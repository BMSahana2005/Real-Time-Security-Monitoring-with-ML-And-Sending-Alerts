import os

def capture_faces():
    os.system("python Caturing Dataset.py") 

def train_faces():
    os.system("python Train.py")  

def detect_and_alert():
    os.system("python Notifying.py")

def main_menu():
    while True:
        print("\n====== DETECTING STRANGER AND SENDING SMS - SNAPSHOT THROUGH MAIL  ======")
        print("1. Capture New Faces")
        print("2. Train Captured Faces")
        print("3. Start Real-Time Detection & Alerting")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            capture_faces()
        elif choice == '2':
            train_faces()
        elif choice == '3':
            detect_and_alert()
        elif choice == '4':
            print("Exiting App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
