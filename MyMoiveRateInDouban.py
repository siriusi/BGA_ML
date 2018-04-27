# coding:utf-8
import urllib.request
from lxml import html
from importlib import reload
import sys

reload(sys)
#sys.setdefaultencoding("utf-8")

k = 1
for j in range(0,11):

    url = 'https://movie.douban.com/people/47048452/collect?sort=time&amp;start='+str(j * 30)
    url += '&amp;filter=all&amp;mode=list&amp;tags_sort=count'
    #url = 'https://movie.douban.com/top250?start={}&filter='.format(i * 25)
    response = urllib.request.urlopen(url)
    con = response.read()

    sel = html.fromstring(con)

    rateMapping = ['rating1-t','rating2-t','rating3-t','rating4-t','rating5-t']
    # 所有的信息都在class属性为info的div标签里，可以先把这个节点取出来
    for i in sel.xpath('//div[@class="item-show"]'):
        # 影片名称
        title = i.xpath('div[@class="title"]/a/text()')[0]
        title = title.lstrip()
        title = title.lstrip('\n')
        title = title.rstrip()
        title = title.rstrip('\n')
        rateStr = i.xpath('div[@class="date"]/span/@class')[0]

        rate = rateMapping.index(rateStr) + 1
        # 导演演员信息
        #info_1 = info[0].replace(" ", "").replace("\n", "")
        # 上映日期
        #date = info[1].replace(" ", "").replace("\n", "").split("/")[0]
        # 制片国家
        #country = info[1].replace(" ", "").replace("\n", "").split("/")[1]
        # 影片类型
        #geners = info[1].replace(" ", "").replace("\n", "").split("/")[2]
        # 评分
        #rate = i.xpath('//span[@class="rating_num"]/text()')[0]
        # 评论人数
        #comCount = i.xpath('//div[@class="star"]/span[4]/text()')[0]

        # 打印结果看看
        print("No.%s" % str(k))
        print(title, " ",rate)

        k += 1
'''
        # 写入文件
        with open("top250.txt", "a") as f:
            f.write(
                "TOP%s\n影片名称：%s\n评分：%s %s\n上映日期：%s\n上映国家：%s\n%s\n" % (k, title, rate, comCount, date, country, info_1))

            f.write("==========================\n")
        
'''
