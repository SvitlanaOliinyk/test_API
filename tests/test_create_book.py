from models.book import Book


def test_new_book(app):
    book = Book(title='Пляшущие человечки', author='К.Дойль')
    new_book = app.create_obj(book)
    #Verification
    assert new_book.status_code == 201
    new_book.json() == book.get_dict()

    # self.book_client.delete_obj(new_book.json())              # Где правильно писать?

def test_new_book_without_autor(app):
    book = Book(title='Пляшущие человечки')
    new_book = app.create_obj(book)
    #Verification
    assert new_book.status_code == 400

def test_book_in_list(app):
    book = Book(title='Пляшущие человечки', author='К.Дойль')
    new_book = app.create_obj(book).json()
    book_list = app.get_list_obj()
    # Verification
    assert new_book in book_list

    # self.book_client.delete_obj(new_book)                     # Где правильно писать?


#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)




