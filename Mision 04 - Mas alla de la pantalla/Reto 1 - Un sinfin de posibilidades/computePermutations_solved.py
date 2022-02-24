def factorial(n):
    if n < 2: return n
    else: return n*factorial(n-1)


def get_solution_string(userIn):
    if int(userIn) < 0: return "numero_no_valido"
    return str(factorial(int(userIn)))


if __name__ == "__main__":
    str = get_solution_string(input())
    print(str)
    if "_" in str: exit()
