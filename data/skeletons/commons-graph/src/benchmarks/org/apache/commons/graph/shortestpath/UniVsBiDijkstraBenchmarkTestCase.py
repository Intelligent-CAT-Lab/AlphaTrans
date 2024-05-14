# Imports Begin
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.GraphException import *
from src.main.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.shortestpath.TargetSourceSelector import *
from src.main.org.apache.commons.graph.shortestpath.ShortestPathAlgorithmSelector import *
from src.main.org.apache.commons.graph.shortestpath.PathWeightedEdgesBuilder import *
from src.main.org.apache.commons.graph.shortestpath.PathSourceSelector import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.BaseWeightedEdge import *
from src.main.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.main.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.CommonsGraph import *
import typing

# Imports End


class UniVsBiDijkstraBenchmarkTestCase:

    # Class Fields Begin
    __NODES: int = None
    __EDGES: int = None
    __graph: DirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[float]] = (
        None
    )
    __weightedEdges: Mapper[BaseLabeledWeightedEdge[float], float] = None
    __sourceListUni: typing.List[BaseLabeledVertex] = None
    __sourceListBi: typing.List[BaseLabeledVertex] = None
    __targetListUni: typing.List[BaseLabeledVertex] = None
    __targetListBi: typing.List[BaseLabeledVertex] = None
    __vertices: typing.List[BaseLabeledVertex] = None
    __weightOperations: OrderedMonoid[float] = None
    # Class Fields End

    # Class Methods Begin
    def testPerformUnidirectionalDijkstra(self) -> None:
        pass

    def testPerformBidirectionalDijkstra(self) -> None:
        pass

    @staticmethod
    def setUp() -> None:
        pass

    # Class Methods End


class Mapper:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def map(self, input: BaseLabeledWeightedEdge[float]) -> float:
        pass

    # Class Methods End


class AbstractGraphConnection:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def connect0(self) -> None:
        pass

    def __addEdge(self, src: BaseLabeledVertex, dst: BaseLabeledVertex) -> bool:
        pass

    # Class Methods End
