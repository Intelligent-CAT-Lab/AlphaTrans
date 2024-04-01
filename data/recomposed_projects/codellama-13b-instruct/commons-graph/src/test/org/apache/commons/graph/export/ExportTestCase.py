# Imports Begin
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.main.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.export.VertexLabelMapper import *
from src.main.org.apache.commons.graph.export.NamedExportSelector import *
from src.main.org.apache.commons.graph.export.ExportSelector import *
from src.main.org.apache.commons.graph.export.EdgeWeightMapper import *
from src.main.org.apache.commons.graph.export.EdgeLabelMapper import *
from src.main.org.apache.commons.graph.export.DotExporter import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.CommonsGraph import *
import unittest
import sys
# Imports End

class ExportTestCase(unittest.TestCase):

    # Class Fields Begin
    __actual: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[float]] = None
    # Class Fields End

    # Class Methods Begin
    def testShouldPrintDotFormat(self) -> None:

            self.export(self.__actual) \
                .withName("DotFormatGraph") \
                .usingDotNotation() \
                .withVertexLabels(VertexLabelMapper()) \
                .withEdgeWeights(EdgeWeightMapper()) \
                .withEdgeLabels(EdgeLabelMapper()) \
                .to1(sys.stdout)

    def tearDown(self) -> None:

            self.__actual = None

    def setUp(self) -> None:

            self.__actual = self.newUndirectedMutableGraph(
                GraphConnection[BaseLabeledVertex, BaseLabeledWeightedEdge[Double]]()
            )
            self.__actual.connect0()

    # Class Methods End


class new AbstractGraphConnection<BaseLabeledVertex,BaseLabeledWeightedEdge<Double>>(...) { ... }(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def connect0(self) -> None:

        start = self.addVertex(BaseLabeledVertex("start"))
        a = self.addVertex(BaseLabeledVertex("a"))
        b = self.addVertex(BaseLabeledVertex("b"))
        goal = self.addVertex(BaseLabeledVertex("goal"))
        self.addEdge(BaseLabeledWeightedEdge("start <-> a", 1.5)) \
            .from_(start) \
            .to(a)
        self.addEdge(BaseLabeledWeightedEdge("a <-> b", 2.0)) \
            .from_(a) \
            .to(b)
        self.addEdge(BaseLabeledWeightedEdge("a <-> goal", 2.0)) \
            .from_(a) \
            .to(goal)
        self.addEdge(BaseLabeledWeightedEdge("b <-> goal", 2.0)) \
            .from_(b) \
            .to(goal)

    def (self) -> None:


        pass # LLM could not translate method body

    # Class Methods End


