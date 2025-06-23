import discord
import random
import os
from dotenv import load_dotenv
load_dotenv()

# takes bot token from local env file(you cant have this)
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Replace with the target david's ID (int)
TARGET_USER_ID = 123456

# gif for auto response
GIF_URL = 'https://cdn.discordapp.com/attachments/920649726553129010/1386338401216757941/attachment.gif?ex=685aa93f&is=685957bf&hm=2a4a92f58fea9441ef3e68b802588e42914d169d109af540a278351978ee6fa9&'

# chatgpt said this is required to track messages (for jarvis, function)
intents = discord.Intents.default()
intents.message_content = True  # Important to enable this!
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot is online as {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    # reply to david
    if message.author.id == TARGET_USER_ID:
        await message.reply(GIF_URL)

    # jarvis question
    content = message.content.strip()
    if content.lower().startswith("jarvis,") and content.endswith("?"):
        response = random.choice(["yes", "no", "maybe", "perhaps"])
        await message.reply(response)

client.run(TOKEN)
