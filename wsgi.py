#@+leo-ver=5-thin
#@+node:2014fall.20141212095015.1775: * @file wsgi.py
# coding=utf-8
# 上面的程式內容編碼必須在程式的第一或者第二行才會有作用

################# (1) 模組導入區
# 導入 cherrypy 模組, 為了在 OpenShift 平台上使用 cherrypy 模組, 必須透過 setup.py 安裝


#@@language python
#@@tabwidth -4

#@+<<declarations>>
#@+node:2014fall.20141212095015.1776: ** <<declarations>> (wsgi)
import cherrypy
# 導入 Python 內建的 os 模組, 因為 os 模組為 Python 內建, 所以無需透過 setup.py 安裝
import os

################# (2) 廣域變數設定區
# 確定程式檔案所在目錄, 在 Windows 下有最後的反斜線
_curdir = os.path.join(os.getcwd(), os.path.dirname(__file__))
# 設定在雲端與近端的資料儲存目錄
if 'OPENSHIFT_REPO_DIR' in os.environ.keys():
    # 表示程式在雲端執行
    download_root_dir = os.environ['OPENSHIFT_DATA_DIR']
    data_dir = os.environ['OPENSHIFT_DATA_DIR']
else:
    # 表示程式在近端執行
    download_root_dir = _curdir + "/local_data/"
    data_dir = _curdir + "/local_data/"

