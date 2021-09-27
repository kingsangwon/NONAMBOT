import traceback
import time

ls = "================================================"
lines = 0

def ErrorLog(error: str): 
    current_time = time.strftime("%Y.%m.%d/%H:%M:%S", time.localtime(time.time())) 
    with open("Log.txt", "a") as f: 
        f.write(f"[{current_time}] - {error}\n")

def newline(gb):
    global lines
    while(lines < gb):
        print("")
        lines = lines + 1

class BotError:
    def deftoken(self):
        newline(30)
        print(f"""
{ls}
                    Error!!!
        초기 설정이 되어있지 않은 모양이에요 
https://discord.com/developers/applications 이곳을 방문한 뒤
        configuration.json 파일을 열어 수정해주세요
{ls}
""")

    def blanktoken(self):
        newline(30)
        print(f"""
{ls}
        토큰 값이 비어있는 것 같아요 제대로된 토큰을 넣어주세요
{ls}
""")

    def loginfail(self):
        newline(30)
        print(f"""
{ls}
        디스코드 로그인에 실패했어요. 토큰이 알맞은지, 공백이 없는지 확인해주세요.
{ls}
""")

    def unknown(self):
        newline(30)
        err = traceback.format_exc()
        print(f"""
{ls}
        알 수 없는 오류가 발생했습니다.
""")
        print(err)
        ErrorLog(err)
        print(f"""{ls}
오류 로그는 봇 "./Log.txt" 에 저장되었습니다
""")
