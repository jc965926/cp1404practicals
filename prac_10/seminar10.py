# def print_scores(player_to_score, player_width):
#     for player in player_to_score:
#         print(f"{player:<{player_width}} {player_to_score[player]:>3}")
#
# print_scores({"Bob": 3, "James": 23}, 5)
#
# def get_high_score(player_to_score):
#     return max([player_to_score[player] for player in player_to_score])
#
# print(get_high_score({"Bob": 3, "James": 23}))

x = 5
for i in range(x):
    x = x + i
    print(x, end=" ")