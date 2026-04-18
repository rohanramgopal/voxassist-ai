import re

def extract_minutes(query: str) -> int:
    match = re.search(r'(\d+)\s*minute', query)
    if match:
        return int(match.group(1))
    return 1


def clean_reminder_text(query: str) -> str:
    text = query.lower().strip()

    # Step 1: normalize phrases
    text = text.replace("what is", "").strip()

    # Step 2: remove trigger phrases
    triggers = [
        "set reminder to",
        "set a reminder to",
        "set reminder",
        "remind me to",
        "reminder to",
        "reminder",
    ]

    for t in triggers:
        if t in text:
            text = text.split(t, 1)[-1].strip()
            break

    # Step 3: remove time part (but KEEP sentence clean)
    text = re.sub(r'\bin\s+\d+\s+minutes?\b', '', text).strip()

    return text
