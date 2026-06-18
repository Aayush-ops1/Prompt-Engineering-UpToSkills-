import cv2
from datetime import datetime

from face_detector import FaceDetector
from phone_detector import PhoneDetector
from rules_engine import RulesEngine
from logger import EventLogger


# Initialize Components
detector = FaceDetector()
phone_detector = PhoneDetector()
rules = RulesEngine()
logger = EventLogger()

# Start Webcam
cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    if not success:
        break

    # Detect Faces
    face_count = detector.detect_faces(frame)

    # Detect Phone
    phone_detected, phone_box = phone_detector.detect_phone(frame)

    # Draw Phone Bounding Box
    if phone_detected and phone_box is not None:

        x1, y1, x2, y2 = phone_box

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 0, 255),
            2
        )

        cv2.putText(
            frame,
            "PHONE",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2
        )

    # Apply Rules
    suspicious, reason = rules.check_rules(
        face_count,
        phone_detected
    )

    # Show Face Count
    cv2.putText(
        frame,
        f"Faces: {face_count}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Suspicious Activity Handling
    if suspicious:

        # Log Event
        logger.log_event(reason)

        # JSON Output
        output = {
            "suspicious": True,
            "reason": reason
        }

        print(output)

        # Save Evidence Screenshot
        filename = (
            "evidence/"
            + datetime.now().strftime("%Y%m%d_%H%M%S")
            + ".jpg"
        )

        cv2.imwrite(
            filename,
            frame
        )

        # Display Warning
        cv2.putText(
            frame,
            "SUSPICIOUS ACTIVITY",
            (20, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            3
        )

        cv2.putText(
            frame,
            reason,
            (20, 150),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2
        )

    # Show Video Feed
    cv2.imshow(
        "Rule Based Suspicious Activity Detector",
        frame
    )

    # Press Q to Exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()