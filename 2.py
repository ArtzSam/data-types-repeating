def text1(text):
    result = ""
    text2 = True

    for char in text:
        if text2 and char.isalpha():
            char = char.upper()
            text2 = False
        elif char in ".!?":
            text2 = True

        result += char

    return result

# input_text = input("Введите текст: ")
input_text = "на этом заканчиваю свое сочинение. поставьте пятерку, Мария Ивановна! я очень старалась!"
output_text = text1(input_text)
print(output_text)

# Ввод: на этом заканчиваю свое сочинение. поставьте пятерку, Мария Ивановна! я очень старалась!
# Вывод: На этом заканчиваю свое сочинение. Поставьте пятерку, Мария Ивановна! Я очень старалась!