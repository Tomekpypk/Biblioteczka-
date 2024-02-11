# models.py
import json

class BookModel:
    def __init__(self, filename='books.json'):
        self.filename = filename
        self.books = self.load_all()

    def load_all(self):
        try:
            with open(self.filename, 'r') as file:
                books = json.load(file)
            return books
        except FileNotFoundError:
            return []

    def save_all(self):
        with open(self.filename, 'w') as file:
            json.dump(self.books, file)

    def all(self):
        return self.books

    def get(self, book_id):
        for book in self.books:
            if book['id'] == book_id:
                return book
        return None

    def create(self, data):
        new_book = {
            'id': len(self.books) + 1,
            'title': data['title'],
            'description': data.get('description', ""),
            'done': False
        }
        self.books.append(new_book)
        self.save_all()
        return new_book

    def delete(self, book_id):
        book = self.get(book_id)
        if book:
            self.books.remove(book)
            self.save_all()
            return True
        return False
