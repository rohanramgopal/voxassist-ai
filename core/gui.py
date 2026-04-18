from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit,
    QHBoxLayout, QLineEdit
)
from PySide6.QtCore import Qt
from core.logger import write_log

class AssistantWindow(QWidget):
    def __init__(self, assistant):
        super().__init__()
        self.assistant = assistant
        self.setWindowTitle("VoxAssist AI")
        self.setMinimumSize(700, 500)
        self.build_ui()

    def build_ui(self):
        layout = QVBoxLayout()

        title = QLabel("VoxAssist AI — Desktop Voice Assistant")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 22px; font-weight: bold; padding: 10px;")
        layout.addWidget(title)

        self.status = QLabel("Status: Ready")
        self.status.setStyleSheet("font-size: 14px; padding: 8px;")
        layout.addWidget(self.status)

        self.history = QTextEdit()
        self.history.setReadOnly(True)
        layout.addWidget(self.history)

        row = QHBoxLayout()

        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Type a command, e.g. jarvis open chrome")
        row.addWidget(self.input_box)

        send_btn = QPushButton("Run Command")
        send_btn.clicked.connect(self.run_text_command)
        row.addWidget(send_btn)

        listen_btn = QPushButton("Voice Listen")
        listen_btn.clicked.connect(self.run_voice_command)
        row.addWidget(listen_btn)

        layout.addLayout(row)
        self.setLayout(layout)

    def append_history(self, speaker: str, text: str):
        self.history.append(f"<b>{speaker}:</b> {text}")

    def run_text_command(self):
        text = self.input_box.text().strip()
        if not text:
            return
        self.status.setText("Status: Processing text command...")
        self.append_history("User", text)
        response = self.assistant.process_text_command(text)
        self.append_history("Assistant", response)
        self.status.setText("Status: Ready")
        self.input_box.clear()

    def run_voice_command(self):
        self.status.setText("Status: Listening...")
        query = self.assistant.listener.listen()
        if not query:
            self.status.setText("Status: No speech detected")
            return
        self.append_history("User", query)
        response = self.assistant.process_text_command(query)
        self.append_history("Assistant", response)
        self.status.setText("Status: Ready")