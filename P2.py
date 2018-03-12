n = int(raw_input())

arr = [[]] * n

for i in range(n):
  arr[i] = list(map(int, raw_input().split())) 
  

t1 = [0]*n
t2 = [0]*n 


t1[0] = 1

for i in range(n):
  for j in range(n):
    if arr[i][j] == 1:
      if t1[j]==1:
        t2[j]=1
        break
  t2[i] = i
  
print t1
print t2
    
