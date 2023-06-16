class Metadata: 
    def __init__(self, difficulty, version, reward):
        self.difficulty = difficulty
        self.version = version
        self.reward = reward
        self.counter_adjusting_difficulity = 0


    def increase_difficulty(self):
        self.difficulty+= 1
        self.counter_adjusting_difficulity = 0

    def get_params(self):
        return self.difficulty, self.version, self.reward
    
