# Telegram AutoBan

> Automatically block anyone who sends you a private message on Telegram.

Telegram AutoBan is a lightweight **Telegram Userbot** built with **Python** and **Telethon**.

It monitors incoming private messages on your Telegram account and automatically:

* ✅ Blocks the sender
* ❌ Deletes the conversation
* 📝 Records the event in `ban.log`
* 🔔 Sends an auto-reply notice to the blocked user

Designed for users who want to completely prevent unsolicited private messages.

---

[中文](README_zh.md)

---

## Features

* ✅ Automatically block unknown users
* 🔔 Auto-reply with ban notice before blocking
* ❌ Automatically delete the chat after blocking
* 📝 Log every blocked user
* ⚠ Whitelist support
* 🙅 Ignore your own account
* 📶 Ignore Telegram contacts
* 🤖 Ignore Telegram's official account (`777000`)
* 🏠 Cross-platform (Windows / Linux / macOS)

---

## Requirements

* Python 3.9+
* Telegram account
* Telegram API ID
* Telegram API Hash

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Serein1202/AutoBan-TG.git

cd AutoBan-TG
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Getting Telegram API Credentials

Telegram AutoBan **does not use a Bot Token**.

Instead, it authenticates using your own Telegram account through Telegram's official API.

### Step 1

Visit:

https://my.telegram.org

Log in using your Telegram account.

---

### Step 2

Open:

```
API Development Tools
```

---

### Step 3

Create a new application.

Example:

| Field      | Value            |
| ---------- | ---------------- |
| App title  | Telegram AutoBan |
| Short name | autoban          |
| Platform   | Desktop          |

---

### Step 4

Telegram will generate your `API_ID` and `API_HASH`. Save both values.

---

## Quick Start

> **Note:** On the first launch, if no `.env` file exists, the program will automatically prompt you to enter your `API_ID` and `API_HASH` interactively. You can also create `.env` manually (see [Configuration](#configuration)).

Run:

```bash
python AutoBan1.1.py
```

Telethon will ask for your phone number. Example:

```
+15551234567
```

Telegram will send a verification code. Enter it when prompted. If Two-Step Verification is enabled, also enter your password.

After a successful login, a session file will be created automatically. You only need to log in once.

---

## Configuration

### Option 1: Auto Setup (First Run)

When running for the first time without a `.env` file, the program will guide you:

```
首次运行，请输入 Telegram API 信息：
API_ID: 12345678
API_HASH: 0123456789abcdef0123456789abcdef
```

A `.env` file will be created automatically.

### Option 2: Manual Setup

Copy the example configuration file.

Linux / macOS:

```bash
cp .env.example .env
```

Windows:

```bat
copy .env.example .env
```

Edit `.env`:

```env
API_ID=12345678
API_HASH=0123456789abcdef0123456789abcdef
```

---

## Running

Start AutoBan:

```bash
python AutoBan1.1.py
```

The program will continue running until you stop it.

Whenever someone sends you a private message, AutoBan will:

1. Send an auto-reply notice to the user
2. Record the event in `ban.log`
3. Block the sender
4. Delete the conversation

---

## Whitelist

Users inside the whitelist will never be blocked.

```python
WHITE_LIST = {
    777000,
    123456789,
}
```

To obtain someone's Telegram ID, temporarily add:

```python
print(sender.id)
```

inside the message handler.

---

## Logs

Every blocked user is recorded in:

```
ban.log
```

Example:

```
========== 2026-06-29 18:05:17 ==========
ID          : 123456789
Name        : John Smith
Username    : @johnsmith
Premium     : False
Bot         : False
Message     : Hello!
=========================================
```

---

## Version History

| Version | Description |
|---------|-------------|
| **AutoBan1.1.py** | Current. Added auto-reply notice, first-run .env setup wizard |
| AutoBan1.0.py | Initial release with basic block + delete + log |

---

## Project Structure

```
AutoBan-TG/
|-- AutoBan1.0.py          # Initial version
|-- AutoBan1.1.py          # Latest version (recommended)
|-- requirements.txt
|-- .env.example
|-- .env                   # Created on first run
|-- README.md
|-- README_zh.md
|-- LICENSE
|-- .gitignore

autoban.session     # Generated after first login
ban.log             # Generated automatically
```

---

## requirements.txt

```text
telethon>=1.41.0
python-dotenv>=1.0.0
```

---

## .gitignore

```gitignore
# Python
__pycache__/
*.py[cod]

# Virtual Environment
.venv/
venv/
env/

# Environment Variables
.env

# Telethon Session
*.session
*.session-journal

# Logs
ban.log

# IDE
.vscode/
.idea/

# macOS
.DS_Store

# Windows
Thumbs.db
```

---

## FAQ

### Does this use a Telegram Bot?

No.

This project uses your own Telegram account via Telethon (Userbot).

---

### Do I need to log in every time?

No.

After the first successful login, Telethon creates a local session file (`autoban.session`), which will be reused automatically.

---

### What's the difference between AutoBan1.0.py and AutoBan1.1.py?

AutoBan1.1.py is the recommended version. Key improvements:

- **Auto-reply**: Sends a ban notice to the blocked user via @Serein0504_bot
- **First-run wizard**: If `.env` is missing, prompts for credentials interactively -- no manual setup needed

---

### Can I run it on a VPS?

Yes.

AutoBan can run on:

* VPS
* Raspberry Pi
* Docker
* NAS
* Home Server
* Always-on PC

---

## Security Notes

Your `.session` file is your authenticated Telegram session.

**Never upload or share it.**

If your session is compromised:

1. Open Telegram
2. Go to **Settings - Devices**
3. Terminate the corresponding session
4. Delete the local `.session` file
5. Log in again

---

## Disclaimer

This project is intended for educational and personal automation purposes.

Use it responsibly and comply with Telegram's Terms of Service.

The author is not responsible for any account restrictions or other consequences resulting from misuse.

---

## License

This project is licensed under the MIT License.