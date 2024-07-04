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
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.InMemoryPath import *
from src.main.org.apache.commons.graph.model.MutableSpanningTree import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.shortestpath.AllVertexPairsShortestPath import *
from src.main.org.apache.commons.graph.shortestpath.DefaultPathSourceSelector import *

# from src.test.org.apache.commons.graph.shortestpath.DefaultPathSourceSelector_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.shortestpath.TargetSourceSelector import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations import *
from src.main.org.apache.commons.graph.weight.primitive.LongWeightBaseOperations import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class DefaultPathSourceSelector_ESTest(unittest.TestCase):

    def test5(self) -> None:

        float_weight_base_operations0 = FloatWeightBaseOperations()
        in_memory_path0 = InMemoryPath(
            float_weight_base_operations0, float_weight_base_operations0
        )
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        default_path_source_selector0 = DefaultPathSourceSelector(
            in_memory_path0, mapper0
        )
        target_source_selector0 = default_path_source_selector0.from_(
            float_weight_base_operations0
        )
        assert target_source_selector0 is not None

    def test4(self) -> None:

        ordered_monoid0 = unittest.mock.Mock(spec=OrderedMonoid)
        in_memory_path0 = InMemoryPath(ordered_monoid0, ordered_monoid0)
        long_weight_base_operations0 = LongWeightBaseOperations()
        ordered_monoid1 = unittest.mock.Mock(spec=OrderedMonoid)
        in_memory_path0.add_connection_in_tail(
            ordered_monoid1, long_weight_base_operations0, ordered_monoid1
        )
        ordered_monoid2 = unittest.mock.Mock(spec=OrderedMonoid)
        mapper0 = unittest.mock.Mock(spec=Mapper)
        mapper0.map.return_value = None
        default_path_source_selector0 = DefaultPathSourceSelector(
            in_memory_path0, mapper0
        )
        ordered_monoid3 = unittest.mock.Mock(spec=OrderedMonoid)
        in_memory_path0.add_connection_in_tail(
            ordered_monoid3, long_weight_base_operations0, ordered_monoid3
        )
        ordered_monoid4 = unittest.mock.Mock(spec=OrderedMonoid)

        with pytest.raises(RuntimeError):
            default_path_source_selector0.applying_floyd_warshall(ordered_monoid4)
            # Impossible to add a shortest distance with a null distance
            verify_exception("org.apache.commons.graph.utils.Assertions")

    def test3(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        undirectedMutableGraph0 = UndirectedMutableGraph()
        mapper0 = Mapper()
        defaultPathSourceSelector0 = DefaultPathSourceSelector(
            undirectedMutableGraph0, mapper0
        )
        directedMutableGraph0.addVertex(defaultPathSourceSelector0)
        defaultPathSourceSelector1 = DefaultPathSourceSelector(
            directedMutableGraph0, None
        )
        orderedMonoid0 = OrderedMonoid()
        orderedMonoid0.compare(orderedMonoid0, orderedMonoid0)
        orderedMonoid0.append(orderedMonoid0, orderedMonoid0)
        orderedMonoid0.identity()
        orderedMonoid0.identity()
        orderedMonoid0.identity()
        defaultPathSourceSelector1.applyingFloydWarshall(orderedMonoid0)

    def test2(self) -> None:

        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        defaultPathSourceSelector0 = DefaultPathSourceSelector(None, mapper0)
        orderedMonoid0 = mock(OrderedMonoid, ViolatedAssumptionAnswer())

        try:
            defaultPathSourceSelector0.applyingFloydWarshall(orderedMonoid0)
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            verifyException(
                "org.apache.commons.graph.shortestpath.DefaultPathSourceSelector", e
            )

    def test1(self) -> None:

        mapper0 = Mock(spec=Mapper)
        mapper0.side_effect = ViolatedAssumptionAnswer()

        defaultPathSourceSelector0 = DefaultPathSourceSelector(None, mapper0)

        with self.assertRaises(RuntimeError):
            defaultPathSourceSelector0.from_(None)

        verifyException("org.apache.commons.graph.utils.Assertions", RuntimeError)

    def test0(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        defaultPathSourceSelector0 = DefaultPathSourceSelector(
            undirectedMutableGraph0, None
        )
        monoid0 = mock(Monoid, ViolatedAssumptionAnswer())
        monoid0.identity.return_value = defaultPathSourceSelector0
        mutableSpanningTree0 = MutableSpanningTree(monoid0, None)
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        defaultPathSourceSelector1 = DefaultPathSourceSelector(
            mutableSpanningTree0, mapper0
        )
        longWeightBaseOperations0 = LongWeightBaseOperations()
        vertexPair0 = VertexPair(longWeightBaseOperations0, longWeightBaseOperations0)
        mutableSpanningTree0.addVertex(vertexPair0)
        monoid1 = mock(Monoid, ViolatedAssumptionAnswer())
        monoid1.identity.return_value = None
        mapper1 = mock(Mapper, ViolatedAssumptionAnswer())
        mutableSpanningTree1 = MutableSpanningTree(monoid1, mapper1)
        orderedMonoid0 = mock(OrderedMonoid, ViolatedAssumptionAnswer())
        orderedMonoid0.compare.return_value = 0
        orderedMonoid0.append.return_value = None
        orderedMonoid0.identity.return_value = None
        allVertexPairsShortestPath0 = defaultPathSourceSelector1.applyingFloydWarshall(
            orderedMonoid0
        )
        self.assertIsNotNone(allVertexPairsShortestPath0)
