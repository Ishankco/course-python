list = []
for i in range(1,11,1):
    list.append(i)
print("original list is:",list)
a=list[0:5]
print("extracted first 5 element are:",a)
a.reverse()
print("reversed extracted element are:",a)