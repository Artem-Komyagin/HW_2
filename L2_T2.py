long=int(input('сколько элементов- '))
i=long
el=0
list =[]
while i>0:
    item = input('введите элемент ')
    list.append(item)
    i-=1
print(list)
for elem in range(int(len(list)/2)):
    list[el], list[el+1] = list[el+1], list[el]
    el+=2
print(list)