from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.GraphException import *
from src.main.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.spanning.SpanningWeightedEdgeMapperBuilder import *
from src.main.org.apache.commons.graph.spanning.SpanningTreeSourceSelector import *
from src.main.org.apache.commons.graph.spanning.SpanningTreeAlgorithmSelector import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.SpanningTree import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.CommonsGraph import *
import io

# Imports End


class MinimumSpanningTreeBenchmarkTestCase:

    # Class Fields Begin
    __NODES: int = None
    __EDGES: int = None
    __graph: UndirectedMutableGraph[
        BaseLabeledVertex, BaseLabeledWeightedEdge[float]
    ] = None
    __weightedEdges: Mapper[BaseLabeledWeightedEdge[float], float] = None
    # Class Fields End

    # Class Methods Begin
    def testPerformPrim(self) -> None:
        pass

    def testPerformKruskal(self) -> None:
        pass

    def testPerformBoruvka(self) -> None:
        pass

    @staticmethod
    def setUp() -> None:
        pass

    # Class Methods End
