
class Book:
    def __init__(self, title = None, author = None, id = None):
        self.title = title
        self.author = author
        self.id = id

    def set_id(self, id):
        self.id = id

    def get_dict_without_id(self):
        return ({"title": self.title,
                 "author": self.author})

    def get_dict(self):
        return ({"id": self.id,
                 "title": self.title,
                 "author": self.author})