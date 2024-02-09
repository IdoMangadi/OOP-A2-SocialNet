class Post:
    # Fields:
    # _type = ""
    # _publisher = None
    # _users_liked = []
    # _comments = []  # A list of dictionaries

    # Constructors:
    def __init__(self, user: 'User'):
        self._publisher = user
        self._users_liked = []
        self._comments = []

    # Methods:


class TextPost(Post):
    # Fields:
    # __content = ""

    # Constructor:
    def __init__(self, user: 'User', content: str):
        super().__init__(user)
        self.__content = content

    # Methods:
    def get_content(self):
        return self.__content


class ImagePost(Post):
    # Constructor:
    def __init__(self, user: 'User', path: str):
        super().__init__(user)
        self.__path = path

    # Methods:
    def get_path(self):
        return self.__path


class SalePost(Post):
    # Constructor
    def __init__(self, user: 'User', description: str, price: int, town: str):
        super().__init__(user)
        self.__description = description
        self.__price = price
        self.__town = town
