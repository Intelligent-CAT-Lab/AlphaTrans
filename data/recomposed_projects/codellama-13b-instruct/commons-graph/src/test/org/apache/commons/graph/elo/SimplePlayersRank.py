# Imports Begin
from src.main.org.apache.commons.graph.elo.PlayersRank import *
import unittest
import typing
from typing import *
# Imports End

class SimplePlayersRank(unittest.TestCase, PlayersRank<String>):

    # Class Fields Begin
    __ranks: typing.Dict[str, float] = "" # LLM could not translate field
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:

            return str(self.__ranks)

    def updateRanking(self, player: str, ranking: float) -> None:

            self.__ranks[player] = ranking

    def getRanking(self, player: str) -> float:

            if player not in self.__ranks:
                return 0.0
            return self.__ranks[player]

    # Class Methods End


