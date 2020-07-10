def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    solutions = []

    lookup = {}

    for integer in a:

        if integer < 0:

            lookup[0 - integer] = integer


    for integer in a:

        if integer > 0:

            try:

                if integer + lookup[integer] == 0:

                    solutions.append(integer)

            except:

                continue
    print(solutions)
    return solutions


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
