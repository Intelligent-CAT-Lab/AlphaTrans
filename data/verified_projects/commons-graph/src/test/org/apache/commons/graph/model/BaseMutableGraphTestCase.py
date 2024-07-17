import pytest

from src.test.org.apache.commons.graph.utils.TestRunner import *
from src.test.org.apache.commons.graph.utils.MultiThreadedTestRunner import *
from src.test.org.apache.commons.graph.utils.GraphUtils import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *
from src.main.org.apache.commons.graph.MutableGraph import *
from src.main.org.apache.commons.graph.GraphException import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.CommonsGraph import *
import unittest
import threading
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import BaseLabeledVertex
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import BaseLabeledEdge


class BaseMutableGraphTestCase(unittest.TestCase):

    class GraphInsert(TestRunner):

        def __init__(self, g: MutableGraph, start: int, end: int) -> None:
            
            self.__g = g
            self.__start = start
            self.__end = end
            self.__lock = threading.Lock()

        def runTest(self) -> None:
            for i in range(self.__start, self.__end):
                v = BaseLabeledVertex(str(i))
                self.__g.addVertex(v)

            with self.__lock:
                for v1 in self.__g.getVertices0():
                    for v2 in self.__g.getVertices0():
                        if not v1.equals(v2):
                            try:
                                e = BaseLabeledEdge(f"{v1} -> {v2}")
                                self.__g.addEdge(v1, e, v2)
                            except GraphException:
                                pass
    
    
    @pytest.mark.test
    def testAddVertexAndEdge(self) -> None:
        g = UndirectedMutableGraph()
        GraphUtils.buildCompleteGraph(50, g)

        self.assertEqual(50, g.getOrder())
        self.assertEqual(1225, g.getSize())
        for v in g.getVertices0():
            self.assertEqual(49, g.getDegree(v))
        
        gDirect = DirectedMutableGraph()
        GraphUtils.buildCompleteGraph(50, gDirect)

        self.assertEqual(50, gDirect.getOrder())
        self.assertEqual(2450, gDirect.getSize())
        for v in gDirect.getVertices0():
            self.assertEqual(98, gDirect.getDegree(v))
        
        gSimple = DirectedMutableGraph()
        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        gSimple.addVertex(one)
        gSimple.addVertex(two)

        gSimple.addEdge(one, BaseLabeledEdge("1 -> 2"), two)

        self.assertEqual(2, gSimple.getOrder())
        self.assertEqual(1, gSimple.getSize())
        self.assertEqual(1, gSimple.getDegree(one))
        self.assertEqual(1, gSimple.getDegree(two))
        self.assertEqual(0, gSimple.getInDegree(one))
        self.assertEqual(1, gSimple.getInDegree(two))
        self.assertEqual(1, gSimple.getOutDegree(one))
        self.assertEqual(0, gSimple.getOutDegree(two))

        self.assertFalse(gSimple.containsEdge(BaseLabeledEdge("Not Exist Edge")))
        self.assertFalse(gSimple.containsVertex(BaseLabeledVertex("Not exist vertex")))
    
    
    @pytest.mark.test
    def testDirectedGraphRemoveEdge(self) -> None:
        g = DirectedMutableGraph()

        source = BaseLabeledVertex(str(1))
        target = BaseLabeledVertex(str(2))

        GraphUtils.buildCompleteGraph(10, g)

        e = g.getEdge(source, target)
        g.removeEdge(e)

        edge = g.getEdge(source, target)
        self.assertIsNone(edge)

    
    @pytest.mark.test
    def testDirectedGraphRemoveEdgeNotExists(self) -> None:
        with self.assertRaises(GraphException):
            g = None
            e = None
            try:
                g = DirectedMutableGraph()
                GraphUtils.buildCompleteGraph(10, g)

                e = BaseLabeledEdge("NOT EXIST")
            except GraphException as ex:
                self.fail(str(ex))

            g.removeEdge(e)
    
    
    @pytest.mark.test
    def testDirectedMultiTh(self) -> None:
        g = CommonsGraph.synchronize2(DirectedMutableGraph())

        tr1 = BaseMutableGraphTestCase.GraphInsert(g, 0, 10)
        tr2 = BaseMutableGraphTestCase.GraphInsert(g, 10, 20)
        tr3 = BaseMutableGraphTestCase.GraphInsert(g, 20, 30)
        
        trs = [tr1, tr2, tr3]
        mttr = MultiThreadedTestRunner(trs)
        mttr.runRunnables()

        self.assertEqual(30, g.getOrder())

        self.assertEqual((30 * (30 - 1)), g.getSize())

    
    @pytest.mark.test
    def testGetConnectedVertices(self) -> None:
        g = UndirectedMutableGraph()
        GraphUtils.buildCompleteGraph(10, g)

        testVertex = BaseLabeledVertex(str(1))
        connectedVertices = g.getConnectedVertices(testVertex)
        self.assertIsNotNone(connectedVertices)

        v = []
        for baseLabeledVertex in connectedVertices:
            v.append(baseLabeledVertex)
        
        self.assertEqual(9, len(v))
        self.assertFalse(testVertex in v)
    
    
    @pytest.mark.test
    def testGetConnectedVerticesNPE(self) -> None:
        with self.assertRaises(GraphException):
            g = None
            notExistsVertex = None
            try:
                g = UndirectedMutableGraph()
                GraphUtils.buildCompleteGraph(10, g)

                notExistsVertex = BaseLabeledVertex(str(1000))
            except GraphException as ex:
                self.fail(str(ex))
            g.getConnectedVertices(notExistsVertex);
    
    
    @pytest.mark.test
    def testGetConnectedVerticesOnNotConnectedGraph(self) -> None:
        g = UndirectedMutableGraph()

        for i in range(4):
            v = BaseLabeledVertex(str(i))
            g.addVertex(v)

        testVertex = BaseLabeledVertex(str(1))
        connectedVertices = g.getConnectedVertices(testVertex)
        self.assertIsNotNone(connectedVertices)

        v = []
        for baseLabeledVertex in connectedVertices:
            v.append(baseLabeledVertex)

        self.assertEqual(0, len(v))
    
    
    @pytest.mark.test
    def testGetEdge(self) -> None:
        g = UndirectedMutableGraph()
        GraphUtils.buildCompleteGraph(10, g)

        source = BaseLabeledVertex(str(1))
        target = BaseLabeledVertex(str(2))
        edge = g.getEdge(source, target)
        self.assertIsNotNone(edge)
    
    
    @pytest.mark.test
    def testGetEgdeNotExistsVertex(self) -> None:
        with self.assertRaises(GraphException):
            g = None
            source = None
            target = None
            try:
                g = UndirectedMutableGraph()
                GraphUtils.buildCompleteGraph(10, g)

                source = BaseLabeledVertex(str(100))
                target = BaseLabeledVertex(str(2))
            except GraphException as e:
                self.fail(str(e))
            
            g.getEdge(source, target)
    
    
    @pytest.mark.test
    def testGetEgdeNotExistsVertex_2(self) -> None:
        with self.assertRaises(GraphException):
            g = None
            source = None
            target = None
            try:
                g = UndirectedMutableGraph()
                GraphUtils.buildCompleteGraph(10, g)

                source = BaseLabeledVertex(str(1))
                target = BaseLabeledVertex(str(200))
            except GraphException as e:
                self.fail(str(e))
            
            g.getEdge(source, target)
    
    
    @pytest.mark.test
    def testGetNotExistsEdge(self) -> None:
        g = UndirectedMutableGraph()
        for i in range(4):
            v = BaseLabeledVertex(str(i))
            g.addVertex(v)

        source = BaseLabeledVertex(str(1))
        target = BaseLabeledVertex(str(2))
        edge = g.getEdge(source, target)
        self.assertIsNone(edge)

    
    @pytest.mark.test
    def testMultiThreadUndirectGraph(self) -> None:
        g = CommonsGraph.synchronize2(UndirectedMutableGraph())

        tr1 = BaseMutableGraphTestCase.GraphInsert(g, 0, 10)
        tr2 = BaseMutableGraphTestCase.GraphInsert(g, 10, 20)
        tr3 = BaseMutableGraphTestCase.GraphInsert(g, 20, 30)

        trs = [tr1, tr2, tr3]
        mttr = MultiThreadedTestRunner(trs)

        mttr.runRunnables()
        
        self.assertEqual(30, g.getOrder())

        self.assertEqual((30 * (30 - 1) / 2), g.getSize())
    
    
    @pytest.mark.test
    def testUndirectedGraphRemoveEdge(self) -> None:
        g = UndirectedMutableGraph()

        source = BaseLabeledVertex(str(1))
        target = BaseLabeledVertex(str(2))

        GraphUtils.buildCompleteGraph(10, g)

        e = g.getEdge(source, target)
        g.removeEdge(e)

        edge = g.getEdge(source, target)

        self.assertIsNone(edge)

    
    @pytest.mark.test
    def testUndirectedGraphRemoveEdgeNotExists(self) -> None:
        with self.assertRaises(GraphException):
            g = None
            e = None
            try:
                g = UndirectedMutableGraph()
                buildCompleteGraph(10, g)
                
                e = BaseLabeledEdge("NOT EXIST")
            except GraphException as ex:
                self.fail(str(ex))
            
            g.removeEdge(e)
