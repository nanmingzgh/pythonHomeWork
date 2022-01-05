def merge(arr1,arr2):
   arrMerge=[]
   arr1Index=0
   arr2Index=0
   while arr1Index<len(arr1) and arr2Index < len(arr2):
      if 1==1 :
         if arr1Index>len(arr1)-1   :
            break
         if arr1[arr1Index]>arr2[arr2Index]:
            arrMerge.append(arr2[arr2Index])
            arr2Index+=1
            continue
         if arr1[arr1Index]<arr2[arr2Index]:
            arrMerge.append(arr1[arr1Index])
            arr1Index+=1
            continue
         if arr1[arr1Index]==arr2[arr2Index]:
            arrMerge.append(arr2[arr2Index])
            arrMerge.append(arr1[arr1Index])
            arr1Index+=1
            arr2Index+=1
            continue
   while arr1Index<len(arr1):
      arrMerge.append(arr1[arr1Index])
      arr1Index+=1
   while arr2Index<len(arr2):
      arrMerge.append(arr2[arr2Index])
      arr2Index+=1
   if isinstance(arr1,tuple):
      return tuple(arrMerge)
   return arrMerge
         
   
print merge([ 1, 2, 7 ],[ 3 ])
print merge((3, 15), (7, 8))