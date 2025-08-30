import discord
from discord.ext import commands
from src import db
from src.bot import bot

class Spending(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command(name="spend")
    async def spend(self,ctx, amount, category,*, notes):
        db.add_expense(str(ctx.author.id),amount,category,notes)
        await ctx.send(f"Added {amount} to expenses")

def setup(bot):
    bot.add_cog(Spending(bot))
