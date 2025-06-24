import constants
import discord
import random

from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

class MessageEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener
    async def on_message(self, message):
        if message.author.bot:
            return

        # handle general messages
        await self.handle_jarvis(message)

        # handle messages by specific people
        await self.handle_david(message)

    async def handle_jarvis(self, message):
        """
        respond with random response to messages starting with "jarvis," and ending with "?"
        Args:
            message: discord message object
        Returns:
            response (string): random response from constants.JARVIS_RESPONSES
        """
        content = message.content.strip()
        if content.lower().startswith("jarvis,") and content.endswith("?"):
            response = random.choice(constants.JARVIS_RESPONSES)
            await message.reply(response)

    async def handle_david(self, message):
        """
        respond with ron schlocock speech bubble gif to any message by david
        Args:
            message: discord message object
        Returns:
            response (string): Discord URL of ron shlocock speech bubble gif
        """
        if message.author.id == constants.DAVID_USER_ID:
            await message.reply(constants.RON_SHLOCOCK_GIF_URL)
