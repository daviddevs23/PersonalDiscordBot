import discord
from discord.ext import commands

# Utility class for start up tasks
class Startup(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        # Set Bot Status
        await self.client.change_presence(status=discord.Status.online,
                activity=discord.Game("Dank Memes And Stuffs"))

        print("Bot is ready")
