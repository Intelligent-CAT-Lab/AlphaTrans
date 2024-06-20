import pytest

from src.main.org.apache.commons.graph.elo.PlayersRank import *
from typing import *


class SimplePlayersRank(PlayersRank):

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
