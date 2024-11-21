from book.service import BookService


def main():
    library = BookService()

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания: ")
            library.add_book(title, author, year)

        elif choice == '2':
            book_id = input("Введите ID книги для удаления: ")
            library.remove_book(book_id)

        elif choice == '3':
            search_by = input("Искать по (title/author/year): ").strip().lower()
            search_value = input(f"Введите значение для поиска по {search_by}: ")
            results = library.search_books(**{search_by: search_value})
            if results:
                for book in results:
                    print(book)
            else:
                print("Книги не найдены.")

        elif choice == '4':
            library.display_books()

        elif choice == '5':
            book_id = input("Введите ID книги для изменения статуса: ")
            new_status = input("Введите новый статус (в наличии/выдана): ")
            library.update_status(book_id, new_status)

        elif choice == '6':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
