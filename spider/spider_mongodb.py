# -*- coding: utf-8 -*-
"""
Created on Sun Oct 02 08:17:27 2016

@author: hexiaosong
"""

# coding=utf-8
import re
import requests
from lxml import etree
import pymongo
import sys


reload(sys)
sys.setdefaultencoding('utf-8')

 
def getpages(url, total):
  nowpage = int(re.search('(\d+)', url, re.S).group(1))
  urls = []
 
  for i in range(nowpage, total + 1):
    link = re.sub('(\d+)', '%s' % i, url, re.S)
    urls.append(link)
 
  return urls
  
def spider(url):
  html = requests.get(url)
 
  selector = etree.HTML(html.text)

  book_url = [] 
 
  book_name = selector.xpath('//*[@id="container"]/ul/li//div/div[2]/a/text()')
  book_author = selector.xpath('//*[@id="container"]/ul/li//div/div[2]/div/a/text()')
  book_url_temp = selector.xpath('//*[@id="container"]/ul/li/div/div[2]/a/@href')
  for url in book_url_temp:
      temp = 'http://readfree.me/'+url
      book_url.append(temp)
  saveinfo(book_name, book_author,book_url)
 
def saveinfo(book_name, book_author,book_url):
  connection = pymongo.MongoClient()
  BookDB = connection.BookDB
  BookTable = BookDB.books
 
  length = len(book_name)
 
  for i in range(0, length):
    books = {}
    books['name'] = str(book_name[i]).replace('\n','').strip()
    books['author'] = str(book_author[i]).replace('\n','').strip()
    books['url'] = str(book_url[i])
    BookTable.insert_one(books)
    
if __name__ == '__main__':
  url = 'http://readfree.me/shuffle/?page=1'
  urls = getpages(url,3)
 
  for each in urls:
    spider(each)
  print "All Done !"
