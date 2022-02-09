from math import acos, sqrt, pi


def computeOrientation(enemy_x, enemy_y, player_x, player_y):
    # Compute the angle between enemy and player taking into account image axis
    x, y = (player_x-enemy_x), -(player_y-enemy_y)
    angle = acos(x / sqrt(x**2+y**2))*180/pi-90
    if y < 0: angle = -180 - angle
    return angle


def get_angle_as_string(userIn):
    angle = computeOrientation(*[int(i) for i in userIn.split(",")])
    return str(int(angle))


if __name__ == "__main__":
    print(get_angle_as_string(input()))