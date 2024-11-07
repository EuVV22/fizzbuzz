# add your code here
for x in range(1, 101):
    # select number to print 
    number = x
    # check if is fizz
    number_is_fizz = number % 3 == 0
    # check if is buzz
    number_is_buzz = number % 5 == 0

    # Build string to print
    str_to_print = ""

    if number_is_fizz:
        str_to_print += "Fizz"
    
    if number_is_buzz:
        str_to_print += "Buzz"
    
    # if string is empty print number
    if str_to_print == "":
        str_to_print = str(number)

    print(str_to_print)
