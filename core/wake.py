class WakeWordProcessor:
    def __init__(self):
        self.valid_wake_words = {
            "vox",
            "voxx",
            "box",
            "fox",
            "walks",
            "vogs",
            "books",
            "bugs"
        }

        self.command_starters = {
            "open", "search", "play", "what", "tell", "create",
            "take", "volume", "mute", "lock", "shutdown", "restart",
            "who", "exit", "quit", "stop", "battery", "read",
            "copy", "remember", "recall", "show", "set"
        }

    def clean_command(self, query: str) -> str:
        query = query.lower().strip()
        if not query:
            return ""

        words = query.split()
        if not words:
            return ""

        if words[0] in self.valid_wake_words:
            while words and words[0] in self.valid_wake_words:
                words.pop(0)
            return " ".join(words).strip()

        for i, word in enumerate(words[:4]):
            if word in self.valid_wake_words:
                return " ".join(words[i + 1:]).strip()

        if words[0] in self.command_starters:
            return " ".join(words).strip()

        for i, word in enumerate(words[:4]):
            if word in self.command_starters:
                return " ".join(words[i:]).strip()

        return ""
