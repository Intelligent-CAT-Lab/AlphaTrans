from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.elo.PlayersRank import *
import typing
from typing import *
import io

# Imports End


class SimplePlayersRank(PlayersRank):

    # Class Fields Begin
    __ranks: typing.Dict[str, float] = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def updateRanking(self, player: str, ranking: float) -> None:
        pass

    def getRanking(self, player: str) -> float:
        pass

    # Class Methods End
