def calculate_special_sum(n):
   i=1
   sum=0
   while i<=n:
      sum+=(i-1)**2*i
      i+=1
   return sum
   
print calculate_special_sum(3)