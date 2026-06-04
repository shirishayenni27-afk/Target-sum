a=list[int]=list(map(int,input()))
b=list(map(int,input()))
result = []
for i in range(len(a)):
    result.append(a[i] + b[i])
print(result)