from commands.app_commands import handle_app_command
from commands.web_commands import handle_web_command
from commands.system_commands import handle_system_command
from commands.utility_commands import handle_utility_command
from commands.ai_commands import handle_ai_command

def parse_command(query: str) -> str:
    handlers = [
        handle_app_command,
        handle_web_command,
        handle_system_command,
        handle_utility_command,
        handle_ai_command,
    ]

    for handler in handlers:
        result = handler(query)
        if result:
            return result

    return "Sorry, I did not understand that command."
