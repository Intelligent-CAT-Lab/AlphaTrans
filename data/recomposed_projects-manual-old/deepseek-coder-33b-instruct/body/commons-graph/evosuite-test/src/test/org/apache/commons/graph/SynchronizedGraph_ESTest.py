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
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.MutableGraph import *
from src.main.org.apache.commons.graph.SynchronizedDirectedGraph import *
from src.main.org.apache.commons.graph.SynchronizedGraph import *

# from src.test.org.apache.commons.graph.SynchronizedGraph_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.SynchronizedMutableGraph import *
from src.main.org.apache.commons.graph.SynchronizedUndirectedGraph import *
from src.main.org.apache.commons.graph.VertexPair import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class SynchronizedGraph_ESTest(unittest.TestCase):

    def test39(self) -> None:

        directedGraph0 = unittest.mock.Mock(spec=DirectedGraph)
        directedGraph0.getVertices0.return_value = None
        synchronizedDirectedGraph0 = SynchronizedDirectedGraph(directedGraph0)
        iterable0 = synchronizedDirectedGraph0.getVertices0()
        object0 = object()
        mutableGraph0 = unittest.mock.Mock(spec=MutableGraph)
        mutableGraph0.getConnectedVertices.return_value = iterable0
        synchronizedMutableGraph0 = SynchronizedMutableGraph(mutableGraph0)
        iterable1 = synchronizedMutableGraph0.getConnectedVertices(object0)
        self.assertIsNone(iterable1)

    def test38(self) -> None:

        # Create a mock object for MutableGraph
        mutableGraph0 = unittest.mock.Mock(spec=MutableGraph)

        # Set the return value for getOrder method
        mutableGraph0.getOrder.return_value = 1

        # Create a SynchronizedMutableGraph object
        synchronizedMutableGraph0 = SynchronizedMutableGraph(mutableGraph0)

        # Call the getOrder method
        int0 = synchronizedMutableGraph0.getOrder()

        # Assert that the return value is as expected
        self.assertEqual(1, int0)

    def test37(self) -> None:

        directed_graph0 = unittest.mock.Mock(spec=DirectedGraph)
        synchronized_directed_graph0 = SynchronizedDirectedGraph(directed_graph0)
        mutable_graph0 = unittest.mock.Mock(spec=MutableGraph)
        mutable_graph0.contains_vertex.return_value = False
        synchronized_mutable_graph0 = SynchronizedMutableGraph(mutable_graph0)
        boolean0 = synchronized_mutable_graph0.contains_vertex(
            synchronized_directed_graph0
        )
        self.assertFalse(boolean0)

    def test36(self) -> None:

        # Create a mock object for MutableGraph
        mutableGraph0 = unittest.mock.Mock(spec=MutableGraph)

        # Create a SynchronizedMutableGraph object using the mock MutableGraph
        synchronizedMutableGraph0 = SynchronizedMutableGraph(mutableGraph0)

        # Call the toString method of the SynchronizedMutableGraph
        string0 = synchronizedMutableGraph0.toString()

        # Assert that the result is not None
        self.assertIsNotNone(string0)

    def test35(self) -> None:

        # Create a mock object for MutableGraph
        mutableGraph0 = unittest.mock.Mock(spec=MutableGraph)
        mutableGraph0.getSize.return_value = 4432

        # Create a SynchronizedMutableGraph object
        synchronizedMutableGraph0 = SynchronizedMutableGraph(mutableGraph0)

        # Create a SynchronizedUndirectedGraph object
        synchronizedUndirectedGraph0 = SynchronizedUndirectedGraph(
            synchronizedMutableGraph0
        )

        # Get the size of the graph
        int0 = synchronizedUndirectedGraph0.getSize()

        # Assert that the size is equal to 4432
        self.assertEqual(4432, int0)

    def test34(self) -> None:

        # Mocking DirectedGraph
        directedGraph0 = unittest.mock.Mock(spec=DirectedGraph)
        directedGraph0.return_value = ViolatedAssumptionAnswer()

        # Mocking MutableGraph
        mutableGraph0 = unittest.mock.Mock(spec=MutableGraph)
        mutableGraph0.getDegree.return_value = 4432

        # Creating instances
        synchronizedDirectedGraph0 = SynchronizedDirectedGraph(directedGraph0)
        synchronizedUndirectedGraph0 = SynchronizedUndirectedGraph(
            synchronizedDirectedGraph0
        )
        synchronizedMutableGraph0 = SynchronizedMutableGraph(mutableGraph0)

        # Calling method
        int0 = synchronizedMutableGraph0.getDegree(synchronizedUndirectedGraph0)

        # Asserting result
        self.assertEqual(4432, int0)

    def test33(self) -> None:

        # Create a mock object for MutableGraph
        mutable_graph0 = unittest.mock.Mock(spec=MutableGraph)
        # Create a SynchronizedMutableGraph object using the mock object
        synchronized_mutable_graph0 = SynchronizedMutableGraph(mutable_graph0)

        # Create a mock object for DirectedGraph
        directed_graph0 = unittest.mock.Mock(spec=DirectedGraph)
        # Set the return value of getVertices1 method to None
        directed_graph0.getVertices1.return_value = None
        # Create a SynchronizedDirectedGraph object using the mock object
        synchronized_directed_graph0 = SynchronizedDirectedGraph(directed_graph0)

        # Call the getVertices1 method with synchronizedMutableGraph0 as argument
        vertex_pair0 = synchronized_directed_graph0.getVertices1(
            synchronized_mutable_graph0
        )

        # Assert that vertex_pair0 is None
        self.assertIsNone(vertex_pair0)

    def test32(self) -> None:

        mutableGraph0 = unittest.mock.Mock(spec=MutableGraph)
        mutableGraph0.containsEdge.return_value = False
        synchronizedMutableGraph0 = SynchronizedMutableGraph(mutableGraph0)

        mutableGraph1 = unittest.mock.Mock(spec=MutableGraph)
        synchronizedMutableGraph1 = SynchronizedMutableGraph(mutableGraph1)

        synchronizedUndirectedGraph0 = SynchronizedUndirectedGraph(
            synchronizedMutableGraph1
        )

        boolean0 = synchronizedMutableGraph0.containsEdge(synchronizedUndirectedGraph0)

        self.assertFalse(boolean0)

    def test31(self) -> None:

        directedGraph0 = mock(DirectedGraph, new=ViolatedAssumptionAnswer())
        synchronizedDirectedGraph0 = SynchronizedDirectedGraph(directedGraph0)
        synchronizedUndirectedGraph0 = SynchronizedUndirectedGraph(
            synchronizedDirectedGraph0
        )
        directedGraph1 = mock(DirectedGraph, new=ViolatedAssumptionAnswer())
        doReturn(synchronizedDirectedGraph0).when(directedGraph1).getEdge(any(), any())
        synchronizedDirectedGraph1 = SynchronizedDirectedGraph(directedGraph1)
        synchronizedMutableGraph0 = SynchronizedMutableGraph(None)
        synchronizedGraph0 = synchronizedDirectedGraph1.getEdge(
            synchronizedMutableGraph0, synchronizedUndirectedGraph0
        )
        self.assertEqual(0, synchronizedGraph0.getSize())

    def test30(self) -> None:

        # Create a mock object for MutableGraph
        mutableGraph0 = unittest.mock.Mock(spec=MutableGraph)

        # Create a SynchronizedMutableGraph object
        synchronizedMutableGraph0 = SynchronizedMutableGraph(mutableGraph0)

        # Create a SynchronizedUndirectedGraph object
        synchronizedUndirectedGraph0 = SynchronizedUndirectedGraph(
            synchronizedMutableGraph0
        )

        # Create an object
        object0 = object()

        # Check if the SynchronizedUndirectedGraph is equal to the object
        boolean0 = synchronizedUndirectedGraph0.equals(object0)

        # Assert that the result is False
        self.assertFalse(boolean0)

    def test29(self) -> None:

        # Create a mock DirectedGraph object
        directedGraph0 = mock(DirectedGraph, new=ViolatedAssumptionAnswer)

        # Create a SynchronizedDirectedGraph object
        synchronizedDirectedGraph0 = SynchronizedDirectedGraph(directedGraph0)

        # Create a SynchronizedUndirectedGraph object
        synchronizedUndirectedGraph0 = SynchronizedUndirectedGraph(
            synchronizedDirectedGraph0
        )

        # Check if the SynchronizedUndirectedGraph object is equal to itself
        boolean0 = synchronizedUndirectedGraph0.equals(synchronizedUndirectedGraph0)

        # Assert that the boolean0 is True
        assert boolean0

    def test28(self) -> None:

        synchronizedMutableGraph0 = SynchronizedMutableGraph(None)
        boolean0 = synchronizedMutableGraph0.equals(None)
        self.assertFalse(boolean0)

    def test26(self) -> None:

        # Create a mock DirectedGraph object
        directedGraph0 = mock(DirectedGraph, new=ViolatedAssumptionAnswer)

        # Create a SynchronizedDirectedGraph object with the mock DirectedGraph
        synchronizedDirectedGraph0 = SynchronizedDirectedGraph(directedGraph0)

        # Call the hashCode method on the SynchronizedDirectedGraph
        synchronizedDirectedGraph0.hashCode()

    def test25(self) -> None:

        synchronizedMutableGraph0 = SynchronizedMutableGraph(None)
        synchronizedMutableGraph0.hashCode()

    def test24(self) -> None:

        synchronizedGraph0 = SynchronizedGraph(None)
        synchronizedUndirectedGraph0 = SynchronizedUndirectedGraph(synchronizedGraph0)

        try:
            synchronizedUndirectedGraph0.containsEdge(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.SynchronizedGraph", e)

    def test23(self) -> None:

        synchronizedMutableGraph0 = SynchronizedMutableGraph(None)
        synchronizedUndirectedGraph0 = SynchronizedUndirectedGraph(
            synchronizedMutableGraph0
        )

        with pytest.raises(RuntimeError):
            synchronizedUndirectedGraph0.containsVertex(synchronizedUndirectedGraph0)
            self.fail("Expecting exception: RuntimeError")

        verifyException("org.apache.commons.graph.SynchronizedGraph", RuntimeError)

    def test22(self) -> None:

        synchronizedUndirectedGraph0 = SynchronizedUndirectedGraph(None)

        with pytest.raises(RuntimeError):
            synchronizedUndirectedGraph0.getConnectedVertices(None)
            self.fail("Expecting exception: RuntimeError")

        verifyException("org.apache.commons.graph.SynchronizedGraph", RuntimeError)

    def test21(self) -> None:

        synchronizedUndirectedGraph0 = SynchronizedUndirectedGraph(None)

        with pytest.raises(RuntimeError):
            synchronizedUndirectedGraph0.getDegree(None)

    def test20(self) -> None:

        synchronizedDirectedGraph0 = SynchronizedDirectedGraph(None)

        try:
            synchronizedDirectedGraph0.getEdges()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.SynchronizedGraph", e)

    def test19(self) -> None:

        synchronizedUndirectedGraph0 = SynchronizedUndirectedGraph(None)

        try:
            synchronizedUndirectedGraph0.getOrder()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.SynchronizedGraph", e)

    def test18(self) -> None:

        synchronized_graph0 = SynchronizedGraph(None)

        try:
            synchronized_graph0.get_size()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.SynchronizedGraph", e)

    def test17(self) -> None:

        synchronizedMutableGraph0 = SynchronizedMutableGraph(None)

        try:
            synchronizedMutableGraph0.getVertices0()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.SynchronizedGraph", e)

    def test16(self) -> None:

        directedGraph0 = mock(DirectedGraph, new=ViolatedAssumptionAnswer())
        synchronizedDirectedGraph0 = SynchronizedDirectedGraph(directedGraph0)
        synchronizedUndirectedGraph0 = SynchronizedUndirectedGraph(None)

        try:
            synchronizedUndirectedGraph0.getVertices1(synchronizedDirectedGraph0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.SynchronizedGraph", e)

    def test15(self) -> None:

        synchronizedMutableGraph0 = SynchronizedMutableGraph(None)

        try:
            synchronizedMutableGraph0.toString()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.evosuite.runtime.System", e)

    def test14(self) -> None:

        directedGraph0 = unittest.mock.Mock(spec=DirectedGraph)
        directedGraph0.containsEdge.return_value = True
        synchronizedDirectedGraph0 = SynchronizedDirectedGraph(directedGraph0)

        mutableGraph0 = unittest.mock.Mock(spec=MutableGraph)
        synchronizedMutableGraph0 = SynchronizedMutableGraph(mutableGraph0)

        boolean0 = synchronizedDirectedGraph0.containsEdge(synchronizedMutableGraph0)
        self.assertTrue(boolean0)

    def test13(self) -> None:

        # Create a mock object for MutableGraph
        mutableGraph0 = unittest.mock.Mock(spec=MutableGraph)
        mutableGraph0.containsVertex.return_value = True

        # Create SynchronizedMutableGraph and SynchronizedUndirectedGraph
        synchronizedMutableGraph0 = SynchronizedMutableGraph(mutableGraph0)
        synchronizedUndirectedGraph0 = SynchronizedUndirectedGraph(
            synchronizedMutableGraph0
        )

        # Create an object
        object0 = object()

        # Call containsVertex method
        boolean0 = synchronizedUndirectedGraph0.containsVertex(object0)

        # Assert that the result is True
        self.assertTrue(boolean0)

    def test12(self) -> None:

        # Create a mock object for MutableGraph
        mutableGraph0 = unittest.mock.Mock(spec=MutableGraph)

        # Set up the mock object to return None when getConnectedVertices is called
        mutableGraph0.getConnectedVertices.return_value = None

        # Create a SynchronizedMutableGraph object with the mock MutableGraph
        synchronizedMutableGraph0 = SynchronizedMutableGraph(mutableGraph0)

        # Call getConnectedVertices on the SynchronizedMutableGraph object
        iterable0 = synchronizedMutableGraph0.getConnectedVertices(None)

        # Assert that the result is None
        self.assertIsNone(iterable0)

    def test11(self) -> None:

        # Mocking the DirectedGraph
        directedGraph0 = unittest.mock.Mock(spec=DirectedGraph)
        directedGraph0.getDegree.return_value = -935

        # Creating SynchronizedDirectedGraph
        synchronizedDirectedGraph0 = SynchronizedDirectedGraph(directedGraph0)

        # Creating SynchronizedUndirectedGraph
        synchronizedUndirectedGraph0 = SynchronizedUndirectedGraph(
            synchronizedDirectedGraph0
        )

        # Getting the degree
        int0 = synchronizedUndirectedGraph0.getDegree(synchronizedDirectedGraph0)

        # Asserting the degree
        self.assertEqual(-935, int0)

    def test10(self) -> None:

        # Mocking the DirectedGraph
        directedGraph0 = unittest.mock.Mock(spec=DirectedGraph)
        directedGraph0.getDegree.return_value = 0

        # Creating a SynchronizedDirectedGraph
        synchronizedDirectedGraph0 = SynchronizedDirectedGraph(directedGraph0)

        # Creating a SynchronizedUndirectedGraph
        synchronizedUndirectedGraph0 = SynchronizedUndirectedGraph(
            synchronizedDirectedGraph0
        )

        # Getting the degree
        int0 = synchronizedUndirectedGraph0.getDegree(synchronizedDirectedGraph0)

        # Asserting the degree
        self.assertEqual(0, int0)

    def test09(self) -> None:

        directedGraph0 = unittest.mock.Mock(spec=DirectedGraph)
        directedGraph0.getEdge.return_value = None
        synchronizedDirectedGraph0 = SynchronizedDirectedGraph(directedGraph0)

        directedGraph1 = unittest.mock.Mock(spec=DirectedGraph)
        synchronizedDirectedGraph1 = SynchronizedDirectedGraph(directedGraph1)

        object0 = synchronizedDirectedGraph0.getEdge(
            synchronizedDirectedGraph1, synchronizedDirectedGraph1
        )
        self.assertIsNone(object0)

    def test08(self) -> None:

        mutableGraph0 = unittest.mock.Mock(spec=MutableGraph)
        mutableGraph0.return_value = None
        synchronizedMutableGraph0 = SynchronizedMutableGraph(mutableGraph0)

        directedGraph0 = unittest.mock.Mock(spec=DirectedGraph)
        directedGraph0.getEdges.return_value = None
        synchronizedDirectedGraph0 = SynchronizedDirectedGraph(directedGraph0)

        iterable0 = synchronizedDirectedGraph0.getEdges()

        mutableGraph1 = unittest.mock.Mock(spec=MutableGraph)
        mutableGraph1.getEdges.return_value = iterable0
        synchronizedMutableGraph1 = SynchronizedMutableGraph(mutableGraph1)

        iterable1 = synchronizedMutableGraph1.getEdges()

        self.assertIsNone(iterable1)

    def test07(self) -> None:

        # Create a mock object for MutableGraph
        mutableGraph0 = unittest.mock.Mock(spec=MutableGraph)

        # Set the return value of getEdges() method to None
        mutableGraph0.getEdges.return_value = None

        # Create a SynchronizedMutableGraph object
        synchronizedMutableGraph0 = SynchronizedMutableGraph(mutableGraph0)

        # Call the getEdges() method
        iterable0 = synchronizedMutableGraph0.getEdges()

        # Assert that the return value is None
        self.assertIsNone(iterable0)

    def test06(self) -> None:

        # Create a mock DirectedGraph object
        directedGraph0 = unittest.mock.Mock(spec=DirectedGraph)
        directedGraph0.getOrder.return_value = -935

        # Create a SynchronizedDirectedGraph object
        synchronizedDirectedGraph0 = SynchronizedDirectedGraph(directedGraph0)

        # Create a SynchronizedUndirectedGraph object
        synchronizedUndirectedGraph0 = SynchronizedUndirectedGraph(
            synchronizedDirectedGraph0
        )

        # Get the order from the SynchronizedUndirectedGraph object
        int0 = synchronizedUndirectedGraph0.getOrder()

        # Assert that the order is -935
        self.assertEqual(-935, int0)

    def test05(self) -> None:

        # Create a mock object for MutableGraph
        mutableGraph0 = unittest.mock.Mock(spec=MutableGraph)

        # Set the return value of getOrder method to 0
        mutableGraph0.getOrder.return_value = 0

        # Create a SynchronizedMutableGraph object
        synchronizedMutableGraph0 = SynchronizedMutableGraph(mutableGraph0)

        # Call the getOrder method
        int0 = synchronizedMutableGraph0.getOrder()

        # Assert that the return value is 0
        self.assertEqual(0, int0)

    def test04(self) -> None:

        # Create a mock DirectedGraph object
        directedGraph0 = unittest.mock.Mock(spec=DirectedGraph)

        # Set the return value of getSize() method to -1
        directedGraph0.getSize.return_value = -1

        # Create a SynchronizedDirectedGraph object with the mock DirectedGraph
        synchronizedDirectedGraph0 = SynchronizedDirectedGraph(directedGraph0)

        # Call the getSize() method on the SynchronizedDirectedGraph object
        int0 = synchronizedDirectedGraph0.getSize()

        # Assert that the return value is -1
        self.assertEqual(-1, int0)

    def test03(self) -> None:

        # Create a mock DirectedGraph object
        directedGraph0 = unittest.mock.Mock(spec=DirectedGraph)

        # Set the return value of getSize() method to 0
        directedGraph0.getSize.return_value = 0

        # Create a SynchronizedDirectedGraph object with the mock DirectedGraph
        synchronizedDirectedGraph0 = SynchronizedDirectedGraph(directedGraph0)

        # Call the getSize() method on the SynchronizedDirectedGraph object
        int0 = synchronizedDirectedGraph0.getSize()

        # Assert that the return value is 0
        self.assertEqual(0, int0)

    def test02(self) -> None:

        mutableGraph0 = unittest.mock.Mock(spec=MutableGraph)
        mutableGraph0.return_value = None
        synchronizedMutableGraph0 = SynchronizedMutableGraph(mutableGraph0)

        directedGraph0 = unittest.mock.Mock(spec=DirectedGraph)
        directedGraph0.getEdges.return_value = None
        synchronizedDirectedGraph0 = SynchronizedDirectedGraph(directedGraph0)

        iterable0 = synchronizedDirectedGraph0.getEdges()

        mutableGraph1 = unittest.mock.Mock(spec=MutableGraph)
        mutableGraph1.getVertices0.return_value = iterable0
        synchronizedMutableGraph1 = SynchronizedMutableGraph(mutableGraph1)

        synchronizedUndirectedGraph0 = SynchronizedUndirectedGraph(
            synchronizedMutableGraph1
        )

        iterable1 = synchronizedUndirectedGraph0.getVertices0()

        self.assertIsNone(iterable1)

    def test01(self) -> None:

        # Create a mock object for MutableGraph
        mutableGraph0 = unittest.mock.Mock(spec=MutableGraph)

        # Set the return value of getVertices0() to None
        mutableGraph0.getVertices0.return_value = None

        # Create a SynchronizedMutableGraph object
        synchronizedMutableGraph0 = SynchronizedMutableGraph(mutableGraph0)

        # Call getVertices0() on the SynchronizedMutableGraph object
        iterable0 = synchronizedMutableGraph0.getVertices0()

        # Assert that the return value is None
        self.assertIsNone(iterable0)

    def test00(self) -> None:

        vertexPair0 = unittest.mock.Mock(spec=VertexPair)
        vertexPair0.toString.return_value = None
        mutableGraph0 = unittest.mock.Mock(spec=MutableGraph)
        mutableGraph0.getVertices1.return_value = vertexPair0
        synchronizedMutableGraph0 = SynchronizedMutableGraph(mutableGraph0)
        mutableGraph1 = unittest.mock.Mock(spec=MutableGraph)
        synchronizedMutableGraph1 = SynchronizedMutableGraph(mutableGraph1)
        vertexPair1 = synchronizedMutableGraph0.getVertices1(synchronizedMutableGraph1)
        self.assertIs(vertexPair1, vertexPair0)
