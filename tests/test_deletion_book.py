import pytest
from models.book import Book

@pytest.fixture
def book(app):
    b = Book(title='Crying people', author='K.Doyle')
    app.create_obj(b)
    return b

def test_delete(app, book):
    new_book = app.delete_obj(book)
    assert new_book.status_code == 204
