for i in range(1, 101):
    string = ""
    if i % 3 == 0 or i % 5 == 0:    # Two checks here - could be avoided?
        if i % 3 == 0:
            string += "Fizz"
        if i % 5 == 0:
            string += "Buzz"
    else:
        string = i

    print(string)
