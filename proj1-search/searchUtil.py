class SearchNode:
    
    def __init__(self, state, previous, move):
        self.state = state
        self.previous = previous
        self.move = move

    def getPrevious(self):
        return self.previous

    def getMove(self):
        return self.move

    def getState(self):
        return self.state
    


