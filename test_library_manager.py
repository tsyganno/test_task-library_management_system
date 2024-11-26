import unittest
from library_manager import LibraryManager


class TestLibraryManager(unittest.TestCase):
    def setUp(self):
        """Создаём экземпляр класса для тестов с пустой библиотекой."""
        self.manager = LibraryManager()
        self.manager.books = []  # Очищаем библиотеку

    def test_add_book(self):
        """Проверка добавления книги."""
        self.manager.add_book("Робинзон Крузо", "Даниэль Дэфо", 1897)
        self.assertEqual(len(self.manager.books), 1)
        self.assertEqual(self.manager.books[0]["title"], "Робинзон Крузо")
        self.assertEqual(self.manager.books[0]["status"], "в наличии")

    def test_delete_book(self):
        """Проверка удаления книги."""
        self.manager.add_book("Робинзон Крузо", "Даниэль Дэфо", 1897)
        self.manager.delete_book("title", "Робинзон Крузо")
        self.assertEqual(len(self.manager.books), 0)

    def test_update_status(self):
        """Проверка изменения статуса книги."""
        self.manager.add_book("Робинзон Крузо", "Даниэль Дэфо", 1897)
        self.manager.update_status("title", "Робинзон Крузо", "выдана")
        self.assertEqual(self.manager.books[0]["status"], "выдана")

    def test_search_books(self):
        """Проверка поиска книги."""
        self.manager.add_book("Робинзон Крузо", "Даниэль Дэфо", 1897)
        results = self.manager.search_books("title", "Робинзон Крузо")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["title"], "Робинзон Крузо")

    def test_search_books_no_results(self):
        """Проверка поиска, когда книга не найдена."""
        self.manager.add_book("Робинзон Крузо", "Даниэль Дэфо", 1897)
        results = self.manager.search_books("title", "Дракула")
        self.assertEqual(len(results), 0)

    def test_add_book_future_year(self):
        """Проверка добавления книги с будущим годом."""
        self.manager.add_book("Робинзон Крузо", "Даниэль Дэфо", 2026)
        self.assertEqual(len(self.manager.books), 0)  # Книга не должна быть добавлена


if __name__ == "__main__":
    unittest.main()
