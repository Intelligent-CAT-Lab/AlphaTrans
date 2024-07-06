from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.elo.PlayersRank import *


class SimplePlayersRank(PlayersRank):

    __ranks: typing.Dict[str, float] = {}

    def toString(self) -> str:
        return str(self.__ranks)

    def updateRanking(self, player: str, ranking: float) -> None:
        self.__ranks[player] = ranking

    def getRanking(self, player: str) -> float:
        if player not in self.__ranks:
            return 0.0
        return self.__ranks[player]
