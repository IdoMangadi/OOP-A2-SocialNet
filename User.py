from Post import *


class Observer:
    """
    This class represents the 'Observer' design pattern
    """
    def __init__(self):
        self.notifications = []

    def update(self, notification_type: str, publisher: 'User'):
        pass


class User(Observer):
    # Constructor:
    def __init__(self, username: str, password: str):
        super().__init__()
        self.__is_connected = False
        self.__username = username
        self.__password = password
        self.__posts = []
        self.__followers = []

    # Methods:
    def get_name(self) -> str:
        return self.__username

    def get_password(self) -> str:
        return self.__password

    def is_connected(self) -> bool:
        return self.__is_connected

    def set_is_connected(self, is_connected: bool) -> None:
        self.__is_connected = is_connected

    def __str__(self):
        return f"User name: {self.__username}, Number of posts: {len(self.__posts)}, " \
               f"Number of followers: {len(self.__followers)} "

    def print_notifications(self):
        print(f"{self.__username}'s notifications:")
        for notification in self.notifications:
            print(notification)

    def add_follower(self, observer: 'Observer'):
        if observer not in self.__followers:
            self.__followers.append(observer)

    def remove_follower(self, observer: 'Observer'):
        if observer in self.__followers:
            self.__followers.remove(observer)

    def follow(self, user_to_follow: 'User'):
        # Connection validation check
        if not self.__is_connected:
            pass
        if user_to_follow == self:
            return None
        user_to_follow.add_follower(self)
        print(f"{self.get_name()} started following {user_to_follow.get_name()}")

    def unfollow(self, user_to_unfollow: 'User') -> None:
        # Connection validation check
        if not self.__is_connected:
            pass
        user_to_unfollow.remove_follower(self)
        print(f"{self.__username} unfollowed {user_to_unfollow.get_name()}")

    def notify_followers(self, notification_type: str):
        for follower in self.__followers:
            follower.update(notification_type, self)

    def update(self, notification_type: str, publisher: 'User'):
        if notification_type == "post":
            notification = f"{publisher.get_name()} has a new post"
            self.notifications.append(notification)
        if notification_type == "like":
            notification = f"{publisher.get_name()} liked your post"
            self.notifications.append(notification)
        if notification_type == "comment":
            notification = f"{publisher.get_name()} commented on your post"
            self.notifications.append(notification)

    def publish_post(self, *args) -> Post:
        """
        This functions implementing the 'Factory' design pattern as requested.
        :param args: args[0] = the type of the post (str), args[1..3] = content
        :return:
        """
        # Connection validation check
        if not self.__is_connected:
            pass
        # Implementing 'Factory' design pattern:
        if type(args[0]) == str:
            # Handling TextPost:
            if args[0] == "Text":
                if args[1] is not None:
                    p = TextPost(self, args[1])  # Creating a new text post
                    self.__posts.append(p)  # Updating the self posts list
                    self.notify_followers("post")  # notify all the followers using the observer DP
                    print(p)
                    return p
            # Handling ImagePost:
            if args[0] == "Image":
                if args[1] is not None:
                    p = ImagePost(self, args[1])  # Creating a new image post with args[1] = image path
                    self.__posts.append(p)  # Updating the self posts list
                    self.notify_followers("post")  # notify all the followers using the observer DP
                    print(p)
                    return p
            # Handling a SalePost:
            if args[0] == "Sale":
                if args[1] is not None:
                    p = SalePost(self, args[1], args[2], args[3])  # Creating a new sale post
                    self.__posts.append(p)  # Updating the self posts list
                    self.notify_followers("post")  # notify all the followers using the observer DP
                    print(p)
                    return p




