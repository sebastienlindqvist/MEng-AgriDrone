import multiprocessing as mp
from multiprocessing import Process

print("Number of processors: ", mp.cpu_count())

#https://stackoverflow.com/questions/7207309/how-to-run-functions-in-parallel
#https://stackoverflow.com/questions/28549641/run-multiple-python-scripts-concurrently
#https://www.youtube.com/watch?v=fKl2JW_qrso&ab_channel=CoreySchafer


def func1():
  print ('func1: starting')
  for i in xrange(10000000): pass
  print ('func1: finishing')

def func2():
  print ('func2: starting')
  for i in xrange(10000000): pass
  print ('func2: finishing')


p1 = Process(target=func1)
p1.start()
p2 = Process(target=func2)
p2.start()
p1.join()
p2.join()
