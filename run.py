from description import BotError
import discord, os, json
from discord.ext import commands

ls = "================================================"
BotError = BotError()
try:
    f = json.loads(open("configuration.json", "r").read())
    token = f['token']
except:
    print("configuration.json 파일을 불러오는데 오류가 발생했어요 파일이 존재하거나 읽기 권한을 확인해주세요")
    exit()
bot = commands.Bot(command_prefix="%", intents=discord.Intents.all())
print(ls)
for cogs in os.listdir("cogs"):
    if cogs.endswith(".py"):
        bot.load_extension(f"cogs.{cogs[:-3]}")
        print(f"cogs.{cogs[:-3]}을 성공적으로 로드했어요!")
print(ls)
@bot.event
async def on_ready():
    print(f"""
{ls}
{bot.user.name} 에 성공적으로 로그인했어요
봇의 ID는 다음과 같아요 "{bot.user.id}"
{ls}
""")


if token == "insert token here!":
    BotError.deftoken()
    exit()
elif token == "":
    BotError.blanktoken()
else:
    try:
        bot.run(token)
    except discord.errors.LoginFailure:
        BotError.unknown()
        exit()
