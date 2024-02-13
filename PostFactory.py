import User
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class PostFactory:
    @staticmethod
    def post_factory(user: 'User', *args) -> 'Post':
        post = None
        if args[0] == "Text":
            post = TextPost(user, args[1])
        if args[0] == "Image":
            post = ImagePost(user, args[1])
        if args[0] == "Sale":
            post = SalePost(user, args[1], args[2], args[3])
        post.notify(user, "post", "")
        return post


class Publisher:
        def notify(self, publisher: 'User', notification_type: str, notification_content: str):
            pass


class Post(Publisher):
    # Constructor:
    def __init__(self, user: 'User.User'):
        self._publisher = user
        self._users_liked = []
        self._comments = []

    # Methods:
    def get_publisher(self) -> 'User.User':
        return self._publisher

    def notify(self, publisher: 'User', notification_type: str, notification_content: str):
        """
        This function handling all the notification process by implementing the 'OBSERVER' design pattern.
        Note: according to the pattern, the 'publisher' is the one that play the roll of the notifier (AKA sender) side.
        :param publisher: the user that made the action causing the notification.
        :param notification_type: the type of the action 'publisher' did.
        :param notification_content: for like will be None, for comment will be the comment's content.
        :return:
        """
        if notification_type == "post":
            notification = f"{publisher.get_name()} has a new post"
            for follower in publisher.get_followers():
                follower.update(notification)

        if notification_type == "like":
            notification = f"{publisher.get_name()} liked your post"
            self._publisher.update(notification)
            print(f"notification to {self._publisher.get_name()}: {publisher.get_name()} liked your post")

        if notification_type == "comment":
            notification = f"{publisher.get_name()} commented on your post"
            self._publisher.update(notification)
            print(f"notification to {self._publisher.get_name()}: "
                  f"{publisher.get_name()} commented on your post: {notification_content}")

    def like(self, user_liked: 'User.User'):
        # Connection validation check:
        if not user_liked.is_connected():
            pass
        # Appending the liker to the liked list of the post:
        if user_liked not in self._users_liked:
            self._users_liked.append(user_liked)
        # Checking for self liking and calling 'notify':
        if self._publisher != user_liked:
            self.notify(user_liked, "like", "")

    def comment(self, user_commented: 'User.User', content: str):
        # Connection validation check:
        if not user_commented.is_connected():
            pass
        # Appending the comment to the comments list:
        self._comments.append((user_commented, content))
        # Checking for self commenting and calling 'notify':
        if self._publisher != user_commented:
            self.notify(user_commented, "comment", content)

    # Method for wrong user behavior:
    def sold(self, password: str):
        pass

    def discount(self, percent: int,  password: str):
        pass

    def display(self):
        pass


class TextPost(Post):
    # Constructor:
    def __init__(self, user: 'User.User', content: str):
        super().__init__(user)
        self.__content = "\""+content+"\""

    # Methods:
    def get_content(self):
        return self.__content

    def __str__(self):
        return f"{self.get_publisher().get_name()} published a post:\n{self.__content}\n"


class ImagePost(Post):
    # Constructor:
    def __init__(self, user: 'User.User', path: str):
        super().__init__(user)
        self.__path = path

    # Methods:
    def get_path(self):
        return self.__path

    def display(self):
        try:
            img = mpimg.imread(self.__path)
            plt.imshow(img)
            plt.axis('off')  # Turn off axis
            plt.show()
        except FileNotFoundError:
            pass
        print("Shows picture")

    def __str__(self):
        return f"{self.get_publisher().get_name()} posted a picture\n"


class SalePost(Post):
    # Constructor
    def __init__(self, user: 'User.User', description: str, price: int, town: str):
        super().__init__(user)
        self.__description = description
        self.__price = price
        self.__town = town
        self.__sold = False

    def discount(self, percent: int,  password: str) -> None:
        # Connection validation check
        if not super().get_publisher().is_connected():
            pass
        if password == self.get_publisher().get_password():
            if percent <= 100:
                self.__price = float(self.__price) * (float(100 - percent) / 100)
                print("Discount on {} product! the new price is: {}".format(self.get_publisher().get_name(), self.__price))

    def sold(self, password: str) -> None:
        if not super().get_publisher().is_connected():
            pass
        if password == self.get_publisher().get_password():
            self.__sold = True
            print("{}'s product is sold".format(self.get_publisher().get_name()))

    def __str__(self):
        if self.__sold:
            status = "Sold!"
        else:
            status = "For sale!"
        return f"{self.get_publisher().get_name()} posted a product for sale:\n{status} {self.__description}," \
               f" price: {self.__price}, pickup from: {self.__town}\n"



