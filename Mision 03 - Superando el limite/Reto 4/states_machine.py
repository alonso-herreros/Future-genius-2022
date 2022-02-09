# Possible states
HighHealth = 1
RegularHealth = 2
LowHealth = 3
Defeated = 4

# Get state and damage flag from user
state_str, damage_str = input().split(",")
state, damageFlag = int(state_str), int(damage_str)
if state not in range(1, 5):
    raise ValueError("State only can be 1, 2, 3 or 4")
if damageFlag not in range(2):
    raise ValueError("State only can be 0 or 1")

# Implementar aqui la máquina de estados
######################################################################################

######################################################################################

# Show state value on the console
print(state)
