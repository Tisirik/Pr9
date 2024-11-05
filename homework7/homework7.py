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

list6=[]
shift_list=[]
number_range = random.randint(0,10)
print('Количество случайных чисел:',number_range)
for i in range(1,number_range+1):
    list6.append(random.randint(-100,100))
if number_cheсker(list6)==1:
     print(list6)
     maximum= max(list6)
     minimum= min(list6)
     if maximum == minimum:
          print('В списке все числа одинаковы')
          exit(0)
     lenght_list6=len(list6)-1
     shift_list.append(list6[lenght_list6])
     list6.pop(lenght_list6)
     shift_list.extend(list6)
     print(shift_list)
elif len(list6)<=1:
          print('Слишком мало чисел в списке')
          exit(0)
else:
      print('Error.Not a number!')
      exit(0)