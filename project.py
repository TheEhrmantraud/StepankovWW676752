import datetime

def create_user():
    return {
        "name": None,
        "lastname": None,
        "midlename": None,
        "age": None,
        "status_hodki": None,
        "status": None,
        "books": None,
        "deadline_book": None,
        "reservation_date_book": None
    }

def popizdelki():
    user = create_user()
    
    # Запрашиваем ввод данных от пользователя
    user["name"] = input("Ваше имя: ").strip()
    user["lastname"] = input("Ваша фамилия: ").strip()
    user["midlename"] = input("Ваше отчество: ").strip()
    user["age"] = int(input("Ваш возраст: "))
    user["books"] = input("Какие книги вы хотите взять? ").strip()
    user["status_hodki"] = input("Ваш статус посещения библиотеки (Каждый день, По будням, По выходным, Иногда): ").strip()
    
    # Определяем статус пользователя исходя из частоты посещений
    if user["status_hodki"].lower() in ("каждый день", "по будням"):
        user["status"] = "Активный"
    else:
        user["status"] = "Пассивный"
        
    # Получаем дату бронирования книги
    reservation_date_str = input("Когда вы хотите взять книгу? (формат ГГГГ-ММ-ДД): ")
    user["reservation_date_book"] = datetime.datetime.strptime(reservation_date_str.strip(), "%Y-%m-%d").date()
    
    # Рассчитываем срок возврата книги (через две недели)
    user["deadline_book"] = user["reservation_date_book"] + datetime.timedelta(days=14)
    
    return user

def main():
    while True:
        print("\n\nЗдравствуйте! Введите информацию о клиенте")
        choice = input("Введите 1 для регистрации клиента (2 - если клиент уже существует): ")
        if choice == "1":
            user = popizdelki()
            
            # Выводим зарегистрированные данные пользователя
            print("\n\n\nРегистрация успешно завершена!\n\nВот данные клиента: ")
            for key, value in user.items():
                print(f"{key}: {value}")
                
            # Предлагаете внести изменения?
            change_choice = input("\n\nХотите внести изменения? Да / Нет: ").strip().lower()
            if change_choice == "да":
                field_to_change = input("Что именно хотите изменить? (например, имя): ").strip().lower()
                if field_to_change == 'имя':
                    new_value = input(f"Ваше новое значение для '{field_to_change}': ").strip()
                    user["name"] = new_value
                elif field_to_change == 'фамилия':
                    new_value = input(f"Ваше новое значение для '{field_to_change}': ").strip()
                    user["lastname"] = new_value
                elif field_to_change == 'отчество':
                    new_value = input(f"Ваше новое значение для '{field_to_change}': ").strip()
                    user["midlename"] = new_value
                elif field_to_change == 'возраст':
                    new_value = input(f"Ваше новое значение для '{field_to_change}': ").strip()
                    user["age"] = new_value
                elif field_to_change == 'статус ходки':
                    new_value = input(f"Ваше новое значение для '{field_to_change}': ").strip()
                    user["status_hodki"] = new_value
                elif field_to_change == 'книги':
                    new_value = input(f"Ваше новое значение для '{field_to_change}': ").strip()
                    user["books"] = new_value
                else:
                    print('Неверный код изменения')

                print("\nИзменения внесены:\n")
                for key, value in user.items():
                    print(f"{key}: {value}")
        if choice == "2":


if __name__ == "__main__":
    main()
