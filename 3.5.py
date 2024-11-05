def get_multiplied_digits(number):
    number = int(number)
    first = []
    str_number = str(number)
    n = 0
    f = first.append(str_number[0])
    f = int(first[0])
    print(f)
    if len(str_number) > 1:
        if str_number[1:] != '0':
            return (f * get_multiplied_digits(int(str_number[1:])))
        else:
            return f
    else:
        return f


print(get_multiplied_digits(40203))
print(get_multiplied_digits(40))
print(get_multiplied_digits(1))
