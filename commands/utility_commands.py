import random
from datetime import datetime
from services.note_service import NoteService

note_service = NoteService()

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why was the developer calm? Because he handled every exception.",
    "I would tell you a UDP joke, but you might not get it."
]

def handle_utility_command(query: str):
    if "what time is it" in query or "current time" in query:
        return f"The current time is {datetime.now().strftime('%I:%M %p')}"

    if "what is the date" in query or "today's date" in query:
        return f"Today's date is {datetime.now().strftime('%d %B %Y')}"

    if query.startswith("create note "):
        note = query.replace("create note ", "").strip()
        return note_service.save_note(note) if note else "Please tell me what to save."

    if "tell me a joke" in query:
        return random.choice(JOKES)

    if "who are you" in query:
        return "I am VoxAssist AI, your desktop voice assistant."

    return None