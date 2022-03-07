import random
from model.liveBehavior.iLiveBehavior import ILiveBehavior
from contract.icell import ICell


class GameOfLive(ILiveBehavior):
    def live(self, cell: ICell, grid, x: int, y: int) -> None:
        nbAlive = self.__countAliveNeighbours(grid, x, y)
        if nbAlive < 2:
            cell.NextState = False
        elif nbAlive == 3:
            cell.NextState = True
        elif nbAlive > 3:
            cell.NextState = False

    def __countAliveNeighbours(self, grid, x: int, y: int) -> int:
        countAlive = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (grid.cellXY(x + i, y + j).State) and not ((i == 0) and (j == 0)):
                    countAlive += 1
        return countAlive
