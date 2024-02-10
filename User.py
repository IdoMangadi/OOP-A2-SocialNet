from Post import *


class Observer:
    def __init__(self):
        self.notifications = []

    def update(self, publisher: 'User'):
        notification = f"{publisher.get_name()} has a new post"
        self.notifications.append(notification)


class Publisher:
    def __init__(self):
        self.__followers = []

    def follow(self, observer: 'Observer'):
        if observer not in self.__followers:
            self.__followers.append(observer)

    def unfollow(self, obsever: 'Observer'):
        self.__followers.remove(obsever)

    def notify_observers(self):
        for observer in self.__followers:
            observer.update()


class User(Observer, Publisher):
    # Constructor:
    def __init__(self, username: str, password: str):
        self.__username = username
        self.__password = password
        self.__follows = []
        self.__posts = []
        self.__followers = []
        self.__notifications = []

    # Methods:
    def get_name(self) -> str:
        return self.__username

    def get_password(self):
        return self.__password

    def set_follower(self, new_follower: 'User'):
        if new_follower not in self.__followers:
            self.__followers.append(new_follower)

    def follow(self, user_to_follow: 'User') -> None:
        """
        This function append the user_to_follow to the current user's follows list.
        If already exist, it will not be appended.
        :param user_to_follow:
        :return: None
        """
        # Validation check:
        if self == user_to_follow:
            return None
        # Checking if already exist:
        if user_to_follow not in self.__follows:
            self.__follows.append(user_to_follow)
            print("{} started following {}".format(self.__username, user_to_follow.get_name()))
        # Updating user_to_follow about new follower:
        user_to_follow.set_follower(self)

    def unfollow(self, user_to_unfollow: 'User') -> None:
        """
        Removes the instance of the parameter user_to_unfollow from the follows list.
        Note: the 'follow' function will append to the list only users that are not yet there.
        :param user_to_unfollow:
        :return: None
        """
        if user_to_unfollow in self.__follows:
            self.__follows.remove(user_to_unfollow)
            print("{} unfollowed {}".format(self.__username, user_to_unfollow.get_name()))

    def new_post_notification(self, publisher: 'User'):
        notification = "{} has a new post".format(publisher.get_name())
        self.__notifications.append(notification)

    """
    Activated when a user (publisher) publishing a new post.
    """
    def notify_followers(self):
        for follower in self.__followers:
            follower.new_post_notification(self)

    def publish_post(self, *args) -> Post:
        # Implementing 'Factory' design pattern:
        if type(args[0]) == str:
            # Handling TextPost:
            if args[0] == "Text":
                if args[1] is not None:
                    p = TextPost(self, args[1])  # Creating a new text post
                    self.__posts.append(p)  # Updating the self posts list
                    self.notify_followers()  # notify all the followers using the observer DP
                    print(p)
                    return p
            # Handling ImagePost:
            if args[0] == "Image":
                if args[1] is not None:
                    p = ImagePost(self, args[1])  # Creating a new image post
                    self.__posts.append(p)  # Updating the self posts list
                    self.notify_followers()  # notify all the followers using the observer DP
                    print(p)
                    # TODO: complete the image opening according to instructions
                    return p
            # Handling a SalePost:
            if args[0] == "Sale":
                if args[1] is not None:
                    p = SalePost(self, args[1], args[2], args[3])  # Creating a new sale post
                    self.__posts.append(p)  # Updating the self posts list
                    self.notify_followers()  # notify all the followers using the observer DP
                    print(p)
                    return p

    def like_notification(self, user_liked: 'User'):
        notification = "{} liked your post".format(user_liked.get_name())
        self.__notifications.append(notification)
        print(f"notification to {self.get_name()}: " + notification)

    def comment_notification(self, user_commented: 'User', content: str):
        notification = "{} commented on your post: {}".format(user_commented.get_name(), content)
        self.__notifications.append(notification)
        print(f"notification to {self.get_name()}:" + notification)




