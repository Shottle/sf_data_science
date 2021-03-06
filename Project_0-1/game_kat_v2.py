"""Игра "Угадай число"
Компьютер сам загадывает и сам угадывает число
менее чем за 20 попыток"""

import numpy as np
from numpy import random # Импортируем библиотеку для генерации случайных чисел.

def game_my_var(number: int = 1) -> int:
    """Вариант игры "Угадай число" за минимальное количество попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0  #Счетчик попыток
    find_number = 0 #Переменная для поиска числа из списка random_array
    n_min = 1
    n_max = 101

    while number != find_number:
        count +=1
        find_number = (n_max + n_min)// 2
        
        if find_number < number:
            n_min = find_number
        elif find_number > number:
            n_max = find_number
        else:
            break
    
    return count


def score_game(game_my_var) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает 
    предложенный алгоритм

    Args:
        game_my_var ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # Загадали список чисел

    for number in random_array:
        count_ls.append(game_my_var(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(game_my_var)
