# coding:utf-8
import urllib.request
from lxml import html
from lxml import etree
from importlib import reload
import sys
import codecs

reload(sys)
#sys.setdefaultencoding("utf-8")


url = 'https://zh-cn.1.boardgamearena.com/incangold?table=39625878'


#
response = urllib.request.urlopen(url)
con = response.read().decode('UTF-8',errors="ignore") 
sel = html.fromstring(con)
#从文件打开，注意对有中文字符的网页要编码转换
#url = 'D:\\Z\\BGA\\Incan_Gold_Test.html'
#file = codecs.open(url,'r','utf-8').read()
#sel = etree.HTML(file)

        
# 所有的信息都在class属性为info的div标签里，可以先把这个节点取出来
for i in sel.xpath('//div[@id="overall-content"]//table[@id = "playArea"] \
        //div[@id = "table_wrap"]/div[@id="tablecards"]/div'):
    # 影片名称
    print(i.xpath("@style")[0])
    #pic_loc = i.xpath('@style')
    #print(pic_loc)
    #title = title.lstrip()
    #title = title.lstrip('\n')
    #title = title.rstrip()
    #title = title.rstrip('\n')
    #rateStr = i.xpath('div[@class="date"]/span/@class')[0]

    #rate = rateMapping.index(rateStr) + 1
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
    #print("No.%s" % str(k))
    #print(title, " ",rate)

    #k += 1
