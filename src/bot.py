import discord
from discord.ext import commands
intents=discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)
@bot.event
async def on_ready():
    print("Read to MEOW")

async def load_cogs():
    bot.load_extension("src.cogs.spending")

def run_bot(token):
    bot.run(token)
    load_cogs()

