from User import User
from typing import List


class SocialNetwork:
    """
    This class represent a social network under to the assignment terms.
    In this class we implemented the 'singleton' design pattern.
    """
    _instance = None

    # Constructor:
    def __init__(self, name):
        # Handling first creation of SocialNetwork:
        if SocialNetwork._instance is None:
            self.__name = name
            self.__users: List[User] = []
            self.__connected_users: List[User] = []
            print("The social network {} was created!".format(self.__name))
            SocialNetwork._instance = self
        else:
            pass

    # Methods:
    def sign_up(self, username: str, password: str) -> User:
        # username validation check:
        for signed_user in self.__users:
            if signed_user.get_name() == username:
                pass
        if len(password) < 4 or len(password) > 8:
            pass

        user = User(username, password)  # Creating the user
        self.__users.append(user)  # Appending to the users list
        self.__connected_users.append(user)
        user.set_is_connected(True)
        return user

    def log_in(self, username: str, password: str):
        for signed_user in self.__users:
            if signed_user.get_name() == username and signed_user.get_password() == password:  # Authentication
                if signed_user not in self.__connected_users:
                    self.__connected_users.append(signed_user)
                    signed_user.set_is_connected(True)
                    print(f"{signed_user.get_name()} connected")

    def log_out(self, username: str):
        for connected_user in self.__connected_users:
            if connected_user.get_name() == username:
                self.__connected_users.remove(connected_user)
                connected_user.set_is_connected(False)
                print(f"{connected_user.get_name()} disconnected")

    def __str__(self) -> str:
        res = f"{self.__name} social network:\n"
        for user in self.__users:
            res = res + f"{user}" + "\n"
        return res
