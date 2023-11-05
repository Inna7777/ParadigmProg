class Library:
    def __init__(self):
        self.library= []

    def add_book(self):
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        book = {"Название": title, "Автор": author}
        self.library.append(book)
        print("Книга добавлена в библиотеку.")
    def display_books(self):
        if not self.library:
            print("Библиотека пуста.")
        else:
            print("Список книг в библиотеке:")
            for book in self.library:
                print(f"Название: {book['Название']}, Автор: {book['Автор']}")

