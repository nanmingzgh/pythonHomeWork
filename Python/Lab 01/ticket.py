
def get_nearest_lucky_ticket(tickeyNumStr):
   tickeyNumOrg=int(tickeyNumStr)
   OffSetInt=1
   while OffSetInt>0:
     #print OffSetInt
     if tickeyNumOrg+OffSetInt>0 and Is_lucky_ticket(tickeyNumOrg+OffSetInt):
        return tickeyNumOrg+OffSetInt
     if tickeyNumOrg-OffSetInt>0 and Is_lucky_ticket(tickeyNumOrg-OffSetInt):
        return tickeyNumOrg-OffSetInt
     OffSetInt+=1
   
   

def Is_lucky_ticket(tickeyNum):
   tickeyNumStr=str(tickeyNum)
   tickeyNumStrArrOdd=tickeyNumStr[0::2]
   tickeyNumStrArrEven=tickeyNumStr[1::2]
   tickeyNumStrArrOddSum=0
   tickeyNumStrArrEvenSum=0
   for tickeyNumStrArrSingle in tickeyNumStrArrOdd:
     tickeyNumStrArrOddSum+=int(tickeyNumStrArrSingle)
   for tickeyNumStrArrSingle in tickeyNumStrArrEven:
     tickeyNumStrArrEvenSum+=int(tickeyNumStrArrSingle)
   
   return tickeyNumStrArrOddSum==tickeyNumStrArrEvenSum
       
       
print get_nearest_lucky_ticket('0923432');