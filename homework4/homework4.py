def num_check(value):
        if value=='':
            print('Вы ввели не число')
            exit(0)
        for i in range(len(value)):
                if value[i] in "0123456789,.-":
                    proove=1
                else:
                    proove=0
                    break
        return proove

list3=[]
counter_even=0
counter_odd=0
input_num=0
Trigger=True
while Trigger:
    print("Введите число")
    number=input()
    if number=="end":
        Trigger=False
        break
    else:
        if num_check(number)==1:
            list3.append(number)
        else:
            print("введите число!")
            Trigger=False
            break
for j in range(len(list3)):
      if int(list3[j])%2==0:
        counter_even+=1
      else:
          counter_odd+=1
print('Четных чисел: ',counter_even,'Нечетных чисел: ',counter_odd)