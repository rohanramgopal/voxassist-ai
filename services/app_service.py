import platform
import subprocess
import webbrowser

class AppService:
    def __init__(self):
        self.system = platform.system().lower()

    def open_app(self, app_name: str) -> str:
        app_name = app_name.lower()

        mac_apps = {
            "chrome": "Google Chrome",
            "google chrome": "Google Chrome",
            "safari": "Safari",
            "vscode": "Visual Studio Code",
            "visual studio code": "Visual Studio Code",
            "terminal": "Terminal",
            "finder": "Finder",
            "spotify": "Spotify",
            "notes": "Notes",
            "calculator": "Calculator",
            "calendar": "Calendar",
            "mail": "Mail",
        }

        try:
            if self.system == "darwin":
                if app_name in mac_apps:
                    subprocess.run(["open", "-a", mac_apps[app_name]], check=False)
                    return f"Opening {app_name}"
                return f"I could not find {app_name} in my known app list."

            return "This version is optimized for macOS first."
        except Exception as e:
            return f"Error opening app: {e}"

    def open_website(self, url: str) -> str:
        if not url.startswith("http"):
            url = "https://" + url
        webbrowser.open(url)
        return f"Opening {url}"