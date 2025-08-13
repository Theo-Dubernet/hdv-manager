from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

def setup_commands(bot: commands.Bot):
    @bot.command()
    async def ping(ctx):
        await ctx.send("Pong !")

    @bot.command()
    async def clear(ctx):
        await ctx.channel.purge(limit=None)
        await ctx.send("Channel purgé", delete_after=5)