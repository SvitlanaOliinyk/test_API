import pytest
from models.book import Book


test_data = []
res = []

with open("test_data_books.txt") as file:
    old = file.read().splitlines()
for item in old:
    res = item.split('&')
    book = Book(title=res[0], author=res[1])
    test_data.append(book)


# test_data = [
#     Book(title='Пляшущие человечки', author='К.Дойль'),
#     Book(title='S', author='O'),
# ]

@pytest.mark.parametrize('book', test_data, ids=[repr(b) for b in test_data])
def test_new_book(app, book):

    new_book = app.create_obj(book)
    #Verification
    assert new_book.status_code == 201
    assert new_book.json() == book.get_dict()
    app.delete_obj(book)

@pytest.mark.parametrize('book', test_data, ids=[repr(b) for b in test_data])
def test_book_in_list(app, book):
    new_book = app.create_obj(book).json()
    book_list = app.get_list_obj()
    # Verification
    assert new_book in book_list
    app.delete_obj(book)


def test_new_book_without_autor(app):
    book = Book(title='Пляшущие человечки')
    new_book = app.create_obj(book)
    #Verification
    assert new_book.status_code == 400




