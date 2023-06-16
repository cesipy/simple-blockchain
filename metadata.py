class Metadata: 
    def __init__(self, difficulty, version, reward):
        self.difficulty = difficulty
        self.version = version
        self.reward = reward

    def get_params(self):
        return self.difficulty, self.version, self.reward
    
    