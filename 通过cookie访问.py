import urllib2
import cookielib

filename = 'myCookie.txt'

cookie = cookielib.MozillaCookieJar(filename)

handler = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(handler)

response = opener.open('http://www.baidu.com')

cookie.save(ignore_discard=True, ignore_expires=True)

result = opener.open("http://i.baidu.com/")

print result.read().decode('utf-8')