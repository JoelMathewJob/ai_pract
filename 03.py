import heapq

graph={
    'A':[('B',1),('C',4)],
    'B':[('A',1),('C',2),('D',5)],
    'C':[('A',4),('B',2),('D',1)],
    'D':[('B',5),('C',1)]
    
}

heuristic ={
    'A':7,
    'B':6,
    'C':2,
    'D':0

}

def a_star(graph, start, goal):
    heap = [[heuristic[start],0, start, [start]]]
    visited = set()
    
    while heap:
        f, g, current, path = heapq.heappop(heap)
        
        if current == goal:
            return path
        
        if current not in visited:
            visited.add(current)
            for neighbor,cost in graph[current]:
                g_new = g + cost
                f_new = g_new + heuristic[neighbor]
                heapq.heappush(heap,(f_new, g_new, neighbor, path+[neighbor]))
                print(f'Heap: {heap}')
                
    return None

path = a_star(graph, 'A', 'D')
if path: print(f'Path found: {'->'.join(path)}')
else: print('Not found')