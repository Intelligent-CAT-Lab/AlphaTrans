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
from src.main.org.apache.commons.graph.model.InMemoryPath import *
from src.main.org.apache.commons.graph.shortestpath.AllVertexPairsShortestPath import *
from src.main.org.apache.commons.graph.shortestpath.DefaultTargetSourceSelector import *

# from src.test.org.apache.commons.graph.shortestpath.DefaultTargetSourceSelector_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.shortestpath.ShortestPathAlgorithmSelector import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations import *
from src.main.org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class DefaultTargetSourceSelector_ESTest(unittest.TestCase):

    def test8(self) -> None:

        double_weight_base_operations0 = DoubleWeightBaseOperations()
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        default_target_source_selector0 = DefaultTargetSourceSelector(
            None, mapper0, double_weight_base_operations0
        )
        shortest_path_algorithm_selector0 = default_target_source_selector0.to(
            double_weight_base_operations0
        )
        self.assertIsNotNone(shortest_path_algorithm_selector0)

    def test7(self) -> None:

        float_weight_base_operations0 = FloatWeightBaseOperations()
        in_memory_path0 = InMemoryPath(
            float_weight_base_operations0, float_weight_base_operations0
        )
        float_weight_base_operations1 = FloatWeightBaseOperations()
        in_memory_path0.add_connection_in_tail(
            float_weight_base_operations0,
            float_weight_base_operations0,
            float_weight_base_operations1,
        )
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        default_target_source_selector0 = DefaultTargetSourceSelector(
            in_memory_path0, mapper0, float_weight_base_operations1
        )
        ordered_monoid0 = mock(OrderedMonoid, ViolatedAssumptionAnswer())
        ordered_monoid0.identity.side_effect = [None, None]
        all_vertex_pairs_shortest_path0 = (
            default_target_source_selector0.applying_belmann_ford(ordered_monoid0)
        )
        self.assertIsNotNone(all_vertex_pairs_shortest_path0)

    def test6(self) -> None:

        float_weight_base_operations0 = FloatWeightBaseOperations()
        in_memory_path0 = InMemoryPath(
            float_weight_base_operations0, float_weight_base_operations0
        )
        in_memory_path0.add_connection_in_tail(
            float_weight_base_operations0,
            float_weight_base_operations0,
            float_weight_base_operations0,
        )
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        mapper0.map.return_value = [float_weight_base_operations0, None, None]
        default_target_source_selector0 = DefaultTargetSourceSelector(
            in_memory_path0, mapper0, float_weight_base_operations0
        )
        ordered_monoid0 = mock(OrderedMonoid, ViolatedAssumptionAnswer())
        ordered_monoid0.compare.return_value = [-2, 0, 0]
        ordered_monoid0.append.return_value = [
            float_weight_base_operations0,
            None,
            None,
        ]
        ordered_monoid0.identity.return_value = float_weight_base_operations0
        default_target_source_selector0.applying_belmann_ford(ordered_monoid0)

    def test5(self) -> None:

        float_weight_base_operations0 = FloatWeightBaseOperations()
        in_memory_path0 = InMemoryPath(
            float_weight_base_operations0, float_weight_base_operations0
        )
        default_target_source_selector0 = DefaultTargetSourceSelector(
            in_memory_path0, None, float_weight_base_operations0
        )

        try:
            default_target_source_selector0.applying_belmann_ford(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verify_exception("org.apache.commons.graph.utils.Assertions", e)

    def test4(self) -> None:

        float0 = float(0.0)
        defaultTargetSourceSelector0 = DefaultTargetSourceSelector(None, None, float0)
        floatWeightBaseOperations0 = FloatWeightBaseOperations()

        with pytest.raises(RuntimeError):
            defaultTargetSourceSelector0.applyingBelmannFord(floatWeightBaseOperations0)
            self.fail("Expecting exception: RuntimeError")
        self.verifyException(
            "org.apache.commons.graph.shortestpath.DefaultTargetSourceSelector", e
        )

    def test3(self) -> None:

        double0 = float(1739.0191174009544)
        inMemoryPath0 = InMemoryPath(double0, double0)
        defaultTargetSourceSelector0 = DefaultTargetSourceSelector(
            inMemoryPath0, None, double0
        )

        with pytest.raises(RuntimeError):
            defaultTargetSourceSelector0.to(None)

    def test2(self) -> None:

        float_weight_base_operations0 = FloatWeightBaseOperations()
        in_memory_path0 = InMemoryPath(
            float_weight_base_operations0, float_weight_base_operations0
        )
        float_weight_base_operations1 = FloatWeightBaseOperations()
        in_memory_path0.add_connection_in_tail(
            float_weight_base_operations1,
            float_weight_base_operations0,
            float_weight_base_operations0,
        )

        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        mapper0.map = Mock(side_effect=[None, None, None, None])

        default_target_source_selector0 = DefaultTargetSourceSelector(
            in_memory_path0, mapper0, float_weight_base_operations1
        )

        ordered_monoid0 = mock(OrderedMonoid, ViolatedAssumptionAnswer())
        ordered_monoid0.compare = Mock(side_effect=[0, 0])
        ordered_monoid0.append = Mock(side_effect=[None, None, None, None])
        ordered_monoid0.identity = Mock(side_effect=[None, None])

        all_vertex_pairs_shortest_path0 = (
            default_target_source_selector0.applying_belmann_ford(ordered_monoid0)
        )

        assert all_vertex_pairs_shortest_path0 is not None

    def test1(self) -> None:

        float_weight_base_operations0 = FloatWeightBaseOperations()
        in_memory_path0 = InMemoryPath(
            float_weight_base_operations0, float_weight_base_operations0
        )
        float_weight_base_operations1 = FloatWeightBaseOperations()
        in_memory_path0.add_connection_in_tail(
            float_weight_base_operations0,
            float_weight_base_operations1,
            float_weight_base_operations0,
        )

        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        mapper0.map.return_value = None

        default_target_source_selector0 = DefaultTargetSourceSelector(
            in_memory_path0, mapper0, float_weight_base_operations0
        )

        ordered_monoid0 = mock(OrderedMonoid, ViolatedAssumptionAnswer())
        ordered_monoid0.compare.return_value = 0
        ordered_monoid0.append.return_value = None
        ordered_monoid0.identity.return_value = None

        all_vertex_pairs_shortest_path0 = (
            default_target_source_selector0.applying_belmann_ford(ordered_monoid0)
        )

        assert all_vertex_pairs_shortest_path0 is not None

    def test0(self) -> None:

        float_weight_base_operations0 = FloatWeightBaseOperations()
        in_memory_path0 = InMemoryPath(
            float_weight_base_operations0, float_weight_base_operations0
        )
        in_memory_path0.add_connection_in_tail(
            float_weight_base_operations0,
            float_weight_base_operations0,
            float_weight_base_operations0,
        )

        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        mapper0.map.return_value = [
            float_weight_base_operations0,
            float_weight_base_operations0,
            float_weight_base_operations0,
        ]

        default_target_source_selector0 = DefaultTargetSourceSelector(
            in_memory_path0, mapper0, float_weight_base_operations0
        )

        ordered_monoid0 = mock(OrderedMonoid, ViolatedAssumptionAnswer())
        ordered_monoid0.compare.return_value = [-4666, 1734, 2]
        ordered_monoid0.append.return_value = [
            float_weight_base_operations0,
            float_weight_base_operations0,
            float_weight_base_operations0,
        ]
        ordered_monoid0.identity.return_value = float_weight_base_operations0

        all_vertex_pairs_shortest_path0 = (
            default_target_source_selector0.applying_belmann_ford(ordered_monoid0)
        )

        assert all_vertex_pairs_shortest_path0 is not None
