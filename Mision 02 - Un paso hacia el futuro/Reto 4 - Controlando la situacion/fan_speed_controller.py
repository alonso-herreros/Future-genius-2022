def proportionalControllerStep(equilibrium, referenceSpeed, currentSpeed, P):
    controlAction = 170
    return controlAction


equilibrium = 12
cur = input()
referenceSpeed_rps = 60
currentSpeed_rps = int(cur)
K = 1
voltage = proportionalControllerStep(equilibrium, referenceSpeed_rps, currentSpeed_rps, K)
print(f'{voltage}V')
