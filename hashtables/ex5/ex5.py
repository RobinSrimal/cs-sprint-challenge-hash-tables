# Your code here
from collections import defaultdict


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here


    lookup = defaultdict(lambda:[])


    for path in files:

        lookup[path.rsplit('/', 1)[-1]].append(path)

    result = []

    for query in queries:

        result = result + lookup[query]

    
    return result



if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
