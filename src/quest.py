from datetime import datetime as dat
import time

quest_name = 'Сбор пиксельники'
quest_goal = 'Соберите 12 ягод пиксельники.'
quest_description = '''
древнем лесу Кодоборье растёт ягода "пиксельника".
Она нужна для приготовления целебных снадобий.
Соберите 12 ягод пиксельники.'''


class Quest:
    """
    Класс создния загадки.
    accept_quest() — чтобы игрок мог взять квест
    pass_quest() — чтобы игрок мог завершить квест.
    """

    def __init__(self, quest_name, quest_goal, quest_description):
        """  Инициализация класса. """

        self.start_time = None
        self.end_time = None
        self.result_test = ''
        self.quest_name = quest_name
        self.quest_goal = quest_goal
        self.quest_description = quest_description

    def accept_quest(self):
        """
        Зафиксировать начало если оно было пустым
        и вернуть фразу 'Начало " + текущая дата и время,
        иначе - вывести что всё уже было
        """

        if self.end_time is None:
            self.start_time = dat.now()
            self.result_test = 'Квест выполняется.'
            return f'Начало "{self.quest_name}"  положено.'
        else:
            self.result_test = 'Квест завершён.'
            return "C этим испытанием вы уже справились."

    def pass_quest(self):
        """
        Фиксирует окончание если начальная дата не пуствая.
        Вычисляет и возвращает разницу.
        """

        if self.start_time:
            return 'Нельзя завершить то, что не имеет начала!'
        else:
            self.end_time = dat.now()
            completion_time_delta = (self.end_time - self.start_time)
            completion_time = completion_time_delta.seconds / 60

            return (f'Квест "{self.quest_name}" окончен. {self.end_time} '
                    f'Время выполнения квеста: {completion_time:.2f}')

    # Вот он — новый метод! Именно в нём описывается то, что должно выводиться
    # при печати объекта.
    def __str__(self):
        result = (f'Цель квеста {self.quest_name} - {quest_goal} '
                  f'{self.result_test}')
        return result


if __name__ == '__main__':
    new_quest = Quest(quest_goal=quest_goal,
                      quest_name=quest_name,
                      quest_description=quest_description)

    print(new_quest.__doc__)
    print(new_quest.pass_quest())
    print(new_quest.accept_quest())
    time.sleep(20)
    print(new_quest.pass_quest())
    print(new_quest.accept_quest())
    print(new_quest)
