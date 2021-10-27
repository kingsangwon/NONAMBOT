import discord
from discord.ext import commands
import os

bot=commands.Bot(commands_prefix='!', intents=discord.Intents.all())

for cogs in os.listdir('cogs'):
    if cogs.endswith('.py'):
        bot.load_extension(f'cogs.{cogs[:-3]}')

@bot.event
async def on_ready():
    print('login success!')

bot.run('token here')