import constants
import discord
import random
import os

from click import command
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

# takes bot token from local env file(you cant have this)
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# chatgpt said this is required to track messages (for jarvis, function)
intents = discord.Intents.default()
intents.message_content = True  # Important to enable this!
intents.members = True

client = discord.Client(intents=intents)

bot = commands.Bot(intents=intents, command_prefix="!", case_insensitive=True)

@client.event
async def on_ready():
    print(f'Bot is online as {client.user}')

    # register slash commands with discord API (specifically slash commands)
    await bot.tree.sync()

    await bot.load_extension("extensions.message_events")
    # await bot.load_extension("extensions.commands.thomasgif")

    # load all files command .py files in extensions/commands
    for command_module in os.listdir(constants.COMMANDS_DIRECTORY):

        # load only .py files
        if command_module.endswith(".py"):
            command_module_path = f"extensions.commands.{command_module[:-3]}"
            await bot.load_extension(command_module_path)

client.run(TOKEN)
