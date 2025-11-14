import datetime
import os
import json

# Файлы для хранения данных
USERS_FILE = "users_data.txt"
BOOKS_FILE = "books_catalog.txt"
ISSUED_BOOKS_FILE = "issued_books.txt"

def initialize_files():
    """Инициализация файлов с данными"""
    # Создаем файл с каталогом книг, если его нет
    if not os.path.exists(BOOKS_FILE):
        books_catalog = [
            {"id": 1, "title": "Война и мир", "author": "Лев Толстой", "available": True},
            {"id": 2, "title": "Преступление и наказание", "author": "Фёдор Достоевский", "available": True},
            {"id": 3, "title": "Мастер и Маргарита", "author": "Михаил Булгаков", "available": True},
            {"id": 4, "title": "Евгений О негин", "author": "Александр Пушкин", "available": True},
            {"id": 5, "title": "Анна Каренина", "author": "Лев Толстой", "available": True},
            {"id": 6, "title": "Идиот", "author": "Фёдор Достоевский", "available": True},
            {"id": 7, "title": "Братья Карамазовы", "author": "Фёдор Достоевский", "available": True},
            {"id": 8, "title": "Мёртвые души", "author": "Николай Гоголь", "available": True},
            {"id": 9, "title": "Отцы и дети", "author": "Иван Тургенев", "available": True},
            {"id": 10, "title": "Герой нашего времени", "author": "Михаил Лермонтов", "available": True},
            {"id": 11, "title": "Капитанская дочка", "author": "Александр Пушкин", "available": True},
            {"id": 12, "title": "Обломов", "author": "Иван Гончаров", "available": True},
            {"id": 13, "title": "Вишнёвый сад", "author": "Антон Чехов", "available": True},
            {"id": 14, "title": "Доктор Живаго", "author": "Борис Пастернак", "available": True},
            {"id": 15, "title": "Тихий Дон", "author": "Михаил Шолохов", "available": True},
            {"id": 16, "title": "Собачье сердце", "author": "Михаил Булгаков", "available": True},
            {"id": 17, "title": "Белая гвардия", "author": "Михаил Булгаков", "available": True},
            {"id": 18, "title": "Один день Ивана Денисовича", "author": "Александр Солженицын", "available": True},
            {"id": 19, "title": "Архипелаг ГУЛАГ", "author": "Александр Солженицын", "available": True},
            {"id": 20, "title": "Палата №6", "author": "Антон Чехов", "available": True},
            {"id": 21, "title": "Дама с собачкой", "author": "Антон Чехов", "available": True},
            {"id": 22, "title": "Пиковая дама", "author": "Александр Пушкин", "available": True},
            {"id": 23, "title": "Руслан и Людмила", "author": "Александр Пушкин", "available": True},
            {"id": 24, "title": "Бедная Лиза", "author": "Николай Карамзин", "available": True},
            {"id": 25, "title": "Горе от ума", "author": "Александр Грибоедов", "available": True},
            {"id": 26, "title": "Что делать?", "author": "Николай Чернышевский", "available": True},
            {"id": 27, "title": "Кому на Руси жить хорошо", "author": "Николай Некрасов", "available": True},
            {"id": 28, "title": "Гранатовый браслет", "author": "Александр Куприн", "available": True},
            {"id": 29, "title": "Олеся", "author": "Александр Куприн", "available": True},
            {"id": 30, "title": "Поединок", "author": "Александр Куприн", "available": True}
        ]
        save_books_catalog(books_catalog)
    
    # Создаем пустые файлы, если их нет
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'w', encoding='utf-8') as f:
            pass
    
    if not os.path.exists(ISSUED_BOOKS_FILE):
        with open(ISSUED_BOOKS_FILE, 'w', encoding='utf-8') as f:
            pass

def save_books_catalog(books):
    """Сохранение каталога книг"""
    with open(BOOKS_FILE, 'w', encoding='utf-8') as f:
        for book in books:
            f.write(json.dumps(book, ensure_ascii=False) + '\n')

