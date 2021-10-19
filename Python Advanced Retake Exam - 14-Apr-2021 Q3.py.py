def flights(*values):               # accept variable length arguments(varargs)
    destination_dict = {}           # create a dictionary of flight-to-passengers
    for i in range(len(values)):    # iterate over the arguments
        if values[i] == "Finish":
            break

        if i % 2 == 0:              # each even arg. is the key, each odd is the value
            flight = values[i]      # we have the key (it is the "flight")
            passengers = destination_dict.get(flight) # check if there's a value in the dict. already for the key
            if passengers is None:  # if "None", i.e. there's no value,
                destination_dict[flight] = 0 # add the key to the dict. and put a value of Zero to it
        else: # odd element, i.e. passengers
            flight = values[i-1] # get the previous argument (i-1), it is the key, i.e. the flight for "this" value, i.e. for this passengers
            passengers = destination_dict.get(flight) # get the passengers for the key, it will be zero or the current passengers(e.g. "Vienna")
            destination_dict[flight] = passengers + int(values[i]) # updage the total number of passengers for the key(the flight)

    return destination_dict # return the ready dictionary


print(flights("Vienna", 256, "Vienna", 26, "Morocco", 98, "Paris", 115, "Finish", "Paris", 15))