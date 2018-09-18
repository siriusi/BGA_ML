# -*- coding: utf-8 -*-
"""
Created on Thu May  3 11:06:12 2018
想写一个从繁体翻译成简体的脚本，不过没有成功，目前卡在翻译模块module_url的解析没有成功，不知道什么原因
@author: Z
"""
import urllib.request
from lxml import etree
from importlib import reload
import sys
import codecs
from langconv import Converter

reload(sys)
#sys.setdefaultencoding("utf-8")


#module_url = 'https://zh-cn.boardgamearena.com/translation?module_id=1126&source_locale=zh_TW&dest_locale=zh_CN&refreshtemplate=1&dojo.preventCache=1525318818027'
url = 'https://zh-cn.boardgamearena.com/#!translation?module_id=1119&source_locale=en_US&dest_locale=zh_CN&page=1'

response = urllib.request.urlopen(url)

con = response.read().decode('UTF-8',errors="ignore") 
print(con)
#sel = etree.XML(con)
#sel = sel.xpath('//div[@style="display:block"]/div')[0]
#for i in sel.xpath('/div'):
#    print("????")
#    print(i)
    
    
simplified = "${player_name} 使用了骰子 (${dice_numeric}) 和移動了一個棋"
print(simplified)
traditional = Converter('zh-hans').convert(simplified)
print(traditional)
