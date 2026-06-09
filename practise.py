list=[5,10,15,20,25]
target=20
replacement=200
if target in list:
    index=list.index(target)
    list[index]=replacement
print(list)
