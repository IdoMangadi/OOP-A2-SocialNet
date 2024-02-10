import User


class Post:
    # Constructor:
    def __init__(self, user: 'User'):
        self._publisher = user
        self._users_liked = []
        self._comments = []

    # Methods:
    def get_publisher(self) -> 'User':
        return self._publisher

    def like(self, user_liked: 'User'):
        if user_liked not in self._users_liked:
            self._users_liked.append(user_liked)
        if self._publisher != user_liked:
            self._publisher.like_notification(user_liked)

    def comment(self, user_commented: 'User', content: str):
        self._comments.append((user_commented, content))
        if self._publisher != user_commented:
            self._publisher.comment_notification(user_commented, content)


class TextPost(Post):
    # Constructor:
    def __init__(self, user: 'User', content: str):
        super().__init__(user)
        self.__content = content

    # Methods:
    def get_content(self):
        return self.__content

    def __str__(self):
        return f"{self.get_publisher().get_name()} published a post:\n{self.__content}\n"


class ImagePost(Post):
    # Constructor:
    def __init__(self, user: 'User', path: str):
        super().__init__(user)
        self.__path = path

    # Methods:
    def get_path(self):
        return self.__path

    def __str__(self):
        return f"{self.get_publisher().get_name()} posted a picture\n"


class SalePost(Post):
    # Constructor
    def __init__(self, user: 'User', description: str, price: int, town: str):
        super().__init__(user)
        self.__description = description
        self.__price = price
        self.__town = town
        self.__sold = False

    def discount(self, percent: int,  password: str) -> None:
        if password == self.get_publisher().get_password():
            if percent <= 100:
                self.__price = float(self.__price) * (float(100 - percent) / 100)
                print("Discount on {} product! the new price is: {}".format(self.get_publisher().get_name(), self.__price))

    def sold(self, password: str) -> None:
        if password == self.get_publisher().get_password():
            self.__sold = True
            print("{}'s product is sold".format(self.get_publisher().get_name()))

    def __str__(self):
        if self.__sold:
            status = "Sold!"
        else:
            status = "For sale!"
        return f"{self.get_publisher().get_name()} posted a product for sale:\n{status} {self.__description}, price: {self.__price}, pickup from: {self.__town}\n"



