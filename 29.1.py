# Створюємо клас HashTable

class HashTable:
    def __init__(self, size):
        self.size = size
        # Створюємо пусту хеш-таблицю з вкладеними списками розміру size
        self.table = [[] for _ in range(self.size)]

    # Використовуємо вбудовану хеш-функцію Python для отримання хешу ключа
    def _hash_function(self, key):
        return hash(key) % self.size

    # Додавання елементу у хеш-таблицю з виправленням колізій методом ланцюжків
    def insert(self, key, value):
        index = self._hash_function(key)  # Обчислюємо індекс у хеш-таблиці
        for i, (k, v) in enumerate(self.table[index]):  # Шукаємо ключ у вкладеному списку за допомогою enumerate
            if k == key:  # Якщо ключ знайдено, оновлюємо значення
                self.table[index][i] = (key, value)
                break
        else:  # Якщо ключ не знайдено, додаємо нову пару ключ-значення
            self.table[index].append((key, value))

    # Пошук елементу у хеш-таблиці
    def get(self, key):
        index = self._hash_function(key)  # Обчислюємо індекс у хеш-таблиці
        for k, v in self.table[index]:  # Шукаємо ключ у вкладеному списку
            if k == key:
                return v  # Якщо ключ знайдено, повертаємо відповідне значення
        else:
            raise KeyError((f"Ключ {key} не знайдено у хеш-таблиці"))  # Якщо ключ не знайдено, викидаємо виняток

    # Видалення елементу у хеш-таблиці
    def remove(self, key):
        index = self._hash_function(key)  # Обчислюємо індекс у хеш-таблиці
        for i, (k, v) in enumerate(self.table[index]):  # Шукаємо ключ у вкладеному списку за допомогою enumerate
            if k == key:
                del self.table[index][i]  # Якщо ключ знайдено, видаляємо його зі списку
                break
        else:
            raise KeyError((f"Ключ {key} не знайдено у хеш-таблиці"))  # Якщо ключ не знайдено, викидаємо виняток

    # Друк хеш-таблиці
    def print_table(self):
        for index, item in enumerate(self.table):
            print(f"{index}: {item}")


if __name__ == "__main__":
            
    # Приклад використання:

    ht = HashTable(10)
    ht.insert(5, "Hello")
    ht.insert(15, "world")  # Приклад виправлення колізії методом ланцюжків
    ht.insert(10, "Hi")
    print(ht.get(5))
    print(ht.get(15))
    ht.print_table()        # Друк хеш-таблиці
    ht.remove(5)            # Видалення елементу у хеш-таблиці
    print(ht.get(5))




