import os
from datetime import datetime

def log_session(clicks):
    os.makedirs("logs", exist_ok=True)  # Ensure folder exists
    with open("logs/actions.log", "a") as f:
        f.write(f"{datetime.now()} - Clicked {clicks} buttons\n")
    print(f"Session logged: {clicks} actions")