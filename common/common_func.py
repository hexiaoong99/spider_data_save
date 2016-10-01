# coding:utf-8
'''
Create on 2016/10/1 21:14
@author: hexiaosong

'''

import urllib2
import os
import requests
from lxml import etree


def show_path():
   print '当前路径为:'+os.getcwd()

def set_path(url):
   os.chdir(url)
   print '当前路径为：'+os.getcwd()

def getHTML(url):
    '''获取页面(str类型)
    @url:页面url
    @return:页面字符串
    '''
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
             'Accept':'text/html;q=0.9,*/*;q=0.8',
             'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
             'Accept-Encoding':'gzip',
             'Connection':'close',
             'Referer':None #注意如果依然不能抓取的话，这里可以设置抓取网站的host
            }
    try:
        request = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(request)
        html = response.read()
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason
    return html

def getHTML_str (url):
    '''通过request获取页面字符串
    @param url:页面url
    @return:页面字符串
    '''
    html = requests.get(url)
    page = html.text
    return page

def save_html (content,path):
   '''
   @param content:保存字符内容
   :param path:保存路径
   :return:无返回
   '''
   file = open(path,'w')
   file.write(content)
   file.close()


def save_image (content,path):
    '''
    @param content:保存图片内容
    @param path:保存路径
    '''
    file = open(path,'wb')
    file.write(content)
    file.close()

def  sub_xml_html_show (Nodes_block):
    #使用lxml解析网页，截取局部，显示成字符串
	temp = etree.tostring(Nodes_block, pretty_print=True)
	print temp

def xml_html (url):
    #使用lxml解析网页，输入url，返回解析过后的对象
	html = requests.get(url)
	page_code = html.encoding
	page = html.text.encode(page_code)
	e_html = etree.HTML(page)
	return e_html

def grep(pattern,vector):
    #类似于R语言的grep()函数
    import re
    result = list()
    for i in vector:
        temp = re.findall(re.compile(pattern),i)
        if len(temp)>0:
          result.append(i)
    return result