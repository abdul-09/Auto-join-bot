# Auto Join Bot (LinkedIn)

## What it does
- Logs in to your LinkedIn  account
- Navigates to suggested groups or friends
- Automatically clicks on "Join", "Add", "Connect", "Follow"
- Handles lazy-loaded content with scroll
- Adds delays to avoid detection
- Logs session results to file

## How to run
1. Install requirements:
   `pip install selenium undetected-chromedriver`

2. Run the bot:
   `python main.py`

3. Log in manually when prompted, then let it run!

## Developer Notes
- You can adjust click limits and keywords in `config.py`
- Use a test account to avoid any platform bans