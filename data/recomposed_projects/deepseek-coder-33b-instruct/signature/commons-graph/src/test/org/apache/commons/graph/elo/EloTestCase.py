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

        tournament = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    HeadVertexConnector(lambda: "Zenio"),
                    HeadVertexConnector(lambda: "Marineking"),
                    HeadVertexConnector(lambda: "Hongun"),
                    HeadVertexConnector(lambda: "Nestea"),
                    HeadVertexConnector(lambda: "Tester"),
                    HeadVertexConnector(lambda: "Nada"),
                    HeadVertexConnector(lambda: "Rainbow"),
                    HeadVertexConnector(lambda: "Thewind"),
                    HeadVertexConnector(lambda: "Inka"),
                    HeadVertexConnector(lambda: "Maka"),
                    HeadVertexConnector(lambda: "Ensnare"),
                    HeadVertexConnector(lambda: "Kyrix"),
                    HeadVertexConnector(lambda: "Killer"),
                    HeadVertexConnector(lambda: "Slayersboxer"),
                    HeadVertexConnector(lambda: "Fruitdealer"),
                    HeadVertexConnector(lambda: "Genius"),
                    TailVertexConnector(lambda: GameResult.WIN, "Zenio", "Marineking"),
                    TailVertexConnector(
                        lambda: GameResult.WIN, "Fruitdealer", "Hongun"
                    ),
                    TailVertexConnector(lambda: GameResult.WIN, "Genius", "Nestea"),
                    TailVertexConnector(lambda: GameResult.WIN, "Tester", "Nada"),
                    TailVertexConnector(lambda: GameResult.WIN, "Thewind", "Rainbow"),
                    TailVertexConnector(lambda: GameResult.WIN, "Maka", "Inka"),
                    TailVertexConnector(lambda: GameResult.WIN, "Kyrix", "Ensnare"),
                    TailVertexConnector(
                        lambda: GameResult.WIN, "Slayersboxer", "Killer"
                    ),
                    TailVertexConnector(
                        lambda: GameResult.WIN, "Marineking", "Fruitdealer"
                    ),
                    TailVertexConnector(lambda: GameResult.WIN, "Tester", "Genius"),
                    TailVertexConnector(lambda: GameResult.WIN, "Thewind", "Maka"),
                    TailVertexConnector(
                        lambda: GameResult.WIN, "Kyrix", "Slayersboxer"
                    ),
                    TailVertexConnector(lambda: GameResult.WIN, "Marineking", "Tester"),
                    TailVertexConnector(lambda: GameResult.WIN, "Kyrix", "Thewind"),
                    TailVertexConnector(lambda: GameResult.WIN, "Kyrix", "Marineking"),
                ]
            )
        )

        playersRank = SimplePlayersRank()

        eloRate(tournament).wherePlayersAreRankedIn(playersRank).withKFactor(80)

        print(playersRank)
