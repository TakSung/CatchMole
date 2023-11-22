

class ScoreManager:
    def __init__(self, init_score:int=0):
        self.set(init_score)

    def set(self, score:int=0)->int:
        self.score = score
        return self.get()

    def get(self):
        return self.score
    
    def add(self, value:int=1):
        return self.set(self.get()+value)