#!/usr/bin/env python
#coding:utf-8

import urllib2  #打包文件用;
import re
import codecs

class JianShuSpider(object):
    def __init__(self,baseUrl,output_name):
        self.baseUrl=baseUrl
        self.f = codecs.open(output_name, 'w', 'utf-8')

    def save_article_info(self,article_url):

        print u"正在爬取"+article_url
        
        my_article = urllib2.urlopen(article_url)
        article_html = my_article.read().decode('utf-8')

        self.save_name(article_html)
        self.save_time(article_html)
        self.save_title(article_html)
        self.f.write('\r\n')  #换行不行的话就+ "\r\n"

    def save_title(self,my_page):
        article_title = re.findall(
            r'<h1 class="title">(.*?)</h1>', my_page,re.S)
        self.f.write(u"发表了" + article_title[0])

    def save_name(self,my_page):
        article_name =re.findall(
            r'<span class="name"><a href=".*?">(.*?)</a></span>', my_page,re.S)
        self.f.write(article_name[0])

    def save_time(self,my_page):
        article_time =re.findall(
            r'<span class="publish-time".*?>(.*?)</span>',my_page, re.S)
        self.f.write(u"在" + article_time[0])

    def read(self):

        print u"开始爬取信息"+self.baseUrl

        my_page = urllib2.urlopen(self.baseUrl)
        html = my_page.read().decode('utf-8')  #读取页面代码;
        movie_items = re.findall(
            r'<a class="title" target="_blank" href="(.*?)">(.*?)</a>', html, re.S)

        for idx, item in enumerate(movie_items):
            self.save_article_info(self.baseUrl + item[0])


def main() :
    print u"""
        ###############################
            一个简单的简书爬虫
            Author: guo_mk
            Version: 0.0.1
            Date: 2017-12-08
        ###############################
    """
    baseURL = 'http://www.jianshu.com'
    output_name="test3.txt"

    my_spider = JianShuSpider(baseURL,output_name)
    my_spider.read()

if __name__ == '__main__':
    main()
