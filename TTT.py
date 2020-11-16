import random
 
class game:
    def __init__(self):
        self.table = [0] * 9
        self.currentPlayer = 1
        self.HAS_WON = 9
        self.HAS_LOST = -1
        self.HAS_ENDED = -3
        self.NO_MOVE = -2

    def validMove(self, index):
        return self.table[index] == 0
    
    def hasWon(self):
        c = 0
        rows = []
        rows.append(self.table[0:3])
        rows.append(self.table[3:6])
        rows.append(self.table[6:9])
        rows.append(self.table[0:9:3])
        rows.append(self.table[1:9:3])
        rows.append(self.table[2:9:3])
        rows.append(self.table[0:9:4])
        rows.append(self.table[2:8:2])
        for row in rows:
            if row[0] == row[1] == row[2] != 0:
                return row[0]
        return 0

    def getOpenSpaces(self):
        counter = 0
        openSpaces = []
        while counter < len(self.table):
            if self.validMove(counter): openSpaces.append(counter)
            counter = counter + 1
        return openSpaces

    def nextMove(self, previousMove):
        if previousMove != self.NO_MOVE:
            if not self.validMove(previousMove):
                print("Betrueger!")
                return "Error: Betrug."
            self.table[previousMove] = self.currentPlayer
        self.currentPlayer = -self.currentPlayer
        winner = self.hasWon()
        if winner != 0:
            if winner == self.currentPlayer: return self.HAS_WON
            else: return self.HAS_LOST
        openSpaces = self.getOpenSpaces()
        if openSpaces == []: return self.HAS_ENDED
        return openSpaces[random.randint(0, len(openSpaces) - 1)]
    
    def printState(self):
        print(self.table[0:3])
        print(self.table[3:6])
        print(self.table[6:9])
        
if __name__ == "__main__":
    gm = game()
    res = gm.NO_MOVE
    while res != gm.HAS_WON and res != gm.HAS_LOST and res != gm.HAS_ENDED:
        res = gm.nextMove(res)
        gm.printState()
        print(res)