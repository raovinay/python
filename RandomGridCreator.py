import random

csv_file = open(r'D:\Technical\Python\MaxContinuousCount\random.csv', 'w')
for i in range(0, 20):
    line = []
    for j in range(0, 20):
        line.append(random.randint(1, 600))
    line = list(map(lambda x:str(x), line))
    csv_file.write(','.join(line)+'\n')
