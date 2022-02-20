m=int(input('Введите месяц- '))
while m>12 or m<=0:
    print('нужно от 1 до 12')
    m=int(input('Введите месяц- '))

list_ses =['зима', 'весна', 'лето', 'осень']
dict_ses ={1:'winter',2:'spring',3:'summer',4:'autumn'}

if m==1 or m==12 or m==2:
    print (list_ses[0])
    print (dict_ses.get(1) )

elif m==3 or m==4 or m==5:
    print (list_ses[1])
    print (dict_ses.get(2) )

elif m==6 or m==7 or m==8:
    print (list_ses[2])
    print (dict_ses.get(3) )

elif m == 9 or m == 10 or m == 11:
    print(list_ses[3])
    print(dict_ses.get(4))