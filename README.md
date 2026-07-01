# Email Automator

A Python tool for sending automated HTML emails via Gmail SMTP. Supports scheduled delivery and rich HTML email templates.

## Features

- Sends styled HTML emails via Gmail SMTP
- Supports scheduled sending with `schedule`
- Environment variable configuration for credentials
- Easy to extend with dynamic content like user stats or error reports

## Tech Stack

- Python
- smtplib
- schedule
- python-dotenv

## Getting Started

### Prerequisites

- Python 3.8+
- A Gmail account with an [App Password](https://support.google.com/accounts/answer/185833) enabled

### Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/email-automator.git
cd email-automator
```

2. Install dependencies

```bash
pip install python-dotenv schedule
```

3. Create a `.env` file in the root directory

```env
SENDER_EMAIL=your@gmail.com
APP_PASSWORD=your_app_password
```

## Usage

Add recipient emails to the `emails` list in `main.py`, then run:

```bash
python main.py
```

To enable scheduled sending, uncomment the `schedule` lines in `main.py` and set your preferred time:

```python
schedule.every().day.at("08:00").do(send_report)
```

## Project Structure

```
email-automator/
├── main.py
├── .env
├── .gitignore
└── README.md
```

## Notes

- Never commit your `.env` file, add it to `.gitignore`
- Gmail App Passwords require 2-Step Verification to be enabled on your account

## License

MIT
