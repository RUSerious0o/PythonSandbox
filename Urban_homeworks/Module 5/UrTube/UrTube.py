from hashlib import md5
from time import sleep

from User import *
from Video import *

class UrTube:
    '''
    Атриубты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)

    Метод log_in, который принимает на вход аргументы: login, password и пытается найти пользователя в users с такмими же логином и паролем. Если такой пользователь суещствует, то current_user меняется на найденного. Помните, что password передаётся в виде строки, а сравнивается по хэшу.

    Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список, если пользователя не существует (с таким же nickname). Если существует, выводит на экран: "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.

    Метод log_out для сброса текущего пользователя на None.

    Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же названием видео ещё не существует. В противном случае ничего не происходит.

    Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).

    Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела), то ничего не воспроизводится, если же находит ведётся отчёт в консоль на какой секунде ведётся просмотр. После текущее время просмотра данного видео
    '''

    __users = []
    __videos = []

    def __hash_pwd(self, password):
        return md5(password.encode()).hexdigest()

    def __init__(self):
        self.__current_user = None

    def __str__(self):
        result = 'Users:\n'
        for user in self.__users:
            result += str(user) + '\n'

        result += 'Current user:\n'
        if self.__current_user:
            result += str(self.__current_user) + '\n'
        else:
            result += 'Никто не авторизован\n'

        result += 'Videos:\n'
        for video in self.__videos:
            result += str(video) + '\n'

        return result

    def get_current_user(self):
        return self.__current_user

    def login(self, login, password):
        for user in self.__users:
            if login == user.get_nickname():
                if self.__hash_pwd(password) == user.get_password():
                    self.__current_user = user
                    # print(f'Добро пожаловать, {user.get_nickname()}!')
                else:
                    print('Введен неверный пароль!')

                break

    def register(self, login, password, age):
        for user in self.__users:
            if user.get_nickname() == login:
                print(f'Пользователь {login} уже зарегистрирован')
                return

        self.__users.append(User(login, self.__hash_pwd(password), age))
        self.login(login, password)

    def log_out(self):
        self.__current_user = None

    def add(self, *videos):
        for item in videos:
            if isinstance(item, Video):
                self.__videos.append(item)
            elif isinstance(item, list):
                for video in item:
                    if isinstance(item, Video):
                        self.__videos.append(video)

    def get_videos(self, key):
        result = []
        for video in self.__videos:
            if str(key).lower() in str(video.get_title()).lower():
                result.append(video)

        return result

    def watch_video(self, video_name):
        if not self.__current_user:
            print('Войдите в аккаунт чтобы смотреть видео')
            return

        selected_video = None
        for video in self.__videos:
            if video.get_title() == video_name:
                selected_video = video
                break

        if not selected_video:
            print('Видео не найдено')
            return

        if selected_video.is_adult() and not self.__current_user.is_adult():
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
            return

        print('Смотрим видео:', selected_video.get_title())
        for i in range(selected_video.get_duration()):
            sleep(0.33)
            print(i + 1, end=' ')
        print('Конец видео')


if __name__ == '__main__':
    tube = UrTube()
    tube.register('Олег', 'abc321', 35)
    tube.register('Олег', 'abc3221', 30)
    tube.register('Ольга', 'abc221', 15)
    tube.register('Петр', 'abc32', 18)
    videos = [Video('Маша и медвед', 7),
              Video('Фиксики', 5),
              Video('X-Men', 12),
              Video('МедвЕди в лесу', 3)]
    adult_video = Video('Happy tree friends', 6, adult_mode=True)
    tube.add(*videos)
    tube.add(adult_video)

    tube.login('Олег', 'a3221')
    tube.login('Олег', 'abc321')

    print('\n', tube, '\n')

    for video in tube.get_videos('мед'):
        print(video)

    for video in tube.get_videos('мffед'):
        print(video)

    print()
    tube.watch_video('videos[0].get_title()')
    tube.watch_video(videos[0].get_title())
    tube.watch_video(adult_video.get_title())
    tube.log_out()
    tube.login('Ольга', 'abc221')
    tube.watch_video(adult_video.get_title())
    tube.watch_video(videos[1].get_title())

    tube_2 = UrTube()
    print('\n', tube, '\n', tube_2)
    tube_2.watch_video(videos[2].get_title())
    tube.watch_video(videos[2].get_title())
