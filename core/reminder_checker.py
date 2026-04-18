from PySide6.QtCore import QThread, Signal
import time

from services.reminder_service import ReminderService

try:
    from plyer import notification
except Exception:
    notification = None


class ReminderChecker(QThread):
    reminder_due = Signal(str)

    def __init__(self):
        super().__init__()
        self.running = True
        self.reminder_service = ReminderService()

    def run(self):
        while self.running:
            due = self.reminder_service.get_due_reminders()

            for reminder_id, content, remind_at, recurring in due:
                if recurring == "daily":
                    self.reminder_service.reschedule_daily(reminder_id, remind_at)
                else:
                    self.reminder_service.mark_triggered(reminder_id)

                self.reminder_due.emit(content)

                if notification:
                    try:
                        notification.notify(
                            title="VoxAssist Reminder",
                            message=content,
                            timeout=5
                        )
                    except Exception:
                        pass

            time.sleep(2)

    def stop(self):
        self.running = False
