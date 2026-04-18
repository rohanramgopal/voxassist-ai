import os
import subprocess
import platform


class SystemService:
    def __init__(self):
        self.system = platform.system().lower()

    def lock_screen(self) -> str:
        try:
            if self.system == "darwin":
                subprocess.run(
                    ["/System/Library/CoreServices/Menu Extras/User.menu/Contents/Resources/CGSession", "-suspend"],
                    check=False
                )
                return "Locking the screen."
            return "Lock screen is configured for macOS."
        except Exception as e:
            return f"Failed to lock screen: {e}"

    def volume_up(self) -> str:
        os.system("osascript -e 'set volume output volume ((output volume of (get volume settings)) + 10)'")
        return "Increasing volume."

    def volume_down(self) -> str:
        os.system("osascript -e 'set volume output volume ((output volume of (get volume settings)) - 10)'")
        return "Decreasing volume."

    def mute(self) -> str:
        os.system("osascript -e 'set volume with output muted'")
        return "Muting system audio."

    def shutdown(self) -> str:
        return "Shutdown is disabled in safe mode."

    def restart(self) -> str:
        return "Restart is disabled in safe mode."
