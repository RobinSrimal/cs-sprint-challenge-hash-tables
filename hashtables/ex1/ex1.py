def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    
    lookup = {}

    for i in range(length):

        if weights[i] in lookup:
            
            if lookup[weights[i]] > i:
                
                return [lookup[weights[i]], i]
            
            else:
                
                return [i, lookup[weights[i]]]

        else:
            
            lookup[limit - weights[i]] = i

    return None



    




    
