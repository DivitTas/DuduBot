import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="$", intents=discord.Intents.default())

@bot.event
async def on_ready():
    print("Read to MEOW")

async def load_cogs():
    bot.load_extension("src.cogs.spending")

def run_bot(token):
    bot.run(token)

