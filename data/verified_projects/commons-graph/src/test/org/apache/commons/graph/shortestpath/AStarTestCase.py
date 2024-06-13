# Imports Begin
from src.main.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.shortestpath.TargetSourceSelector import *
from src.main.org.apache.commons.graph.shortestpath.ShortestPathAlgorithmSelector import *
from src.main.org.apache.commons.graph.shortestpath.PathWeightedEdgesBuilder import *
from src.main.org.apache.commons.graph.shortestpath.PathSourceSelector import *
from src.main.org.apache.commons.graph.shortestpath.PathNotFoundException import *
from src.main.org.apache.commons.graph.shortestpath.HeuristicBuilder import *
from src.main.org.apache.commons.graph.shortestpath.Heuristic import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.InMemoryWeightedPath import *
from src.test.org.apache.commons.graph.model.BaseWeightedEdge import *
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.CommonsGraph import *
import unittest
import pathlib
# Imports End

class AStarTestCase(unittest.TestCase):

    def testFindShortestPathAndVerify(self) -> None:
        graph = UndirectedMutableGraph()

        start = BaseLabeledVertex("start")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        goal = BaseLabeledVertex("goal")

        graph.addVertex(start)
        graph.addVertex(a)
        graph.addVertex(b)
        graph.addVertex(c)
        graph.addVertex(d)
        graph.addVertex(e)
        graph.addVertex(goal)

        graph.addEdge(start, BaseLabeledWeightedEdge("start <-> a", 1.5), a)
        graph.addEdge(start, BaseLabeledWeightedEdge("start <-> d", 2.0), d)

        graph.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 2.0), b)
        graph.addEdge(b, BaseLabeledWeightedEdge("b <-> c", 3.0), c)
        graph.addEdge(c, BaseLabeledWeightedEdge("c <-> goal", 3.0), goal)

        graph.addEdge(d, BaseLabeledWeightedEdge("d <-> e", 3.0), e)
        graph.addEdge(e, BaseLabeledWeightedEdge("e <-> goal", 2.0), goal)

        heuristics = {
            a: 4.0,
            b: 2.0,
            c: 4.0,
            d: 4.5,
            e: 2.0,
            goal: 6.0
        }

        heuristic = HeuristicAStarTestCaseTestFindShortestPathAndVerify(heuristics)

        expected = InMemoryWeightedPath(
            start,
            goal,
            DoubleWeightBaseOperations(),
            BaseWeightedEdge
        )

        expected.addConnectionInTail(
            start,
            BaseLabeledWeightedEdge("start <-> a", 1.5),
            a
        )
        expected.addConnectionInTail(
            a,
            BaseLabeledWeightedEdge("a <-> b", 2.0),
            b
        )
        expected.addConnectionInTail(
            b,
            BaseLabeledWeightedEdge("b <-> c", 3.0),
            c
        )
        expected.addConnectionInTail(
            c,
            BaseLabeledWeightedEdge("c <-> goal", 3.0),
            goal
        )

        actual = CommonsGraph.findShortestPath(graph)\
            .whereEdgesHaveWeights(BaseWeightedEdge<())\
            .from_(start)\
            .to(goal)\
            .applyingAStar(DoubleWeightBaseOperations())\
            .withHeuristic(heuristic)

        self.assertEqual(expected, actual)


    def testNotConnectGraph(self) -> None:
        with self.assertRaises(PathNotFoundException):
            graph = UndirectedMutableGraph()

            a = BaseLabeledVertex("a")
            b = BaseLabeledVertex("b")
            graph.addVertex(a)
            graph.addVertex(b)

            heuristics = dict()

            heuristic = HeuristicAStarTestCaseTestNotConnectGraph(heuristics)

            CommonsGraph.findShortestPath(graph)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .from_(a)\
                .to(b)\
                .applyingAStar(DoubleWeightBaseOperations())\
                .withHeuristic(heuristic)


    def testNullGraph(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            CommonsGraph.findShortestPath(None)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .from_(None)\
                .to(None)\
                .applyingAStar(DoubleWeightBaseOperations())\
                .withHeuristic(None)

    
    def testNullHeuristic(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            graph = UndirectedMutableGraph()

            CommonsGraph.findShortestPath(graph)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .from_(BaseLabeledVertex("a"))\
                .to(BaseLabeledVertex("b"))\
                .applyingAStar(DoubleWeightBaseOperations())\
                .withHeuristic(None)
    
    
    def testNullMonoid(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            graph = UndirectedMutableGraph()

            a = BaseLabeledVertex("a")
            b = BaseLabeledVertex("b")
            heuristics = dict()
            heuristic = None

            try:
                graph.addVertex(a)
                graph.addVertex(b)

                heuristic = HeuristicAStarTestCaseTestNullMonoid(heuristics)
            except (TypeError, AttributeError) as e:
                self.fail(str(e))
            
            CommonsGraph.findShortestPath(graph)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .from_(a)\
                .to(b)\
                .applyingAStar(None)\
                .withHeuristic(heuristic)

    
    def testNullVertices(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            graph = UndirectedMutableGraph()

            CommonsGraph.findShortestPath(graph)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .from_(None)\
                .to(None)\
                .applyingAStar(DoubleWeightBaseOperations())\
                .withHeuristic(None)


class HeuristicAStarTestCaseTestFindShortestPathAndVerify(Heuristic):

    def applyHeuristic(self, current, goal) -> float:
        return self.heuristics[current]
    

    def __init__(self, heuristics, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.heuristics = heuristics


class HeuristicAStarTestCaseTestNotConnectGraph(Heuristic):

    def applyHeuristic(self, current, goal) -> float:
        return self.heuristics[current]
    

    def __init__(self, heuristics, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.heuristics = heuristics
    

class HeuristicAStarTestCaseTestNullMonoid(Heuristic):

    def applyHeuristic(self, current, goal) -> float:
        return self.heuristics[current]
    

    def __init__(self, heuristics, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.heuristics = heuristics





