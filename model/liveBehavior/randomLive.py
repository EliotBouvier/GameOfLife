import random
from model.liveBehavior.iLiveBehavior import ILiveBehavior
from contract.icell import ICell


class RandomLive(ILiveBehavior):
    def live(self, cell: ICell, grid, x: int, y: int) -> None:
        if random.randint(0, 1) == 1:
            cell.NextState = True
        else:
            cell.NextState = False
