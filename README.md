Project Overview

This project is a motion detection and alert system built using Python and OpenCV. The application captures images from a webcam, identifies any significant movement, and sends an email alert with an attached image of the moving object. This project could be used for security purposes, such as detecting intruders or monitoring spaces for unusual activity.


Directory Structure

WebcamAlertApp/

│

├── images/

│   ├── *.png  # Directory to store captured images

│

├── emailing.py  # Script to handle email notifications

└── main.py  # Main script to handle motion detection and webcam functionality


How It Works

Motion Detection: The app uses OpenCV to capture video from the webcam and processes each frame to detect significant movement. When movement is detected, an image is saved and used for email alerts.

Email Alert: When a moving object is detected, the app sends an email with the image attached using Python's smtplib library.

Folder Cleaning: Images saved during motion detection are periodically cleaned to manage storage.


Code Breakdown

Imports

cv2: OpenCV library for real-time computer vision.

time: To introduce delays when necessary.

glob: For file pattern matching (used to collect images).

os: To handle file removal operations.

Thread: From the threading library, used to run the email and folder-cleaning functions asynchronously.
smtplib, imghdr, EmailMessage: Used in emailing.py to send email notifications with image attachments.


Functionality

1. Motion Detection (main.py)

Captures frames from the webcam and converts them to grayscale.
Applies Gaussian blur to reduce noise and smooth the image.
Calculates the difference between the first frame and the current frame to detect motion.
Highlights significant movements using contour detection and stores images for alert purposes.

2. Email Notification (emailing.py)

Configures and sends an email with an image attachment.
Uses smtplib for connecting to the Gmail SMTP server.
The email subject humorously warns the user of "village people" intruders.

3. Cleaning Captured Images (main.py)

Removes images from the images folder periodically to manage storage space.


Common Errors & Solutions

1. Incorrect Attribute Name:

Error: AttributeError: module 'cv2' has no attribute 'waitkey'.

Solution: Use cv2.waitKey(1) instead of cv2.waitkey(1).

2. Incorrect Argument Spelling:

Error: Misspelled function arguments, e.g., targer instead of target.

Solution: Correct spelling to target in Thread initialization.

3. Object Detection Sensitivity:

To ensure the app only detects moving objects and not everything in the frame:

Adjust Contour Area Threshold: Use a more refined threshold to ignore small movements or background noise (e.g., if cv2.contourArea(contour) < 5000).

Update Background Frame: Periodically update first_frame to adjust to background changes over time.

Use Adaptive Thresholding: This method may help if the lighting conditions in the environment vary.


Future Improvements
1. Implement a more secure method for handling email credentials.
2. Optimize the image saving and cleaning mechanism.
3. Explore more advanced motion detection techniques for better accuracy.


Contact
For any questions or suggestions, feel free to not reach out or contribute to the project!
IM JUST JOKING, please by all means reach out and contribute!!!
