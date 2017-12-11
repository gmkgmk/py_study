#!/usr/bin/env python
#coding:utf-8


import urllib2  #打包文件用;
import re 
import codecs

url = "http://movie.douban.com/top250?start={page}&filter=&type="

arr = []

def read(my_page) :
  print(my_page)
  html = my_page.read().decode('utf-8') #读取页面代码;
  movie_items = re.findall('<span class="title">(.*?)</span>', html, re.S)
  for idx, item in enumerate(movie_items):
    if item.find("&nbsp") == -1 :
      arr.append(item);

i = 1
while  i<= 2 :
  my_page = urllib2.urlopen(url.format(page=i))
  read(my_page)
  i+=1;

# 一:
# f = codecs.open("test.txt",'w','utf-8')
# f.write(u'中文')

# 二:
# f = codecs.open("test.txt",'w','utf-8')
# f.write('\n,'.join(arr))  

#三
f = codecs.open("test.txt", 'w', 'utf-8')
for idx, item in enumerate(arr):
    f.write(str(idx + 1) + "\n" + ":" + item + "\n" + ";")
    f.write('\r\n')#换行不行的话就+ "\r\n"

f.close()
