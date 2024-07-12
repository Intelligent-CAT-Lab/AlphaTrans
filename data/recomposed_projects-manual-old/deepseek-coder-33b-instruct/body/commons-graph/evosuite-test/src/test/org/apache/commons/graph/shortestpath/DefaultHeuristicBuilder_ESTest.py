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
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.InMemoryPath import *
from src.main.org.apache.commons.graph.model.InMemoryWeightedPath import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.shortestpath.DefaultHeuristicBuilder import *

# from src.test.org.apache.commons.graph.shortestpath.DefaultHeuristicBuilder_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.shortestpath.Heuristic import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class DefaultHeuristicBuilder_ESTest(unittest.TestCase):

    def test5(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        mapper0 = Mock(spec=Mapper)
        ordered_monoid0 = Mock(spec=OrderedMonoid)
        ordered_monoid0.identity.side_effect = [None, None]
        default_heuristic_builder0 = DefaultHeuristicBuilder(
            directed_mutable_graph0,
            mapper0,
            directed_mutable_graph0,
            directed_mutable_graph0,
            ordered_monoid0,
        )
        heuristic0 = Mock(spec=Heuristic)
        heuristic0.applyHeuristic.return_value = None
        weighted_path0 = default_heuristic_builder0.withHeuristic(heuristic0)
        self.assertIsNotNone(weighted_path0)

    def test4(self) -> None:

        integer0 = Integer(3)
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        inMemoryWeightedPath0 = InMemoryWeightedPath(
            integer0, integer0, integerWeightBaseOperations0, mapper0
        )
        mapper1 = mock(Mapper, ViolatedAssumptionAnswer())
        integer1 = Integer(0)
        defaultHeuristicBuilder0 = DefaultHeuristicBuilder(
            inMemoryWeightedPath0,
            mapper1,
            integer0,
            integer1,
            integerWeightBaseOperations0,
        )
        heuristic0 = mock(Heuristic, ViolatedAssumptionAnswer())
        doReturn(None).when(heuristic0).applyHeuristic(anyInt(), anyInt())

        try:
            defaultHeuristicBuilder0.withHeuristic(heuristic0)
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            verifyException(
                "org.apache.commons.graph.shortestpath.DefaultHeuristicBuilder", e
            )

    def test3(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        object0 = Object()
        directed_mutable_graph0.add_vertex(object0)
        ordered_monoid0 = mock(OrderedMonoid, ViolatedAssumptionAnswer())
        ordered_monoid0.identity.return_value = object0
        directed_mutableGraph0.add_edge(object0, object0, object0)
        default_heuristic_builder0 = DefaultHeuristicBuilder(
            directed_mutable_graph0,
            mapper0,
            object0,
            directed_mutable_graph0,
            ordered_monoid0,
        )
        heuristic0 = mock(Heuristic, ViolatedAssumptionAnswer())
        heuristic0.apply_heuristic.return_value = None

        with pytest.raises(RuntimeError):
            default_heuristic_builder0.with_heuristic(heuristic0)
            verifyException(
                "org.apache.commons.graph.shortestpath.DefaultHeuristicBuilder",
                RuntimeError,
            )

    def test2(self) -> None:

        object0 = object()
        inMemoryPath0 = InMemoryPath(object0, object0)
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        object1 = object()
        orderedMonoid0 = mock(OrderedMonoid, ViolatedAssumptionAnswer())
        orderedMonoid0.identity.return_value = None
        defaultHeuristicBuilder0 = DefaultHeuristicBuilder(
            inMemoryPath0, mapper0, object1, inMemoryPath0, orderedMonoid0
        )
        heuristic0 = mock(Heuristic, ViolatedAssumptionAnswer())
        heuristic0.applyHeuristic.return_value = None

        try:
            defaultHeuristicBuilder0.withHeuristic(heuristic0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test1(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        defaultHeuristicBuilder0 = DefaultHeuristicBuilder(
            undirectedMutableGraph0,
            mapper0,
            undirectedMutableGraph0,
            mapper0,
            integerWeightBaseOperations0,
        )

        try:
            defaultHeuristicBuilder0.withHeuristic(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test0(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        mapper0 = Mock(spec=Mapper)
        mapper0.toString.return_value = None
        orderedMonoid0 = Mock(spec=OrderedMonoid)
        orderedMonoid0.identity.return_value = None
        defaultHeuristicBuilder0 = DefaultHeuristicBuilder(
            undirectedMutableGraph0,
            mapper0,
            mapper0,
            undirectedMutableGraph0,
            orderedMonoid0,
        )
        heuristic0 = Mock(spec=Heuristic)
        heuristic0.applyHeuristic.return_value = None

        with pytest.raises(RuntimeError):
            defaultHeuristicBuilder0.withHeuristic(heuristic0)
            assert False, "Expecting exception: RuntimeError"
        assert "org.apache.commons.graph.model.BaseGraph" in str(
            e.value
        ), "no message in exception (getMessage() returned null)"
