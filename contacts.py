contacts_list = []

while True:
    action = input("1 - Додати контакт, 2 - Переглянути, 3 - Вийти: ")
    if action == '1':
        number = input("Введіть номер телефону: ")
        contacts_list.append(number)
    elif action == '2':
        print("Список номерів:", contacts_list)
    elif action == '3':
        break