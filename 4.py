def num(algebry, geometry, trigonometry):

    algebry = set(algebry.split())
    geometry = set(geometry.split())
    trigonometry = set(trigonometry.split())

    num1 = algebry & geometry & trigonometry

    if num1:
        return ' '.join(sorted(num1))
    else:
        return 'Все три задачи никто не решил'

algebry1 = input("Фамилии учащихся, решивших задачу по алгебре: ")
geometry1 = input("Фамилии учащихся, решивших задачу по геометрии: ")
trigonom1 = input("Фамилии учащихся, решивших задачу по тригонометрии: ")

result = num(algebry1, geometry1, trigonom1)
print(result)

# Ввод:
# Иванов Петров Сидоров Михайлов
# Иванов Михайлов
# Сидоров Михайлов
# Вывод: Михайлов