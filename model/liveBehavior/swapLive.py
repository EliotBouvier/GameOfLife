from model.liveBehavior.iLiveBehavior import ILiveBehavior
from contract.icell import ICell


class SwapLive(ILiveBehavior):
    def live(self, cell: ICell, grid, x: int, y: int) -> None:
        cell.NextState = not cell.State
