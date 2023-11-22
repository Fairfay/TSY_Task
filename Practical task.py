# 1. Создание переменной для отслеживания общей суммы продаж
total_sales = 0


# 2. Создание функции для вычисления общей суммы продаж 
def calculate_sales(prices):
    global total_sales
    for price in prices:
        total_sales += price
    return print(f'{total_sales}')


# 3. Создаём словарь с товарами
# Для каждого товара указано количество на складе и цена
product_stock = {
    'Товар A': [10, 1000],  # Количество: 10, Цена: 1000
    'Товар B': [20, 500],   # Количество: 20, Цена: 500
    'Товар C': [30, 200]    # Количество: 30, Цена: 200
}


# 4. Создание функции для проверки наличия товара
def check_stock(product):
    # Проверка наличия товара в словаре product_stock
    if product in product_stock.keys():
        # Если товар найден, проверяем количество на складе
        if product_stock[product][0] > 0:
            # Если товар в наличии, выводим информацию о товаре
            print(f'Товар в наличии: {product}, '
                  f'количество: {product_stock[product][0]}, '
                  f'цена: {product_stock[product][1]}')
        else:
            # Если товара нет на складе, выводим сообщение об отсутствии
            print(f'Товар отсутствует: {product}')
    else:
        # Если товара нет в словаре, выводим сообщение о его отсутствии
        print('Товар не найден')


# 5. Создание функции для вычисления выручки и обновления общих продаж
def calculate_revenue(product, quantity):
    global total_sales
    # Проверка наличия товара в словаре product_stock
    if product in product_stock.keys():
        # Проверка хватает ли товара для продажи в указанном количестве
        if product_stock[product][0] < quantity:
            # Если товара недостаточно, выводим сообщение
            print("Продажа не возможна: недостаточно товара")
        else:
            # Обновление количества товара и общей суммы продаж
            product_stock[product][0] -= quantity
            total_sales += quantity*product_stock[product][1]
            # Вывод информации
            print(f'Продано: {quantity} единиц товара, '
                  f'выручка: {quantity*product_stock[product][1]}')


# Создаем список цен товаров
product_prices = [1000, 500, 200]

# Вычисляем общую сумму продаж
calculate_sales(product_prices)

# Проверяем наличие товара
check_stock('Товар A')
check_stock('Товар D')  # Товара D нет в словаре

# Вычисляем выручку и обновляем общие продажи
calculate_revenue('Товар B', 3)
calculate_revenue('Товар C', 25)
