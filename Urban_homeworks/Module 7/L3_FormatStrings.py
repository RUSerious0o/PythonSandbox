team_name = ['Мастера кода', 'Волшебники данных']
team_members = [7, 8]
team_score = [51, 53]
team_time = [19016.3, 19210]

print('В команде %s участников: %d !' % (team_name[0], team_members[0]))
print('Итого сегодня в командах участников: %d и %d !' % (team_members[0], team_members[1]))

print('Команда {} решила задач: {} !'.format(team_name[1], team_score[1]))
print('{0} решили задачи за {1:.1f} с !'.format(team_name[0], team_time[0]))

print(f'Команды решили {team_score[0]} и {team_score[1]} задач.')


winner = ''
if team_score[0] == team_score[1]:
    winner = team_name[0] if team_time[0] < team_time[1] else team_name[1]
else:
    winner = team_name[0] if team_score[0] > team_score[1] else team_name[1]

print(f'Результат битвы: победа команды {winner}!')
print(f'Сегодня было решено {sum(team_score)} задач, '
      f'в среднем по {sum(team_time)/sum(team_score):.1f} секунды на задачу!')
