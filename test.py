import  functools
def log(func):
    '''@functools.wraps(func)'''
    def wrapper(*args, **kw):
        print(' 执行 %s()' %func.__name__)
        return  func(*args, **kw)
    return  wrapper
@log
def now():
    print('日志')
now()
