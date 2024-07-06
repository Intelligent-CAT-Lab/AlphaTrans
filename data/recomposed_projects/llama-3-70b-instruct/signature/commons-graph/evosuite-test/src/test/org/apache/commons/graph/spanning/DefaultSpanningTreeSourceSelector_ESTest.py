from __future__ import annotations
import time
import re
import mock
import os
import pathlib
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.SpanningTree import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.InMemoryPath import *
from src.main.org.apache.commons.graph.model.RevertedGraph import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.spanning.DefaultSpanningTreeSourceSelector import *

# from src.test.org.apache.commons.graph.spanning.DefaultSpanningTreeSourceSelector_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.spanning.SpanningTreeAlgorithmSelector import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations import *
from src.main.org.apache.commons.graph.weight.primitive.LongWeightBaseOperations import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class DefaultSpanningTreeSourceSelector_ESTest(unittest.TestCase):

    def test11(self) -> None:

        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        longWeightBaseOperations0 = LongWeightBaseOperations()
        inMemoryPath0 = InMemoryPath(
            longWeightBaseOperations0, longWeightBaseOperations0
        )
        defaultSpanningTreeSourceSelector0 = DefaultSpanningTreeSourceSelector(
            inMemoryPath0, mapper0
        )

        with pytest.raises(RuntimeError):
            defaultSpanningTreeSourceSelector0.fromSource(longWeightBaseOperations0)
            verifyException("org.apache.commons.graph.utils.Assertions", RuntimeError)

    def test10(self) -> None:

        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        longWeightBaseOperations0 = LongWeightBaseOperations()
        inMemoryPath0 = InMemoryPath(
            longWeightBaseOperations0, longWeightBaseOperations0
        )
        defaultSpanningTreeSourceSelector0 = DefaultSpanningTreeSourceSelector(
            inMemoryPath0, mapper0
        )
        floatWeightBaseOperations0 = FloatWeightBaseOperations()
        inMemoryPath0.addConnectionInHead(
            longWeightBaseOperations0,
            floatWeightBaseOperations0,
            longWeightBaseOperations0,
        )
        orderedMonoid0 = mock(OrderedMonoid, ViolatedAssumptionAnswer())
        orderedMonoid0.identity.side_effect = [floatWeightBaseOperations0, None, None]

        with pytest.raises(RuntimeError) as e:
            defaultSpanningTreeSourceSelector0.applyingReverseDeleteAlgorithm(
                orderedMonoid0
            )

        verifyException("org.apache.commons.graph.model.BaseGraph", e)

    def test09(self) -> None:

        mapper0 = mock(Mapper, ViolatedAssumptionAnswer)
        longWeightBaseOperations0 = LongWeightBaseOperations()
        inMemoryPath0 = InMemoryPath(
            longWeightBaseOperations0, longWeightBaseOperations0
        )
        defaultSpanningTreeSourceSelector0 = DefaultSpanningTreeSourceSelector(
            inMemoryPath0, mapper0
        )
        longWeightBaseOperations1 = LongWeightBaseOperations()
        floatWeightBaseOperations0 = FloatWeightBaseOperations()
        inMemoryPath0.addConnectionInHead(
            longWeightBaseOperations1,
            floatWeightBaseOperations0,
            longWeightBaseOperations1,
        )
        orderedMonoid0 = mock(OrderedMonoid, ViolatedAssumptionAnswer)
        orderedMonoid0.identity.side_effect = [
            floatWeightBaseOperations0,
            floatWeightBaseOperations0,
            floatWeightBaseOperations0,
        ]
        spanningTree0 = (
            defaultSpanningTreeSourceSelector0.applyingReverseDeleteAlgorithm(
                orderedMonoid0
            )
        )
        self.assertIsNotNone(spanningTree0)

    def test08(self) -> None:

        longWeightBaseOperations0 = LongWeightBaseOperations()
        inMemoryPath0 = InMemoryPath(
            longWeightBaseOperations0, longWeightBaseOperations0
        )
        longWeightBaseOperations1 = LongWeightBaseOperations()
        floatWeightBaseOperations0 = FloatWeightBaseOperations()
        inMemoryPath0.addConnectionInHead(
            longWeightBaseOperations1,
            floatWeightBaseOperations0,
            longWeightBaseOperations0,
        )

        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        mapper0.map = Mock(return_value=None)

        defaultSpanningTreeSourceSelector0 = DefaultSpanningTreeSourceSelector(
            inMemoryPath0, mapper0
        )

        orderedMonoid0 = mock(OrderedMonoid, ViolatedAssumptionAnswer())
        orderedMonoid0.append = Mock(return_value=None)
        orderedMonoid0.identity = Mock(side_effect=[None, None])

        spanningTree0 = (
            defaultSpanningTreeSourceSelector0.applyingReverseDeleteAlgorithm(
                orderedMonoid0
            )
        )

        self.assertIsNotNone(spanningTree0)

    def test07(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        revertedGraph0 = RevertedGraph(directedMutableGraph0)
        mapper0 = Mapper()
        defaultSpanningTreeSourceSelector0 = DefaultSpanningTreeSourceSelector(
            revertedGraph0, mapper0
        )

        # Undeclared exception in Java code
        try:
            defaultSpanningTreeSourceSelector0.fromArbitrarySource()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # Spanning tree cannot be calculated on an empty graph
            verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test06(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph[
            FloatWeightBaseOperations, FloatWeightBaseOperations
        ]()
        floatWeightBaseOperations0 = FloatWeightBaseOperations()
        undirectedMutableGraph0.addVertex(floatWeightBaseOperations0)
        defaultSpanningTreeSourceSelector0 = DefaultSpanningTreeSourceSelector[
            FloatWeightBaseOperations,
            FloatWeightBaseOperations,
            FloatWeightBaseOperations,
        ](undirectedMutableGraph0, None)
        spanningTreeAlgorithmSelector0 = (
            defaultSpanningTreeSourceSelector0.fromArbitrarySource()
        )
        self.assertIsNotNone(spanningTreeAlgorithmSelector0)

    def test04(self) -> None:

        float_weight_base_operations0 = FloatWeightBaseOperations()
        long_weight_base_operations0 = LongWeightBaseOperations()
        in_memory_path0 = InMemoryPath(
            long_weight_base_operations0, long_weight_base_operations0
        )
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        default_spanning_tree_source_selector0 = DefaultSpanningTreeSourceSelector(
            in_memory_path0, mapper0
        )
        long_weight_base_operations1 = LongWeightBaseOperations()
        in_memory_path0.add_connection_in_head(
            long_weight_base_operations0,
            float_weight_base_operations0,
            long_weight_base_operations1,
        )
        ordered_monoid0 = mock(OrderedMonoid, ViolatedAssumptionAnswer())
        ordered_monoid0.identity.return_value = float_weight_base_operations0

        with pytest.raises(RuntimeError):
            default_spanning_tree_source_selector0.applying_reverse_delete_algorithm(
                ordered_monoid0
            )
            verifyException(
                "org.apache.commons.graph.spanning.ReverseDeleteGraph", RuntimeError
            )

    def test03(self) -> None:

        defaultSpanningTreeSourceSelector0 = DefaultSpanningTreeSourceSelector[
            Long, Long, Long
        ](None, None)

        with pytest.raises(RuntimeError):
            defaultSpanningTreeSourceSelector0.fromArbitrarySource()
            verifyException(
                "org.apache.commons.graph.spanning.DefaultSpanningTreeSourceSelector",
                RuntimeError,
            )

    def test02(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        defaultSpanningTreeSourceSelector0 = DefaultSpanningTreeSourceSelector(
            directedMutableGraph0, None
        )

        with pytest.raises(RuntimeError):
            defaultSpanningTreeSourceSelector0.fromSource(None)

    def test01(self) -> None:

        defaultSpanningTreeSourceSelector0 = DefaultSpanningTreeSourceSelector[
            Long, Long, Long
        ](None, None)
        long0 = Long(1140)

        with pytest.raises(RuntimeError):
            defaultSpanningTreeSourceSelector0.fromSource(long0)
            verifyException(
                "org.apache.commons.graph.spanning.DefaultSpanningTreeSourceSelector",
                RuntimeError,
            )

    def test00(self) -> None:

        mapper0 = Mock(spec=Mapper)
        mapper0.side_effect = ViolatedAssumptionAnswer()

        longWeightBaseOperations0 = LongWeightBaseOperations()
        inMemoryPath0 = InMemoryPath(
            longWeightBaseOperations0, longWeightBaseOperations0
        )
        defaultSpanningTreeSourceSelector0 = DefaultSpanningTreeSourceSelector(
            inMemoryPath0, mapper0
        )
        floatWeightBaseOperations0 = FloatWeightBaseOperations()
        inMemoryPath0.addConnectionInHead(
            longWeightBaseOperations0,
            floatWeightBaseOperations0,
            longWeightBaseOperations0,
        )
        spanningTreeAlgorithmSelector0 = defaultSpanningTreeSourceSelector0.fromSource(
            longWeightBaseOperations0
        )

        self.assertIsNotNone(spanningTreeAlgorithmSelector0)
