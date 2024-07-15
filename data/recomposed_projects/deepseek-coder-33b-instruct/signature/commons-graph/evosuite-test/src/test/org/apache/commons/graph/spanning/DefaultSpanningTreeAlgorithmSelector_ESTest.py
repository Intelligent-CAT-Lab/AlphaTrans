from __future__ import annotations
import time
import re
import mock
import collections
import os
import typing
from typing import *
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
from src.main.org.apache.commons.graph.model.InMemoryWeightedPath import *
from src.main.org.apache.commons.graph.model.RevertedGraph import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.spanning.DefaultSpanningTreeAlgorithmSelector import *

# from src.test.org.apache.commons.graph.spanning.DefaultSpanningTreeAlgorithmSelector_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.spanning.ReverseDeleteGraph import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.primitive.BigIntegerWeightBaseOperations import *
from src.main.org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class DefaultSpanningTreeAlgorithmSelector_ESTest(unittest.TestCase):

    def test14(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        floatWeightBaseOperations0 = FloatWeightBaseOperations()
        mapper0 = Mapper()
        mapper0.violatedAssumptionAnswer()
        undirectedMutableGraph0.addVertex(floatWeightBaseOperations0)
        defaultSpanningTreeAlgorithmSelector0 = DefaultSpanningTreeAlgorithmSelector(
            undirectedMutableGraph0, mapper0, floatWeightBaseOperations0
        )
        orderedMonoid0 = OrderedMonoid()
        orderedMonoid0.identity()
        spanningTree0 = defaultSpanningTreeAlgorithmSelector0.applyingBoruvkaAlgorithm(
            orderedMonoid0
        )
        self.assertIsNotNone(spanningTree0)

    def test13(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        floatWeightBaseOperations0 = FloatWeightBaseOperations()
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        floatWeightBaseOperations1 = FloatWeightBaseOperations()
        undirectedMutableGraph0.addVertex(floatWeightBaseOperations1)
        undirectedMutableGraph0.addVertex(floatWeightBaseOperations0)
        defaultSpanningTreeAlgorithmSelector0 = DefaultSpanningTreeAlgorithmSelector(
            undirectedMutableGraph0, mapper0, floatWeightBaseOperations0
        )
        orderedMonoid0 = mock(OrderedMonoid, ViolatedAssumptionAnswer())
        orderedMonoid0.identity.return_value = None

        with pytest.raises(RuntimeError):
            defaultSpanningTreeAlgorithmSelector0.applyingBoruvkaAlgorithm(
                orderedMonoid0
            )
            verifyException("org.apache.commons.graph.utils.Assertions", RuntimeError)

    def test12(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        big_integer0 = BigInteger.ONE
        list0 = [big_integer0] * 10
        linked_list0 = LinkedList()
        reverse_delete_graph0 = ReverseDeleteGraph(
            directed_mutable_graph0, list0, linked_list0
        )
        mapper0 = Mapper()
        mapper0.map = MagicMock(side_effect=[None, None, None, None, None])
        default_spanning_tree_algorithm_selector0 = (
            DefaultSpanningTreeAlgorithmSelector(
                reverse_delete_graph0, mapper0, big_integer0
            )
        )
        ordered_monoid0 = OrderedMonoid()
        ordered_monoid0.compare = MagicMock(side_effect=[0, 0, 0, 0, 0])
        ordered_monoid0.identity = MagicMock(return_value=None)
        spanning_tree0 = (
            default_spanning_tree_algorithm_selector0.applying_kruskal_algorithm(
                ordered_monoid0
            )
        )
        self.assertIsNotNone(spanning_tree0)

    def test11(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        big_integer0 = BigInteger.ONE
        list0 = [
            big_integer0,
            big_integer0,
            big_integer0,
            big_integer0,
            big_integer0,
            big_integer0,
            big_integer0,
            big_integer0,
            big_integer0,
            big_integer0,
        ]
        linked_list0 = LinkedList()
        reverse_delete_graph0 = ReverseDeleteGraph(
            directed_mutable_graph0, list0, linked_list0
        )
        float_weight_base_operations0 = FloatWeightBaseOperations()
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        mapper0.map = Mock(
            side_effect=[
                float_weight_base_operations0,
                float_weight_base_operations0,
                float_weight_base_operations0,
                float_weight_base_operations0,
                float_weight_base_operations0,
            ]
        )
        default_spanning_tree_algorithm_selector0 = (
            DefaultSpanningTreeAlgorithmSelector(
                reverse_delete_graph0, mapper0, big_integer0
            )
        )
        directed_mutable_graph0.addVertex(big_integer0)
        ordered_monoid0 = mock(OrderedMonoid, ViolatedAssumptionAnswer())
        ordered_monoid0.compare = Mock(side_effect=[0, 4, 0, 4, 1])
        ordered_monoid0.identity = Mock(return_value=float_weight_base_operations0)

        with pytest.raises(RuntimeError):
            default_spanning_tree_algorithm_selector0.applyingKruskalAlgorithm(
                ordered_monoid0
            )
            verifyException(
                "org.apache.commons.graph.spanning.DefaultSpanningTreeAlgorithmSelector",
                RuntimeError,
            )

    def test10(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[BigInteger, BigInteger]()
        bigInteger0 = BigInteger.ZERO
        directedMutableGraph0.addVertex(bigInteger0)
        directedMutableGraph0.addEdge(bigInteger0, bigInteger0, bigInteger0)

        defaultSpanningTreeAlgorithmSelector0 = DefaultSpanningTreeAlgorithmSelector[
            BigInteger, FloatWeightBaseOperations, BigInteger
        ](directedMutableGraph0, None, bigInteger0)

        orderedMonoid0 = unittest.mock.Mock(
            spec=OrderedMonoid[FloatWeightBaseOperations]
        )
        orderedMonoid0.identity.return_value = None

        spanningTree0 = defaultSpanningTreeAlgorithmSelector0.applyingKruskalAlgorithm(
            orderedMonoid0
        )

        self.assertIsNotNone(spanningTree0)

    def test09(self) -> None:

        bigIntegerWeightBaseOperations0 = BigIntegerWeightBaseOperations()
        directedMutableGraph0 = DirectedMutableGraph()
        revertedGraph0 = RevertedGraph(directedMutableGraph0)
        defaultSpanningTreeAlgorithmSelector0 = DefaultSpanningTreeAlgorithmSelector(
            revertedGraph0, None, bigIntegerWeightBaseOperations0
        )

        try:
            defaultSpanningTreeAlgorithmSelector0.applyingPrimAlgorithm(
                bigIntegerWeightBaseOperations0
            )
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.apache.commons.graph.model.BaseGraph", e)

    def test08(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        floatWeightBaseOperations0 = FloatWeightBaseOperations()
        mapper0 = Mapper()
        undirectedMutableGraph0.addVertex(floatWeightBaseOperations0)
        defaultSpanningTreeAlgorithmSelector0 = DefaultSpanningTreeAlgorithmSelector(
            undirectedMutableGraph0, mapper0, floatWeightBaseOperations0
        )
        orderedMonoid0 = OrderedMonoid()
        orderedMonoid0.identity = None
        spanningTree0 = defaultSpanningTreeAlgorithmSelector0.applyingPrimAlgorithm(
            orderedMonoid0
        )
        self.assertIsNotNone(spanningTree0)

    def test07(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        floatWeightBaseOperations0 = FloatWeightBaseOperations()
        defaultSpanningTreeAlgorithmSelector0 = DefaultSpanningTreeAlgorithmSelector(
            undirectedMutableGraph0, None, floatWeightBaseOperations0
        )

        with pytest.raises(RuntimeError):
            defaultSpanningTreeAlgorithmSelector0.applyingBoruvkaAlgorithm(None)
            self.fail("Expecting exception: RuntimeError")

    def test06(self) -> None:

        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        defaultSpanningTreeAlgorithmSelector0 = DefaultSpanningTreeAlgorithmSelector(
            None, mapper0, None
        )
        orderedMonoid0 = mock(OrderedMonoid, ViolatedAssumptionAnswer())
        orderedMonoid0.identity.return_value = None

        with pytest.raises(RuntimeError):
            defaultSpanningTreeAlgorithmSelector0.applyingBoruvkaAlgorithm(
                orderedMonoid0
            )

    def test05(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        big_integer0 = BigInteger.ZERO
        default_spanning_tree_algorithm_selector0 = (
            DefaultSpanningTreeAlgorithmSelector(
                directed_mutable_graph0, None, big_integer0
            )
        )

        # Undeclared exception handling in Python is done using try-except blocks
        try:
            default_spanning_tree_algorithm_selector0.applying_kruskal_algorithm(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # The Kruskal algorithm cannot be calculated with null weight operations
            self.verify_exception("org.apache.commons.graph.utils.Assertions", e)

    def test04(self) -> None:

        bigInteger0 = BigInteger.ONE
        linkedList0 = LinkedList[BigInteger]()
        inMemoryPath0 = InMemoryPath[BigInteger, BigInteger](bigInteger0, bigInteger0)
        reverseDeleteGraph0 = ReverseDeleteGraph[BigInteger, BigInteger](
            inMemoryPath0, linkedList0, linkedList0
        )
        inMemoryPath0.addConnectionInTail(bigInteger0, bigInteger0, bigInteger0)
        mapper0 = mock(
            Mapper[BigInteger, FloatWeightBaseOperations], ViolatedAssumptionAnswer()
        )
        defaultSpanningTreeAlgorithmSelector0 = DefaultSpanningTreeAlgorithmSelector[
            BigInteger, FloatWeightBaseOperations, BigInteger
        ](reverseDeleteGraph0, mapper0, bigInteger0)
        orderedMonoid0 = mock(
            OrderedMonoid[FloatWeightBaseOperations], ViolatedAssumptionAnswer()
        )
        orderedMonoid0.identity = lambda: None

        try:
            defaultSpanningTreeAlgorithmSelector0.applyingKruskalAlgorithm(
                orderedMonoid0
            )
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.model.BaseGraph", e)

    def test03(self) -> None:

        bigIntegerWeightBaseOperations0 = BigIntegerWeightBaseOperations()
        monoid0 = mock(Monoid, ViolatedAssumptionAnswer())
        monoid0.identity = lambda: None
        bigIntegerWeightBaseOperations1 = BigIntegerWeightBaseOperations()
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        inMemoryWeightedPath0 = InMemoryWeightedPath(
            bigIntegerWeightBaseOperations0,
            bigIntegerWeightBaseOperations1,
            monoid0,
            mapper0,
        )
        mapper1 = mock(Mapper, ViolatedAssumptionAnswer())
        defaultSpanningTreeAlgorithmSelector0 = DefaultSpanningTreeAlgorithmSelector(
            inMemoryWeightedPath0, mapper1, bigIntegerWeightBaseOperations0
        )

        try:
            defaultSpanningTreeAlgorithmSelector0.applyingPrimAlgorithm(
                bigIntegerWeightBaseOperations1
            )
            self.fail("Expecting exception: ValueError")
        except ValueError as e:
            verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test02(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        big_integer0 = BigInteger.ZERO
        default_spanning_tree_algorithm_selector0 = (
            DefaultSpanningTreeAlgorithmSelector(
                directed_mutable_graph0, None, big_integer0
            )
        )

        try:
            default_spanning_tree_algorithm_selector0.applying_prim_algorithm(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verify_exception("org.apache.commons.graph.utils.Assertions", e)

    def test01(self) -> None:

        bigIntegerWeightBaseOperations0 = BigIntegerWeightBaseOperations()
        inMemoryPath0 = InMemoryPath(
            bigIntegerWeightBaseOperations0, bigIntegerWeightBaseOperations0
        )
        defaultSpanningTreeAlgorithmSelector0 = DefaultSpanningTreeAlgorithmSelector(
            inMemoryPath0, None, bigIntegerWeightBaseOperations0
        )

        with self.assertRaises(RuntimeError):
            defaultSpanningTreeAlgorithmSelector0.applyingPrimAlgorithm(
                bigIntegerWeightBaseOperations0
            )

    def test00(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        byteArray0 = bytearray(3)
        bigInteger0 = BigInteger(byteArray0)
        bigInteger1 = BigInteger(byteArray0)
        directedMutableGraph0.addVertex(bigInteger0)
        directedMutableGraph0.addEdge(bigInteger1, bigInteger1, bigInteger1)
        mapper0 = Mapper(bigInteger0)
        defaultSpanningTreeAlgorithmSelector0 = DefaultSpanningTreeAlgorithmSelector(
            directedMutableGraph0, mapper0, bigInteger0
        )
        orderedMonoid0 = OrderedMonoid()

        try:
            defaultSpanningTreeAlgorithmSelector0.applyingPrimAlgorithm(orderedMonoid0)
            self.fail("Expecting exception: NotImplementedError")
        except NotImplementedError as e:
            self.verifyException(
                "org.apache.commons.graph.collections.FibonacciHeap", e
            )
