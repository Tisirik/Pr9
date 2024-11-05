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

list2=[]
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
            list2.append(number)
        else:
            print("введите число!")
            Trigger=False
            break
for j in range(len(list2)):
     if int(list2[j])%2!=0:
        print(list2[j])