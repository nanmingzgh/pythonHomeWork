def get_primes(n):
   i=3
   arrRes=[]
   if 2<n:arrRes.append(2)
   while i<=n:
      j=2
      while j<=i/2:
         if i%j==0:
            break
         j+=1
      if j>i/2:
         arrRes.append(i)
      i+=1
   return arrRes
print get_primes(23)