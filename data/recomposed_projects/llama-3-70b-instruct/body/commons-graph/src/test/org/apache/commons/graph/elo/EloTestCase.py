from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.elo.KFactorBuilder import *
from src.main.org.apache.commons.graph.elo.PlayersRank import *
from src.main.org.apache.commons.graph.elo.RankingSelector import *
from src.test.org.apache.commons.graph.elo.SimplePlayersRank import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.main.org.apache.commons.graph.elo.GameResult import *


class EloTestCase(unittest.TestCase):

    def testPerformElo(self) -> None:
        tournament: DirectedGraph[str, GameResult] = (
            CommonsGraph.newDirectedMutableGraph(
                AbstractGraphConnection[str, GameResult]().connect0()
            )
        )

        playersRank: PlayersRank[str] = SimplePlayersRank()

        CommonsGraph.eloRate(tournament).wherePlayersAreRankedIn(
            playersRank
        ).withKFactor(80)

        print(playersRank)
