def anagram(str1, str2):

    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()


    return set(str1) == set(str2)


# Запрос ввода от пользователя
string1 = input("Введите первую строку: ")
string2 = input("Введите вторую строку: ")

if anagram(string1, string2):
    print("Эти строки являются анаграммами.")
else:
    print("Эти строки не являются анаграммами.")

# примеры для ввода
# "listen" и "silent"
# "debit card" и "bad credit"
# "astronomer" и "moon starer"
# "eleven plus two" и "twelve plus one"
# "funeral" и "real fun"