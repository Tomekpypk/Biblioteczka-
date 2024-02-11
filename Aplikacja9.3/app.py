
from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired
from models import BookModel
from forms import BookForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"
books = BookModel()



class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description')


@app.route("/api/v1/books/", methods=["GET"])
def books_list_api_v1():
    return jsonify(books.all())


@app.route("/api/v1/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = books.get(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    return jsonify({"book": book})


@app.route("/api/v1/books/", methods=["POST"])
def create_book():
    form = BookForm()
    if request.method == "POST" and form.validate_on_submit():
        new_book = books.create(form.data)
        return jsonify({'book': new_book}), 201
    return jsonify({'error': 'Invalid data'}), 400


@app.route("/api/v1/books/<int:book_id>", methods=['DELETE'])
def delete_book(book_id):
    result = books.delete(book_id)
    if not result:
        return jsonify({'error': 'Book not found'}), 404
    return jsonify({'result': result})



@app.route("/", methods=["GET"])
def index():
    form = BookForm()
    return render_template("index.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
