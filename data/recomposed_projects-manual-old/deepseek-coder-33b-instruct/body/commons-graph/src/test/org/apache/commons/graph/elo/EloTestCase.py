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
            AbstractGraphConnection().connect0(
                lambda: [
                    self.addVertex(vertex)
                    for vertex in [
                        "Zenio",
                        "Marineking",
                        "Hongun",
                        "Nestea",
                        "Tester",
                        "Nada",
                        "Rainbow",
                        "Thewind",
                        "Inka",
                        "Maka",
                        "Ensnare",
                        "Kyrix",
                        "Killer",
                        "Slayersboxer",
                        "Fruitdealer",
                        "Genius",
                    ]
                ]
                + [
                    self.addEdge(GameResult.WIN).from_(vertex_from).to(vertex_to)
                    for vertex_from, vertex_to in [
                        ("Zenio", "Marineking"),
                        ("Fruitdealer", "Hongun"),
                        ("Genius", "Nestea"),
                        ("Tester", "Nada"),
                        ("Thewind", "Rainbow"),
                        ("Maka", "Inka"),
                        ("Kyrix", "Ensnare"),
                        ("Slayersboxer", "Killer"),
                        ("Marineking", "Fruitdealer"),
                        ("Tester", "Genius"),
                        ("Thewind", "Maka"),
                        ("Kyrix", "Slayersboxer"),
                        ("Tester", "Marineking"),
                        ("Kyrix", "Thewind"),
                        ("Kyrix", "Marineking"),
                    ]
                ]
            )
        )

        playersRank = SimplePlayersRank()

        eloRate(tournament).wherePlayersAreRankedIn(playersRank).withKFactor(80)

        print(playersRank)
