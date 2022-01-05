import time
import random
import sys
import traceback

def handle_error(re_raise=True,log_traceback=True,exc_type=Exception,tries=1,delay=0,backoff=1):
    def decorator(f):
        def wrap(*args, **kwargs):
            times=tries
            exc_typeLoc=exc_type
            delayLoc=delay
            while times:
                try:
                    return f(*args, **kwargs)
                except exc_typeLoc:
                    if log_traceback:
                       exc_typetemp, exc_instance, exc_traceback = sys.exc_info()
                       formatted_traceback = ''.join(traceback.format_tb(exc_traceback))
                       message = '\n{0}\n{1}:\n{2}'.format(formatted_traceback,exc_typetemp.__name__,exc_instance)
                       print(message)
                    if re_raise  and times<2 :#the last try,should raise exception
                       raise exc_typeLoc(message)
                    
                    times -= 1
                    time.sleep(delayLoc)
                    delayLoc =backoff*delayLoc
                    continue
        return wrap
    return decorator

'''
# suppress exception , log traceback
@handle_error ( re_raise = False )
def some_function (): 
   x = 1 / 0 # ZeroDivisionError
some_function ()
print ( 1 ) # line will be executed as exception is suppressed
'''
'''
#re - raise exception and doesn 't log traceback as exc_type doesn't match
@handle_error ( re_raise =False , exc_type = KeyError )
def some_function (): 
   x = 1 / 0 # ZeroDivisionError
some_function ()
print ( 1 )
'''
'''
@handle_error ( re_raise =True , tries =3, delay =0.5 , backoff =2 )
def some_function ():
   if random.random () < 0.5:
      x = 1 / 0 # ZeroDivisionError
some_function ()
'''

class handle_error_context(object):
 
    def __init__(self, re_raise=True,log_traceback=True,exc_type=Exception):
        self.re_raise = re_raise
        self.log_traceback = log_traceback
        self.exc_type = exc_type

 
    def __enter__(self):
        return self
 
    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.log_traceback:
           #exc_type, exc_instance, exc_tb = sys.exc_info()
           formatted_traceback = ''.join(traceback.format_tb(exc_tb))
           message = '\n{0}\n{1}:\n{2}'.format(formatted_traceback,exc_type.__name__,exc_value)
           print(message)
        if self.re_raise:
           raise exc_type(message)
                    
                    
        return True
 
# log traceback , re - raise exception
with handle_error_context ( log_traceback =True , exc_type = ValueError ):
   raise ValueError ()