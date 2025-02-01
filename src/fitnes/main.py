class InfoMessage():
    """Класс для создания объектов сообщений о тренировках.

    Атрибуты:
        training_type (str): Тип тренировки (например, 'Бег', 'Ходьба',
        'Плавание').
        duration (float): Длительность тренировки в часах.
        calories (float): Потраченные калории.
        distance (float): Пройденная дистанция в километрах.
        speed (float): Средняя скорость в километрах в час.
    """
    def __init__(self, *params: dict):
        (self.training_type, self.duration, self.calories, self.distance,
            self.speed) = params

    def get_message(self):
        return (f'Тип тренировки: {self.training_type}; Длительность: '
                f'{self.duration:.3f} ч.; Дистанция: {self.distance:.3f} км; '
                f'Ср. скорость: {self.speed:.3f} км/ч; Потрачено ккал:'
                f'{self.calories:.3f}.')


class Training():
    """фитнес-трекер - базовый класс"""

    # Длина шага в метрах
    LEN_STEP = 0.65
    M_IN_KM = 1000

    def __init__(self, action: int, duration: float):
        """
        action, тип int — количество совершённых действий
        duration float -- длительность в часах
        (число шагов при ходьбе и беге либо гребков — при плавании).

        time_training_minuntes - время тренировки в минутах
        """
        self.action = action
        self.duration = duration

    def get_distance(self) -> float:
        """
        возвращает дистанцию (в километрах), которую преодолел
        пользователь за время тренировки
        """
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self, kmh: bool = True) -> float:
        """
        возвращает значение средней скорости движения во время тренировки.
        скорость в км/ч
        """
        # преодолённая_дистанция_за_тренировку
        distance = self.get_distance()
        if kmh:
            # скорость в км/ч
            return distance / self.duration
        else:
            # скорость в м/c
            return (distance / self.M_IN_KM) / (self.duration * 3600)

    def get_spent_calories(self):
        """
        возвращает количество килокалорий, израсходованных за время тренировки.
        переопределяем для каждого вида спорта
        """
        pass

    def show_training_info(self, params):
        """ возвращает объект класса сообщения """

        msg = InfoMessage(*params)
        # print(msg.get_message())
        return msg

    def __str__(self):
        return "это базовый класс"


class Running(Training):
    """Класс для бега.

    Атрибуты:
        LEN_STEP (float): Длина шага в метрах для бега.
        CALORIES_MEAN_SPEED_MULTIPLIER (float): Множитель для расчета калорий.
        CALORIES_MEAN_SPEED_SHIFT (float): Смещение для расчета калорий.
    """

    LEN_STEP = 0.9
    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 1.79

    def __init__(self, *data):
        """Инициализация класса Running.

        Аргументы:
            data (tuple): Шаги, длительность и вес.
        """
        self.steps, self.duration, self.weight = data
        super().__init__(self.steps, self.duration)

    def get_spent_calories(self):
        """расчёт количества калорий, израсходованных за тренировку."""
        # средняя_скорость
        avg_speed = self.get_mean_speed()
        # время в минутах
        time_training_minuntes = self.duration * 60
        # метры не меняются в км
        m_in_km = super().M_IN_KM

        calories = ((self.CALORIES_MEAN_SPEED_MULTIPLIER * avg_speed +
                    self.CALORIES_MEAN_SPEED_SHIFT) * self.weight /
                    m_in_km * time_training_minuntes)
        return calories

    def show_training_info(self):
        """создание объекта сообщения о результатах тренировки."""

        calories = self.get_spent_calories()
        distance = self.get_distance()
        speed = self.get_mean_speed()

        params = ('Бег', self.duration, calories, distance, speed)

        msg = super().show_training_info(params)
        return msg

    def __str__(self):
        return "Класс для бега"


class SportsWalking(Training):
    """ПоХодим"""
    LEN_STEP = 0.65
    CALORIES_MEAN_SPEED_MULTIPLIER = 0.035
    CALORIES_MEAN_SPEED_SHIFT = 0.029

    def __init__(self, *data):
        self.steps, self.duration, self.weight, self.height = data
        super().__init__(self.steps, self.duration)

    def get_spent_calories(self):
        # средняя_скорость_в_метрах_в_секунду
        avg_speed = self.get_mean_speed(kmh=False)
        time_training_minuntes = self.duration * 60
        calories = ((self.CALORIES_MEAN_SPEED_MULTIPLIER * self.weight +
                    (avg_speed**2 / self.height) *
                    self.CALORIES_MEAN_SPEED_SHIFT * self.weight) *
                    time_training_minuntes)
        return calories

    def show_training_info(self):
        """создание объекта сообщения о результатах тренировки."""

        calories = self.get_spent_calories()
        distance = self.get_distance()
        speed = self.get_mean_speed()

        params = ('Хотьба', self.duration, calories, distance, speed)

        msg = super().show_training_info(params)
        return msg

    def __str__(self):
        return "Класс для хотьбы"


class Swimming(Training):
    """Поплаваем"""
    # Расстояние за один гребок
    LEN_STEP = 0.2
    M_IN_KM = 1000
    CALORIES_MEAN_SPEED_MULTIPLIER = 1.1
    CALORIES_MEAN_SPEED_SHIFT = 2

    def __init__(self, *data):
        """
        Входные данные:
        количество гребков, время в часах, вес пользователя,
        длина бассейна, сколько раз пользователь переплыл бассейн.
        """

        (self.action, self.duration, self.weight, self.length_pool,
         self.count_pool) = data
        self.time_training_minuntes = self.duration * 60
        super().__init__(self.action, self.duration)

    def get_mean_speed(self):
        """расчёт средней скорости движения во время тренировки."""
        return (self.length_pool * self.count_pool / self.M_IN_KM /
                self.time_training_minuntes)

    def get_spent_calories(self):
        """расчёт количества калорий, израсходованных за тренировку."""
        # средняя_скорость
        avg_speed = self.get_mean_speed()
        calories = ((avg_speed + self.CALORIES_MEAN_SPEED_MULTIPLIER) *
                    self.CALORIES_MEAN_SPEED_SHIFT * self.weight *
                    self.time_training_minuntes)

        return calories

    def show_training_info(self):
        """создание объекта сообщения о результатах тренировки."""

        calories = self.get_spent_calories()
        distance = self.get_distance()
        speed = self.get_mean_speed()

        params = ('Плавание', self.duration, calories, distance, speed)
        msg = super().show_training_info(params)
        return msg

    def __str__(self):
        return "Класс для плавания"


def read_package(workout_type, data: list):
    sports_classes = {'RUN': Running, 'SWM': Swimming, 'WLK': SportsWalking}
    if sports_classes.get(workout_type):
        sport_class: Training = sports_classes[workout_type](*data)
        return sport_class


def main(training: Training):
    info: InfoMessage = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training: Training = read_package(workout_type, data)
        if training:
            main(training)
