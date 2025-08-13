import os
import traceback

from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv("TOKEN_DISCORD")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    log_channel = bot.get_channel(1405171691579244716)
    await log_channel.send(f"Je suis connecté !")
    print(f"{bot.user} est connecté !")

def chunk_text(text, size=1900):
    """Découpe le texte en morceaux de `size` caractères maximum"""
    for i in range(0, len(text), size):
        yield text[i:i+size]

@bot.event
async def on_command_error(ctx, error):
    channel = bot.get_channel(1405183350863298591)
    err_text = "".join(traceback.format_exception(type(error), error, error.__traceback__))

    for chunk in chunk_text(err_text):
        await channel.send(f"🚨 **Erreur détectée :**\n```py\n{chunk}\n```")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong !")

@bot.check
async def global_check(ctx):
    return ctx.author.id == os.getenv("MY_ID")

def start_bot():
    bot.run(TOKEN)