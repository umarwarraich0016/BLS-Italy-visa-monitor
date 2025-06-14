import requests
from telegram import Bot
import time

TOKEN = "7555721402:AAGpjnWQjfZOORJHlQQlRdksWi_jYJ6SuqY"  # Your token
CHAT_ID = "7656263171"                                    # Your chat ID
BLS_URL = "https://pakistan.blsitaly.com/appointment"

bot = Bot(token=TOKEN)

def check_slots():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    while True:
        try:
            response = requests.get(BLS_URL, headers=headers, timeout=10)
            if "Study Visa" in response.text and "Available" in response.text:
                bot.send_message(
                    chat_id=CHAT_ID,
                    text=f"🚨 BLS ITALY SLOT OPEN!\n{BLS_URL}\nTime: {time.strftime('%Y-%m-%d %H:%M:%S')}"
                )
            time.sleep(300)  # Check every 5 minutes (to avoid blocking)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(60)

if __name__ == "__main__":
    print("Monitoring BLS Italy slots...")
    check_slots()
