

class Blockchain():
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.blocks = []

    def add_block(self, block):
        self.blocks.append(block)

    def save_to_file(self, file_path):
        with open(file_path, 'w') as f:
            for block in self.blocks:
                f.write(str(block) + '\n')



