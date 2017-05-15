# #coding=utf-8
import urllib2
import cookielib
import urllib

#
# # #coding=utf-8
# import urllib2
# import cookielib
# import urllib
# loginUrl = 'http://demo.duokongkeji.com/user/login'  # 登录教务系统的URL，成绩查询网址
# # #创建MozillaCookieJar实例对象
# cookie = cookielib.MozillaCookieJar()
# #从文件中读取cookie内容到变量
# cookie.load('cookie99.txt', ignore_discard=True, ignore_expires=True)
# #创建请求的request
# req = urllib2.Request("http://demo.duokongkeji.com/scan/scanproductview/productlist")
# #利用urllib2的build_opener方法创建一个opener
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# response = opener.open(req)
# print response.read()
#
# # 第二步模拟登陆并保存登录的cookie
# filename = 'cookie99.txt'  # 创建文本保存cookie
# mycookie = cookielib.MozillaCookieJar(filename)  # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
#
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(mycookie))  # 定义这个opener，对象是cookie
#
# # 第三步利用cookie请求访问另一个网址，教务系统总址
# gradeUrl = 'http://demo.duokongkeji.com/scan/scanproductview/productlist'  # 只要是帐号密码一样的网址就可以， 请求访问成绩查询网址
# result = opener.open(gradeUrl)
# print result.read()



# 第一步先给出账户密码网址准备模拟登录
# postdata = urllib.urlencode({
#     'username': 'admin2',
#     'Password': '111111',
#     'rememberMe': 'true',
# })
# loginUrl = 'http://www.lenovo.com.cn/index.html'  # 登录教务系统的URL，成绩查询网址
# req = urllib2.Request(loginUrl)
# # 第二步模拟登陆并保存登录的cookie
# filename = 'cookie888.txt'  # 创建文本保存cookie
# mycookie = cookielib.MozillaCookieJar(filename)  # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(mycookie))  # 定义这个opener，对象是cookie
# result = opener.open(loginUrl)
#
# mycookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
# print result.read()

# # 第三步利用cookie请求访问另一个网址，教务系统总址
# gradeUrl = 'http://demo.duokongkeji.com/scan/scanproductview/productlist'  # 只要是帐号密码一样的网址就可以， 请求访问成绩查询网址
# result = opener.open(loginUrl)
# print result.read()

import cookielib
import urllib2,time
# 创建MozillaCookieJar实例对象
cookie = cookielib.MozillaCookieJar()
# 从文件中读取cookie内容到变量
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# 创建请求的request
req = urllib2.Request("http://www.lenovo.com.cn/index.html")
# 利用urllib2的build_opener方法创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()
mobile = '17606567116'
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    "Referer" : "http://www.lenovo.com.cn/index.html"
}
r = str(int(round(time.time() * 1000)))
data1 = urllib.urlencode({
    'mobile': mobile,
    'callback':'response.getMobileCaptCode',
    '_' :r
})
url1 = "http://reg.lenovo.com.cn/captcha/mobile/show?"+data1
Request = urllib2.Request(url1,headers=header)
Res = opener.open(Request)
# Res = urllib2.urlopen(Request)
print Res.read()









# # coding=utf-8
# import urllib
# import urllib2
# import cookielib
#
#
#
# loginUrl = "http://www.lenovo.com.cn/index.html"
# filename = 'cookie222.txt'  # 创建文本保存cookie
# mycookie = cookielib.MozillaCookieJar(filename)  # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(mycookie))  # 定义这个opener，对象是cookie
# result = opener.open(loginUrl)
# mycookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中


# filename = 'mycookies2.txt'
# #声明一个类对象保存
# mycookie = cookielib.MozillaCookieJar(filename)
# #cookie的处理器
# handler = urllib2.HTTPCookieProcessor(mycookie)
# #构造opener
#
# opener = urllib2.build_opener(handler)
# response = opener.open("")
# for item in mycookie:
#     print "name="+item.name
#     print "value="+item.value
#
# mycookie.save(filename,ignore_discard=True, ignore_expires=True)
# mobile = '17606567117'
#
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
#     "Referer" : "http://www.lenovo.com.cn/index.html"
# }
# r = str(int(round(time.time() * 1000)))
# data1 = urllib.urlencode({
#     'mobile': mobile,
#     'callback':'response.getMobileCaptCode',
#     '_' :r
# })
# url1 = "http://reg.lenovo.com.cn/captcha/mobile/show?"+data1
# print url1
# Request = urllib2.Request(url1,headers=header)
# Res = urllib2.urlopen(Request)
# print Res.read()

