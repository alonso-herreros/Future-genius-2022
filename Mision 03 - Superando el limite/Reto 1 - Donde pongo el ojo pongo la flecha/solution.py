import math

# Pega la función entre estas dos filas de Almohadillas
#########################################################

#########################################################

positions = input()
enemy_x_str, enemy_y_str, player_x_str, player_y_str = positions.split(",")
enemy_x, enemy_y, player_x, player_y = int(enemy_x_str), int(enemy_y_str), int(player_x_str), int(player_y_str)
angle = angle = computeOrientation(enemy_x, enemy_y, player_x, player_y)
print(angle)
