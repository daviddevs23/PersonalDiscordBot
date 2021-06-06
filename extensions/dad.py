import discord
import os
import random
from discord.ext import commands


# Classic dad tom-foolery
class Dad(commands.Cog):
    def __init__(self, client):
        self.client = client

    # The classic "I'm"
    @commands.Cog.listener()
    async def on_message(self, ctx):
        
        content = ctx.content

        # lower case and and format string for accurate checking later
        smallContent = content.lower()
        smallContent = smallContent.replace("i'm", "im")

        # Self check 
        if ctx.author.id == self.client.user.id:
            return

        # Check if the message has "I'm" in it
        if "im" in smallContent:
            imIndex = smallContent.find("im")
            message = f"Hi{content[imIndex + 3:]}, I'm dad bot"
            
            await ctx.channel.send(message)