def load_books_catalog():
    """Загрузка каталога книг"""
    books = []
    try:
        with open(BOOKS_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    books.append(json.loads(line.strip()))
    except FileNotFoundError:
        return []
    return books

def save_user(user):
    """Сохранение пользователя в файл"""
    with open(USERS_FILE, 'a', encoding='utf-8') as f:
        user_copy = user.copy()
        # Конвертируем даты в строки для сохранения
        if user_copy.get("reservation_date_book"):
            user_copy["reservation_date_book"] = str(user_copy["reservation_date_book"])
        if user_copy.get("deadline_book"):
            user_copy["deadline_book"] = str(user_copy["deadline_book"])
        f.write(json.dumps(user_copy, ensure_ascii=False) + '\n')

def load_users():
    """Загрузка всех пользователей из файла"""
    users = []
    try:
        with open(USERS_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    user = json.loads(line.strip())
                    # Конвертируем строки обратно в даты
                    if user.get("reservation_date_book") and user["reservation_date_book"] != "None":
                        user["reservation_date_book"] = datetime.datetime.strptime(
                            user["reservation_date_book"], "%Y-%m-%d").date()
                    if user.get("deadline_book") and user["deadline_book"] != "None":
                        user["deadline_book"] = datetime.datetime.strptime(
                            user["deadline_book"], "%Y-%m-%d").date()
                    users.append(user)
    except FileNotFoundError:
        return []
    return users

def update_user_in_file(updated_user):
    """Обновление данных пользователя в файле"""
    users = load_users()
    # Находим и обновляем пользователя
    for i, user in enumerate(users):
        if (user["name"] == updated_user["name"] and 
            user["lastname"] == updated_user["lastname"] and
            user["midlename"] == updated_user["midlename"]):
            users[i] = updated_user
            break
    
    # Перезаписываем файл
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        for user in users:
            user_copy = user.copy()
            if user_copy.get("reservation_date_book"):
                user_copy["reservation_date_book"] = str(user_copy["reservation_date_book"])
            if user_copy.get("deadline_book"):
                user_copy["deadline_book"] = str(user_copy["deadline_book"])
            f.write(json.dumps(user_copy, ensure_ascii=False) + '\n')

def search_books(query, search_type="all"):
    """Поиск книг по названию или автору"""
    books = load_books_catalog()
    results = []
    query_lower = query.lower()
    
    for book in books:
        if search_type == "title":
            if query_lower in book["title"].lower():
                results.append(book)
        elif search_type == "author":
            if query_lower in book["author"].lower():
                results.append(book)
        else:  # all
            if query_lower in book["title"].lower() or query_lower in book["author"].lower():
                results.append(book)
    
    return results

def display_books(books):
    """Отображение списка книг"""
    if not books:
        print("Книги не найдены.")
        return
    
    print("\n" + "="*80)
    print(f"{'ID':<5} {'Название':<35} {'Автор':<30} {'Доступна':<10}")
    print("="*80)
    for book in books:
        available = "Да" if book["available"] else "Нет"
        print(f"{book['id']:<5} {book['title']:<35} {book['author']:<30} {available:<10}")
    print("="*80)

def issue_book(user_name, book_id):
    """Выдача книги читателю"""
    books = load_books_catalog()
    users = load_users()
    
    # Проверяем существование пользователя
    user_found = False
    for user in users:
        if f"{user['lastname']} {user['name']}" == user_name or user['name'] == user_name:
            user_found = True
            break
    
    if not user_found:
        print(f"Читатель {user_name} не найден в системе!")
        return False
    
    # Находим книгу
    book_found = None
    for i, book in enumerate(books):
        if book["id"] == book_id:
            book_found = book
            if not book["available"]:
                print(f"Книга '{book['title']}' уже выдана!")
                return False
            books[i]["available"] = False
            break
    
    if not book_found:
        print(f"Книга с ID {book_id} не найдена!")
        return False
    
    # Сохраняем обновленный каталог
    save_books_catalog(books)
    
    # Записываем информацию о выдаче
    issue_date = datetime.date.today()
    return_date = issue_date + datetime.timedelta(days=14)
    
    issue_record = {
        "user_name": user_name,
        "book_id": book_id,
        "book_title": book_found["title"],
        "issue_date": str(issue_date),
        "return_date": str(return_date),
        "returned": False
    }
    
    with open(ISSUED_BOOKS_FILE, 'a', encoding='utf-8') as f:
        f.write(json.dumps(issue_record, ensure_ascii=False) + '\n')
    
    print(f"\nКнига '{book_found['title']}' успешно выдана читателю {user_name}")
    print(f"Дата выдачи: {issue_date}")
    print(f"Дата возврата: {return_date}")
    return True

def return_book(book_id):
    """Приём книги от читателя"""
    books = load_books_catalog()
    issued_records = []
    
    # Загружаем записи о выданных книгах
    try:
        with open(ISSUED_BOOKS_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    issued_records.append(json.loads(line.strip()))
    except FileNotFoundError:
        print("Нет записей о выданных книгах.")
        return False
    
    # Находим запись о выдаче
    record_found = False
    for record in issued_records:
        if record["book_id"] == book_id and not record["returned"]:
            record["returned"] = True
            record_found = True
            print(f"\nКнига '{record['book_title']}' принята от {record['user_name']}")
            break
    
    if not record_found:
        print(f"Книга с ID {book_id} не числится как выданная.")
        return False
    
    # Обновляем доступность книги
    for i, book in enumerate(books):
        if book["id"] == book_id:
            books[i]["available"] = True
            break
    
    save_books_catalog(books)
    
    # Перезаписываем файл выданных книг
    with open(ISSUED_BOOKS_FILE, 'w', encoding='utf-8') as f:
        for record in issued_records:
            f.write(json.dumps(record, ensure_ascii=False) + '\n')
    
    return True

def create_user():
    """Создание структуры пользователя"""
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

def register_user():
    """Регистрация нового читателя"""
    user = create_user()
    
    print("\n--- Регистрация нового читателя ---")
    user["name"] = input("Имя: ").strip()
    user["lastname"] = input("Фамилия: ").strip()
    user["midlename"] = input("Отчество: ").strip()
    user["age"] = int(input("Возраст: "))
    user["status_hodki"] = input("Статус посещения (Каждый день, По будням, По выходным, Иногда): ").strip()
    
    # Определяем статус
    if user["status_hodki"].lower() in ("каждый день", "по будням"):
        user["status"] = "Активный"
    else:
        user["status"] = "Пассивный"
    
    # Сохраняем пользователя
    save_user(user)
    
    print("\n✓ Читатель успешно зарегистрирован!")
    return user

def find_user():
    """Поиск пользователя по ФИО"""
    users = load_users()
    
    if not users:
        print("В системе нет зарегистрированных читателей.")
        return None
    
    print("\n--- Поиск читателя ---")
    search_name = input("Введите фамилию или имя: ").strip().lower()
    
    found_users = []
    for user in users:
        full_name = f"{user['lastname']} {user['name']} {user['midlename']}".lower()
        if search_name in full_name:
            found_users.append(user)
    
    if not found_users:
        print("Читатель не найден.")
        return None
    
    if len(found_users) == 1:
        return found_users[0]
    
    # Если найдено несколько пользователей
    print("\nНайдено несколько читателей:")
    for i, user in enumerate(found_users, 1):
        print(f"{i}. {user['lastname']} {user['name']} {user['midlename']}, {user['age']} лет")
    
    choice = int(input("\nВыберите номер читателя: "))
    return found_users[choice - 1]

def display_user(user):
    """Отображение информации о читателе"""
    print("\n" + "="*60)
    print("ИНФОРМАЦИЯ О ЧИТАТЕЛЕ")
    print("="*60)
    print(f"ФИО: {user['lastname']} {user['name']} {user['midlename']}")
    print(f"Возраст: {user['age']}")
    print(f"Статус посещения: {user['status_hodki']}")
    print(f"Статус: {user['status']}")
    if user.get('books'):
        print(f"Взятые книги: {user['books']}")
    if user.get('reservation_date_book'):
        print(f"Дата резервирования: {user['reservation_date_book']}")
    if user.get('deadline_book'):
        print(f"Срок возврата: {user['deadline_book']}")
    print("="*60)

def edit_user(user):
    """Редактирование данных читателя"""
    print("\n--- Редактирование данных читателя ---")
    print("Что хотите изменить?")
    print("1. Имя")
    print("2. Фамилия")
    print("3. Отчество")
    print("4. Возраст")
    print("5. Статус посещения")
    
    choice = input("\nВыберите номер поля: ").strip()
    
    if choice == "1":
        user["name"] = input("Новое имя: ").strip()
    elif choice == "2":
        user["lastname"] = input("Новая фамилия: ").strip()
    elif choice == "3":
        user["midlename"] = input("Новое отчество: ").strip()
    elif choice == "4":
        user["age"] = int(input("Новый возраст: "))
    elif choice == "5":
        user["status_hodki"] = input("Новый статус посещения: ").strip()
        if user["status_hodki"].lower() in ("каждый день", "по будням"):
            user["status"] = "Активный"
        else:
            user["status"] = "Пассивный"
    else:
        print("Неверный выбор.")
        return
    
    update_user_in_file(user)
    print("\n✓ Данные успешно обновлены!")

def main():
    """Главная функция программы"""
    initialize_files()
    
    while True:
        print("\n" + "="*60)
        print("СИСТЕМА УПРАВЛЕНИЯ БИБЛИОТЕКОЙ")
        print("="*60)
        print("1. Регистрация нового читателя")
        print("2. Найти читателя")
        print("3. Поиск книг")
        print("4. Просмотр всех книг")
        print("5. Выдать книгу")
        print("6. Принять книгу")
        print("7. Редактировать данные читателя")
        print("0. Выход")
        print("="*60)
        
        choice = input("\nВыберите действие: ").strip()
        
        if choice == "1":
            register_user()
        
        elif choice == "2":
            user = find_user()
            if user:
                display_user(user)
        
        elif choice == "3":
            print("\n--- Поиск книг ---")
            print("1. По названию")
            print("2. По автору")
            print("3. По всем полям")
            search_type_choice = input("Выберите тип поиска: ").strip()
            
            search_type_map = {"1": "title", "2": "author", "3": "all"}
            search_type = search_type_map.get(search_type_choice, "all")
            
            query = input("Введите запрос: ").strip()
            results = search_books(query, search_type)
            display_books(results)
        
        elif choice == "4":
            books = load_books_catalog()
            display_books(books)
        
        elif choice == "5":
            user_name = input("Введите ФИО читателя: ").strip()
            book_id = int(input("Введите ID книги: "))
            issue_book(user_name, book_id)
        
        elif choice == "6":
            book_id = int(input("Введите ID книги для возврата: "))
            return_book(book_id)
        
        elif choice == "7":
            user = find_user()
            if user:
                display_user(user)
                edit_user(user)
        
        elif choice == "0":
            print("\nДо свидания!")
            break
        
        else:
            print("\nНеверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
