import hashlib

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = int(hashlib.sha256(password.encode()).hexdigest(), 16)  # Хешируем пароль
        self.age = age

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

from time import sleep

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        """ Метод для входа пользователя """
        hashed_password = int(hashlib.sha256(password.encode()).hexdigest(), 16)
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                return f"Пользователь {nickname} успешно вошел."
        return "Неверный логин или пароль."

    def register(self, nickname, password, age):
        """ Метод для регистрации нового пользователя """
        new_user = User(nickname, password, age)
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует.")
                return
        self.users.append(new_user)
        self.log_in(nickname, password)
        print(f"Пользователь {nickname} зарегистрирован и выполнен вход.")

    def log_out(self):
        """ Метод для выхода текущего пользователя """
        if self.current_user is not None:
            self.current_user = None
            print("Вы вышли из аккаунта.")
        else:
            print("Нет активного пользователя для выхода.")

    def add(self, *videos):
        """ Метод для добавления новых видео """
        for video in videos:
            if any(video.title == existing_video.title for existing_video in self.videos):
                continue
            self.videos.append(video)

    def get_videos(self, search_word):
        """ Метод для поиска видео по ключевому слову """
        search_word = search_word.lower()  # Приводим к нижнему регистру
        results = [video.title for video in self.videos if search_word in video.title.lower()]
        return results

    def watch_video(self, title):
        """ Метод для воспроизведения видео """
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        found_video = next((video for video in self.videos if video.title == title), None)
        if found_video is None:
            print(f"Видео '{title}' не найдено.")
            return

        if found_video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        print(f"Секунды воспроизведения: ", end="")
        for second in range(found_video.time_now + 1, found_video.duration + 1):
            print(second, end=" ")
            sleep(1)  # Пауза между секциями
        print("\nКонец видео")
        found_video.time_now = 0  # Сброс времени после окончания видео


if __name__ == "__main__":
    ur = UrTube()

    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавляем видео
    ur.add(v1, v2)

    # Проверяем поиск
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Пробуем посмотреть видео без авторизации
    ur.watch_video('Для чего девушкам парень программист?')

    # Регистрация и попытка посмотреть видео
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')

    # Повторная регистрация другого пользователя
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Пытаемся войти под другим аккаунтом
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user.nickname)

    # Попробовать воспроизвести несуществующее видео
    ur.watch_video('Лучший язык программирования 2024 года!')