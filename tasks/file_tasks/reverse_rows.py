"""
Написать функцию revert_rows, которая принимает путь к файлу и делает новый
файл. Создать новый файл, каждая строка которого получается из соответствующей
строки исходного файла перестановкой слов в обратном порядке.
"""


def revert_rows(file: str):
    with open(file) as file:
        with open("new file.txt", "w") as w_file:
            for line in file:
                temp_list = line.split(' ')
                reverse_string = ' '.join(temp_list[::-1]) + "\n"
                w_file.write(reverse_string)


revert_rows("text.txt")
