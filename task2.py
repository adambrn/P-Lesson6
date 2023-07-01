# *Выведите все успешные варианты расстановок

from chess import generate_successful_arrangements

successful_arrangements = generate_successful_arrangements()

for idx, arrangement in enumerate(successful_arrangements, start=1):
    print(f"Правильная расстановка {idx}: {arrangement}")