import numpy as np

def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count+=1
        predict = np.random.randint(1, 101) # предполагаемое число
        if number == predict: 
            return(count) # выход из цикла, если угадали
 
       
def score_game(game_core_v1):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v1(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# запускаем
score_game(game_core_v1)

def game_core_v2(number):
    '''Используется метод бинарного поиска. 
       С учётом неизменности функции игры, вбил параметры в код функции
       Вариант "не курильщика" - параметризовать границы для угадывания
       и добавить исключение, когда загаданное число вне границ'''
    count = 0
    maximum = 100
    minimum = 0
    medium = (maximum + minimum) // 2
    while number != medium and minimum <= maximum:
        count+=1
        if number > medium: 
            minimum = medium + 1
        else:
            maximum = medium - 1
        medium = (maximum + minimum) // 2
    return(count)

# Проверяем
score_game(game_core_v2)