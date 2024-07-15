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
from src.main.org.apache.commons.graph.SynchronizedDirectedGraph import *

# from src.test.org.apache.commons.graph.SynchronizedDirectedGraph_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class SynchronizedDirectedGraph_ESTest(unittest.TestCase):

    def test12(self) -> None:

        directedGraph0 = unittest.mock.Mock(spec=DirectedGraph)
        directedGraph0.getOutDegree.return_value = -1
        synchronizedDirectedGraph0 = SynchronizedDirectedGraph(directedGraph0)
        integer0 = -3147
        int0 = synchronizedDirectedGraph0.getOutDegree(integer0)
        self.assertEqual(-1, int0)

    def test11(self) -> None:

        directedGraph0 = unittest.mock.Mock(spec=DirectedGraph)
        directedGraph0.getInDegree.return_value = -1
        synchronizedDirectedGraph0 = SynchronizedDirectedGraph(directedGraph0)
        integer0 = -3147
        int0 = synchronizedDirectedGraph0.getInDegree(integer0)
        self.assertEqual(-1, int0)

    def test10(self) -> None:

        directedGraph0 = unittest.mock.Mock(spec=DirectedGraph)
        directedGraph0.getOutbound.return_value = None
        synchronizedDirectedGraph0 = SynchronizedDirectedGraph(directedGraph0)
        integer0 = -3147
        iterable0 = synchronizedDirectedGraph0.getOutbound(integer0)
        self.assertIsNone(iterable0)

    def test09(self) -> None:

        integer0 = -585
        synchronizedDirectedGraph0 = SynchronizedDirectedGraph(None)

        with pytest.raises(RuntimeError):
            synchronizedDirectedGraph0.getInDegree(integer0)

    def test08(self) -> None:

        synchronizedDirectedGraph0 = SynchronizedDirectedGraph(None)
        integer0 = Integer(-2476)

        try:
            synchronizedDirectedGraph0.getInbound(integer0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.SynchronizedDirectedGraph", e)

    def test07(self) -> None:

        synchronized_directed_graph0 = SynchronizedDirectedGraph(DirectedGraph())
        integer0 = Integer(0)

        try:
            synchronized_directed_graph0.getOutDegree(integer0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.SynchronizedDirectedGraph", e)

    def test06(self) -> None:

        synchronizedDirectedGraph0 = SynchronizedDirectedGraph(DirectedGraph())
        integer0 = 854

        with pytest.raises(RuntimeError):
            synchronizedDirectedGraph0.getOutbound(integer0)
            self.fail("Expecting exception: RuntimeError")

        verifyException(
            "org.apache.commons.graph.SynchronizedDirectedGraph", RuntimeError
        )

    def test05(self) -> None:

        # Create a mock DirectedGraph object
        directedGraph0 = unittest.mock.Mock(spec=DirectedGraph)

        # Set up the mock object to return 1 when getInDegree is called
        directedGraph0.getInDegree.return_value = 1

        # Create a SynchronizedDirectedGraph object with the mock DirectedGraph
        synchronizedDirectedGraph0 = SynchronizedDirectedGraph(directedGraph0)

        # Create an Integer object with value -1
        integer0 = Integer(-1)

        # Call getInDegree on the SynchronizedDirectedGraph object
        int0 = synchronizedDirectedGraph0.getInDegree(integer0)

        # Assert that the result is 1
        self.assertEqual(1, int0)

    def test04(self) -> None:

        # Create a mock DirectedGraph object
        directedGraph0 = unittest.mock.Mock(spec=DirectedGraph)

        # Set the return value of getInDegree method to 0
        directedGraph0.getInDegree.return_value = 0

        # Create a SynchronizedDirectedGraph object with the mock DirectedGraph
        synchronizedDirectedGraph0 = SynchronizedDirectedGraph(directedGraph0)

        # Create an Integer object with value -358
        integer0 = Integer(-358)

        # Call the getInDegree method on the SynchronizedDirectedGraph object
        int0 = synchronizedDirectedGraph0.getInDegree(integer0)

        # Assert that the return value is 0
        self.assertEqual(0, int0)

    def test03(self) -> None:

        # Create a mock DirectedGraph object
        directedGraph0 = unittest.mock.Mock(spec=DirectedGraph)

        # Configure the mock object to return None when getInbound is called
        directedGraph0.getInbound.return_value = None

        # Create a SynchronizedDirectedGraph object with the mock DirectedGraph
        synchronizedDirectedGraph0 = SynchronizedDirectedGraph(directedGraph0)

        # Create an Integer object
        integer0 = Integer(-1)

        # Call getInbound on the SynchronizedDirectedGraph object
        iterable0 = synchronizedDirectedGraph0.getInbound(integer0)

        # Assert that the result is None
        self.assertIsNone(iterable0)

    def test02(self) -> None:

        directedGraph0 = unittest.mock.Mock(spec=DirectedGraph)
        directedGraph0.getOutDegree.return_value = 1
        synchronizedDirectedGraph0 = SynchronizedDirectedGraph(directedGraph0)
        integer0 = -1
        int0 = synchronizedDirectedGraph0.getOutDegree(integer0)
        self.assertEqual(1, int0)

    def test01(self) -> None:

        directedGraph0 = unittest.mock.Mock(spec=DirectedGraph)
        directedGraph0.getOutDegree.return_value = 0
        synchronizedDirectedGraph0 = SynchronizedDirectedGraph(directedGraph0)
        integer0 = -358
        int0 = synchronizedDirectedGraph0.getOutDegree(integer0)
        self.assertEqual(0, int0)

    def test00(self) -> None:

        integer0 = -1
        directedGraph0 = unittest.mock.Mock(spec=DirectedGraph)
        directedGraph0.getOutbound.return_value = None
        synchronizedDirectedGraph0 = SynchronizedDirectedGraph(directedGraph0)
        iterable0 = synchronizedDirectedGraph0.getOutbound(integer0)
        self.assertIsNone(iterable0)
