# Imports Begin
from src.main.org.apache.commons.graph.elo.PlayersRank import *
import unittest
import typing
from typing import *
# Imports End

class SimplePlayersRank(PlayersRank):

    # Class Methods Begin
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__ranks = {}

    
    def getRanking(self, player: str) -> float:
        if player not in self.__ranks:
            return 0.0
        return self.__ranks[player]
    

    def updateRanking(self, player: str, ranking: float) -> None:
        self.__ranks[player] = ranking

    
    def toString(self) -> str:
        return str(self.__ranks)

    # Class Methods End


