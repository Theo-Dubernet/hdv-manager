import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from .views import ViewBuyItemManager

load_dotenv()

def setup_commands(bot: commands.Bot):
    @bot.command()
    async def ping(ctx):
        await ctx.send("Pong !")

    @bot.command()
    async def clear(ctx):
        await ctx.channel.purge(limit=None)
        await ctx.send("Channel purgé", delete_after=5)

    @bot.command(name="buy_manager")
    async def views_sales_manager(ctx):
        embed = discord.Embed(
            title="Gestion des ventes",
            description="Interface de vente",
            color=discord.Color.blue(),
        )
        await ctx.channel.purge(limit=None)
        await ctx.send(embed=embed, view=ViewBuyItemManager())