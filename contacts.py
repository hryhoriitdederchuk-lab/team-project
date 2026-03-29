contacts_list = []

contacts_dict = {}

while True:
    action = input("\n1 - Додати, 2 - Переглянути, 3 - Видалити, 4 - Вийти: ")
    
    if action == '1':
        name = input("Введіть ПІБ: ")
        number = input("Введіть номер: ")
        contacts_dict[name] = number # Збереження у словник
        print(f"Контакт {name} додано.")
        
    elif action == '2':
        print("Список контактів:")
        for name, number in contacts_dict.items():
            print(f"{name}: {number}")
            
    elif action == '3':
        name = input("Введіть ПІБ для видалення: ")
        if name in contacts_dict:
            del contacts_dict[name] # Видалення зі словника
            print("Контакт видалено.")
        else:
            print("Такого контакту немає.")
            
    elif action == '4':
        break