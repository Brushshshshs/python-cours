def single_root_words(root_word, *other_words):
    count = 0
    same_words = []
    s = []
    t = []
    root_word_2 = root_word.lower()
    other_words_2 = []


    for i in other_words:
        t = i.lower()
        t = other_words_2.append(t)
        count += 1
        if root_word_2 in other_words_2[count - 1]:
            s = same_words.append(other_words_2[count - 1])
        if other_words_2[count - 1] in root_word_2:
            s = same_words.append(other_words[count - 1])


    return (same_words)

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)



# def test_func(*params):
#     print("Тип:", type(params))
#     print("Аргумент:", params)
#
# #
# # test_func(1, 2, 3, 4)
#
# def summator(txt, *values, type="sum"):
#     s = 0
#     for i in values:
#         s += i
#     return f'{txt}{s} {type}'
#
#
#
# print(summator("Сумма чисел: ", 2, 3, 4, type="summator"))


# def info(value, *types, names_author="Den", **values):
#     print("Тип:", type(values))
#     print("Аргумент:", values)
#     for key, value in values.items():
#         print(key, value)
#     print(types)
#
#
# info("Пример использования параметров всех типов", 2, 3, 4, names_author="Denis", name="Den", course="Python")


#def my_sum(n, *args, txt="Сумма чисел"):
 #   s = 0
  #  for i in range(len(args)):
   #     s += args[i] ** n
   # print(txt + ":", s)


#my_sum(1, 1, 2, 3, 4, 5)
#my_sum(2, 2, 3, 4, 5, txt="Сумма квадратов")