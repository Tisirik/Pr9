import random

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

def generate_ticket():
    lottery_ticket=[]
    used_numbers=[]
    for index in range(5):
        str_lottery_ticket =[]
        while len(str_lottery_ticket) < 5:
            new_number = random.randint(1, 100)
            if new_number not in used_numbers:
                str_lottery_ticket.append(new_number)
                used_numbers.append(new_number)
        lottery_ticket.append(str_lottery_ticket)
    print(lottery_ticket)
    return lottery_ticket

def user_choice():
    lottery_ticket_edit= lottery_ticket.copy()
    user_numbers=[]
    for index in range(5):
        array=[]
        for sublist in lottery_ticket_edit:
            for element in sublist:
                array.append(element)
        number = input(f'Выберите одно число из чисел в ряду: ')
        if num_check(number)==1:
                if int(number) in array:
                    user_numbers.append(str(number))
                    for x in range (len(lottery_ticket_edit)-1):
                        if int(number) in lottery_ticket_edit[x]:
                               del lottery_ticket_edit[x]
                else:
                    print('Вы ввели число которое отсутсвует в списке или выбрали 2 числа из одного ряда')
                    exit(0)
        else:
            print('Вы ввели не число!')
            exit(0)
    return user_numbers

def computer_choice():
    random_numbers = []
    for row in lottery_ticket:
        random_number = random.choice(row)
        random_numbers.append(str(random_number))
    return random_numbers
while True:
    lottery_ticket= generate_ticket()
    user_numbers = user_choice()
    random_numbers = computer_choice()
    count=0
    for num in range(5):
         for subnum in range(5):
              if user_numbers[num] == random_numbers[subnum]:
                   count+=1
    print('Выигрышные позиции: ', random_numbers)
    print(f'Вы угадали {count} из 5 чисел')