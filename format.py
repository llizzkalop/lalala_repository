# -*- coding: utf-8 -*-
first_team = 10
name_team_1 = 'Мастера кода'
second_team = 8
name_team_2 = 'Волшебники данных'

print('Команда "%s", состоит из %s участников' % (name_team_1, first_team))
print('Количество участников в командах : %s и %s' % (first_team, second_team))

scoar_1st_team = 15
scoar_sec_team = 10
print('Команда "{}" решила: {} задач.'.format(name_team_2, scoar_sec_team))
team1_time = 780.50
team2_time = 900.20
print('"{}" решили задачи за: {} с.'.format(name_team_2, team2_time))
print(f'Команды решили по {scoar_1st_team} и {scoar_sec_team} задач.')

if scoar_sec_team >= scoar_1st_team:
    print(f'Победила команда "{name_team_2}"')
else:
    scoar_1st_team <= scoar_sec_team
    print(f'Победила команда "{name_team_1}".')

task_total = scoar_1st_team + scoar_sec_team
all_time = team1_time + team2_time
time_ovg = all_time//25
print(f'Сегодня было решено {task_total} задач, в среднем за {time_ovg} с.!')