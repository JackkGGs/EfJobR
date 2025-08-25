# EfJobR

## Overview
This is a Discord bot, specifically `discord.py`. It runs on weaker CPUs and requires stable internet speeds of over 100 KB/s and a latency lower than 100ms to be used efficiently. It uses Gemini 2.5 Flash-Lite to give dynamics. With this bot, you can easily find recruitment forms for free. Note that it doesn't send messages to servers. Instead, it directly messages you on your PMs. It's protected by encryption, and the person running the program can't directly see what you're doing.

## Features
  - **Dynamic Responses**: Parameters of the LLM are randomised on every message it receives.
  - **Private**: Received and sent messages are not directly visible to the bot's program executor. It is multi-layer encrypted, and the encryption is randomised for every message received and sent.
  - **Efficient**: Low system requirements. Internet speeds are not a big deal, as latency is more important. 50ms is already very responsive.

## Installation and Setup

### Prerequisites
  - [Python 3.8](https://www.python.org/downloads/)
  - [discord.py](https://pypi.org/project/discord.py/)

### Setup

#### 1. Clone This Repository

Clone the repository to your local machine.

```bash
git clone https://github.com/JackkGGs/EfJobR/
cd EfJobR
```

#### 2. Install Dependencies

Install Required Modules.

```bash
pip install -r requirements.txt
```

`requirements.txt` should include discord.py:
```
discord.py>=2.0
```
If `pip` isn't recogni
