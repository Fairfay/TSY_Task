import numpy as np

# Создание случайного массива
random_array = np.random.randint(1, 100, size=(5, 5))

# Вывод созданного массива
print("Случайный массив:")
print(random_array)

# Сортировка по возрастанию
sorted_array_asc = np.sort(random_array, axis=None)

# Вывод отсортированного массива по возрастанию
print("\nОтсортированный массив по возрастанию:")
print(sorted_array_asc)

# Сортировка по убыванию
sorted_array_desc = np.sort(random_array, axis=None)[::-1]

# Вывод отсортированного массива по убыванию
print("\nОтсортированный массив по убыванию:")
print(sorted_array_desc)

# Проверка, что созданный массив не изменился
print("\nПроверка, что исходный массив не изменился:")
print(random_array)
