def enter_numbers():
    user_input = input("Enter digits using space as separator: \n")

    result = user_input.split()
    return [int(x) for x in result]

def make_sum(input):
    sum_of_input = sum(input)
    return print("Result is " + str(sum_of_input))


f = enter_numbers()
make_sum(f)