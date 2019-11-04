def sum_or_concatenate():
    first_value = input("Input first value: ")
    second_value = input("Input second value: ")

    try:
        print("The sum is: {}".format(float(first_value) + float(second_value)))
    except ValueError:
        print("The concatenated result is: {}.".format(first_value + second_value))
    finally:
        print("That's it! Good luck :-)")


print(sum_or_concatenate())
