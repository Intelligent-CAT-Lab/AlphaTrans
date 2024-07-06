from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.elo.GameResult import *
from src.main.org.apache.commons.graph.elo.KFactorBuilder import *
from src.main.org.apache.commons.graph.elo.PlayersRank import *


class DefaultKFactorBuilder(KFactorBuilder):

    __playerRanking: PlayersRank[typing.Any] = None

    __tournamentGraph: DirectedGraph[typing.Any, GameResult] = None

    __DEFAULT_K_FACTOR: int = 32
    __DEFAULT_DIVISOR: float = 400
    __DEFAULT_POW_BASE: float = 10.0

    def withKFactor(self, kFactor: int) -> None:
        for player in self.__tournamentGraph.getVertices0():
            for opponent in self.__tournamentGraph.getOutbound(player):
                gameResult = self.__tournamentGraph.getEdge(player, opponent)
                self.__evaluateMatch(player, gameResult, opponent, kFactor)

    def withDefaultKFactor(self) -> None:
        self.withKFactor(self.__DEFAULT_K_FACTOR)

    def __init__(
        self,
        tournamentGraph: DirectedGraph[typing.Any, GameResult],
        playerRanking: PlayersRank[typing.Any],
    ) -> None:
        self.__tournamentGraph = tournamentGraph
        self.__playerRanking = playerRanking

    def __updateRanking(
        self, player: typing.Any, kFactor: float, sFactor: float, eFactor: float
    ) -> None:
        newRanking = self.__playerRanking.getRanking(player) + (
            kFactor * (sFactor - eFactor)
        )
        self.__playerRanking.updateRanking(player, newRanking)

    def __evaluateMatch(
        self,
        playerA: typing.Any,
        gameResult: GameResult,
        playerB: typing.Any,
        kFactor: int,
    ) -> bool:
        qA = self.__calculateQFactor(playerA)
        qB = self.__calculateQFactor(playerB)

        eA = self.__calculateEFactor(qA, qB)
        eB = self.__calculateEFactor(qB, qA)

        sA: float
        sB: float
        if gameResult == GameResult.WIN:
            sA = 1
            sB = 0
        elif gameResult == GameResult.DRAW:
            sA = 0.5
            sB = 0.5
        else:
            raise ValueError("Input GameResult not accepted")

        self.__updateRanking(playerA, kFactor, sA, eA)
        self.__updateRanking(playerB, kFactor, sB, eB)
        return True

    def __calculateQFactor(self, player: typing.Any) -> float:
        ranking = self.__playerRanking.getRanking(player)
        return pow(self.__DEFAULT_POW_BASE, ranking / self.__DEFAULT_DIVISOR)

    @staticmethod
    def __calculateEFactor(qA: float, qB: float) -> float:
        return qA / (qA + qB)
