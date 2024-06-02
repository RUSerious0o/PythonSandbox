class User:
    __nickname = ''
    __password = ''
    __age = 1

    __ADULT_AGE = 18

    def __init__(self, nickname, password, age):
        self.__nickname = nickname
        self.__password = password
        self.__age = age

    def __str__(self):
        return f'Пользователь: {self.__nickname}, возраст: {self.__age}'

    def set_password(self, pwd):
        self.__password = pwd

    def set_nickname(self, nick):
        self.__nickname = nick

    def set_age(self, age):
        self.__age = age

    def get_password(self):
        return self.__password

    def get_nickname(self):
        return self.__nickname

    def get_age(self):
        return self.__age

    def is_adult(self):
        return self.__age >= self.__ADULT_AGE