# Bot Framework imports
import discord
from discord.ext import commands

# Import personal Code
from extensions.misc import get_token

# Import extensions
from extensions.meme import Meme
from extensions.startup import Startup
from extensions.admin import Admin
from extensions.dad import Dad

client = commands.Bot(command_prefix=get_token(0))

# Register extensions
client.add_cog(Meme(client))
client.add_cog(Startup(client))
client.add_cog(Admin(client))
client.add_cog(Dad(client))

# Run the bot
if __name__ == "__main__":
    client.run(get_token(1))
