# 🤖 Auto Join Bot – LinkedIn  Group Auto-Clicker

**Author:** Abdulaziz Hussein  
**Interview Task Submission** – AI Synergy Team

## 🎯 Goal

This automation script logs into a social media platform (LinkedIn), navigates to group or connection suggestions, and **automatically clicks relevant buttons** like:

- ✅ "Join Group"
- ✅ "Add"
- ✅ "Connect"
- ✅ "Follow"

Supports scrolling and dynamic loading, and mimics human behavior to avoid detection.

---

## 🛠 Tech Stack

- **Python 3.10+**
- **Selenium** (for browser control)
- **undetected-chromedriver** (for stealth)
- Manual login (secure, no password storage)

---

## 🚀 Features

| Feature | Description |
|--------|-------------|
| 🔐 Manual Login Flow | Login securely yourself; no password stored in code |
| 🔍 Smart Button Detection | Matches button text against keywords like "Join", "Follow" |
| ⏱ Human-like Behavior | Random delays between actions to avoid detection |
| 📜 Logs & Limits | Logs number of buttons clicked, limits max per session |
| 🧭 Auto Scroll | Scrolls to load more dynamic content |
| 🎩 Stealth Mode | Hides `navigator.webdriver`, spoofs user-agent, disables automation flags |

---

## 📦 Installation

1. Clone the repo:

```bash
git clone https://github.com/your-username/auto-join-bot.git
cd auto-join-bot


## How to run
1. Install requirements:
   `pip install selenium undetected-chromedriver`

2. Run the bot:
   `python main.py`

3. Log in manually when prompted, then let it run!

## Developer Notes
- You can adjust click limits and keywords in `config.py`
- Stealth - navigator.webdriver // should be undefined or false
- Use a test account to avoid any platform bans