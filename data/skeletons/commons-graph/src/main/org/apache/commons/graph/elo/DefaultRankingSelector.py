from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.elo.RankingSelector import *
from src.main.org.apache.commons.graph.elo.PlayersRank import *
from src.main.org.apache.commons.graph.elo.KFactorBuilder import *
from src.main.org.apache.commons.graph.elo.GameResult import *
from src.main.org.apache.commons.graph.elo.DefaultKFactorBuilder import *
from src.main.org.apache.commons.graph.DirectedGraph import *
import typing
from typing import *
import io

# Imports End


class DefaultRankingSelector(RankingSelector):

    # Class Fields Begin
    __tournamentGraph: DirectedGraph[typing.Any, GameResult] = None
    # Class Fields End

    # Class Methods Begin
    def wherePlayersAreRankedIn(
        self, playersRank: PlayersRank[typing.Any]
    ) -> KFactorBuilder[typing.Any]:
        pass

    def __init__(self, tournamentGraph: DirectedGraph[typing.Any, GameResult]) -> None:
        pass

    # Class Methods End
