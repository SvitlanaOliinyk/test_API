import unittest
from pulse_api_client import PulseRestAPI
from models import Book


class BookTestCase(unittest.TestCase):
    def setUp(self):
        self.book_client = PulseRestAPI('books')

    def test_new_book(self):
        book = Book(title='Пляшущие человечки', author='К.Дойль')
        new_book = self.book_client.create_obj(book)
        #Verification
        self.assertEqual(new_book.status_code, 201)
        self.assertDictEqual(new_book.json(), book.get_dict())

        self.book_client.delete_obj(new_book.json())              # Где правильно писать?

    def test_book_in_list(self):
        book = Book(title='Пляшущие человечки', author='К.Дойль')
        new_book = self.book_client.create_obj(book).json()
        book_list = self.book_client.get_list_obj()
        # Verification
        self.assertIn(new_book,book_list)

        self.book_client.delete_obj(new_book)                     # Где правильно писать?



if __name__ == '__main__':
    unittest.main(verbosity=2)




