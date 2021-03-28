import requests
import json
import re
import sys

if __name__ == "__main__":
    getToken_url = 'https://qczj.h5yunban.com/qczj-qndxx/cgi-bin/login/we-chat/callback'
    getUserInfo_url = 'https://qczj.h5yunban.com/qczj-qndxx/cgi-bin/user-api/course/last-info'
    getClass_url = 'https://qczj.h5yunban.com/qczj-qndxx/cgi-bin/common-api/course/current'
    checkin_url = 'https://qczj.h5yunban.com/qczj-qndxx/cgi-bin/user-api/course/join'
    openId = {
        'appid':'wx56b888a1409a2920',
        'openid': ''#在这里填入你的openId，至于openId的获得，可使用Fiddler等抓包软件
    }
    headers = {
        'Content-Type': 'text/plain'
    }
    try:
        getToken = requests.get(url=getToken_url,params=openId,headers=headers)
        Token_raw = getToken.text

        Token = re.findall('[A-Z0-9]{8}[-][A-Z0-9]{4}[-][A-Z0-9]{4}[-][A-Z0-9]{4}[-][A-Z0-9]{12}', Token_raw)[0]
        print('获取Token为:'+Token)
    except:
        print('获取Token失败，请检查openId是否正确')
    accessToken = {
        'accessToken':Token
    }
   
    checkinData = {
        'course': "",#在这里输入大学习期次的代码，例如C0046
        'subOrg':None,
        'nid':"",#在这里输入你的团组织编号，如N003************，一样请使用抓包软件获取
        'cardNo':"" #在这里输入你打卡时用的昵称，不写也行
    }


    checkin = requests.post(checkin_url,params=accessToken,data=json.dumps(checkinData),headers=headers)
    result = checkin.json()

    if(result["status"]==200):
        print("签到成功")
    else:
        print('出现错误，错误码：')
        print(result["status"])
        print('错误信息：'+result["message"])
    input('按任意键关闭')
    sys.exit(0)
