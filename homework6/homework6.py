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

list5=[]
number_range = random.randint(0,10)
print('Количество случайных чисел:',number_range)
for i in range(1,number_range+1):
    list5.append(random.randint(-100,100))
if number_cheсker(list5)==1:
     print(list5)
     maximum= max(list5)
     minimum= min(list5)
     if maximum == minimum:
          print('В списке все числа одинаковы')
          exit(0)
     indexmax=list5.index(maximum)
     indexmin=list5.index(minimum)
     list5.remove(maximum)
     list5.remove(minimum)
     list5.insert(indexmax,minimum)
     list5.insert(indexmin,maximum)
     print(list5)
elif len(list5)<=1:
          print('Слишком мало чисел в списке')
          exit(0)
else:
       print('Error.Not a number!!!')
       exit(0)