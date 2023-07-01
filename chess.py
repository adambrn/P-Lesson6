from random import randint
def check_queens(queens):
    
    ''' Функция проверки правильности расстановки всех ферзей'''
    
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                return False
    return True

def generate_queens():
    
    ''' Функция генерации случайной расстановки ферзей'''
    
    queens = []
    while len(queens) < 8:
        new_queen = (randint(1, 8), randint(1, 8))
        if new_queen not in queens:
            queens.append(new_queen)

    return queens

def generate_successful_arrangements():
    
    ''' Функция поиска правильной расстановки ферзей'''
    
    successful_arrangements = []

    def generate_queens(queens, current_row):
        if current_row > 8: # Поставил 8 выходим
            successful_arrangements.append(queens)
            return

        for col in range(1, 9):# Перебор колонок
            new_queen = (current_row, col)

            if all(not (new_queen[0] == q[0] or new_queen[1] == q[1] or abs(new_queen[0] - q[0]) == abs(new_queen[1] - q[1])) for q in queens):
                generate_queens(queens + [new_queen], current_row + 1) # Если новый ферзь не бьет все предыдущие ставим его на следующи ряд

    generate_queens([], 1) # Ставим первый ферзь на первый ряд

    return successful_arrangements