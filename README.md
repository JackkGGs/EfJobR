# EfJobR

## Overview
This program interactively searches for recruitments. This project uses `discord.py` as its base. It runs on weaker CPUs and requires stable internet speeds of over 100 KB/s and a latency lower than 100ms to be used efficiently and quickly. It uses Gemini 2.5 Flash-Lite to give responses. It's protected by encryption, and the person running the program can't directly see what you're doing.

## Features
  - **Dynamic Responses**: Parameters of the LLM are randomised on every message it receives.
  - **Private**: Received and sent messages are not directly visible to the bot's program executor. The messages are directly sent to Gemini.
  - **Efficient**: Low system requirements. Internet speeds are not a big deal; however, latency is more important. 50ms is already very responsive.
  - **Multilingual**: Supports a wide range of languages. You can even use Akkadian if you insist.

## Installation and Setup

### Prerequisites
  - [Python 3.8](https://www.python.org/downloads/)
  - [discord.py](https://pypi.org/project/discord.py/)

### Setup

#### 1. Clone This Repository

Clone this repository to your local machine.

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

If `pip` isn't recognised:

1. Re-open your Python installation.
2. Click `Modify`.
3. Check `pip`.
4. Click next.
5. Click install.
6. Redo `pip install -r requirements.txt` in the directory of the project.

#### 3. Set Up Your Discord Bot Token and Gemini API Key
- Create a bot on the [Discord Developer Portal](https://discord.com/developers/applications).
- Create a [Gemini Flash-Lite 2.5 Key](https://aistudio.google.com/apikey)
- Obtain the Bot Token and Gemini API Key and save them in config.py.

#### 4. Run the Bot
Once the setup is complete, you can run the bot (note that the terminal must be in the same directory as your code) with:

```bash
python bot.py
```

#### What is main_c.py for?
This'll be your canvas for potential changes on the command line. This helps to gain speed. It's a one-to-one copy, at least for me.

## Usage
This bot only uses one command, and that is:
`!job_recommendations [your interests]`

However, if the user values privacy more (by means of not wanting to give what their education was, for example), the user can use:
`!job_recommendations lets talk on the DMs for more privacy.`

# Thanks.
This repository is completely open-source. Any changes do not need credits.
