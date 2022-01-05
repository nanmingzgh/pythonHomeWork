import itertools;
##Task 1
def transpose(list):
   return zip(*list)
   
print transpose([[1, -1], [2, 3]])


##Task 2
def scalar_product(list1,list2):
   list1=map(getNumber,list1)
   list2=map(getNumber,list2)
   product = [x*y for x,y in zip(list1,list2)]
   return sum(product)

def getNumber(s):
    try:
        float(s)
        return float(s)
    except ValueError:
        pass
                
    try:
        int(s)
        return int(s)
    except ValueError:
        pass
        
    if s[:2] not in ['0b','0B','0O','0o','0X','0x']:return None
    
    try:
        int(s,2)
        return int(s,2)
    except ValueError:
        pass
        
    try:
        int(s,8)
        return int(s,8)
    except ValueError:
        pass
         
    try:
        int(s,16)
        return int(s,16)
    except ValueError:
        pass
        
    return None
print scalar_product(["0120", "0o2"], [-1, 1])
