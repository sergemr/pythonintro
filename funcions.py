def printValues(value):
    text_to_print = value
    print(text_to_print)


def is_greater_than(param1, param2):
    if param1 > param2:
        print("yes")
    elif param1 == param2:
        print("they are equal")
    else:
        print("no")


var_input1 = int(input("Enter First value: "))
var_input2 = int(input("Enter Second value: "))
printValues("556")
is_greater_than(var_input1, var_input2)
is_greater_than(5, 10)
