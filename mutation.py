
from operator import index


string = "abracadabra"


# type 1 
# l = list(string)
# l[5] = 'k'
# string = ''.join(l)
# print(string)


# type 2
# string = string[:5] + "k" + string[6:]
# print(string) 

# type 3
def mutate_string(string, position, character):
    l = list(string)
    l.pop(position)
    l.insert(position,character)
    string = "".join(l)
    return string
