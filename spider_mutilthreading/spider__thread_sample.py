'''
python是支持多线程的，主要是通过thread和threading这两个模块来实现的。thread模块是比较底层的模块，threading模块是对thread做了一些包装的，可以更加方便的使用。
虽然python的多线程受GIL限制，并不是真正的多线程，但是对于I/O密集型计算还是能明显提高效率，比如说爬虫。

分别用两种方式获取10个访问速度比较慢的网页，一般方式耗时50s，多线程耗时10s。
'''

# -*-coding:utf-8 -*-
import urllib2, time
import threading


class MyThread(threading.Thread):
    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.args = args
        self.func = func

    def run(self):
        apply(self.func, self.args)


def open_url(url):
    request = urllib2.Request(url)
    html = urllib2.urlopen(request).read()
    print len(html)
    return html


if __name__ == '__main__':
    # 构造url列表
    urlList = []
    for p in range(1, 10):
        urlList.append('http://s.wanfangdata.com.cn/Paper.aspx?q=%E5%8C%BB%E5%AD%A6&p=' + str(p))

    # 一般方式
    n_start = time.time()
    for each in urlList:
        open_url(each)
    n_end = time.time()
    print 'the normal way take %s s' % (n_end - n_start)

    # 多线程
    t_start = time.time()
    threadList = [MyThread(open_url, (url,)) for url in urlList]
    for t in threadList:
        t.setDaemon(True)
        t.start()
    for i in threadList:
        i.join()
    t_end = time.time()
    print 'the thread way take %s s' % (t_end - t_start)
