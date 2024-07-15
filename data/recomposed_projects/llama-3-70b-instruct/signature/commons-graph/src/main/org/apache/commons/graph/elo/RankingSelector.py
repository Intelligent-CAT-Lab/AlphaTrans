from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.elo.KFactorBuilder import *
from src.main.org.apache.commons.graph.elo.PlayersRank import *


class RankingSelector(ABC):

    def wherePlayersAreRankedIn(
        self, playersRank: PlayersRank[typing.Any]
    ) -> KFactorBuilder[typing.Any]:
        return KFactorBuilder(playersRank)
