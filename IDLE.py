from wxpy import Bot
from time import sleep
from traceback import format_exc
try:
    bot = Bot()
except KeyError:
    print('您的账号有问题，无法登录！')
    print(format_exc())
    exit(0)
friend = bot.friends().search(input('请输入朋友姓名：'))[0]
while True:
    try:
        friend.send("ॣ ॣ ॣ")
    except AttributeError:
        print('搜不到朋友！')
    else:
        break
msg = input('你要不断发送的消息：')
while True:
    try:
        interval = int(input('时间间隔（秒）：'))
    except ValueError:
        print('输入无效！')
    else:
        break
print('按下Ctrl - C停止')
try:
    while True:
        friend.send(msg)
        sleep(interval)
except KeyboardInterrupt:
    print('发送结束！')
