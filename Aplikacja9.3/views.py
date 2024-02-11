from flask import render_template, redirect, url_for, request
from app import app
from forms import BookForm
from models import books

@app.route('/')
def index():
    return render_template('index.html', books=books.all())

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        books.create({'title': form.title.data, 'description': form.description.data, 'done': False})
        return redirect(url_for('index'))
    return render_template('add_book.html', form=form)

@app.route('/delete_book/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    books.delete(book_id)
    return redirect(url_for('index'))
