data = tuple(open(r'D:\Technical\Python\MaxContinuousCount\random.csv', 'r'))
data = list(map(lambda x:x.rstrip(), data))
data = list(map(lambda x:x.split(','), data))
data = list(map(lambda x:list(map(lambda y:int(y), x)), data))

current_i = -1
current_j = -1
max_cost = 0
max_i = 0
max_j = 0

def traverse(i, j, initial_cost):
    global current_i, current_j, max_i, max_j, max_cost, data
    current_cost = data[i][j]
    total_cost = initial_cost+current_cost
    if i<19 and data[i+1][j] > current_cost:
        cost = traverse(i+1, j, total_cost)
        compare_and_decide(cost, i, j)
    if i>0 and data[i-1][j] > current_cost:
        cost = traverse(i-1, j, total_cost)
        compare_and_decide(cost, i, j)
    if j<19 and data[i][j+1] > current_cost:
        cost = traverse(i, j+1, total_cost)
        compare_and_decide(cost, i, j)
    if i>0 and data[i][j-1] > current_cost:
        cost = traverse(i, j-1, total_cost)
        compare_and_decide(cost, i, j)
    return total_cost


def compare_and_decide(cost, i, j):
    global max_cost, max_i, max_j, current_i, current_j
    if cost > max_cost:
        print(cost, 'end at:', i, j)
        max_cost, max_i, max_j = cost, current_i, current_j


for i in range(0,20):
    for j in range(0,20):
        current_i, current_j = i, j
        traverse(i, j, 0)
print('start at: ',max_cost, max_i, max_j)