import functools

heights = [185, 190, 175, 195, 180, 192, 170, 198, 177, 182, 191, 176, 186, 181, 194, 172, 199, 178, 183, 187]


def count_players(teams, height):
    if height >= 190:
        teams['basketball'] += 1
    else:
        teams['football'] += 1
    return teams


initial_teams = {'basketball': 0, 'football': 0}
final_teams = functools.reduce(count_players, heights, initial_teams)

print(f"В баскетбольную команду будет направлено {final_teams['basketball']} человек")
print(f"В футбольную команду будет направлено {final_teams['football']} человек")