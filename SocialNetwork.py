from User import User


class SocialNetwork:
    # Fields:
    __name = ""
    __users = []

    # Constructor:
    # TODO: singleton implementation needed!
    def __init__(self, name):
        self.__name = name
        print("The social network {} was created!".format(self.__name))

    # Methods:
    def sign_up(self, username, password) -> User:
        user = User(username, password)  # Creating the user
        self.__users.append(user)  # Appending to the users list
        return user



