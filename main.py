from CompoundInterest import interest as interest


def _inputchecker(message, boolean):
    while (boolean):
        try:
            value = input(message)
            boolean = False
        except NameError:
            print "Please provide valid input"
        if (type(value) != float and type(value) != int):
            print "Please provide a float input!"
            boolean = True
    boolean = True
    return (value, boolean)


if (__name__ == "__main__"):
    loopcond = True
    while (loopcond):
        (start_val, loopcond) = _inputchecker(
            "Provide a start value: ", loopcond)
        (years, loopcond) = _inputchecker(
            "Provide total number of years to save: ", loopcond)

        multiplier = input("[OPTIONAL] Provide a multiplier: ")

        promo = input("[OPTIONAL] Provide an average expected promotion: ")

        if (multiplier and promo):
            print(interest(start_val, years, multiplier, promo))
        elif (multiplier):
            print(interest(start_val, years, multiplier))
        elif (promo):
            print(interest(start_val, years, promo))
        else:
            print(interest(start_val, years))

        run_again = (input("Run again? [y/n]"))
        loopcond = (run_again.lower().startswith("y"))
