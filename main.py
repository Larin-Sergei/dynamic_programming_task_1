def count_sequences(n):
    if n == 0:
        return 1

    if n == 1:
        return 2

    a = 1
    b = 2

    for i in range(2, n + 1):
        a, b = b, a + b

    return b


n = int(input("Введите длину последовательности n: "))

if n < 0:
    print("Ошибка: n должно быть неотрицательным числом.")
else:
    result = count_sequences(n)
    print(f"Количество допустимых последовательностей: {result}")
