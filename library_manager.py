import json
from typing import List, Dict, Optional

# Определение пути к файлу для хранения данных
DATA_FILE = "library.json"

# Тип данных для книги
Book = Dict[str, str | int]


class LibraryManager:
    def __init__(self):
        self.books: List[Book] = []
        self.load_data()

    def load_data(self) -> None:
        """Загрузка данных из файла."""
        try:
            with open(DATA_FILE, 'r') as file:
                self.books = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []

    def save_data(self) -> None:
        """Сохранение данных в файл."""
        with open(DATA_FILE, 'w') as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, title: str, author: str, year: int) -> None:
        """Добавление новой книги в библиотеку."""
        if year > 2024:
            print(f"Выбранный год {year} еще не наступил!")
        else:
            new_book = {
                "id": len(self.books) + 1,
                "title": title,
                "author": author,
                "year": year,
                "status": "в наличии"
            }
            self.books.append(new_book)
            self.save_data()
            print("Книга успешно добавлена!")

    def delete_book(self, search_key: str, search_value: str) -> None:
        """Удаление книги по названию или автору."""
        matches = [book for book in self.books if book[search_key].lower() == search_value.lower()]
        if not matches:
            print("Книга не найдена.")
            return
        elif len(matches) > 1:
            print("Найдено несколько книг:")
            for i, book in enumerate(matches, 1):
                print(f"{i}. {book['title']} - {book['author']} ({book['year']}), статус: {book['status']}")
            choice = input("Введите номер книги для удаления: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(matches):
                book_to_delete = matches[int(choice) - 1]
            else:
                print("Некорректный выбор.")
                return
        else:
            book_to_delete = matches[0]

        self.books.remove(book_to_delete)
        self.save_data()
        print("Книга успешно удалена!")

    def search_books(self, key: str, value: str | int) -> List[Book]:
        """Поиск книг по полю."""
        return [book for book in self.books if str(book[key]).lower() == str(value).lower()]

    def display_books(self) -> None:
        """Отображение всех книг."""
        if not self.books:
            print("Библиотека пуста.")
            return
        print("Список книг:")
        for book in self.books:
            print(
                f"ID: {book['id']}, Название: {book['title']}, "
                f"Автор: {book['author']}, Год: {book['year']}, Статус: {book['status']}"
            )

    def update_status(self, search_key: str, search_value: str, new_status: str) -> None:
        """Изменение статуса книги по названию или автору."""
        matches = [book for book in self.books if book[search_key].lower() == search_value.lower()]
        if not matches:
            print("Книга не найдена.")
            return
        elif len(matches) > 1:
            print("Найдено несколько книг:")
            for i, book in enumerate(matches, 1):
                print(f"{i}. {book['title']} - {book['author']} ({book['year']}), статус: {book['status']}")
            choice = input("Введите номер книги для изменения статуса: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(matches):
                book_to_update = matches[int(choice) - 1]
            else:
                print("Некорректный выбор.")
                return
        else:
            book_to_update = matches[0]

        if new_status in ["в наличии", "выдана"]:
            book_to_update["status"] = new_status
            self.save_data()
            print("Статус успешно обновлён!")
        else:
            print("Некорректный статус. Используйте 'в наличии' или 'выдана'.")


def main() -> None:
    """Основная функция приложения."""
    manager = LibraryManager()

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            title = input("Введите название книги: ").strip()
            author = input("Введите автора книги: ").strip()
            year = int(input("Введите год издания книги: ").strip())
            manager.add_book(title, author, year)
        elif choice == "2":
            search_key = input("Введите поле для поиска книги (title/author): ").strip()
            if search_key not in ["title", "author"]:
                print("Некорректное поле для поиска.")
                continue
            search_value = input(f"Введите значение для {search_key}: ").strip()
            manager.delete_book(search_key, search_value)
        elif choice == "3":
            key = input("Введите поле для поиска (title/author/year): ").strip()
            value = input("Введите значение для поиска: ").strip()
            if key in ["title", "author"]:
                results = manager.search_books(key, value)
            elif key == "year":
                results = manager.search_books(key, int(value))
            else:
                print("Некорректное поле для поиска.")
                continue
            if results:
                for book in results:
                    print(
                        f"ID: {book['id']}, Название: {book['title']}, "
                        f"Автор: {book['author']}, Год: {book['year']}, Статус: {book['status']}"
                    )
            else:
                print("Книги не найдены.")
        elif choice == "4":
            manager.display_books()
        elif choice == "5":
            search_key = input("Введите поле для поиска книги (title/author): ").strip()
            if search_key not in ["title", "author"]:
                print("Некорректное поле для поиска.")
                continue
            search_value = input(f"Введите значение для {search_key}: ").strip()
            new_status = input("Введите новый статус (в наличии/выдана): ").strip()
            manager.update_status(search_key, search_value, new_status)
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор.")


if __name__ == "__main__":
    main()
