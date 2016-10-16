'''
GIL无疑就是一把全局排他锁。毫无疑问全局锁的存在会对多线程的效率有不小影响。甚至就几乎等于Python是个单线程的程序。
那么读者就会说了，全局锁只要释放的勤快效率也不会差啊。只要在进行耗时的IO操作的时候，能释放GIL，这样也还是可以提升运行效率的嘛。或者说再差也不会比单线程的效率差吧。理论上是这样，而实际上呢？Python比你想的更糟。

下面我们就对比下Python在多线程和单线程下得效率对比。
一个通过单线程执行两次，一个多线程执行。
'''

# -*- coding: utf-8 -*-
from threading import Thread
import time
def my_counter():
	i = 0
	for _ in range(10000000):
		i = i + 1
	return True
def main():
	thread_array = {}
	start_time = time.time()
	for tid in range(2):
		t = Thread(target=my_counter)
		thread_array[tid] = t
	for i in range(2):thread_array[i].start()
        thread_array[i].join()
	end_time = time.time()
	print("Total time: {}".format(end_time - start_time))
if __name__ == '__main__':
	main()