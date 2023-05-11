import hashlib

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self._encrypt_password(password)

    def _encrypt_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
class Authentication:
    def __init__(self):
        self.users = []

    def register(self, username, password):
        for user in self.users:
            if user.username == username:
                print("Користувач з таким логіном вже зареєстрований")
                return False
        user = User(username, password)
        self.users.append(user)
        return print("Користувач зареєстрований успішно")

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == hashlib.sha256(password.encode()).hexdigest():
                print("Ласкаво просимо, {}!".format(username))
                return True
        print("Неправильний логін чи пароль")
        return False
    



if __name__ == "__main__":
    
    # Виконання програми
    
    auth = Authentication()
    
    while True:
        print("Виберіть опцію:")
        print("1 - Зареєструватись")
        print("2 - Увійти")
        print("3 - Вийти")
        choice = input("Ваш вибір: ")

        if choice == "1":
            username = input("Введіть логін: ")
            password = input("Введіть пароль: ") 
            auth.register(username, password)
        elif choice == "2":
            username = input("Введіть логін: ")
            password = input("Введіть пароль: ") 
            auth.login(username, password)
        elif choice == "3":
            break
        else:
            print("Невірний вибір")
