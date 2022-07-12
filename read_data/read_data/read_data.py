import os

source_file = open(input("Please enter the file name: "), 'r', encoding = 'ISO-8859-1')

if os.stat(str(source_file.name)).st_size == 0:
    print("The file is empty!")
    exit()


year_input = int(input("Please enter the oldest collection year you want in the results: "))
size_input = int(input("Please enter the smallest sample size you want in the results: "))
lines = []

class processFile:
    def __init__(self, data):
        state, city, name, year, food, something1, something2, sample, ppm = data.split('\t')
        self.state = state
        self.city = city
        self.name = name
        self.year = year
        self.food = food
        self.something1 = something1
        self.something2 = something2
        self.sample = sample
        self.ppm = ppm

for line in source_file:
    s = processFile(line)
    if int(s.year[:4]) >= year_input and int(s.sample) >= size_input:
        lines.append(s)


if len(lines) == 0:
    print("There were no records with the given parameters.")
else:
    for item in lines:
        print(f"""
State name: {item.state}
Date: {item.year}
Food: {item.food}
Sample size: {item.sample}
Pb(ppm): {item.ppm.split(' ')[0]}
        """)