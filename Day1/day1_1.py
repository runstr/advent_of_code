import Tools
import os
day = os.path.dirname(__file__)[-1:]
input_filename = __file__[:-9]+"input.txt"
test_input1_filename = __file__[:-9]+"test_input.txt"


def execution():
    input_full = list(map(int, Tools.read_input_as_line(input_filename)))
    bigger=0
    prev = 1000000000
    for i in input_full:
        if i > prev:
            bigger += 1
        prev = i
    print("Answer to day {} task one is: {}".format(day, bigger))
