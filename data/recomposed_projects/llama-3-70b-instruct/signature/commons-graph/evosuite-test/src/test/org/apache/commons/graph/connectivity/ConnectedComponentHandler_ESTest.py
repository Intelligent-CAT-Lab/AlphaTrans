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
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.connectivity.ConnectedComponentHandler import *

# from src.test.org.apache.commons.graph.connectivity.ConnectedComponentHandler_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.model.InMemoryWeightedPath import *
from src.main.org.apache.commons.graph.visit.VisitState import *
from src.main.org.apache.commons.graph.weight.Monoid import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class ConnectedComponentHandler_ESTest(unittest.TestCase):

    def test4(self) -> None:

        connectedComponentHandler0 = ConnectedComponentHandler(None)

        with pytest.raises(RuntimeError):
            connectedComponentHandler0.finishVertex(connectedComponentHandler0)
            self.fail("Expecting exception: RuntimeError")

        verifyException(
            "org.apache.commons.graph.connectivity.ConnectedComponentHandler", e
        )

    def test3(self) -> None:

        linkedList0 = LinkedList[InMemoryPath[Object, Object]]()
        connectedComponentHandler0 = ConnectedComponentHandler[
            InMemoryPath[Object, Object], InMemoryPath[Object, Object]
        ](linkedList0)
        list0 = connectedComponentHandler0.onCompleted()
        self.assertEqual(0, len(list0))

    def test2(self) -> None:

        linkedList0 = LinkedList()
        connectedComponentHandler0 = ConnectedComponentHandler(linkedList0)
        list0 = [linkedList0, linkedList0, linkedList0, linkedList0, linkedList0]
        linkedList0.push(list0)

        with pytest.raises(RecursionError):
            connectedComponentHandler0.finishVertex(linkedList0)

    def test1(self) -> None:

        linkedList0 = LinkedList[Object]()
        list0 = [linkedList0, linkedList0]
        connectedComponentHandler0 = ConnectedComponentHandler[
            LinkedList[Object], Comparable[Object]
        ](list0)

        try:
            connectedComponentHandler0.finishVertex(linkedList0)
            self.fail("Expecting exception: NotImplementedError")

        except NotImplementedError as e:
            verifyException("java.util.ImmutableCollections", e)

    def test0(self) -> None:

        linkedList0 = LinkedList()
        connectedComponentHandler0 = ConnectedComponentHandler(linkedList0)
        object0 = Object()
        monoid0 = Monoid()
        monoid0.identity = lambda: None
        mapper0 = Mapper()
        inMemoryWeightedPath0 = InMemoryWeightedPath(
            object0, connectedComponentHandler0, monoid0, mapper0
        )
        connectedComponentHandler0.finishVertex(inMemoryWeightedPath0)
        list0 = connectedComponentHandler0.onCompleted()
        assert not list0, "List should not be empty"
