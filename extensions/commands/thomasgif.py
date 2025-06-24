import constants
import discord
import random

from discord import app_commands
from discord.ext import commands


class ThomasGIF(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("/thomasgif command loaded")

    @discord.app_commands.command(name="thomasgif", description="send a gif of a naked black man")
    async def thomasgif(self, interaction: discord.Interaction):
        await interaction.response.send_message(random.choice(constants.THOMAS_GIFS))
