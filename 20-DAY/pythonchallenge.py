def getPrimeNumber(n): 
   for i in range(2, n):
      if n % i == 0:    return False
   return True 
   
for i in range(1, 250):
   if i != 1 and getPrimeNumber(i):
      print(i, end = '\t')
      with open('results.txt', 'at') as fopen: 
         fopen.write(f"{i}\t")