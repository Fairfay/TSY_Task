numbers = []

try:
    with open('input.txt', 'r') as file:
        for line in file:
            # Разделение строки на числа и их преобразование в целые числа
            nums = [int(num) for num in line.strip().split() if num.isdigit()]
            numbers.extend(nums)
# Обработка ошибок
except FileNotFoundError:
    print("Файл input.txt не найден.")
except Exception as e:
    print(f"Ошибка при чтении файла input.txt: {e}")

# Проверка, что список чисел не пустой
if not numbers:
    print("Файл input.txt не содержит чисел.")
else:
    # Вычисление суммы чисел
    total_sum = sum(numbers)

    # Запись результата в файл output.txt
    try:
        with open('output.txt', 'w') as file:
            file.write(str(total_sum))
    except Exception as e:
        print(f"Ошибка при записи в файл output.txt: {e}")
