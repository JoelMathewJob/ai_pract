from collections import deque

graph = {
    'A':['B','D'],
    'B':['A','C','D'],
    'C':['B','D', 'F'],
    'D':['A','B','C','E'],
    'E':['D','F'],
    'F':['C','E']
}

def bfs(graph, start, goal):
    queue = deque([[start]])
    visited= set()
    
    while queue:
        path = queue.popleft()
        current = path[-1]
        
        if current == goal:
            return path
        
        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                print(f'queue: {queue}')
                
    return None

path = bfs(graph, 'A', 'F')

if path: print(f'path found: {' -> '.join(path)}')
else: print('path not found')
            