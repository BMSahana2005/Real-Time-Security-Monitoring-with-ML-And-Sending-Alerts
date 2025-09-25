# Real-Time-Security-Monitoring-with-ML-And-Sending-Alerts
AlertCam is a smart security solution that uses machine learning and facial recognition to provide real-time security monitoring and automated threat detection. Upon detecting an unauthorized individual, the system immediately sends alerts via SMS and email to ensure a swift response.

**AlertCam: Real-Time Security Monitoring with ML and Sending Alerts**

AlertCam is a smart, real-time security monitoring solution that leverages machine learning to provide automated threat detection. It is designed to be a scalable and efficient system suitable for various environments like campuses, homes, and workplaces, enhancing safety through intelligent decision-making and automation.


**Key Features**

--Real-Time Monitoring: Integrates with existing CCTV infrastructure to continuously process live video feeds for face detection and identification.

--Custom ML Model: The system's core is a custom-trained machine learning model, built from scratch to ensure transparency, customizability, and educational value.

--Automated Alerting: Upon detecting an unknown or unauthorized face, the system instantly triggers automated alerts via SMS using the Twilio API and sends a snapshot of the intruder to a designated email address.

--Robust Performance: The model's effectiveness has been validated with strong performance metrics, including an accuracy of 85.0%, a precision of 83.3%, and a recall of 71.4%.

--Scalable and Adaptable: Its modular architecture allows for future expansion, such as integration with more sophisticated deep learning models and cloud-based analytics for enhanced capabilities.

**How It Works**

--Data Capture: The system captures live video streams from a camera feed.

--Preprocessing: The video frames undergo an initial cleaning process using libraries like OpenCV and NumPy.

--Facial Recognition: A custom-trained machine learning model compares faces detected in the live feed against a secure database of authorized individuals.

--Threat Detection: If an unknown face is detected, the system classifies it as an unauthorized individual.

--Alert System: An immediate alert is sent to administrators via SMS and email, including a captured snapshot of the intruder.

**Project Structure**
AlertCam/
├── Caturing Dataset.py     # Script for capturing and enrolling new authorized faces
├── Train.py                # Script for training the ML model with new data
├── Notifying.py            # Main script for real-time scanning and alerting
├── known_faces/            # Directory to store the dataset of known faces
    └── known_faces.pkl     # Serialized data of facial embeddings
├── Main.py                 # Integrating all code


**Note: You will need to configure your Twilio API credentials and email service settings within the project files to enable the alert functionality.**

**Results and Performance**

The system's performance metrics highlight its practical utility and reliability in enhancing security monitoring.


