

class User:
    # Fields:
    __username = ""
    __password = ""
    __follows = None  # A list of the users that self is follows after

    # Constructor:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__follows = []

    # Methods:
    def get_name(self) -> str:
        return self.__username

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

