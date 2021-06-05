import discord, requests, re, os, random, asyncpraw
from discord.ext import commands

from .misc import get_token

# Cog based class that grabs a meme using the asyncpraw library
class Meme(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Command that grabs and posts the meme
    @commands.command()
    async def meme(self, ctx):
        # Instantiate asyncronous instance of Reddit API
        reddit = asyncpraw.Reddit(
                client_id=get_token(2),
                client_secret=get_token(3),
                user_agent="Shunned_Bot"
                )

        # List of "safe"-ish subreddits
        subs = [
                "memes",
                "dankmemes",
                "antimeme",
                "wholesomememes",
                "terriblefacebookmemes",
                "funny",
                "PrequalMemes",
                "crappyoffbrands",
                "bonehurtingjuice",
                ]

        sub = await reddit.subreddit(random.choice(subs))

        memes = []
        url = ""
        file_name = ""

        # Grab all of the best memes that are safe for work and non admin posts
        async for post in sub.hot(limit=25):
            if not post.stickied and not post.over_18:
                memes.append(post)

        # Choose url and make sure it is valid
        url = random.choice(memes).url
        file_name = url.split("/")

        if len(file_name) == 0:
            file_name = re.findall("/(.*?)", url)

        file_name = file_name[-1]

        if "." not in file_name:
            file_name += ".jpg"

        # Download image
        r = requests.get(url)

        # Write to local directory so you can send it with discord
        with open(file_name, "wb") as f:
            f.write(r.content)

        await ctx.send(file=discord.File(file_name))

        # Clean up the tempory local file
        os.remove(file_name)


