def crossover_function(parent1, parent2):
    # Check that both arrays have the same length
    if len(parent1) != len(parent2):
        #raise ValueError("Parents_length")
        raise ValueError("Parents length must be equall")
        exit()
    # Check that both arrays are bit arrays
    for i in range(len(parent1)):
        if parent1[i] != 0 and parent1[i] != 1 or parent2[i] != 0 and parent2[i] != 1:
            #raise ValueError("Must_be_binary")
            raise ValueError("Parents must be binary value arrays")
            exit()

    # Perform crossover

    midpoint = len(parent1) // 2
    child1 = parent1[:midpoint] + parent2[midpoint:]
    child2 = parent2[:midpoint] + parent1[midpoint:]

    return child1, child2


def get_crossover_as_string(userIn):
    parent1, parent2 = [[int(j) for j in i.split(",")] for i in userIn.split(";")]

    child1, child2 = crossover_function(parent1, parent2)
    string1 = ''.join([str(element) for element in child1])
    string1 = ''.join(string1.split())
    string2 = ''.join([str(element) for element in child2])
    string2 = ''.join(string2.split())
    return str(string1)+";"+str(string2)


if __name__ == "__main__":

    # "\nIntroduce parent 1 y parent 2, de la forma: "
    # "parent1[0],parent1[1],...,parent1[n];parent2[0],parent2[1],...,parent2[n]")
    print(get_crossover_as_string(input()))
