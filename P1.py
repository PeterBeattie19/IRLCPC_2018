_ = raw_input()

arr = list(map(int, raw_input().split())) 

arr.sort()

res = []
i = 0

while True:
  if len(res) == len(arr):
    break
  
  res.append(arr[i])
  res.append(arr[len(arr)-i-1])
  i+=1
  
print res
