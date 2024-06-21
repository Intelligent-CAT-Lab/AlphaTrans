from __future__ import annotations
from abc import ABC
import io
import typing
from typing import *


class PlayersRank(ABC):

    def updateRanking(self, player: typing.Any, ranking: float) -> None:

        # Your code here
        pass

    def getRanking(self, player: typing.Any) -> float:

        # Your code here
        pass
