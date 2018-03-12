n = int(raw_input())

arr = [[]] * n

for i in range(n):
  arr[i] = list(map(int, raw_input().split())) 
  

t1 = [0]*n
t2 = [0]*n 


t1[0] = 1

for i in range(1,n):
  found = False
  for j in range(n):
    if arr[i][j] == 1:
      if t1[j]==1:
        t2[i]=1
        found = True
        break
  if found == False:
    t1[i] = 1
  
  
print t1
print t2
  
for i in range(0,n):
  if t1[i] == 1:
    print i,
    
print 

for i in range(0,n):
  if t2[i] == 1:
    print i,
