# /usr/bin/env python
# coding=utf8
import http
import hashlib
import urllib.request
import random
import json

while True:
    fin = open(r'G:\MachineLearning\Coursera\machine-learning-ex8\machine-learning-ex8\ex8\movie_ids.txt', 'r')               #以读的方式打开输入文件
    fout = open(r'G:\MachineLearning\Coursera\machine-learning-ex8\machine-learning-ex8\ex8\2.txt', 'w')             #以写的方式打开输出文件
    for eachLine in fin:
        appid = '20180110000113508'    #参考百度翻译后台，申请appid和secretKey
        secretKey = 'icVksvKMHTNASJ8bWw7u'
        httpClient = None
        myurl = '/api/trans/vip/translate'
        q = eachLine.strip()                   #文本文件中每一行作为一个翻译源
        fromLang = 'en'                         #中文
        toLang = 'zh'                             #英文
        salt = random.randint(32768, 65536)
        sign = appid+q+str(salt)+secretKey
        sign = sign.encode('UTF-8')
        m1 = hashlib.md5()
        m1.update(sign)
        sign = m1.hexdigest()
        myurl = myurl+'?appid='+appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        #response是HTTPResponse对象
        response = httpClient.getresponse()
        html= response.read().decode('UTF-8')
        #print(html)
        target2 = json.loads(html)
        src = target2["trans_result"][0]["dst"]
        #print(src)#取得翻译后的文本结果,测试可删除注释
        outStr = src
        fout.write(outStr.strip() + '\n')
    fin.close()
    fout.close()
    print('翻译成功，请查看文件')
    break
'''
reload(sys)

import requests


def fanyi():
    while True:
        context = input("请输入翻译的内容(退出q)：")

        if context in ['q', 'Q']:
            break
        else:
            url = 'http://fanyi.baidu.com/v2transapi/'
            data = {
                'from': 'en',
                'to': 'zh',
                'query': context,
                'transtype': 'translang',
                'simple_means_flag': '3',
            }
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0'}
            response = requests.post(url, data, headers=headers)
            head = response.headers

            # text = response.text
            # text = json.loads(text)
            # res = text['trans_result']['data'][0]['dst']
            # print(res)
            print(head['Content-Type'])
            print(response.json()['trans_result']['data'][0]['dst'])


fanyi()
'''

'''
url = 'http://fanyi.baidu.com/?aldtype=85#en/zh/Clerks'

response = urllib.request.urlopen(url)
con = response.read()

sel = html.fromstring(con)

word = sel.xpath('//div[@id="transOtherResutl"]//strong[@class="dict-comment-mean"]/text()')
print(word)
# 所有的信息都在class属性为info的div标签里，可以先把这个节点取出来

for i in sel.xpath('//div[@class="item-show"]'):
    # 影片名称
    title = i.xpath('div[@class="title"]/a/text()')[0]
    title = title.lstrip()
    title = title.lstrip('\n')
    title = title.rstrip()
    title = title.rstrip('\n')
    rateStr = i.xpath('div[@class="date"]/span/@class')[0]
'''
