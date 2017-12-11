#!/usr/bin/env python
#coding:utf-8

import urllib2  #打包文件用;
import re
import codecs
import urllib  #打包文件用;
import os  #打包文件用;

class JianShuSpider(object):
    def __init__(self, baseUrl, output_name):
        self.baseUrl = baseUrl
        self.f = codecs.open(output_name, 'w', 'utf-8')

    def save_article_info(self, article_url):

        print u"正在爬取" + article_url

        my_article = urllib2.urlopen(article_url)
        article_html = my_article.read().decode('utf-8')
        self.page = article_html

        self.save_name()
        self.save_time()
        self.save_pic()
        self.save_title()
        self.f.write('\r\n')  #换行不行的话就+ "\r\n"

    def save_title(self):
        article_title = re.findall(
          r'<h1 class="title">(.*?)</h1>', self.page, re.S)
        self.f.write(u"发表了" + article_title[0])

    def save_name(self):
        article_name = re.findall(
            r'<span class="name"><a href=".*?">(.*?)</a></span>', self.page,
            re.S)
        self.f.write(article_name[0])

    def save_time(self):
        article_time = re.findall(
            r'<span class="publish-time".*?>(.*?)</span>', self.page, re.S)
        self.f.write(u"在" + article_time[0])

    def save_pic(self):
        article_pic = re.findall(
          r'<div class="image-view".*?><img data-original-src="//(.*?)".*?></div>', self.page,re.S)
        path_name =  re.findall(
          r'<h1 class="title">(.*?)</h1>', self.page,re.S)
        self.save_article_pic(article_pic,path_name[0])
    def save_article_pic(self,article_pic,path_name):
        if len(article_pic)>0:
            for i in article_pic:
                print(i)
                #格式化图片格式
                url =  "http://"+i
                #获取图片后缀名
                file_suffix = os.path.splitext(url)[1]
                splitPath =url.split('/')
                # 根据后缀名设置图片名称
                if file_suffix == "":
                    fTail = splitPath.pop()+".jpeg"
                else:
                    fTail = splitPath.pop()
                #设置文件夹
                path=self.mkdir(path_name)
                print(fTail)

                #请求图片
                urllib.urlretrieve(url, path+'\{a}'.format(a=fTail))

    def mkdir(self,path):
        path = path
        r1 = u'[a-zA-Z’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}-~]+'#用户也可以在此进行自定义过滤字符
        tem=re.sub(r1, '', path) #过滤内容中的各种标点符号
        isExists=os.path.exists(tem)
        if not isExists:
                os.makedirs(tem)
          
        return tem

    def read(self):

        print u"开始爬取信息" + self.baseUrl

        my_page = urllib2.urlopen(self.baseUrl)
        html = my_page.read().decode('utf-8')  #读取页面代码;
        movie_items = re.findall(
            r'<a class="title" target="_blank" href="(.*?)">(.*?)</a>', html,
            re.S)

        for idx, item in enumerate(movie_items):
            self.save_article_info(self.baseUrl + item[0])


def main():
    print u"""
        ###############################
            一个简单的简书爬虫
            Author: guo_mk
            Version: 0.0.1
            Date: 2017-12-08
        ###############################
    """
    baseURL = 'http://www.jianshu.com'
    output_name = "my.txt"

    my_spider = JianShuSpider(baseURL, output_name)
    my_spider.read()


if __name__ == '__main__':
    main()
