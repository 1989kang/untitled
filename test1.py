import time,functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        t1 = time.time()
        r = func(*args, **kw)
        print('%s excute in %s ms'%(func.__name__,1000*(time.time()-t1)))
        return  r
    return  wrapper
#@log
#def fast(x, y):
   # return  x+y
@log
def fast(x, y, z):
    time.sleep(0.1234)
    return  x+y+z
#@log
#def fast(x, y):
#    time.sleep(0.0012)
 #   return  x+y
#print(fast(3, 6))

print(fast(1, 2, 4))
