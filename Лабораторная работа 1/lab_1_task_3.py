# TODO разделить список игроков напополам и вывести две команды
list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

middle_index = len(list_players) // 2

first_team = list_players[:middle_index]
second_team = list_players[middle_index:]

print('первая команда: ', first_team)
print('вторая команда: ', second_team)