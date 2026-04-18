from services.app_service import AppService

app_service = AppService()

def handle_app_command(query: str):
    if query.startswith("open "):
        app_name = query.replace("open ", "").strip()

        website_map = {
            "youtube": "https://www.youtube.com",
            "google": "https://www.google.com",
            "gmail": "https://mail.google.com",
            "github": "https://github.com",
            "linkedin": "https://www.linkedin.com",
        }

        if app_name in website_map:
            return app_service.open_website(website_map[app_name])

        return app_service.open_app(app_name)

    return None