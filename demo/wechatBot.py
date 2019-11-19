'''
@File : wechatBot.py
@Author : liruichuan
@Date: 2019/11/19
@Desc: 微信机器人
'''
#导入模块
from wxpy import *

def qr_callback():
    print("获取二维码")

def login_callback():
    print("登录回调")

def logout_callback():
    print("登出回调")

#cache_path保持登录，Bot初始化中可以加入参数：console_qr是否在控制台显示二维码
#bot = Bot(cache_path=True,qr_callback=qr_callback,login_callback=login_callback,logout_callback=logout_callback)
bot = Bot(cache_path=True)

# 给机器人自己发送消息
bot.self.send('Hello World!')
bot.logout()


