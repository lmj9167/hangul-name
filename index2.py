#!C:\Users\lmj91\AppData\Local\Programs\Python\Python38-32\python.exe
import cgi

import sys #파파고, 한글안깨지게


#한글안깨지게-------------------------------------------------------------
import io #한글안깨지게
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
print("content-type: text/html; charset=utf-8\n")
#--------------------------------------------------------------------------

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form['id'].value
    description = open('data/'+pageId, 'r').read()
else:
    pageId = 'welcome'
    description = ''

print('''
<html>
<head>
<title>My Hangul</title>
<meta charset="utf-8"/>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body>
<h1><a href="index2.py">My Hangul</a></h1>



    <form action="create.py" method="post">

        <label for="name">Hangul Name Making</label>
        <br>
        <!--이름 입력칸-->
        <input type="text" name="ename" placeholder="Enter your name" autofocus maxlength="8">

        <!--전송 버튼-->
        <input type="submit" value="Make">
<p>ex) jackson, aiden, lucas, liam, noah, ethan, mason, caden, oliver, elijah</p>
        <br>
        <br>

    </form>


<p>{desc}</p>
</body>
</html>

'''.format(title=pageId, desc=description))
