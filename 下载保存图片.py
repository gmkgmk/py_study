#!/usr/bin/env python
#coding:utf-8

import urllib  #打包文件用;
import os  #打包文件用;

import os
path = "assets"
isExists=os.path.exists(path)

if not isExists:
  os.makedirs(path)

# url = "https://pic1.zhimg.com/50/20aee78682f79a45b70cc83a0e5902f8_hd.jpg"
url = "https://pic1.zhimg.com/50/20aee78682f79a45b70cc83a0e5902f8_hd.jpg"
file_suffix = os.path.splitext(url)[1]
print(file_suffix)
if file_suffix == "":
  file_suffix="jpeg"

splitPath =url.split('/')
fTail = splitPath.pop()
print(fTail)

urllib.urlretrieve(url, path+'\{a}.{b}'.format(a=fTail,b=file_suffix))
