from random import randint
# импортируем функцию run_screensaver().
from graphic_arts.start_game_banner import run_screensaver

# Вот она — новая глобальная константа.
DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10


class Character:
    """Базовый класс"""

    # Константа для диапазона очков урона.
    RANGE_VALUE_ATTACK = (1, 3)
    # Новая переменная класса — диапазон значения защиты.
    RANGE_VALUE_DEFENCE = (1, 5)

    SPECIAL_SKILL = 'Удача'
    SPECIAL_BUFF = 15

    # описание класса
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'

    def __init__(self, name):
        self.name = name
        self.msg_default = True

    def attack(self):
        # распаковка кортежа
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс урон противнику равный '
                f'{value_attack}')

    def defence(self):
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} ед. урона')

    def special(self):
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')

    def __str__(self):
        """Возвращает имя класса и описание класса"""
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}'


class Warrior(Character):
    """Воин"""
    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный, но тупой '
                             'как пробка!')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    # SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'

    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def __str__(self):
        if self.msg_default:
            return super().__str__()
        else:
            return f'{self.name}, ты Воитель — отличный боец ближнего боя.'


class Mage(Character):
    """Маг"""

    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом, но более слабый '
                             'в защите')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'

    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def __str__(self):
        if self.msg_default:
            return super().__str__()
        else:
            return (f'{self.name}, ты Маг — превосходный укротитель стихий.')


class Healer(Character):
    """Лекарь"""

    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита'

    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def __str__(self):
        if self.msg_default:
            return super().__str__()
        else:
            return (f'{self.name}, , ты Лекарь — чародей, способный исцелять '
                    'раны.')


def choice_char_class(char_name: str) -> Character:
    """
    Возвращает строку с выбранным
    классом персонажа.
    """
    # Добавили словарь, в котором соотносится ввод пользователя и класс
    # персонажа.
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}

    approve_choice: str = None

    while approve_choice != 'y':
        selected_class = input('Введи название персонажа, '
                               'за которого хочешь играть: Воитель — warrior, '
                               'Маг — mage, Лекарь — healer: ')
        # Выбираем selected_class
        # Явно указываем что тип класс Character - преобразуем получается
        # из строки
        # Сразу передаём в класс char_class:Character имя char_name
        char_class: Character = game_classes[selected_class](char_name)
        # Вывели в терминал описание персонажа.
        print(char_class)
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


def start_training(char_class: Character):
    char_class.msg_default = False
    print(char_class)
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = ''
    while cmd != 'skip':
        cmd = input('Введи команду (attack, defend, heal или skip):').lower()

        # Проверяем, существует ли метод с таким названием
        method_to_call = getattr(char_class, cmd, None)

        if method_to_call:  # Если метод существует
            result = method_to_call()  # Вызываем метод
            print(result)  # Выводим результат
        elif cmd != 'skip':
            print(f"Команда '{cmd}' не найдена.")
    return 'Тренировка окончена.'


def main():
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class(char_name)
    print(start_training(char_class))


if __name__ == '__main__':
    main()
