import pyttsx3
import threading
import queue


class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 195)
        self.engine.setProperty("volume", 1.0)

        self.queue = queue.Queue()
        self.is_speaking = False

        self.engine.connect('started-utterance', self._on_start)
        self.engine.connect('finished-utterance', self._on_end)

        self.worker = threading.Thread(target=self._run, daemon=True)
        self.worker.start()

    def _on_start(self, name):
        self.is_speaking = True

    def _on_end(self, name, completed):
        self.is_speaking = False

    def _run(self):
        while True:
            text = self.queue.get()
            if text is None:
                break
            try:
                print(f"Assistant: {text}")
                self.engine.say(text)
                self.engine.runAndWait()
            except Exception as e:
                print(f"TTS Error: {e}")
                self.is_speaking = False
            finally:
                self.queue.task_done()

    def speak(self, text: str):
        if text and text.strip():
            self.queue.put(text)

    def stop(self):
        try:
            self.engine.stop()
        except Exception:
            pass
        self.is_speaking = False
