import time

# ДЗ: исправить ошибки подсчета времени, добавить комментарии, описать какую парадигму использовали.
# В данном коде используется объектно-ориентированная парадигма программирования.
# Создан Класс StopWatch с логикой работы секундомера.
# 1. Создан экземпляр класса StopWatch.
# 2. Создано меню управления для пользователя.
# 3. Выбор пользователя  вызывает соответствующие методы класса StopWatch.
# 4. Время секундомера выводится в формате мм:сс.
class StopWatch:
    def __init__(self):
        self.start_time = None  # Переменная для хранения времени начала работы секундомера
        self.bool_pause_time = False # Флаг для указания наличия паузы
        self.pause_start_time = None  # Переменная для хранения времени начала паузы
        self.total_paused_time = 0 # время пауз


    def start(self): # запуск секундомера
        if not self.start_time:  # Если время начала работы секундомера не установлено
            self.start_time = time.time()  # Устанавливаем время в качестве времени начала
        elif self.bool_pause_time:  # Если была пауза и секундомер находится в режиме паузы
            self.total_paused_time += time.time() - self.pause_start_time # Учет время паузы
            self.bool_pause_time = False # Убираем флаг паузы

    def pause(self):
        if self.start_time and not self.bool_pause_time: # Проверяем если время начала работы секундомера
            # установлено и секундомер не находится в режиме паузы
            self.bool_pause_time = True  # Устанавливаем флаг паузы
            self.pause_start_time = time.time()  # Устанавливаем текущее время в качестве времени начала паузы

    def resume(self):
        if self.bool_pause_time:  # Проверяем если секундомер находится в режиме паузы
            self.bool_pause_time = False   # Снимаем флаг паузы
            self.total_paused_time += time.time() - self.pause_start_time  # Добавляем время паузы к общему
            # времени паузы

    def stop(self):
        self.start_time = None   # Сбрасываем время начала работы секундомера
        self.bool_pause_time = False # Сбрасываем флаг паузы
        self.pause_start_time = None # Сбрасываем время начала паузы
        self.total_paused_time = 0 # Сбрасываем общее время пауз

    # Ошибка в том, что в  методе  get_time() неправильно  вычисляется временя
    # при наличии паузы. Ошибка в определении условия.
    # В условии вместо self.pause_start_time, нужно использовать
    # self.bool_pause_time.
    def get_time(self):
        if self.start_time:  # Проверка если время начала работы секундомера установлено
            if self.bool_pause_time:  # Проверка если время начала работы секундомера установлено
                return self.pause_start_time - self.start_time - self.total_paused_time  # Вычисляем время с учетом паузы
            else:
                return time.time() - self.start_time - self.total_paused_time # Вычисляем общее время без паузы
        else:
            return 0 # Возвращаем 0, если время начала работы секундомера не установлено

    def get_time_format(self):
        time = int(self.get_time())
        min = time // 60  # Вычисляем количество минут
        sec = time % 60   # Вычисляем количество секунд
        return f"{min:02}: {sec:02}"


if __name__ == "__main__":  # Создаем экземпляр класса StopWatch
    name = StopWatch()
    while True:  # Создаем меню пользователя
        print("1 - start")
        print("2 - pause")
        print("3 - continue")
        print("4 - stop")
        print("5 - exit")

        choice = input("Choose number: ") # Определяем выбор пользователя
        if choice == "1":
            name.start()
        elif choice == "2":
            name.pause()
        elif choice == "3":
            name.resume()
        elif choice == "4":
            name.stop()
        elif choice == "5":
            print("Exit")
            break # Выходим из цикла

    total = name.get_time_format()  # Получаем отформатированное время работы секундомера
    print("time", total) # Выводим время работы секундомера
