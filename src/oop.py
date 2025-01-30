
class Human:
    def __init__(self, name):
        self.name = name

    # ответ по умолчанию для всех одинаковый, можно
    # доверить его родительскому классу
    def answer_question(self, question, ich_wais: bool = False):
        print(f"-- «Очень интересный вопрос! Не знаю.»")


class Student(Human):
    def __init__(self, name):
        super().__init__(name=name)
        self.name = name

    #  метод ask_question() принимает параметр someone:
    #  это объект, экземпляр класса Curator, Mentor или CodeReviewer,
    #  которому Student задаёт вопрос;
    #  параметр question — это просто строка
    #  имя объекта и текст вопроса задаются при вызове метода ask_question
    def ask_question(self, someone: Human, question: str, ich_wais: bool = False):
        # напечатайте на экран вопрос в нужном формате
        print(f"{someone.name}, {question}")
        # запросите ответ на вопрос у someone
        someone.answer_question(question, ich_wais)
        print()  # этот print выводит разделительную пустую строку


class Curator(Human):

    def __init__(self, name):
        super().__init__(name)

    def answer_question(self, question, ich_wais: bool = False):
        # здесь нужно проверить, пришёл куратору знакомый вопрос или нет
        if ich_wais:
            # если да - ответить на него
            print("Держись, всё получится. Хочешь видео с котиками?")
        else:
            # если нет - вызвать метод answer_question() у родительского класса
            super().answer_question(question)


# объявите и реализуйте классы CodeReviewer и Mentor
class Mentor(Human):

    def __init__(self, name):
        super().__init__(name)

    def answer_question(self, question, ich_wais: bool = False):
        # здесь нужно проверить, пришёл куратору знакомый вопрос или нет
        if ich_wais:
            # если да - ответить на него
            print("Отдохни и возвращайся с вопросами по теории.")
        else:
            # если нет - вызвать метод answer_question() у родительского класса
            print("Сейчас расскажу.")


class CodeReviewer(Human):

    def __init__(self, name):
        super().__init__(name)

    def answer_question(self, question, ich_wais: bool = False):
        # здесь нужно проверить, пришёл куратору знакомый вопрос или нет
        if ich_wais:
            # если да - ответить на него
            print("О, вопрос про проект, это я люблю.")
        else:
            # если нет - вызвать метод answer_question() у родительского класса
            super().answer_question(question)

# следующий код менять не нужно, он работает, мы проверяли


student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')
friend = Human('Виталя')

student1.ask_question(curator, 'мне грустненько, что делать?', True)
student1.ask_question(mentor, 'мне грустненько, что делать?', True)
student1.ask_question(reviewer, 'когда каникулы?')
student1.ask_question(reviewer, 'что не так с моим проектом?', True)
student1.ask_question(friend, 'как устроиться на работу питонистом?')
student1.ask_question(mentor, 'как устроиться работать питонистом?')
