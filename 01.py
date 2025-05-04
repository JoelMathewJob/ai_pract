env={'A': 'Dirty', 'B': 'Clean'}

class Agent:
    def __init__(self, location):
        self.location=location
        
class simple(Agent):
    def act(self, env):
        print('Simple Agent:\n ')
        for _ in range(2):
            print(f'Location: {self.location} , Status: {env[self.location]}')
            if env[self.location] == 'Dirty':
                env[self.location]= 'Clean'
                print(f'Action- Cleaned:  {self.location}')
            
            self.location = 'B' if self.location=='A' else 'A'
            print(f'Action- Move:  {self.location}')
        if env['A'] == env['B'] == 'Clean':
            print('SimpleAgent finished cleaning')

class model(Agent):
    def __init__(self, location):
        super().__init__(location)
        self.memory = {'A': None, 'B': None}
        
    def act(self,env):
        print("Model Agent:\n ")
        for _ in range(2):
            print(' Memory: ', self.memory)
            print(f'Location: {self.location} , Percieved: {env[self.location]}')
            self.memory[self.location] = env[self.location] 
            print(' Memory: ', self.memory)
            
            
            if env[self.location] == 'Dirty':
                env[self.location]= 'Clean'
                self.memory[self.location] = env[self.location] 
                print(f'Action- Cleaned:  {self.location}')
            
            self.location = 'B' if self.location=='A' else 'A'
            print(f'Action- Move:  {self.location}')
            
        if env['A'] == env['B'] == 'Clean':
            print('ModelAgent finished cleaning')
        
class goal(Agent):
    def act(self, env):
        print('Goal Agent: \n')
        goal={'A': 'Clean', 'B': 'Clean'}
        print('Goa state is: ', goal)
        for i in ['A', 'B']:
            print(f'Location: {i} , Status: {env[i]}')
            if env[i] == 'Dirty':
                env[i]= 'Clean'
                print(f'Action- Cleaned:  {i}')
            if goal != env:
                i = 'B' if i=='A' else 'A'
                print(f'Action- Move:  {i}')
                
        if goal == env:
            print('Goal state achieved')
            print('GoalAgent finished cleaning')
        
            
class utility(Agent):
    
    def __init__(self, location):
        super().__init__(location)
        self.utility_score = 0
        self.memory = {'A': None, 'B': None}
        
    def utility(self, action):
        self.score = 0
        if action == 'Clean':
            self.score = 10
        elif action == 'Move':
            self.score = -1
        return self.score
                
    def act(self, env):
        print('Utility Agent:\n ')
        print('Utility score: ', self.utility_score)
        for i in ['A', 'B']:
            print(f'Location : {i}, Percieved: {env[i]}')
            self.memory[i]= env[i]
            print(' Memory: ', self.memory)
            if env[i] == 'Dirty':
                env[i] = 'Clean'
                self.memory[i]= env[i]
                self.utility_score+= self.utility('Clean')
                print(f'Action- Cleaned:  {i} UtilityScore: {self.utility_score}')
                print(' Memory: ', self.memory)
            if self.memory != {'A': 'Clean', 'B': 'Clean'}:
                # self.utility_score+= self.utility('Move')
                next = 'A' if self.location=='B' else 'B'
                self.utility_score+= self.utility('Move')
                print(f'Action - Move:  {next} UtilityScore: {self.utility_score}')
        print('UtilityAgent finished cleaning')
            
                
            
            
                

        
simple('A').act(env)
model('A').act(env)
goal('B').act(env)
utility('A').act(env)