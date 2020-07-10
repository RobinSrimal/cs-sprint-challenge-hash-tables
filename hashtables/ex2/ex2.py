#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    lookup = {}

    for ticket in tickets:

        lookup[ticket.source] = ticket.destination

    print(lookup)


    start = lookup["NONE"]

    route = [start]

    for _ in range(length - 1):

        route.append(lookup[route[-1]])


    return route
