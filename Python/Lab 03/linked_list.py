class  Node(object):
   _value=0
   _next_=None
   def  __init__(self , value , next_=None):
      #assert next_==None or type(next_)==Node
      self._value = value
      self._next_ = next_
      
   def getvalue():
       return self._value
   def getnext():
       return self._next_
   def setvalue(value):
       self._value=value
   def setnext(next_=None):
       self._next_=next_
       
   def __iter__(self):
        cur=self._next_
        while cur!=None:
            print(cur._value)
            cur=cur._next_
        print()
    
def flatten_linked_list(node):
    list = []
    cur=node
    while cur!=None:
        if type(cur._value)==Node:
           map(lambda x:list.append(x),flatten_linked_list(cur._value))
        else:
           list.append(cur._value)
        cur=cur._next_
    return list
      
      
r1 = Node(1)# 1 -> None - just  one  node
r2 = Node(7, Node(2, Node(9)))# 7 -> 2 -> 9 -> None
# 3 -> (19 -> 25 -> None) -> 12 -> None
r3 = Node(3, Node(Node(19, Node(25)), Node(12)  ) )
r3_flattenned = flatten_linked_list(r3)# 3 -> 19 -> 25 -> 12 -> None
r3_expected_flattenned_collection = [3, 19, 25 , 12]
assert  r3_expected_flattenned_collection == list(r3_flattenned)