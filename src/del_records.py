"""
При копировании из браузера получаются  не нужные
пробелы с цифрами такого вида:

6
    def __init__(self, latitude, longitude):
7
        self.latitude = radians(latitude)
8
        self.longitude = radians(longitude)
9
?
Вставляем этот код в MY_FILE
Копируем нормальный из MY_FILE_OUT после запуска
"""

from pathlib import Path

MY_FILE = ('D:\\my_file.txt')
MY_FILE_OUT = ('D:\\my_file_out.txt')


def not_contains_digit_followed_by_newline(string):
    # Проверяем наличие первой цифры и перенос строки
    # d = bool(s) and any(char.isdigit() for char in s.splitlines()[0]) and '\n' in s
    if len(string)<=4 and string[0].isdigit():
        return False
    else:
        return True


def read_txt_file() -> list:
    lst = []
    if Path(MY_FILE).exists():
        with open(MY_FILE, encoding="cp1251") as test_file:
            return test_file.readlines()
    else:
        return lst


def delete_empty_strings(my_text: list):
    lst_out = []
    for string in my_text:
        if not_contains_digit_followed_by_newline(string):
            # Если в строке знак вопроса и перенос строки
            if len(string) == 2 and '?\n' in string:
                string = '\n'
            lst_out.append(string)
    return lst_out


def save_to_file(my_list):
    # Открываем файл в режиме записи (w)
    with open(MY_FILE_OUT, 'w', encoding="cp1251") as file:
        # Проходим по каждому элементу списка
        for item in my_list:
            # Записываем элемент в файл
            file.write(item)

    print(f"Список успешно записан в файл {MY_FILE_OUT}.")


if __name__ == "__main__":
    file_text = read_txt_file()
    lst_out = delete_empty_strings(file_text)
    if lst_out:
        save_to_file(lst_out)
