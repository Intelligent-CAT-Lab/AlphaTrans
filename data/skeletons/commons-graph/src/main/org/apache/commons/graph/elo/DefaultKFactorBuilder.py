from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.elo.PlayersRank import *
from src.main.org.apache.commons.graph.elo.KFactorBuilder import *
from src.main.org.apache.commons.graph.elo.GameResult import *
from src.main.org.apache.commons.graph.DirectedGraph import *
import typing
from typing import *
import io

# Imports End


class DefaultKFactorBuilder(KFactorBuilder):

    # Class Fields Begin
    __DEFAULT_POW_BASE: float = None
    __DEFAULT_DIVISOR: float = None
    __DEFAULT_K_FACTOR: int = None
    __tournamentGraph: DirectedGraph[typing.Any, GameResult] = None
    __playerRanking: PlayersRank[typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def withKFactor(self, kFactor: int) -> None:
        pass

    def withDefaultKFactor(self) -> None:
        pass

    def __init__(
        self,
        tournamentGraph: DirectedGraph[typing.Any, GameResult],
        playerRanking: PlayersRank[typing.Any],
    ) -> None:
        pass

    def __updateRanking(
        self, player: typing.Any, kFactor: float, sFactor: float, eFactor: float
    ) -> None:
        pass

    def __evaluateMatch(
        self,
        playerA: typing.Any,
        gameResult: GameResult,
        playerB: typing.Any,
        kFactor: int,
    ) -> bool:
        pass

    def __calculateQFactor(self, player: typing.Any) -> float:
        pass

    @staticmethod
    def __calculateEFactor(qA: float, qB: float) -> float:
        pass

    # Class Methods End
