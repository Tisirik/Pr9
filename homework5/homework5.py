import random

def number_cheсker(lst):
    results = []
    for value in lst:
             results.append(str(value))
    for str_value in results:
        if str_value=='':
                print('Не число!')
                exit(0)
        for i in range(len(str_value)):
                    if str_value[i] in "0123456789,.-":
                        proove=1
                    else:
                        proove=0
                        break
        return proove

list4=[]
number_range = random.randint(0,10)
print('Количество случайных чисел:',number_range)
for i in range(1,number_range+1):
    list4.append(random.randint(-100,100))
if number_cheсker(list4)==1:
    print(list4)
    a=0
    b=1
    while a!=len(list4)-1 and b!=len(list4):
        if list4[b]>list4[a]:
            print(list4[b])
        a+=1
        b+=1
    if list4[len(list4)-1]<list4[0]:
        print(list4[0])
elif len(list4)<=1:
    print('Слишком мало чисел в списке')
    exit(0)
else:
     print('Не число')
     exit(0)