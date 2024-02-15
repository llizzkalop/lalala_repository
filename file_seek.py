from pprint import pprint

file_name = 'file1.txt'
with open(file_name, mode='r') as file:
    for line in file:
        print(line)
print(file.closed)# тот самый пособ проверить закрыт ли файл** к ответу задания

