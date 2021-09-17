import discord, asyncio, os, json
from discord.ext import commands
from datetime import datetime
 
bot = commands.Bot(command_prefix="%", intents=discord.Intents.all())

for cogs in os.listdir("cogs"):
    if cogs.endswith(".py"):
        bot.load_extension(f"cogs.{cogs[:-3]}")
        print(f"cogs.{cogs[:-3]}을 성공적으로 로드했어요!")
@bot.event
async def on_ready():
    print(f'{bot.user.name} 에 성공적으로 로그인했어요')
    print(f'봇의 ID는 다음과 같아요 "{bot.user.id}"')
    date = datetime.now()
    while(True):        
        await bot.change_presence(activity = discord.Streaming(name = "곰탱쓰 도움", url= "https://www.twitch.tv/bookguk_gom"))
        await asyncio.sleep(5)
        await bot.change_presence(activity = discord.Streaming(name = f"ver. BATA {date.year}. {date.month}. {date.day}. ", url= "https://www.twitch.tv/bookguk_gom"))
        await asyncio.sleep(5)



bot.run(token)