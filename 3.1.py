calls = 0
mas = []
new_li = []

def count_calls():
        global calls
        calls += 1
        return calls


def string_info(str_):
    global mas
    mas = []
    count_calls()
    str_ = str(str_)
    len_ = len(str_)
    mas.append(len_)
    h_reg = str_.upper()
    mas.append(h_reg)
    l_reg = str_.lower()
    mas.append(l_reg)
    return mas


def is_contains(string, list_to_search):
    count_calls()
    global new_li
    string = string.lower()
    new_li = [x.lower() for x in list_to_search]
    return (string in new_li)


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(count_calls() - 1)
