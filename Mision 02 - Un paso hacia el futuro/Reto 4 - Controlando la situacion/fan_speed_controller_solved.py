def proportionalControllerStep(currentSpeed):
    return int(referenceSpeed_rps - currentSpeed + K*equilibrium)


equilibrium = 12
referenceSpeed_rps = 60
K = 1

if __name__ == "__main__":
    cur = input()
    currentSpeed_rps = int(cur)
    voltage = proportionalControllerStep(currentSpeed_rps)
    print(str(voltage) + 'V')
