import hashlib

# Словник, що зберігає логіни та паролі користувачів
users = {}


def register():
    # Отримання логіну та пароля в інтерактивному режимі
    username = input("Введіть логін: ")
    password = input("Введіть пароль: ")

    # Шифрування пароля за допомогою алгоритму SHA256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Перевірка на колізії
    if username in users:
        print("Користувач з таким логіном вже зареєстрований")
    else:
        # Збереження логіну та шифрованого пароля у словник
        users[username] = hashed_password
        print("Користувач зареєстрований успішно")


def login():
    # Отримання логіну та пароля в інтерактивному режимі
    username = input("Введіть логін: ")
    password = input("Введіть пароль: ")

    # Шифрування пароля за допомогою алгоритму SHA256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Перевірка наявності логіну та співпадіння паролів
    if username not in users:
        print("Користувача з таким логіном не знайдено")
    elif users[username] != hashed_password:
        print("Невірний пароль")
    else:
        print("Користувач авторизований успішно")


# Виконання програми
while True:
    print("Виберіть опцію:")
    print("1 - Зареєструватись")
    print("2 - Увійти")
    print("3 - Вийти")
    choice = input("Ваш вибір: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Невірний вибір")
