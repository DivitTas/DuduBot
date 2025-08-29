from dotenv import load_dotenv
from src.bot import run_bot
import os

if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.getenv("BOT_TOKEN")
    if not TOKEN:
        raise ValueError("No bot token found")
    run_bot(TOKEN)
