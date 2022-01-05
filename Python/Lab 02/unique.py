def compress():
   arrList=(1,2,1,3)
   arrdict={}
   arrRes=[]
   for i in arrList:
      if arrdict.has_key(i):
         arrdict[i]+=1
      else:
         arrdict[i]=1
   
   for i in arrdict:
      arrRes.append((i,arrdict[i]))
      
   return arrRes


print compress()