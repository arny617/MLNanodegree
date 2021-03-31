### Passing Cars: Count how many times cars pass each other, West -> 1, East -> 0.
def countPassingCars(A):
    stack = []
    countEast = 0
    for item in A:
        if item==0:
            countEast += 1
        else:
            stack.append(countEast)
    return sum(stack)
