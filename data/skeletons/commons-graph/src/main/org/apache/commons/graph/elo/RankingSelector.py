from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.elo.PlayersRank import *
from src.main.org.apache.commons.graph.elo.KFactorBuilder import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class RankingSelector(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def wherePlayersAreRankedIn(
        self, playersRank: PlayersRank[typing.Any]
    ) -> KFactorBuilder[typing.Any]:
        pass

    # Class Methods End
