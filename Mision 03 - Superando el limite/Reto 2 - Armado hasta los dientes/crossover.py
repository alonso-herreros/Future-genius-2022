def crossover_function(parent1, parent2):
    # Check that both arrays have the same length
    if :
        raise ValueError("Parents_length")
        exit()
    # Check that both arrays are bit arrays
    for i in range(len(parent1)):
        if :
            raise ValueError("Must_be_binary")
            exit()

    # Perform crossover

    return child1, child2


# "\nIntroduce parent 1 y parent 2, de la forma: "
# "parent1[0],parent1[1],...,parent1[n];parent2[0],parent2[1],...,parent2[n]")
str1, str2 = input().split(";")
array_str1, array_str2 = str1.split(","), str2.split(",")

parent1, parent2 = [], []

for i in range(len(array_str1)):
    parent1.append(int(array_str1[i]))

for i in range(len(array_str2)):
    parent2.append(int(array_str2[i]))


child1, child2 = crossover_function(parent1, parent2)
string1 = ''.join([str(element) for element in child1])
string1 = ''.join(string1.split())
string2 = ''.join([str(element) for element in child2])
string2 = ''.join(string2.split())
print(str(string1)+";"+str(string2))
