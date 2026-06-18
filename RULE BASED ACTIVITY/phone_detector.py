from ultralytics import YOLO

class PhoneDetector:

    def __init__(self):

        self.model = YOLO("yolov8n.pt")

        self.phone_class_id = 67

    def detect_phone(self, frame):

        results = self.model(frame, verbose=False)

        phone_found = False

        for result in results:

            boxes = result.boxes

            for box in boxes:

                class_id = int(box.cls[0])

                if class_id == self.phone_class_id:

                    phone_found = True

                    x1, y1, x2, y2 = map(
                        int,
                        box.xyxy[0]
                    )

                    return phone_found, (
                        x1, y1, x2, y2
                    )

        return False, None