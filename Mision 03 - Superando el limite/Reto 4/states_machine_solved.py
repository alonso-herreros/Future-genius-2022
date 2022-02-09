# Possible states
HighHealth = 1
RegularHealth = 2
LowHealth = 3
Defeated = 4


def update_state(state, damageFlag):
    state += 0 if state == Defeated else (damageFlag or -int(state == LowHealth))
    return state

def get_state_as_string(userIn):
    # Get state and damage flag from user
    state, damageFlag = [int(i) for i in userIn.split(",")]
    if state not in range(1, 5):
        raise ValueError("State only can be 1, 2, 3 or 4")
    if damageFlag not in range(2):
        raise ValueError("State only can be 0 or 1")


if __name__ == "__main__":
    # Show state value on the console
    print(get_state_as_string(input()))
