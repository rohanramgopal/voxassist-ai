import time
import speech_recognition as sr


class Listener:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.pause_threshold = 0.5
        self.recognizer.energy_threshold = 170
        self.recognizer.dynamic_energy_threshold = True
        self.calibrated = False

    def listen(self) -> str:
        with sr.Microphone() as source:
            print("Listening...")
            if not self.calibrated:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.4)
                self.calibrated = True

            audio = self.recognizer.listen(
                source,
                timeout=None,
                phrase_time_limit=4
            )

        try:
            print("Recognizing...")
            query = self.recognizer.recognize_google(audio, language="en-US")
            print(f"User: {query}")
            return query.lower().strip()
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            time.sleep(0.3)
            return ""
        except Exception:
            return ""
