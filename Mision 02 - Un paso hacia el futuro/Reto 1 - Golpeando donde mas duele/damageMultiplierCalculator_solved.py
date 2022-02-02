TYPES = [
    "Normal",
    "Fighting",
    "Flying",
    "Poison",
    "Ground",
    "Rock",
    "Bug",
    "Ghost",
    "Steel",
    "Fire",
    "Water",
    "Grass",
    "Electric",
    "Psychic",
    "Ice",
    "Dragon",
    "Dark",
    "Fairy"
]

TYPE_CHART = [
    [1, 2, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 2, 1, 1, .5, .5, 1, 1, 1, 1, 1, 1, 2, 1, 1, .5, 2],
    [1, .5, 1, 1, 0, 2, .5, 1, 1, 1, 1, .5, 2, 1, 2, 1, 1, 1],
    [1, .5, 1, .5, 2, 1, .5, 1, 1, 1, 1, .5, 1, 2, 1, 1, 1, .5],
    [1, 1, 1, .5, 1, .5, 1, 1, 1, 1, 2, 2, 0, 1, 2, 1, 1, 1],
    [.5, 2, .5, .5, 2, 1, 1, 1, 2, .5, 2, 2, 1, 1, 1, 1, 1, 1],
    [1, .5, 2, 1, .5, 2, 1, 1, 1, 2, 1, .5, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, .5, 1, 1, .5, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
    [.5, 2, .5, 0, 2, .5, .5, 1, .5, 2, 1, .5, 1, .5, .5, .5, 1, .5],
    [1, 1, 1, 1, 2, 2, .5, 1, .5, .5, 2, .5, 1, 1, .5, 1, 1, .5],
    [1, 1, 1, 1, 1, 1, 1, 1, .5, .5, .5, 2, 2, 1, .5, 1, 1, 1],
    [1, 1, 2, 2, .5, 1, 2, 1, 1, 2, .5, .5, .5, 1, 2, 1, 1, 1],
    [1, 1, .5, 1, 2, 1, 1, 1, .5, 1, 1, 1, .5, 1, 1, 1, 1, 1],
    [1, .5, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, .5, 1, 1, 2, 1],
    [1, 2, 1, 1, 1, 2, 1, 1, 2, 2, 1, 1, 1, 1, .5, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, .5, .5, .5, .5, 1, 2, 2, 1, 2],
    [1, 2, 1, 1, 1, 1, 2, .5, 1, 1, 1, 1, 1, 0, 1, 1, .5, 2],
    [1, .5, 1, 2, 1, 1, .5, 1, 2, 1, 1, 1, 1, 1, 1, 0, .5, 1]
]


def computeDamageMultiplier(attackType, targetType1, targetType2=None):
    mult = 1
    try:
        mult *= TYPE_CHART[TYPES.index(targetType1)][TYPES.index(attackType)]
        mult *= TYPE_CHART[TYPES.index(targetType2)][TYPES.index(attackType)]
    except (ValueError, TypeError): pass
    return mult




#"Introduce attack type, target pokemon type1 and target pokemon type2, separated by a comma, without spaces between:
#"Example1, Blastoise uses Hydro Pump against Charizard --> User Input: Water,Fire,Flying"
#"Example2, Pidgey uses Tornado against Rattata --> User Input: Flying,Normal"

if __name__ == "__main__":
    enteredTypes = input().split(",")

    print("x"+str(computeDamageMultiplier(*enteredTypes)))
