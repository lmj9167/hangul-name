#!C:\Users\lmj91\AppData\Local\Programs\Python\Python38-32\python.exe
print("content-type: text/html; charset=utf-8\n")
print()

import cgi
form = cgi.FieldStorage()
# pageId = form["id"].value
# print(pageId)
# title = form["title"].value
ename = "oliver, "+form['ename'].value
# print(ename)


import os #파파고
import urllib.request #파파고
import sys #파파고, 한글안깨지게

#한글안깨지게-------------------------------------------------------------
import io #한글안깨지게
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#--------------------------------------------------------------------------

#파파고 API
import json
client_id = "pYPi5eyooZX1N4eBzm9B" # 개발자센터에서 발급받은 Client ID 값
client_secret = "M5sQ_kZsEV" # 개발자센터에서 발급받은 Client Secret 값

#번역할 메모장 불러오기
# with open('source.py','r',encoding='utf8') as f:
#     srcText = f.read()

#'jackson, aiden, lucas, liam, noah, ethan, mason, caden, oliver, elijah'

encText = urllib.parse.quote(ename)
data = "source=en&target=ko&text=" + ename

url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    #print(response_body.decode('utf-8'))

    #json 형 변환
    res = json.loads(response_body.decode('utf-8'))
    from pprint import pprint
    # pprint(res)

    # 파일 생성
    with open('translate.txt', 'w',encoding='utf8')as f:
        f.write(res['message']['result']['translatedText'])

else:
    print("Error Code:" + rescode)


#외국인 이름을 한국이름으로 잘 번역되게 강화

#
# with open('source.py','r',encoding='utf8') as f:
#     delete = f.read()
if 'oliver, ' in ename:
    ename = ename.replace("oliver, ", "")
    with open('translate.txt','r',encoding='utf8') as f:
        kname = f.read()
    kname = kname.replace("올리버, ", "")
#리다이렉팅 실패 ㅜ
# print("Location: hangul_main?id="+title)
print("영문이름: ", form['ename'].value)
print("  / 한글이름: ", kname)
print("  / 한글 글자수: ", len(kname))
