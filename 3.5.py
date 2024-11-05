def get_multiplied_digits(number):
    first = []
    str_number = str(number)

    f = first.append(str_number[0])
    f = int(first[0])
    if len(str_number) > 1:
        return (f * get_multiplied_digits(int(str_number[1:])))
    else:
        return (f)

print(get_multiplied_digits(40203))
print(get_multiplied_digits(4))