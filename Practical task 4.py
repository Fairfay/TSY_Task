def print_sticks(sticks):
    # Функция для вывода текущего состояния палочек
    print("Осталось палочек:", sticks)
    print("| " * sticks)


def main():
    sticks = 21
    print("Добро пожаловать в игру '21'!")
    print("Правила просты: каждый ход вы можете взять от 1 до 3 палочек.")
    print("Цель игры - не взять последнюю палочку.")

    while sticks > 0:
        print_sticks(sticks)
        while True:
            try:
                # Запрос ввода количества палочек у пользователя
                player_choice = int(input("Сколько палочек вы хотите взять? "
                                          "(1-3): "))
                if player_choice < 1 or player_choice > 3:
                    print("Некорректное количество палочек. Пожалуйста, "
                          "выберите от 1 до 3.")
                    continue
                break
            # Обработка ошибки, если пользователь ввел не число
            except ValueError:
                print("Ошибка: введите число от 1 до 3.")
        sticks -= player_choice
        if sticks <= 0:
            print("Вы взяли последнюю палочку. Вы проиграли!")
            break
        print_sticks(sticks)
        computer_choice = 4 - player_choice
        print("Компьютер взял", computer_choice, "палочек.")
        sticks -= computer_choice
        if sticks <= 0:
            print("Компьютер взял последнюю палочку. Вы победили!")
            break


if __name__ == "__main__":
    main()
