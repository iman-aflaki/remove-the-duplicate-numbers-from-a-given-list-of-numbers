list1 = [1,2,3,2,4,5,4,6,1]
result = []
for i in list1:
    if i in result:
        pass
    else:
        result.append(i)
print(result)