# Function that uses the model to infere age from player score
def infereAge(score):
    slope = 214.81
    intercept = 179.67
    age = round( (score-intercept)/slope )
    return age


if __name__ == "__main__":
    score = int(input())
    print(infereAge(score))
