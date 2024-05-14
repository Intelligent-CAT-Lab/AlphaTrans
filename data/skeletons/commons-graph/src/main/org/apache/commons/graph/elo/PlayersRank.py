# Imports Begin
import typing
from abc import ABC

# Imports End


class PlayersRank(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def updateRanking(self, player: typing.Any, ranking: float) -> None:
        pass

    def getRanking(self, player: typing.Any) -> float:
        pass

    # Class Methods End
