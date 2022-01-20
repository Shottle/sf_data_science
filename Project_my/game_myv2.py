"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
минимальное число попыток"""

import numpy as np  
from numpy import random # Импортируем библиотеку для генерации случайных чисел.

def game_my_var(number: int = 1) -> int:
    """Вариант игры "Угадай число" за минимальное количество попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # Счетчик попыток
    n_min = 1
    n_max = 100
    predict = np.random.randint(1, 101) # Рандомное число

    while predict != number:
        count += 1
        number = (n_max + n_min)// 2

        if number < predict:
            n_min = number
        elif number > predict:
            n_max = number
        else:
            break
    
    return count

def score_game(game_my_var) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        game_my_var ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_my_var(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(game_my_var)
