from __future__ import annotations
import time
import re
import mock
import os
import unittest
import pytest
import pathlib
import io
import unittest
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.InMemoryPath import *
from src.main.org.apache.commons.graph.model.RevertedGraph import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.shortestpath.DefaultShortestPathAlgorithmSelector import *

# from src.test.org.apache.commons.graph.shortestpath.DefaultShortestPathAlgorithmSelector_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.shortestpath.HeuristicBuilder import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.primitive.BigIntegerWeightBaseOperations import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class DefaultShortestPathAlgorithmSelector_ESTest(unittest.TestCase):

    def test12(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        orderedMonoid0 = mock(OrderedMonoid, ViolatedAssumptionAnswer())
        defaultShortestPathAlgorithmSelector0 = DefaultShortestPathAlgorithmSelector(
            undirectedMutableGraph0, mapper0, orderedMonoid0, orderedMonoid0
        )
        orderedMonoid1 = mock(OrderedMonoid, ViolatedAssumptionAnswer())
        orderedMonoid1.identity = MagicMock(return_value=None)
        weightedPath0 = defaultShortestPathAlgorithmSelector0.applyingDijkstra(
            orderedMonoid1
        )
        mapper1 = mock(Mapper, ViolatedAssumptionAnswer())
        orderedMonoid2 = mock(OrderedMonoid, ViolatedAssumptionAnswer())
        defaultShortestPathAlgorithmSelector1 = DefaultShortestPathAlgorithmSelector(
            weightedPath0, mapper1, orderedMonoid2, orderedMonoid2
        )
        orderedMonoid3 = mock(OrderedMonoid, ViolatedAssumptionAnswer())
        heuristicBuilder0 = defaultShortestPathAlgorithmSelector1.applyingAStar(
            orderedMonoid3
        )
        assert heuristicBuilder0 is not None

    def test11(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        reverted_graph0 = RevertedGraph(directed_mutable_graph0)
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        default_shortest_path_algorithm_selector0 = (
            DefaultShortestPathAlgorithmSelector(
                reverted_graph0, mapper0, reverted_graph0, reverted_graph0
            )
        )
        ordered_monoid0 = mock(OrderedMonoid, ViolatedAssumptionAnswer())
        ordered_monoid0.identity.side_effect = [reverted_graph0, reverted_graph0]

        with pytest.raises(RuntimeError) as e:
            default_shortest_path_algorithm_selector0.applyingBidirectionalDijkstra(
                ordered_monoid0
            )

        assert "org.apache.commons.graph.model.BaseGraph" in str(e.value)

    def test10(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        reverted_graph0 = RevertedGraph(directed_mutable_graph0)
        directed_mutable_graph0.add_vertex(reverted_graph0)
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        default_shortest_path_algorithm_selector0 = (
            DefaultShortestPathAlgorithmSelector(
                reverted_graph0, mapper0, reverted_graph0, reverted_graph0
            )
        )
        ordered_monoid0 = mock(OrderedMonoid, ViolatedAssumptionAnswer())
        ordered_monoid0.identity.side_effect = [reverted_graph0, reverted_graph0]

        with pytest.raises(RuntimeError):
            default_shortest_path_algorithm_selector0.applying_bidirectional_dijkstra(
                ordered_monoid0
            )
            verifyException(
                "org.apache.commons.graph.shortestpath.DefaultShortestPathAlgorithmSelector",
                RuntimeError,
            )

    def test07(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        mapper0 = Mapper(mock(Mapper, ViolatedAssumptionAnswer()))
        defaultShortestPathAlgorithmSelector0 = DefaultShortestPathAlgorithmSelector(
            directedMutableGraph0, mapper0, None, None
        )

        with pytest.raises(RuntimeError):
            defaultShortestPathAlgorithmSelector0.applyingAStar(None)
            verifyException("org.apache.commons.graph.utils.Assertions", RuntimeError)

    def test06(self) -> None:

        bigIntegerWeightBaseOperations0 = BigIntegerWeightBaseOperations()
        inMemoryPath0 = InMemoryPath(
            bigIntegerWeightBaseOperations0, bigIntegerWeightBaseOperations0
        )
        bigIntegerWeightBaseOperations1 = BigIntegerWeightBaseOperations()
        defaultShortestPathAlgorithmSelector0 = DefaultShortestPathAlgorithmSelector(
            inMemoryPath0,
            None,
            bigIntegerWeightBaseOperations1,
            bigIntegerWeightBaseOperations1,
        )

        try:
            defaultShortestPathAlgorithmSelector0.applyingBidirectionalDijkstra(
                bigIntegerWeightBaseOperations0
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Impossible to get the degree of input vertex; org.apache.commons.graph.weight.primitive.BigIntegerWeightBaseOperations@3 not contained in this path
            self.verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test05(self) -> None:

        object0 = object()
        defaultShortestPathAlgorithmSelector0 = DefaultShortestPathAlgorithmSelector[
            object, object, object
        ](None, None, object0, object0)

        try:
            defaultShortestPathAlgorithmSelector0.applyingBidirectionalDijkstra(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test04(self) -> None:

        bigIntegerWeightBaseOperations0 = BigIntegerWeightBaseOperations()
        inMemoryPath0 = InMemoryPath(
            bigIntegerWeightBaseOperations0, bigIntegerWeightBaseOperations0
        )
        defaultShortestPathAlgorithmSelector0 = DefaultShortestPathAlgorithmSelector(
            inMemoryPath0,
            None,
            bigIntegerWeightBaseOperations0,
            bigIntegerWeightBaseOperations0,
        )

        try:
            defaultShortestPathAlgorithmSelector0.applyingBidirectionalDijkstra(
                bigIntegerWeightBaseOperations0
            )
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException(
                "org.apache.commons.graph.shortestpath.DefaultShortestPathAlgorithmSelector",
                e,
            )

    def test03(self) -> None:

        bigIntegerWeightBaseOperations0 = BigIntegerWeightBaseOperations()
        inMemoryPath0 = InMemoryPath(
            bigIntegerWeightBaseOperations0, bigIntegerWeightBaseOperations0
        )
        bigIntegerWeightBaseOperations1 = BigIntegerWeightBaseOperations()
        defaultShortestPathAlgorithmSelector0 = DefaultShortestPathAlgorithmSelector(
            inMemoryPath0,
            None,
            bigIntegerWeightBaseOperations1,
            bigIntegerWeightBaseOperations0,
        )

        try:
            defaultShortestPathAlgorithmSelector0.applyingDijkstra(
                bigIntegerWeightBaseOperations0
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Impossible to get the degree of input vertex; org.apache.commons.graph.weight.primitive.BigIntegerWeightBaseOperations@3 not contained in this path
            self.verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test02(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        roundingMode0 = RoundingMode.UNNECESSARY
        defaultShortestPathAlgorithmSelector0 = DefaultShortestPathAlgorithmSelector(
            undirectedMutableGraph0, None, roundingMode0, roundingMode0
        )

        try:
            defaultShortestPathAlgorithmSelector0.applyingDijkstra(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test01(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        bigIntegerWeightBaseOperations0 = BigIntegerWeightBaseOperations()
        defaultShortestPathAlgorithmSelector0 = DefaultShortestPathAlgorithmSelector(
            directedMutableGraph0, None, bigIntegerWeightBaseOperations0, None
        )

        try:
            defaultShortestPathAlgorithmSelector0.applyingDijkstra(
                bigIntegerWeightBaseOperations0
            )
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException(
                "org.apache.commons.graph.shortestpath.DefaultShortestPathAlgorithmSelector",
                e,
            )

    def test00(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        mapper0 = Mapper()
        rounding_mode0 = RoundingMode.CEILING
        default_shortest_path_algorithm_selector0 = (
            DefaultShortestPathAlgorithmSelector(
                directed_mutable_graph0,
                mapper0,
                rounding_mode0,
                directed_mutable_graph0,
            )
        )
        ordered_monoid0 = OrderedMonoid()
        ordered_monoid0.identity = lambda: None

        with pytest.raises(RuntimeError):
            default_shortest_path_algorithm_selector0.applying_dijkstra(ordered_monoid0)
