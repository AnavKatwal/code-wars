# I was just trying to learn git hub.
# So, sorry if you were looking for some thing.
# But this piece of code is just a training code from code wars.

def in_array(array1, array2):
    in_list = []
    for item in array1:
        for i in array2:
            if item in i and item not in in_list:
                in_list.append(item)

    return(in_list)


print(in_array(["hi", "bye", "sar"], ["hibrew", "test", "bye bye", "sarcasm", "sars"]))

# the same code just pretending to have made changes