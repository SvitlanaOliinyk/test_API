import pytest
from models.book import Book

test_data = [
    Book(title='Пляшущие человечки', author='К.Дойль'),
    Book(title='S', author='O'),
]

@pytest.mark.parametrize('book', test_data, ids=[repr(b) for b in test_data])
def test_new_book(app, book):

    new_book = app.create_obj(book)
    #Verification
    assert new_book.status_code == 201
    new_book.json() == book.get_dict()
    #app.delete_obj(new_book)              # Где правильно писать?

@pytest.mark.parametrize('book', test_data, ids=[repr(b) for b in test_data])
def test_book_in_list(app, book):
    new_book = app.create_obj(book).json()
    book_list = app.get_list_obj()
    # Verification
    assert new_book in book_list
    #app.delete_obj(new_book.json())


def test_new_book_without_autor(app):
    book = Book(title='Пляшущие человечки')
    new_book = app.create_obj(book)
    #Verification
    assert new_book.status_code == 400



