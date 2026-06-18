import time

class RulesEngine:

    def __init__(self):

        self.face_missing_start = None

        self.face_missing_threshold = 10

        self.last_alert_time = 0

        self.cooldown = 5

    def can_alert(self):

        current_time = time.time()

        if (
            current_time
            - self.last_alert_time
            > self.cooldown
        ):

            self.last_alert_time = current_time

            return True

        return False

    def check_rules(
        self,
        face_count,
        phone_detected
    ):

        # ----------------
        # PHONE RULE
        # ----------------

        if phone_detected:

            if self.can_alert():

                return True, "Phone Detected"

        # ----------------
        # MULTIPLE PERSONS
        # ----------------

        if face_count > 1:

            if self.can_alert():

                return True, (
                    "Multiple Persons Detected"
                )

        # ----------------
        # FACE MISSING
        # ----------------

        current_time = time.time()

        if face_count > 0:

            self.face_missing_start = None

        else:

            if self.face_missing_start is None:

                self.face_missing_start = current_time

            elapsed = (
                current_time
                - self.face_missing_start
            )

            if elapsed > self.face_missing_threshold:

                if self.can_alert():

                    return True, (
                        "Face Missing >10 Seconds"
                    )

        return False, "None"