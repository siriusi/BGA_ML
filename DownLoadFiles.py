#!/usr/bin/env python
# -*- coding:utf-8 -*-

from gevent import monkey

monkey.patch_all()
from gevent.pool import Pool
import gevent
from lxml import html
import urllib.request
import requests
import sys
import threading
import os
import time


def Handler(start, end, url, filename):
    headers = {'Range': 'bytes=%d-%d' % (start, end)}
    r = requests.get(url, headers=headers, stream=True)

    # 写入文件对应位置
    with open(filename, "r+b") as fp:
        fp.seek(start)
        var = fp.tell()
        fp.write(r.content)


def download_file(url, oriURL, dirName, num_thread=5):

    #如果文件夹不存在则新建
    if not os.path.exists(dirName):
        os.makedirs(dirName)

    #整理URL，是之正确
    url = url.replace('./', oriURL, 1)
    #print(url)
    if url[0:4] != 'http':
        url = oriURL + url
    #print(url)
    url = url[0:len(url)-1] if url[-1] == '/' else url
    file_DirAndName = dirName + '\\' + url.split('/')[-1].strip()

    r = requests.head(url)
    try:
        file_size = int(
            r.headers['content-length'])  # Content-Length获得文件主体的大小，当http服务器使用Connection:keep-alive时，不支持Content-Length
    except:
        print("检查URL，或不支持多线程下载")
        return

    # 创建一个和要下载文件一样大小的文件
    fp = open(file_DirAndName, "wb")
    fp.truncate(file_size)
    fp.close()

    # 启动多线程写文件
    part = file_size // num_thread  # 如果不能整除，最后一块应该多几个字节
    for i in range(num_thread):
        start = part * i
        if i == num_thread - 1:  # 最后一块
            end = file_size
        else:
            end = start + part

        t = threading.Thread(target=Handler, kwargs={'start': start, 'end': end, 'url': url, 'filename': file_DirAndName})
        t.setDaemon(True)
        t.start()

    # 等待所有线程下载完成
    main_thread = threading.current_thread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        t.join()
    print('%s 下载完成' % file_DirAndName)


def download(url, oriURL, dirName):
    chrome = 'Mozilla/5.0 (X11; Linux i86_64) AppleWebKit/537.36 ' + '(KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'
    headers = {'User-Agent': chrome}

    #如果文件夹不存在则新建
    if not os.path.exists(dirName):
        os.makedirs(dirName)

    #整理URL，是之正确
    url = url.replace('./', oriURL, 1)
    #print(url)
    if url[0:4] != 'http':
        url = oriURL + url
    #print(url)
    url = url[0:len(url)-1] if url[-1] == '/' else url
    file_DirAndName = dirName + '\\' + url.split('/')[-1].strip()

    r = requests.get(url.strip(), headers=headers, stream=True)
    start_time = time.time()
    with open(file_DirAndName, 'wb') as f:

        block_size = 1024
        '''
        count = 1
        try:
            total_size = int(r.headers.get('content-length'))
            print('file total size :', total_size)
        except TypeError:
            print('using dummy length !!!')
            total_size = 10000000
       '''
        for chunk in r.iter_content(chunk_size=block_size):
            if chunk:
                '''
                duration = time.time() - start_time
                progress_size = int(count * block_size)
                if duration >= 2:
                    speed = int(progress_size / (1024 * duration))
                    percent = int(count * block_size * 100 / total_size)
                    sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" %
                                 (percent, progress_size / (1024 * 1024), speed, duration))
              '''
                f.write(chunk)
                f.flush()
                # count += 1

        print(file_DirAndName, " 完成！")

if __name__ == "__main__":
    #url = 'http://vision.stanford.edu/teaching/cs131_fall1415/schedule.html'
    url = 'http://cvgl.stanford.edu/teaching/cs231a_winter1415/schedule.html'
    #dirName = 'G:\\MachineLearning\\CS131_ComputerVision_FoundationsAndApplications'
    dirName = 'G:\\MachineLearning\\CS231A_ComputerVision_From3DReconstructionToRecognition'
    #oriURL = 'http://vision.stanford.edu/teaching/cs131_fall1415/'
    oriURL = 'http://cvgl.stanford.edu/teaching/cs231a_winter1415/'
    response = urllib.request.urlopen(url)
    con = response.read()
    sel = html.fromstring(con)

    # 定位到TR
    #tempTable = sel.xpath('//div[@id="content"]/div/table/tbody/tr')
    tempTable = sel.xpath('//div[@class="panel panel-default"]/table//tr')
    p = Pool(5)
    lastLectureNo = 1
    for i in range(0, len(tempTable)):
        tempTR = tempTable[i]
        tdList = tempTR.xpath('td//a/@href')

        #找出第几章节
        #lectureNoList = tempTR.xpath('td')[0].xpath('strong/text()')
        lectureNoList = tempTR.xpath('td')[0].xpath('text()')
        lectureNo = lastLectureNo if (len(lectureNoList) == 0 or not lectureNoList[0].isdigit()) else lectureNoList[0]
        lastLectureNo = lectureNo

        for downURL in tdList:
            print(downURL)
            subDirName = dirName + '\\Lecture' + lectureNo
            #download_file(downURL, oriURL, subDirName, 5)
            p.spawn(download, downURL, oriURL, subDirName)
    p.join()
            # if len(sys.argv) == 2:
            #    filename = sys.argv[1]
            # f = open(filename, "r")
'''
        for line in f.readlines():
            if line:
                p.spawn(download, line.strip())
                key = line.split('/')[-1].strip()
                removeLine(key, filename)
                f.close()
                p.join()
            else:
                print('Usage: python %s urls.txt' % sys.argv[0])
'''
