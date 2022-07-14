import os
import requests
from keep_alive import keep_alive
from bs4 import BeautifulSoup
import time

TOKEN = os.environ['TOKEN']
CHAT_ID = os.environ['CHAT_ID']
CHANNEL_ID = os.environ['CHANNEL_ID']
CHANNEL_NAME = os.environ['CHANNEL_NAME']
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/"
YOUTUBE_URL = f"https://www.youtube.com/channel/{CHANNEL_ID}/live"

def is_live():
    req = requests.get(YOUTUBE_URL)
    soup = BeautifulSoup(req.text, "lxml")
    element = soup.find("link", {"rel": "canonical"})
    
    if "watch" in str(element):
        return True
    else:
        return False

def send_message(message):
    params = {"chat_id": CHAT_ID, "text": message}
    requests.get(TELEGRAM_URL + "sendMessage", params=params)

def hello_world():
    print("==== BOT IS UP AND RUNNING! ====")

keep_alive()
hello_world()

notificationSent = False
while True:
    if is_live(): # channel is live
        if not notificationSent: # user has not been notified yet
            send_message(f"✅ {CHANNEL_NAME} IS LIVE!")
            notificationSent = True
        # sleep and check every 1 minute if the channel is still livestreaming
        time.sleep(60)
    else: # channel is not live
        if notificationSent: # user has been notified about channel being live
            send_message(f"❌ {CHANNEL_NAME} IS NO LONGER LIVE!")
            notificationSent = False
        # sleep and check every 1 minute if the channel is livestreaming again
        time.sleep(60)
