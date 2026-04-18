# 🚀 VoxAssist AI  
### 🎙️ Premium Desktop Voice Assistant

<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdThyZGZpZTF0c2p1eWFyZ3F4c2Z5YjF6M3B4c2R3dG5hNmM4dHc4NiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/26tn33aiTi1jkl6H6/giphy.gif" width="700"/>
</p>

---

## 🏷️ Badges

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![PySide6](https://img.shields.io/badge/GUI-PySide6-green?style=for-the-badge&logo=qt)
![Speech](https://img.shields.io/badge/Speech-Recognition-orange?style=for-the-badge)
![SQLite](https://img.shields.io/badge/Database-SQLite-purple?style=for-the-badge&logo=sqlite)
![Status](https://img.shields.io/badge/Project-Advanced%20AI%20Assistant-black?style=for-the-badge)

---

## 🌟 Overview

**VoxAssist AI** is a **voice-first desktop assistant** built in Python that can control your system, manage reminders, remember information, and assist with daily productivity — all through natural voice commands.

It combines:
- 🎤 Voice Recognition  
- 🔊 Text-to-Speech  
- 🖥️ Desktop Automation  
- 🧠 Persistent Memory  
- ⏰ Smart Reminders  
- 🎨 Premium GUI  

This is a **full-scale product-style project**, not just a script.

---

## ⚡ Features

### 🎙️ Voice Assistant
- Speak naturally (no strict commands)
- Smart wake-word handling (`vox`, `box`, etc.)
- Continuous listening mode

### 🖥️ Desktop Automation
- Open apps (Chrome, VS Code, etc.)
- Open websites instantly
- Google search & YouTube playback
- Take screenshots
- Control system (volume, lock, etc.)

### ⏰ Reminder System
- `in 30 seconds`
- `in 5 minutes`
- `at 5 PM`
- `daily reminders`
- Popup + voice alerts

### 🧠 Memory System
- Store info → `remember my goal is startup`
- Recall anytime → `what do you remember`
- Clear memory safely

### 📋 Productivity Tools
- Notes creation
- Clipboard read/write
- Battery status
- IP address detection

### 🛡️ Smart Safety
- Voice confirmation for dangerous actions
- Prevents accidental system commands

### 🎨 Premium GUI
- Built with **PySide6**
- Dark futuristic theme
- Animated voice orb
- Live conversation log

---

## 🧠 How It Works

```text
Voice Input
   ↓
Speech Recognition
   ↓
Command Parser
   ↓
Execution Engine
   ↓
Response (TTS + GUI)

📂 Project Structure

voxassist-ai/
│
├── app.py
├── requirements.txt
│
├── config/
│   └── settings.py
│
├── core/
│   ├── assistant.py
│   ├── listener.py
│   ├── speaker.py
│   ├── wake.py
│   ├── parser.py
│   ├── gui.py
│   └── reminder_checker.py
│
├── commands/
│   ├── app_commands.py
│   ├── web_commands.py
│   ├── system_commands.py
│   └── utility_commands.py
│
├── services/
│   ├── reminder_service.py
│   ├── memory_service.py
│   ├── note_service.py
│   ├── screenshot_service.py
│   └── db_service.py
│
└── data/
    ├── logs/
    ├── notes/
    └── voxassist.db

🎤 Example Voice Commands
🔹 Apps & Web
vox open chrome
vox open youtube
vox search ai roadmap
vox play lofi music
🔹 Reminders
vox set reminder drink water in 1 minute
vox set reminder stretch in 30 seconds
vox set reminder call mom at 5 pm
vox set daily reminder workout at 7 am
🔹 Memory
vox remember I like Python
vox what do you remember
vox clear memory
🔹 Utilities
vox what time is it
vox battery status
vox read clipboard
vox take a screenshot
🔹 Exit
stop

⚙️ Installation
git clone https://github.com/rohanramgopal/voxassist-ai.git
cd voxassist-ai

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python app.py

🧰 Tech Stack
Python
PySide6 (GUI)
SpeechRecognition
PyAudio
pyttsx3
SQLite
pyautogui
plyer
psutil
python-dotenv

🏆 Why This Project Stands Out

This is a real product-level system, combining:
Voice AI
GUI Engineering
Automation
Database systems
Modular backend architecture


📈 Future Enhancements
Offline speech recognition
Wake-word detection engine
Calendar integration
Email automation
Local LLM integration (ChatGPT-style)
Cross-platform support
macOS app packaging

👨‍💻 Author

Rohan Ramgopal
GitHub: https://github.com/rohanramgopal
