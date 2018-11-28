
# -*- coding:utf-8 -*-
from api.CorpApi import CorpApi, CORP_API_TYPE
from api.AbstractApi import ApiException
from Conf import config


import random


if __name__ == "__main__":


    #企业号通讯录管理 创建联系人、查询联系人、删除联系人
    client = CorpApi(config['CORP_ID'], config['CONTACT_SYNC_SECRET'])
    try :
        ##新建联系人
        result = client.httpCall(
                CORP_API_TYPE['USER_CREATE'],
                {
                    'userid' : 'zhangsan',
                    'name' : 'zhangsanfeng',
                    'mobile' : '131488888888',
                    'email' : 'zhangsan@ipp.cas.cn',
                    'department' : 1,
                })
        if result.get('errCode',-1) == 0 :
            print('联系人创建成功！')
        else:
            print(result.get('errMsg'))


       

        ##
        result = client.httpCall(
                CORP_API_TYPE['USER_GET'],
                { 
                    'userid' : 'zhangsan',
                })
        print (result)

        ##
        result = client.httpCall(
                CORP_API_TYPE['USER_DELETE'],
                { 
                    'userid' : 'zhangsan',
                })
        print (result)

    except ApiException as e :
        print (e.errCode, e.errMsg)
        
    #自建已用发送信息
    client2 = CorpApi(config['CORP_ID'], config['APP_SECRET'])
    try :
    ##
        response = client2.httpCall(
                CORP_API_TYPE['MESSAGE_SEND'],
                {
                    "touser": "LiaoYongMing",
                    "agentid": 1000002,
                    'msgtype' : 'text',
                    'climsgid' : 'climsgidclimsgid_%f' % (random.random()),
                    'text' : {
                        'content':'我是文本消息热爱祖国热爱人民热爱中国共产党我是文本消息热爱祖国',
                    },
                    'safe' : 0,
                })
        print (response) 
    except ApiException as e :
        print (e.errCode, e.errMsg)