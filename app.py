import sys
from config.settings import ENABLE_GUI
from core.assistant import VoiceAssistant

def main():
    assistant = VoiceAssistant()

    if ENABLE_GUI:
        from PySide6.QtWidgets import QApplication
        from core.gui import AssistantWindow

        app = QApplication(sys.argv)
        window = AssistantWindow(assistant)
        window.show()
        sys.exit(app.exec())
    else:
        assistant.run()

if __name__ == "__main__":
    main()