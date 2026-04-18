from core.listener import Listener
from core.speaker import Speaker
from core.parser import parse_command
from core.logger import write_log
from core.wake import WakeWordProcessor
from config.settings import ASSISTANT_NAME, USER_NAME


class VoiceAssistant:
    def __init__(self):
        self.listener = Listener()
        self.speaker = Speaker()
        self.wake = WakeWordProcessor()
        self.active = True
        self.history = []
        self.pending_confirmation = None

    def greet(self):
        message = (
            f"Hello {USER_NAME}. I am {ASSISTANT_NAME}. "
            f"Speak naturally and I will try to catch your command."
        )
        self.speaker.speak(message)
        write_log("Assistant started")

    def needs_confirmation(self, command: str) -> bool:
        risky = [
            "shutdown",
            "restart",
            "clear memory",
            "clear reminders",
            "lock screen"
        ]
        return any(item in command for item in risky)

    def handle_confirmation(self, query: str) -> str:
        if not self.pending_confirmation:
            return ""

        yes_words = {"yes", "yeah", "confirm", "do it", "okay", "ok"}
        no_words = {"no", "cancel", "stop", "never mind"}

        if query in yes_words:
            command = self.pending_confirmation
            self.pending_confirmation = None
            response = parse_command(command)
            return response

        if query in no_words:
            self.pending_confirmation = None
            return "Cancelled."

        return "Please say yes or no."

    def handle_query(self, query: str) -> str:
        query = query.strip().lower()
        if not query:
            return ""

        write_log(f"User said: {query}")
        self.history.append(("user", query))

        if self.pending_confirmation:
            response = self.handle_confirmation(query)
            self.history.append(("assistant", response))
            write_log(f"Assistant response: {response}")
            return response

        if query in {"exit", "quit", "stop assistant", "stop"}:
            self.active = False
            response = "Goodbye. Have a great day."
            self.history.append(("assistant", response))
            write_log(f"Assistant response: {response}")
            return response

        command = self.wake.clean_command(query)

        if not command:
            return "Sorry, I did not understand that command."

        if self.needs_confirmation(command):
            self.pending_confirmation = command
            return "This action needs confirmation. Please say yes or no."

        response = parse_command(command)
        self.history.append(("assistant", response))
        write_log(f"Assistant response: {response}")
        return response

    def run(self):
        self.greet()
        while self.active:
            query = self.listener.listen()
            if not query:
                continue
            response = self.handle_query(query)
            if response:
                self.speaker.speak(response)

    def process_text_command(self, text: str) -> str:
        response = self.handle_query(text)
        if response:
            self.speaker.speak(response)
        return response
