import re

def split_email(email):
    pattern = r'([^@]+)@(.+)'
    match = re.match(pattern, email)
    special_characters = r'[!#$%^&*()<>?/\|{}[\]:;"\'`~]'

    if match:
        username = match.group(1)  
        domain = match.group(2)   
        if re.search(special_characters, username):
            return None, None  
        else:
            return username, domain
    else:
        return None, None

email_input = input("Введите ваш email: ")
username, domain = split_email(email_input)

if username and domain:
    if username[0].isdigit() or username[0]=='.' or username[0]== '-':
        print('email не может оканчиваться на цифры, точки или деффис')
    if domain[len(domain)-1].isdigit() or domain[len(domain)-1]=='.' or domain[len(domain)-1]== '-':
        print('email не может начинаться с цифры, точки или деффиса')
    if len(username)>64 or len(domain)>253:
        print('Адрес электронной почты должен содержать от 1 до 64 символов до знака "@" и от 1 до 253 символов после него.')
    if ' ' in  email_input:
        print('email не должен содержать пробелов')
    else:
        print(f"имя пользователя: {username}")
        print(f"доменное имя почты: {domain}")
else:
    print("Некорректный email адрес.")
