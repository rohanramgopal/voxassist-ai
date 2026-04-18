from datetime import datetime, timedelta
from services.db_service import DatabaseService


class ReminderService:
    def __init__(self):
        self.db = DatabaseService()

    def add_reminder_in_minutes(self, text: str, minutes: int = 1) -> str:
        remind_at = (datetime.now() + timedelta(minutes=minutes)).strftime("%Y-%m-%d %H:%M:%S")

        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO reminders (content, remind_at, recurring, triggered) VALUES (?, ?, ?, 0)",
            (text.strip(), remind_at, "none")
        )
        conn.commit()
        conn.close()

        return f"Reminder set. I will remind you to {text} in {minutes} minute{'s' if minutes != 1 else ''}."

    def add_reminder_in_seconds(self, text: str, seconds: int = 30) -> str:
        remind_at = (datetime.now() + timedelta(seconds=seconds)).strftime("%Y-%m-%d %H:%M:%S")

        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO reminders (content, remind_at, recurring, triggered) VALUES (?, ?, ?, 0)",
            (text.strip(), remind_at, "none")
        )
        conn.commit()
        conn.close()

        return f"Reminder set. I will remind you to {text} in {seconds} second{'s' if seconds != 1 else ''}."

    def add_reminder_at_time(self, text: str, hour: int, minute: int, am_pm: str) -> str:
        now = datetime.now()
        am_pm = am_pm.lower()

        if am_pm == "pm" and hour != 12:
            hour += 12
        if am_pm == "am" and hour == 12:
            hour = 0

        remind_at = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
        if remind_at <= now:
            remind_at += timedelta(days=1)

        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO reminders (content, remind_at, recurring, triggered) VALUES (?, ?, ?, 0)",
            (text.strip(), remind_at.strftime("%Y-%m-%d %H:%M:%S"), "none")
        )
        conn.commit()
        conn.close()

        spoken_hour = hour % 12 or 12
        spoken_ampm = "PM" if hour >= 12 else "AM"
        return f"Reminder set. I will remind you to {text} at {spoken_hour}:{minute:02d} {spoken_ampm}."

    def add_daily_reminder(self, text: str, hour: int, minute: int, am_pm: str) -> str:
        now = datetime.now()
        am_pm = am_pm.lower()

        if am_pm == "pm" and hour != 12:
            hour += 12
        if am_pm == "am" and hour == 12:
            hour = 0

        remind_at = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
        if remind_at <= now:
            remind_at += timedelta(days=1)

        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO reminders (content, remind_at, recurring, triggered) VALUES (?, ?, ?, 0)",
            (text.strip(), remind_at.strftime("%Y-%m-%d %H:%M:%S"), "daily")
        )
        conn.commit()
        conn.close()

        spoken_hour = hour % 12 or 12
        spoken_ampm = "PM" if hour >= 12 else "AM"
        return f"Daily reminder set for {spoken_hour}:{minute:02d} {spoken_ampm} to {text}."

    def list_reminders(self) -> str:
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, content, remind_at, recurring, triggered FROM reminders ORDER BY id DESC LIMIT 15"
        )
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            return "You have no reminders."

        reminders = []
        for _, content, remind_at, recurring, triggered in rows:
            status = "done" if triggered and recurring == "none" else "active"
            tag = f", repeating {recurring}" if recurring != "none" else ""
            reminders.append(f"{content} at {remind_at}{tag} [{status}]")

        return "Your reminders are: " + "; ".join(reminders)

    def clear_reminders(self) -> str:
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM reminders")
        conn.commit()
        conn.close()
        return "All reminders cleared."

    def get_due_reminders(self):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, content, remind_at, recurring
            FROM reminders
            WHERE triggered = 0 AND remind_at <= ?
            ORDER BY remind_at ASC
        """, (now,))
        rows = cursor.fetchall()
        conn.close()
        return rows

    def mark_triggered(self, reminder_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE reminders SET triggered = 1 WHERE id = ?", (reminder_id,))
        conn.commit()
        conn.close()

    def reschedule_daily(self, reminder_id: int, remind_at: str):
        old_dt = datetime.strptime(remind_at, "%Y-%m-%d %H:%M:%S")
        new_dt = old_dt + timedelta(days=1)

        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE reminders SET remind_at = ?, triggered = 0 WHERE id = ?",
            (new_dt.strftime("%Y-%m-%d %H:%M:%S"), reminder_id)
        )
        conn.commit()
        conn.close()
