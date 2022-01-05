#@profile
import timeit

#Task 3
def clock(func):
    def clocked(*args, **kwargs):
        start = timeit.default_timer()
        res = func(*args, **kwargs)
        run_time = timeit.default_timer() - start
        func_name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('call>>>%s(%s)   return>>>%r   timeout>>>%0.8fs' % (func_name, arg_str, res, run_time))
        return res

    return clocked
@clock
def  func ():
   return  sum(range(1000))
#if __name__ == '__main__':
#    func()
    
    
#Task 4    
class timer(object):
 
    def __init__(self):
        self.start = timeit.default_timer()

 
    def __enter__(self):
        return self
 
    def __exit__(self, exc_type, exc_value, exc_tb):
        print("runtime:",timeit.default_timer()-self.start)
                    
                    
        return True
with timer():
   print(sum(range(1000)))
