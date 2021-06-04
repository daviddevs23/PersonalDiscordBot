# Bot Framework imports
import discord
from discord.ext import commands

# Import personal Code
from extensions.misc import get_token

# Import extensions
from extensions.test import Test

client = commands.Bot(command_prefix=get_token(0))
print("Bot has started")

# Register extensions
client.add_cog(Test(client))

# Run the bot
if __name__ == "__main__":
    client.run(get_token(1))
