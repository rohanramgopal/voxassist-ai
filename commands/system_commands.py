from services.system_service import SystemService
from services.screenshot_service import ScreenshotService

system_service = SystemService()
screenshot_service = ScreenshotService()

def handle_system_command(query: str):
    if "lock screen" in query:
        return system_service.lock_screen()

    if "volume up" in query:
        return system_service.volume_up()

    if "volume down" in query:
        return system_service.volume_down()

    if "mute" in query:
        return system_service.mute()

    if "screenshot" in query or "screen shot" in query or "take a screenshot" in query or "take screenshot" in query:
        return screenshot_service.take_screenshot()

    if "shutdown system" in query:
        return system_service.shutdown()

    if "restart system" in query:
        return system_service.restart()

    return None
