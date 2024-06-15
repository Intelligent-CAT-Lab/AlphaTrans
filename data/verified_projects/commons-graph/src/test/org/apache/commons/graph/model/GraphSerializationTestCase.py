# Imports Begin
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.MutableSpanningTree import *
from src.main.org.apache.commons.graph.model.InMemoryWeightedPath import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.test.org.apache.commons.graph.model.BaseWeightedEdge import *
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *
from src.main.org.apache.commons.graph.builder.LinkedConnectionBuilder import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.MutableGraph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.CommonsGraph import *
import unittest
import pickle
from typing import *
import os
# Imports End

class GraphSerializationTestCase(unittest.TestCase):

    # Class Fields Begin
    __FILE_NAME: str = "target/serializedGraph.dat"
    # Class Fields End

    # Class Methods Begin

    @staticmethod
    def __buildGraphConnections() -> GraphConnection:
        return GraphConnectionGraphSerializationTestCaseBuildGraphConnections()
    

    @staticmethod
    def __buildWeightedGraphConnections() -> GraphConnection:
        return GraphConnectionGraphSerializationTestCaseBuildWeightedGraphConnections()
    

    @staticmethod
    def __checkSerialization(g: Graph) -> None:
        try:
            with open(GraphSerializationTestCase.__FILE_NAME, "wb") as fout:
                pickle.dump(g, fout)

            with open(GraphSerializationTestCase.__FILE_NAME, "rb") as fin:
                cloned = pickle.load(fin)

            GraphSerializationTestCase.assertEqual(g, cloned)

        except (FileNotFoundError, IOError, OSError, ModuleNotFoundError, ImportError) as e:
            # Fail the test case with the appropriate error message
            GraphSerializationTestCase.fail(f"An exception occurred: {e}")
    

    def tearDown(self) -> None:
        f = GraphSerializationTestCase.__FILE_NAME
        if os.path.exists(f):
            os.remove(f)

    
    def testSerializeDirectedGraph(self) -> None:
        try:
            g = CommonsGraph.newDirectedMutableGraph(GraphSerializationTestCase\
                .__buildGraphConnections())
            GraphSerializationTestCase.__checkSerialization(g)
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    def testSerializeDirectedWeightdGraph(self) -> None:
        try:
            g = CommonsGraph.newDirectedMutableGraph(GraphSerializationTestCase\
                .__buildWeightedGraphConnections())
            GraphSerializationTestCase.__checkSerialization(g)
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    def testSerializePath(self) -> None:
        try:
            start = BaseLabeledVertex("start")
            goal = BaseLabeledVertex("goal")
            a = BaseLabeledVertex("a")
            b = BaseLabeledVertex("b")
            c = BaseLabeledVertex("c")

            g = InMemoryWeightedPath(
                start,
                goal,
                DoubleWeightBaseOperations(),
                BaseWeightedEdge()
            )

            g.addConnectionInTail(start, BaseLabeledWeightedEdge("start <-> a", 1.5), a)
            g.addConnectionInTail(a, BaseLabeledWeightedEdge("a <-> b", 2), b)
            g.addConnectionInTail(b, BaseLabeledWeightedEdge("b <-> c", 3), c)
            g.addConnectionInTail(c, BaseLabeledWeightedEdge("c <-> goal", 3), goal)

            GraphSerializationTestCase.__checkSerialization(g)
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    def testSerializeSpanningTree(self) -> None:
        try:
            spanningTree = MutableSpanningTree(
                DoubleWeightBaseOperations(), BaseWeightedEdge()
            )

            CommonsGraph.populate(spanningTree)\
                .withConnections(GraphSerializationTestCase.__buildWeightedGraphConnections())
            
            GraphSerializationTestCase.__checkSerialization(spanningTree)
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    def testSerializeSyncronyzedDirectedWeightdGraph(self) -> None:
        try:
            g = CommonsGraph.synchronize2(
                CommonsGraph.newDirectedMutableGraph(GraphSerializationTestCase\
                    .__buildWeightedGraphConnections())
            )

            GraphSerializationTestCase.__checkSerialization(g)
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    def testSerializeUndirectedGraph(self) -> None:
        try:
            g = CommonsGraph.newUndirectedMutableGraph(GraphSerializationTestCase\
                .__buildGraphConnections())
            
            GraphSerializationTestCase.__checkSerialization(g)
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    def testSerializeUndirectedWeightdGraph(self) -> None:
        try:
            g = CommonsGraph.newUndirectedMutableGraph(GraphSerializationTestCase\
                .__buildWeightedGraphConnections())
            
            GraphSerializationTestCase.__checkSerialization(g)
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    # Class Methods End


class GraphConnectionGraphSerializationTestCaseBuildGraphConnections(AbstractGraphConnection):

    def connect0(self) -> None:
        a = self.addVertex(BaseLabeledVertex("a"))
        b = self.addVertex(BaseLabeledVertex("b"))
        c = self.addVertex(BaseLabeledVertex("c"))
        d = self.addVertex(BaseLabeledVertex("d"))

        self.addEdge(BaseLabeledEdge("a -> c")).from_(a).to(c)
        self.addEdge(BaseLabeledEdge("c -> d")).from_(c).to(d)
        self.addEdge(BaseLabeledEdge("d -> b")).from_(d).to(b)
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class GraphConnectionGraphSerializationTestCaseBuildWeightedGraphConnections(AbstractGraphConnection):

    def connect0(self) -> None:
        a = self.addVertex(BaseLabeledVertex("a"))
        b = self.addVertex(BaseLabeledVertex("b"))
        c = self.addVertex(BaseLabeledVertex("c"))
        d = self.addVertex(BaseLabeledVertex("d"))

        self.addEdge(BaseLabeledWeightedEdge("a -> c", 1.0)).from_(a).to(c)
        self.addEdge(BaseLabeledWeightedEdge("c -> d", 1.0)).from_(c).to(d)
        self.addEdge(BaseLabeledWeightedEdge("d -> b", 1.0)).from_(d).to(b)
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
