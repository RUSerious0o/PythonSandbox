class Video:
    __title = ''
    __duration = ''
    __time_now = 0
    __adult_mode = False

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.__title = title
        self.__duration = duration
        self.__time_now = time_now
        self.__adult_mode = adult_mode

    def __str__(self):
        return (f'Название: {self.__title}, продолжительность: {self.__duration}, '
                f'пауза: {self.__time_now}, для взрослых: {'да' if self.__adult_mode else 'нет'}')

    def __repr__(self):
        return self.get_title()

    def get_title(self):
        return self.__title

    def is_adult(self):
        return self.__adult_mode

    def get_duration(self):
        return self.__duration
