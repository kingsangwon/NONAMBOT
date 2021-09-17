import discord, asyncio, os, json
from discord.ext import commands
from datetime import datetime
try:
 f = json.loads(open("setup.json", "r").read())
 token = f['token']
expect:
 print("setup.json 파일을 불러오는데 오류가 발생했어요 파일이 존재하거나 읽기 권한을 확인해주세요")
 exit()
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


if token == "insert token here!":
 print("""초기 설정이 되어있지 않은 모양이에요 
 https://discord.com/developers/applications 이곳을 방문한 뒤
 setup.json 파일을 열어 수정해주세요
 """)
 exit()
elif toke == "":
 print("토큰 값이 비어있는 것 같아요 제대로된 토큰을 넣어주세요")
else:
 bot.run(f['token'])
