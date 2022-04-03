import re
import configparser
import random
from os import system
from datetime import datetime

from telethon import TelegramClient, events
from telethon.sync import TelegramClient

from datetime import date, datetime
    
config = configparser.ConfigParser()
config.read("config.ini")
        
api_id   = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
name = config['Telegram']['username']

client   = TelegramClient(name, api_id, api_hash)

@client.on(events.NewMessage(chats=("https://t.me/stoprussiachannel")))
async def get_channel_messages(data):
    channels = re.findall("https?://t.me/[^\s;,./]+", data.message.message)
    channels = list(set(channels))

    for i in range(len(channels)):
        if len(channels) > 0:
            if "https://t.me/stoprussiachannel" in channels[i]:
                channels.pop(i) 
            elif "https://t.me/ivukr/222" in channels[i]:
                channels.pop(i)
                
    if len(channels) != 0:
        print("I got new channels: ", "\n".join(channels))
        with open("channels.txt", "a") as file:
            for channel in channels:
                file.write(f"{channel}\n")
        with open("daily_channels.txt", "a") as file:
            for channel in channels:
                file.write(f"{channel}\n")        
        print("download on github")
        system("git add channels.txt")
        system("git add daily_channels.txt")
        system(f'git commit -m "update data for {datetime.now().strftime("%d.%m.%Y %H:%M")}"')
        system('git push')
        print("download finish\n")

async def main():
    pass

if __name__ == "__main__":
    system("cls")
    print("I run")
    client.start()
    client.run_until_disconnected()
    print("I finish")