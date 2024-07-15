from __future__ import annotations
import time
import re
import mock
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.elo.DefaultKFactorBuilder import *

# from src.test.org.apache.commons.graph.elo.DefaultKFactorBuilder_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.elo.GameResult import *
from src.main.org.apache.commons.graph.elo.PlayersRank import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class DefaultKFactorBuilder_ESTest(unittest.TestCase):

    def test4(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        defaultKFactorBuilder0 = DefaultKFactorBuilder(directedMutableGraph0, None)
        defaultKFactorBuilder0.withDefaultKFactor()

    def test2(self) -> None:

        defaultKFactorBuilder0 = DefaultKFactorBuilder(None, None)

        with pytest.raises(RuntimeError):
            defaultKFactorBuilder0.withDefaultKFactor()
            self.fail("Expecting exception: RuntimeError")

        verifyException(
            "org.apache.commons.graph.elo.DefaultKFactorBuilder", RuntimeError
        )

    def test1(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        double0 = float(2324.7)
        double1 = float(-1238.378389823641)
        players_rank0 = PlayersRank()
        players_rank0.getRanking = MagicMock(
            side_effect=[double0, double1, double1, double0]
        )
        default_k_factor_builder0 = DefaultKFactorBuilder(
            directed_mutable_graph0, players_rank0
        )
        game_result0 = GameResult.DRAW
        directed_mutable_graph0.addVertex(game_result0)
        directed_mutable_graph0.addEdge(game_result0, game_result0, game_result0)
        default_k_factor_builder0.withKFactor(-1250)

    def test0(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        double0 = float(0.5)
        players_rank0 = PlayersRank()
        players_rank0.getRanking = lambda x: double0
        default_k_factor_builder0 = DefaultKFactorBuilder(
            directed_mutable_graph0, players_rank0
        )
        game_result0 = GameResult()
        game_result0.DRAW = GameResult()
        directed_mutable_graph0.addVertex(game_result0.DRAW)
        game_result1 = GameResult()
        game_result1.WIN = GameResult()
        directed_mutable_graph0.addVertex(game_result1.WIN)
        directed_mutable_graph0.addEdge(
            game_result0.DRAW, game_result1.WIN, game_result1.WIN
        )
        default_k_factor_builder0.withKFactor(-1)
