from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.elo.DefaultKFactorBuilder import *
from src.main.org.apache.commons.graph.elo.GameResult import *
from src.main.org.apache.commons.graph.elo.KFactorBuilder import *
from src.main.org.apache.commons.graph.elo.PlayersRank import *
from src.main.org.apache.commons.graph.elo.RankingSelector import *
from src.main.org.apache.commons.graph.utils.Assertions import *


class DefaultRankingSelector(RankingSelector):

    __tournamentGraph: DirectedGraph[typing.Any, GameResult] = None

    def wherePlayersAreRankedIn(
        self, playersRank: PlayersRank[typing.Any]
    ) -> KFactorBuilder[typing.Any]:

        playersRank = checkNotNull(
            playersRank, "ELO ranking can not be applied if players can not be ranked!"
        )

        return DefaultKFactorBuilder(self.__tournamentGraph, playersRank)

    def __init__(self, tournamentGraph: DirectedGraph[typing.Any, GameResult]) -> None:

        self.__tournamentGraph = tournamentGraph
