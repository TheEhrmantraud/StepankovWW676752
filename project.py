# def user1(cmd):
#         user1={"name": None, "lastname": None, "midlename": None, "age": None, "status": None, "books": None, "deadline_book": None, "reservation_date_book":None}
#         user1["name"]=cmd.strip()
#         user1["lastname"]=cmd.strip()
#         user1["midlename"]=cmd.strip()
#         user1["age"]=cmd.strip()
#         user1["books"]=cmd.strip()
#         user1["status"]=cmd.strip()
#         user1["reservation_date_book"]=cmd.strip()
#         user1["deadline_book"]=cmd.strip()

# def popizdelki():
#         user1["name"]=input("Ваше имя: ").strip()
#         user1["lastname"]=input("Ваша фамилия : ").strip()
#         user1["midlename"]=input("Ваше отчество: ").strip()
#         user1["age"]=int(input("Ваш возраст: "))
#         user1["books"]=input("Какую-кие книгу-ги вы хотите взять? ").strip()
#         user1["status"]=input("Ваш статус: ").strip()
#         user1["reservation_date_book"]=input("Когда вы хотите взять книгу? ").strip()
#         user1["deadline_book"]=input("Ваше имя: ").strip()

# def main():
#     while True:
#         print("Здравствуйте! Добро пожаловать в библиотеку.\nОу, у вас нет читательского билета?\nДавайте его заведем!")
#         print('Начнем по схеме: (1)Имя, (2)Фамилия, (3)Отчество, (4)Сколько вам лет и ваш статус')
#         namba=int(input())
#         if namba==1: popizdelki()

# if __name__ == "__main__":
#     main()

import datetime

def create_user():
    return {
        "name": None,
        "lastname": None,
        "midlename": None,
        "age": None,
        "status_hodki": None,
        "status":None,
        "books": None,
        "deadline_book": None,
        "reservation_date_book": None
    }

def popizdelki():
    user = create_user()
    user["name"] = input("Ваше имя: ").strip()
    user["lastname"] = input("Ваша фамилия: ").strip()
    user["midlename"] = input("Ваше отчество: ").strip()
    user["age"] = int(input("Ваш возраст: "))
    user["books"] = input("Какую книгу вы хотите взять? ").strip()
    user["status_hodki"] = input("Ваш статус (Каждый день, По будням, По выходным): ").strip()
#    #if 
    user["status"] = input("Ваш статус (Активный, Пассивный): ").strip()
    user["reservation_date_book"] = datetime.datetime.strptime(input("Когда вы хотите взять книгу? (формат ГГГГ-ММ-ДД): ").strip(), "%Y-%m-%d").date()
    today = user["reservation_date_book"] 
    user["deadline_book"] = today + datetime.timedelta(days=14)
    return user

def main():
    while True:
        print("\n\nЗдравствуйте! Введите информацию о клиенте")
        print('\nПо схеме: Имя, Фамилия, Отчество, Сколько вам лет, Ваш статус и Какие книги вы хотите взять')
        namba = int(input("Введите 1 чтобы начать регистрацию: "))
        if namba == 1: 
            user = popizdelki()
            print("\n✅ Регистрация завершена! Вот данные клиента:")
            for k, v in user.items():
                print(f"{k}: {v}")
        x=input('Вы хотите внести изменения? ').strip().lower()
        if x=='да':
            x1=input('Что вы хотите изменить? ').strip().lower()
            if x1=='имя':
                user["name"] = input('Ваше новое имя: ').strip()
                for k, v in user.items():
                    print(f"{k}: {v}")

if __name__ == "__main__":
    main()
