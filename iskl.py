def string_to_int(s):
    try:
        return int(s)
    except ValueError:
        return f"Не могу это сделать {s} - не является числом..."


def read_files(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Файл '{filename}'не найден")
    except IOError:
        print(f"Ошибка при работе с файлом'{filename}'")


def divides_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Ошибка деления на ноль"
    except TypeError:
        return "Ошибка, я не могу сложить число и строку"


def access_list_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return f"Ошибка: индекс {index} не входит в диапазон списка"
    except TypeError:
        return f"Ошибка: индекс должен быть целым числом"

print(string_to_int('Hello'))
read_files('pop.txt')
print(divides_numbers('0',5))
print(divides_numbers(10,0))
print(access_list_element("Low",15))
print(access_list_element(15,5.5))
