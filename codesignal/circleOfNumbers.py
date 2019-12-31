def circleOfNumbers(n, firstNumber):
    if firstNumber + (n//2) > n:
        return firstNumber - (n//2)
    elif firstNumber + (n//2) == n:
        return 0
    return firstNumber + (n//2)
