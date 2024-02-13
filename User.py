from PostFactory import *
from typing import List


class Observer:
    """
    This class represents the 'Observer' design pattern
    """
    def __init__(self):
        self.notifications = []

    def update(self, notification: str):
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
               f"Number of followers: {len(self.__followers)}"

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

    def get_followers(self) -> 'List':
        return self.__followers

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
        if self in user_to_unfollow.get_followers():
            user_to_unfollow.remove_follower(self)
            print(f"{self.__username} unfollowed {user_to_unfollow.get_name()}")

    def update(self, notification: str):
        self.notifications.append(notification)

    def publish_post(self, *args) -> Post:
        post = PostFactory.post_factory(self, *args)
        self.__posts.append(post)  # Updating the self posts list
        print(post)
        return post

