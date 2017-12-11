#!/usr/bin/env python
#coding:utf-8


import urllib2  #打包文件用;
import re 
import codecs

url = "http://www.jianshu.com/trending/weekly?seen_snote_ids%5B%5D=20360178&seen_snote_ids%5B%5D=20250480&seen_snote_ids%5B%5D=20400190&seen_snote_ids%5B%5D=20513670&seen_snote_ids%5B%5D=20363375&seen_snote_ids%5B%5D=20218991&seen_snote_ids%5B%5D=20251650&seen_snote_ids%5B%5D=20330068&seen_snote_ids%5B%5D=20398412&seen_snote_ids%5B%5D=20551635&seen_snote_ids%5B%5D=20364281&seen_snote_ids%5B%5D=20224903&seen_snote_ids%5B%5D=20301380&seen_snote_ids%5B%5D=20300513&seen_snote_ids%5B%5D=20505858&seen_snote_ids%5B%5D=20417199&seen_snote_ids%5B%5D=19155100&seen_snote_ids%5B%5D=20305060&seen_snote_ids%5B%5D=20295723&seen_snote_ids%5B%5D=19930869&page={page}"

arr = []

def read(my_page) :
  html = my_page.read().decode('utf-8') #读取页面代码;
  
  movie_items = re.findall(r'<a class="title" target="_blank" href="(.*?)">(.*?)</a>', html, re.S)
  for idx, item in enumerate(movie_items):
      arr.append(item[1]);

i = 1
while  i<= 10 :
  my_page = urllib2.urlopen(url.format(page=i))
  read(my_page)
  i+=1;

f = codecs.open("test1.txt", 'w', 'utf-8')
for idx, item in enumerate(arr):
    f.write(str(idx + 1) + "\n" + ":" + item + "\n" + ";")
    f.write('\r\n')#换行不行的话就+ "\r\n"

f.close()
