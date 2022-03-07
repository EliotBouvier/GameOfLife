import random
from model.liveBehavior.iLiveBehavior import ILiveBehavior
from contract.icell import ICell


class Cell(ICell):
    __state: bool
    __liveBehavior: ILiveBehavior
    __nextState: bool

    def __init__(self, state: bool, liveBehavior: ILiveBehavior):
        self.__liveBehavior = liveBehavior
        self.__nextState = True
        self.__state = state
        # if random.randint(0, 2) == 0:
        #     self.__state = True
        # else:
        #     self.__state = False

    @property
    def State(self) -> bool:
        return self.__state

    @State.setter
    def State(self, state: bool) -> None:
        self.__state = state

    @property
    def NextState(self) -> bool:
        return self.__nextState

    @NextState.setter
    def NextState(self, nextState: bool) -> None:
        self.__nextState = nextState

    def takeDecision(self, grid, x: int, y: int) -> None:
        self.__liveBehavior.live(self, grid, x, y)

    def doDecision(self) -> None:
        self.State = self.NextState
