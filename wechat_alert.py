#!/usr/bin/python
#coding=utf8
import urllib
import requests
import json
import sys

def GetToken():
    Corpid='ww3083060923921313121'
    CorpSecret='5_vWbwROiUQJkc2wBEPxkO0slPe2NsJ_qpvx2bW_M'
    gettoken_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + Corpid + '&corpsecret=' + CorpSecret
    #print  (gettoken_url)
    try:
        token_file =requests.get(gettoken_url)
    except Exception as e:
        print (e)
    token_data = token_file.text
    token_json = json.loads(token_data)
    token_json.keys()
    token = token_json['access_token']
    return token

def Send_Message(Token,Tag,Subject,Content):

    post_data={
       'touser' : '',
       'toparty' :'',
       'totag' : Tag,
       'msgtype' : 'text',
       'agentid' : 1000002,
       'text' : {
           'content' : Subject+'\n'+Content
       },
       'safe':0
    }

    #print (post_data)
    post_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='+Token
    #json_post_data = json.dumps(post_data,False,False)

    try:
        r =requests.post(post_url,data=json.dumps(post_data))
       # request_post = urllib.request.urlopen(post_url,json_post_data.encode(encoding='UTF8'))
    except Exception as e:
        print (e)
    #print (request_post.text)



if __name__ == '__main__':
    Corpid='ww308306023cc53c84'
    CorpSecret='5_vWbwROiUQJkc2wBEPsdPeGelovs2NsJ_qpvx2bW_M'
    #User = sys.argv[1]
    #Party=sys.argv[2]
    #Subject = sys.argv[3]
    #Content = sys.argv[4]
    Tag='2'
    Subject='服务器空间报警'
    Content='磁盘满啦'
    Token=GetToken()
    Send_Message(Token,Tag,Subject,Content)
