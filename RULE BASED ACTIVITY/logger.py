from datetime import datetime


class EventLogger:

    def log_event(self, reason):

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        with open(
            "suspicious_log.txt",
            "a"
        ) as file:

            file.write(
                f"[{timestamp}] {reason}\n"
            )