'''以下為近端 input() 與 for 迴圈應用的程式碼, 若要將程式送到 OpenShift 執行, 除了採用 CherryPy 網際框架外, 還要轉為 html 列印
# 利用 input() 取得的資料型別為字串
toprint = input("要印甚麼內容?")
# 若要將 input() 取得的字串轉為整數使用, 必須利用 int() 轉換
repeat_no = int(input("重複列印幾次?"))
for i in range(repeat_no):
    print(toprint)
'''
#@-<<declarations>>
#@+others
#@+node:2014fall.20141212095015.1777: ** class Hello
################# (3) 程式類別定義區
# 以下改用 CherryPy 網際框架程式架構
# 以下為 Hello 類別的設計內容, 其中的 object 使用, 表示 Hello 類別繼承 object 的所有特性, 包括方法與屬性設計
class Hello(object):

    # Hello 類別的啟動設定
    _cp_config = {
    'tools.encode.encoding': 'utf-8',
    'tools.sessions.on' : True,
    'tools.sessions.storage_type' : 'file',
    'tools.sessions.locking' : 'explicit',
    # session 以檔案儲存, 而且位於 data_dir 下的 tmp 目錄
    'tools.sessions.storage_path' : data_dir+'/tmp',
    # session 有效時間設為 60 分鐘
    'tools.sessions.timeout' : 60
    }

    #@+others
    #@+node:2014fall.20141212095015.2004: *3* __init__
    def __init__(self):
        # 配合透過案例啟始建立所需的目錄
        if not os.path.isdir(data_dir+'/tmp'):
            os.mkdir(data_dir+'/tmp')
        if not os.path.isdir(data_dir+"/downloads"):
            os.mkdir(data_dir+"/downloads")
        if not os.path.isdir(data_dir+"/images"):
            os.mkdir(data_dir+"/images")
    #@+node:2014fall.20141212095015.1778: *3* index
    # 以 @ 開頭的 cherrypy.expose 為 decorator, 用來表示隨後的成員方法, 可以直接讓使用者以 URL 連結執行
    @cherrypy.expose
    # index 方法為 CherryPy 各類別成員方法中的內建(default)方法, 當使用者執行時未指定方法, 系統將會優先執行 index 方法
    # 有 self 的方法為類別中的成員方法, Python 程式透過此一 self 在各成員方法間傳遞物件內容
    def index(self, toprint="設計一甲 40323143 陳靖廷期末報告<br/>乘法表請在網址後輸入 /w11<br/>猜數字請在網址後輸入 /w15<br/>與程式互動請在網址後輸入/w16<br/>w16運作方法:<br/>更改列印內容請輸入?var1=想要列印的字串<br/>更改列印次數請輸入&var2=想要列印的次數<br/>第一次更改用? 第二次更改用&"):
        return toprint 

    #@+node:2014fall.20141212095015.1779: *3* hello
    @cherrypy.expose
    def hello(self, toprint="Hello World!"):
        return toprint
    #@+node:2015.20150109095437.1746: *3* w11
    @cherrypy.expose
    def w11(self):
        return"<html><head></head><body>1x1=1&nbsp;1x2=2&nbsp;1x3=3&nbsp;1x4=4&nbsp;1x5=5&nbsp;1x6=6&nbsp;1x7=7&nbsp;1x8=8&nbsp;1x9=9&nbsp;<br>2x1=2&nbsp;2x2=4&nbsp;2x3=6&nbsp;2x4=8&nbsp;2x5=10&nbsp;2x6=12&nbsp;2x7=14&nbsp;2x8=16&nbsp;2x9=18&nbsp;<br>3x1=3&nbsp;3x2=6&nbsp;3x3=9&nbsp;3x4=12&nbsp;3x5=15&nbsp;3x6=18&nbsp;3x7=21&nbsp;3x8=24&nbsp;3x9=27&nbsp;<br>4x1=4&nbsp;4x2=8&nbsp;4x3=12&nbsp;4x4=16&nbsp;4x5=20&nbsp;4x6=24&nbsp;4x7=28&nbsp;4x8=32&nbsp;4x9=36&nbsp;<br>5x1=5&nbsp;5x2=10&nbsp;5x3=15&nbsp;5x4=20&nbsp;5x5=25&nbsp;5x6=30&nbsp;5x7=35&nbsp;5x8=40&nbsp;5x9=45&nbsp;<br>6x1=6&nbsp;6x2=12&nbsp;6x3=18&nbsp;6x4=24&nbsp;6x5=30&nbsp;6x6=36&nbsp;6x7=42&nbsp;6x8=48&nbsp;6x9=54&nbsp;<br>7x1=7&nbsp;7x2=14&nbsp;7x3=21&nbsp;7x4=28&nbsp;7x5=35&nbsp;7x6=42&nbsp;7x7=49&nbsp;7x8=56&nbsp;7x9=63&nbsp;<br>8x1=8&nbsp;8x2=16&nbsp;8x3=24&nbsp;8x4=32&nbsp;8x5=40&nbsp;8x6=48&nbsp;8x7=56&nbsp;8x8=64&nbsp;8x9=72&nbsp;<br>9x1=9&nbsp;9x2=18&nbsp;9x3=27&nbsp;9x4=36&nbsp;9x5=45&nbsp;9x6=54&nbsp;9x7=63&nbsp;9x8=72&nbsp;9x9=81&nbsp;<br></body></html>" 
    w11.exposed = True
    #@+node:2015.20150109095437.1747: *3* w15
    @cherrypy.expose
    def w15(self):
            # This is a guess the number game.
            import random
            
            guessesTaken = 0
            
            print('Hello! What is your name?')
            myName = input()
            
            number = random.randint(1, 20)
            print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')
            
            while guessesTaken < 6:
                print('Take a guess.') # There are four spaces in front of print.
                guess = input()
                guess = int(guess)
            
                guessesTaken = guessesTaken + 1
            
                if guess < number:
                    print('Your guess is too low.') # There are eight spaces in front of print.
            
                if guess > number:
                    print('Your guess is too high.')
            
                if guess == number:
                    break
            
            if guess == number:
                guessesTaken = str(guessesTaken)
                print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
            
            if guess != number:
                number = str(number)
                print('Nope. The number I was thinking of was ' + number)
    w15.exposed = True
    #@+node:2015.20150109095437.1748: *3* w16
    @cherrypy.expose
        
    def w16(self,var1='hello',var2=2):
        outstring=' '
        for i in range(int(var2)):
            outstring += var1 +'<br />'
        return outstring
           
    w16.exposed = True  
    #@-others
#@-others
################# (4) 程式啟動區
# 配合程式檔案所在目錄設定靜態目錄或靜態檔案
application_conf = {'/static':{
        'tools.staticdir.on': True,
        # 程式執行目錄下, 必須自行建立 static 目錄
        'tools.staticdir.dir': _curdir+"/static"},
        '/downloads':{
        'tools.staticdir.on': True,
        'tools.staticdir.dir': data_dir+"/downloads"},
        '/images':{
        'tools.staticdir.on': True,
        'tools.staticdir.dir': data_dir+"/images"}
    }

if 'OPENSHIFT_REPO_DIR' in os.environ.keys():
    # 表示在 OpenSfhit 執行
    application = cherrypy.Application(Hello(), config=application_conf)
else:
    # 表示在近端執行
    cherrypy.quickstart(Hello(), config=application_conf)
#@-leo
