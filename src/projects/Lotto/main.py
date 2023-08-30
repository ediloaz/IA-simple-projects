from collections import Counter
import numpy as np
import os

data_folder = "src/projects/Lotto/data"
years = list(range(2022, 2024)) # 2013 - 2023, but we only get from 2018 due to recents
top_numbers_to_display = 15


print_numbers_numbers_by_year = True
def NumbersByYear():
    all_years_numbers = Counter()
    for year in years:
        lotto_numbers = Counter()
        revancha_numbers = Counter()
        all_numbers = Counter()

        file_path = os.path.join(data_folder, f"{year}.txt")

        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                lines = f.readlines()
                for line in lines:
                    fields = line.strip().split(";")
                    game_type = fields[1]
                    numbers = fields[2].split(",")

                    all_numbers.update(numbers)
                    all_years_numbers.update(numbers)

                    if game_type == "Lotto":
                        lotto_numbers.update(numbers)
                    elif game_type == "Revancha":
                        revancha_numbers.update(numbers)

        # print(f"Year: {year}")
        
        # if lotto_numbers:
        #     print(f"Most common Lotto numbers: {', '.join([f'{num} ({count})' for num, count in lotto_numbers.most_common(top_numbers_to_display)])}")

        
        # if revancha_numbers:
        #     print(f"Most common Revancha numbers: {', '.join([f'{num} ({count})' for num, count in revancha_numbers.most_common(top_numbers_to_display)])}")
        if all_numbers:
            if (print_numbers_numbers_by_year): print(f"Year {year}: {';'.join([f'{num}({count})' for num, count in all_numbers.most_common(top_numbers_to_display)])}")
            
        # print("-" * 30)
    if (print_numbers_numbers_by_year): print(f"De todos los años: {';'.join([f'{num}({count})' for num, count in all_years_numbers.most_common(top_numbers_to_display)])}")
    return all_years_numbers
        

historical_numbers_counter = NumbersByYear()


# Calcular estadísticas básicas utilizando los valores del contador
mean = np.mean(list(map(int, historical_numbers_counter.keys())))
std_dev = np.std(list(map(int, historical_numbers_counter.keys())))
median = np.median(list(map(int, historical_numbers_counter.keys())))
mode = historical_numbers_counter.most_common(1)[0][0]
print()
print("Estadísticas básicas:")
print(f"Promedio: {mean:.2f}")
print(f"Desviación estándar: {std_dev:.2f}")
print(f"Mediana: {median}")
print(f"Moda: {mode}")