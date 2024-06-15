# Imports Begin
from src.main.org.apache.commons.graph.elo.GameResult import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.elo.RankingSelector import *
from src.main.org.apache.commons.graph.elo.PlayersRank import *
from src.main.org.apache.commons.graph.elo.KFactorBuilder import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.CommonsGraph import *
import unittest
from SimplePlayersRank import SimplePlayersRank
# Imports End

class EloTestCase(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testPerformElo(self) -> None:
        tournament = CommonsGraph.newDirectedMutableGraph(
            GraphConnectionEloTestCaseTestPerformElo()
        )

        playersRank = SimplePlayersRank()

        CommonsGraph.eloRate(tournament)\
            .wherePlayersAreRankedIn(playersRank).withKFactor(80)
        
        print(playersRank)

    # Class Methods End


class GraphConnectionEloTestCaseTestPerformElo(AbstractGraphConnection):

    def connect0(self) -> None:
        zenio = self.addVertex("Zenio")
        marineking = self.addVertex("Marineking")
        hongun = self.addVertex("Hongun")
        nestea = self.addVertex("Nestea")
        tester = self.addVertex("Tester")
        nada = self.addVertex("Nada")
        rainbow = self.addVertex("Rainbow")
        thewind = self.addVertex("Thewind")
        inka = self.addVertex("Inka")
        maka = self.addVertex("Maka")
        ensnare = self.addVertex("Ensnare")
        kyrix = self.addVertex("Kyrix")
        killer = self.addVertex("Killer")
        slayersboxer = self.addVertex("Slayersboxer")
        fruitdealer = self.addVertex("Fruitdealer")
        genius = self.addVertex("Genius")

        self.addEdge(GameResult.WIN).from_(zenio).to(marineking)
        self.addEdge(GameResult.WIN).from_(fruitdealer).to(hongun)
        self.addEdge(GameResult.WIN).from_(genius).to(nestea)
        self.addEdge(GameResult.WIN).from_(tester).to(nada)
        self.addEdge(GameResult.WIN).from_(thewind).to(rainbow)
        self.addEdge(GameResult.WIN).from_(maka).to(inka)
        self.addEdge(GameResult.WIN).from_(kyrix).to(ensnare)
        self.addEdge(GameResult.WIN).from_(slayersboxer).to(killer)
        self.addEdge(GameResult.WIN).from_(marineking).to(fruitdealer)
        self.addEdge(GameResult.WIN).from_(tester).to(genius)
        self.addEdge(GameResult.WIN).from_(thewind).to(maka)
        self.addEdge(GameResult.WIN).from_(kyrix).to(slayersboxer)
        self.addEdge(GameResult.WIN).from_(marineking).to(tester)
        self.addEdge(GameResult.WIN).from_(kyrix).to(thewind)
        self.addEdge(GameResult.WIN).from_(kyrix).to(marineking)

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # Class Methods End


