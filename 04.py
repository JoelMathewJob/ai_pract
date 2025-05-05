
import random

cities = ['A', 'B', 'C', 'D', 'E']

distances={
    ('A','B'):6, ('A','C'):10, ('A','D'):20, ('A','E'):10,
    ('B','C'):8, ('B','D'):5, ('B','E'):4,
    ('C','D'):13, ('C','E'):22,
    ('D','E'):7
}

for (a,b),d in list(distances.items()):
    distances[(b,a)]=d

def total_cost(path):
    cost = 0
    for i in range(len(path)-1):
        cost += distances[(path[i], path[i+1])]
    cost+=distances[(path[-1], path[0])]
    return cost

def get_neighbours(path):
    neighbours = []
    for i in range(len(path)):
        for j in range(i+1, len(path)):
            neighbour = path[:]
            neighbour[i],neighbour[j]=neighbour[j],neighbour[i]
            neighbours.append(neighbour)
            print(f'Neighbours: {neighbour}, Cost: {total_cost(neighbour)}')
            
    return neighbours

def hill(cities, iterations=20):
    current= cities[:]
    random.shuffle(current)
    current_cost = total_cost(current)
    print(f'Initial solution: {current}, Cost: {current_cost}')
    
    for it in range(1, iterations+1):
        neighbours =  get_neighbours(current)
        next_best = current
        next_best_cost = current_cost
        
        for neighbour in neighbours:
            cost = total_cost(neighbour)
            if cost <next_best_cost:
                next_best = neighbour
                next_best_cost = cost
                temp = it
                
        if next_best_cost<current_cost:
            print(f'Iteration{temp}: Improved to {next_best}, cost: {next_best_cost}')
            current = next_best
            current_cost = next_best_cost
            
        else:
            print(f'Iteration{it}: No better neighbour found (Local Maximum)')
            # break
    return current, current_cost

path, cost = hill(cities, iterations=15)
print(f'Final solution:{path} cost: {cost}')