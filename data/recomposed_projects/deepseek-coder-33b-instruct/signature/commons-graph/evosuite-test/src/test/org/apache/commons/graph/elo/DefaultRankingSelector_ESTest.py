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
from src.main.org.apache.commons.graph.elo.DefaultRankingSelector import *

# from src.test.org.apache.commons.graph.elo.DefaultRankingSelector_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.elo.KFactorBuilder import *
from src.main.org.apache.commons.graph.elo.PlayersRank import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.RevertedGraph import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *


class DefaultRankingSelector_ESTest(unittest.TestCase):

    def test1(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        default_ranking_selector0 = DefaultRankingSelector(directed_mutable_graph0)

        try:
            default_ranking_selector0.where_players_are_ranked_in(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # ELO ranking can not be applied if players can not be ranked
            self.verify_exception("org.apache.commons.graph.utils.Assertions", e)

    def test0(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        reverted_graph0 = RevertedGraph(directed_mutable_graph0)
        default_ranking_selector0 = DefaultRankingSelector(reverted_graph0)
        players_rank0 = (
            PlayersRank()
        )  # Assuming PlayersRank is a class with a mock method
        k_factor_builder0 = default_ranking_selector0.where_players_are_ranked_in(
            players_rank0
        )
        assert k_factor_builder0 is not None
