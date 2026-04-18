import webbrowser
import urllib.parse


def handle_web_command(query: str):
    if query.startswith("search "):
        term = query.replace("search ", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={urllib.parse.quote(term)}")
        return f"Searching Google for {term}"

    if query.startswith("play "):
        term = query.replace("play ", "").strip()
        webbrowser.open(f"https://www.youtube.com/results?search_query={urllib.parse.quote(term)}")
        return f"Playing {term} on YouTube"

    return None
