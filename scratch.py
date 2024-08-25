

class SnakeGame:

    def getNewHead(self, direction):
        curHead = self.snake[-1]
        newHead = None
        if direction == "RIGHT":
            newHead = (curHead[0], (curHead[1] + 1) % self.boardSize)
        elif direction == "LEFT":
            newHead = (curHead[0], (curHead[1] - 1) % self.boardSize)
        elif direction == "UP":
            newHead = ((curHead[0] - 1) % self.boardSize, curHead[1])
        elif direction == "DOWN":
            newHead = ((curHead[0] + 1) % self.boardSize, curHead[1])

        return newHead

    def checkGameIsOver(self, newHead):
        for coord in self.snake:
            if coord == newHead:
                return True
        return False

    def __init__(self):
        self.boardSize = 7
        self.snake = [(0, 0), (0, 1), (0, 2), (0, 3)] # (6, 2)
        self.isGameOver = False
        self.move = 1

    def moveSnake(self, direction):
        newHead = self.getNewHead(direction)

        self.isGameOver = self.checkGameIsOver(newHead)
        if self.isGameOver:
            return

        if self.move % 5 == 0:
            self.snake.append(newHead)
        else:
            self.snake.pop(0)
            self.snake.append(newHead)

        self.move += 1


    def getGamestatus(self):
        return self.isGameOver



if __name__ == "__main__":
    game = SnakeGame()
    game.moveSnake("DOWN")
    game.moveSnake("LEFT")
    game.moveSnake("UP")
    print(game.snake, game.getGamestatus())



#
#
#
