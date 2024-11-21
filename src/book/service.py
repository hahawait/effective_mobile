import json
from book.models import Book


class BookService:
    def __init__(self, storage_file='books.json'):
        self.storage_file = storage_file
        self.books = self.load_books()

    def load_books(self):
        try:
            with open(self.storage_file, 'r', encoding='utf-8') as file:
                books_data = json.load(file)
                return [Book(**book) for book in books_data]
        except FileNotFoundError:
            return []

    def save_books(self):
        with open(self.storage_file, 'w', encoding='utf-8') as file:
            json.dump([book.__dict__ for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title, author, year):
        new_book = Book(title=title, author=author, year=year)
        self.books.append(new_book)
        self.save_books()
        print(f"Книга '{title}' добавлена.")

    def remove_book(self, book_id):
        book_to_remove = next((book for book in self.books if book.id == book_id), None)
        if book_to_remove:
            self.books.remove(book_to_remove)
            self.save_books()
            print(f"Книга с ID {book_id} удалена.")
        else:
            print(f"Книга с ID {book_id} не найдена.")

    def search_books(self, **kwargs):
        results = self.books
        for key, value in kwargs.items():
            results = [book for book in results if getattr(book, key) == value]
        return results

    def display_books(self):
        if not self.books:
            print("Библиотека пуста.")
        else:
            for book in self.books:
                print(book)

    def update_status(self, book_id, new_status):
        book_to_update = next((book for book in self.books if book.id == book_id), None)
        if book_to_update:
            book_to_update.status = new_status
            self.save_books()
            print(f"Статус книги с ID {book_id} обновлен на '{new_status}'.")
        else:
            print(f"Книга с ID {book_id} не найдена.")
