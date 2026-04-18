import os
from datetime import datetime
import pyautogui


class ScreenshotService:
    def take_screenshot(self) -> str:
        file_path = os.path.join(
            "data",
            f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        )
        shot = pyautogui.screenshot()
        shot.save(file_path)
        return f"Screenshot saved as {file_path}"
