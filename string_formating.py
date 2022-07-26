def print_formatted(number):
    # number = 17
    width = len("{0:b}".format(number))
    for i in range(1,number+1):
        print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i,w =width))
    # your code goes here
    # width = (int(width[2:]))
# for i in range(1,number+1):
#     print(str(i).rjust(width," "),oct(i)[2:].rjust(width," "),hex(i)[2:].upper().rjust(width," "),bin(i)[2:].rjust(width," "))
