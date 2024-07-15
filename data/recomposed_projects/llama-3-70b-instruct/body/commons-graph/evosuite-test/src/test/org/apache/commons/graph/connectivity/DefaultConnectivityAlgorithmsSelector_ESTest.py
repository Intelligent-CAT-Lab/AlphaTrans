from __future__ import annotations
import time
import re
import mock
import os
import typing
from typing import *
import pathlib
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.connectivity.DefaultConnectivityAlgorithmsSelector import *

# from src.test.org.apache.commons.graph.connectivity.DefaultConnectivityAlgorithmsSelector_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.model.InMemoryPath import *
from src.main.org.apache.commons.graph.model.MutableSpanningTree import *
from src.main.org.apache.commons.graph.weight.Monoid import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class DefaultConnectivityAlgorithmsSelector_ESTest(unittest.TestCase):

    def test4(self) -> None:

        tree_set0 = TreeSet()
        default_connectivity_algorithms_selector0 = (
            DefaultConnectivityAlgorithmsSelector(None, tree_set0)
        )
        collection0 = (
            default_connectivity_algorithms_selector0.applying_minimum_spanning_tree_algorithm()
        )
        self.assertIsNotNone(collection0)

    def test3(self) -> None:

        linkedList0 = LinkedList()
        linkedList1 = LinkedList()
        list0 = [
            linkedList0,
            linkedList0,
            linkedList0,
            linkedList1,
            linkedList1,
            linkedList1,
            linkedList1,
            linkedList0,
            linkedList0,
        ]
        inMemoryPath0 = InMemoryPath(linkedList1, linkedList1)
        hashSet0 = set(list0)
        defaultConnectivityAlgorithmsSelector0 = DefaultConnectivityAlgorithmsSelector(
            inMemoryPath0, hashSet0
        )
        monoid0 = Monoid()
        monoid0.identity = lambda: list0
        inMemoryPath0.addConnectionInTail(linkedList0, linkedList1, linkedList0)
        mutableSpanningTree0 = MutableSpanningTree(monoid0, None)
        linkedList0.offer(mutableSpanningTree0)

        try:
            defaultConnectivityAlgorithmsSelector0.applyingMinimumSpanningTreeAlgorithm()
            self.fail("Expecting exception: ValueError")
        except ValueError as e:
            verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test1(self) -> None:

        linked_list0 = LinkedList[Object]()
        list0 = [
            linked_list0,
            linked_list0,
            linked_list0,
            linked_list0,
            linked_list0,
            linked_list0,
            linked_list0,
            linked_list0,
            linked_list0,
        ]
        in_memory_path0 = InMemoryPath[LinkedList[Object], LinkedList[Object]](
            linked_list0, linked_list0
        )
        hash_set0 = HashSet[LinkedList[Object]](list0)
        linked_list0.offer_first(hash_set0)
        default_connectivity_algorithms_selector0 = (
            DefaultConnectivityAlgorithmsSelector[
                LinkedList[Object], LinkedList[Object]
            ](in_memory_path0, hash_set0)
        )

        with pytest.raises(StackOverflowError):
            default_connectivity_algorithms_selector0.applying_minimum_spanning_tree_algorithm()

    def test0(self) -> None:

        linkedList0 = LinkedList()
        linkedList1 = LinkedList()
        list0 = [
            linkedList0,
            linkedList0,
            linkedList0,
            linkedList1,
            linkedList1,
            linkedList1,
            linkedList1,
            linkedList0,
            linkedList0,
        ]
        object0 = Object()
        linkedList1.add(object0)
        inMemoryPath0 = InMemoryPath(linkedList1, linkedList1)
        inMemoryPath0.addConnectionInTail(linkedList0, linkedList1, linkedList1)
        hashSet0 = HashSet(list0)
        inMemoryPath0.addConnectionInTail(linkedList0, linkedList0, linkedList0)
        defaultConnectivityAlgorithmsSelector0 = DefaultConnectivityAlgorithmsSelector(
            inMemoryPath0, hashSet0
        )

        try:
            defaultConnectivityAlgorithmsSelector0.applyingMinimumSpanningTreeAlgorithm()
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            verifyException(
                "org.apache.commons.graph.visit.DefaultVisitAlgorithmsSelector", e
            )
