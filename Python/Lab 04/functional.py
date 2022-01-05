class BoundedMeta(type):
    max_instance_countmeta = 1
    max_instance_count = 0
    @classmethod
    def __prepare__(metacls, name, bases, **kargs):
        return super().__prepare__(name, bases, **kargs)
 
    def __new__(metacls, name, bases, namespace, **kargs):
        return super().__new__(metacls, name, bases, namespace)
 
    def __init__(cls, name, bases, namespace, max_instance_count = 1, **kargs):
        BoundedMeta.max_instance_count = max_instance_count
        super().__init__(name, bases, namespace)
 
    def __call__(self, *args, **kwargs):
        if BoundedMeta.max_instance_count is not None:
            if BoundedMeta.max_instance_countmeta > BoundedMeta.max_instance_count:
                raise TypeError

        BoundedMeta.max_instance_countmeta = BoundedMeta.max_instance_countmeta + 1
		
class C(metaclass = BoundedMeta , max_instance_count =2 ):
   pass
c1 = C ()
c2 = C ()
try :
   c3 = C ()
except TypeError :
   print ('everything works fine !')
else :
   print ('something goes wrong !')
   
   
   
from abc import ABCMeta, abstractmethod

class BoundedBase():
  @abstractmethod
  def get_max_instance_count(self):
          """"""
  instance_count=0
  def __init__(self):
     if BoundedBase.instance_count >= 1:
       raise TypeError
           
     BoundedBase.instance_count = BoundedBase.instance_count + 1

class D ( BoundedBase ):
  @classmethod
  def get_max_instance_count ( cls ):
    return 0
        
d1 = D ()
try :
  d2 = D ()
except TypeError :
  print ('everything works fine !')
else :
  print ('something goes wrong !')
  
  
def smart_function(func):
    RunCount = [0]
    def call_func():
        func()
        RunCount[0] += 1
        print("runcount:",RunCount[0])
    return call_func
@smart_function
def test():
    pass
test()
test()
test()
 