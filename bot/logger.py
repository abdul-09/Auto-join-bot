import os
from datetime import datetime

def log_session(action_type, clicks):
    os.makedirs("logs", exist_ok=True)

    action_verb = {
        "groups": "groups joined",
        "connect": "people connected",
        "follow": "people followed"
    }.get(action_type, "actions")

    with open("logs/actions.log", "a") as f:
        f.write(f"{datetime.now()} - {clicks} {action_verb}\n")

    print(f"📋 Session logged: {clicks} {action_verb}")
