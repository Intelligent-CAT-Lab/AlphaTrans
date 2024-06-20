import pytest

from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.export.NamedExportSelector import *
from src.main.org.apache.commons.graph.export.ExportSelector import *
from src.main.org.apache.commons.graph.export.DotExporter import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.CommonsGraph import *

from src.test.org.apache.commons.graph.export.VertexLabelMapper import VertexLabelMapper
from src.test.org.apache.commons.graph.export.EdgeLabelMapper import EdgeLabelMapper
from src.test.org.apache.commons.graph.export.EdgeWeightMapper import EdgeWeightMapper
import unittest
import sys

class ExportTestCase(unittest.TestCase):

    
    __actual = None
    
    
    def setUp(self) -> None:
        self.__actual = CommonsGraph.newUndirectedMutableGraph(
            GraphConnectionExportTestShouldPrintDotFormat()
        )
    

    def tearDown(self) -> None:
        self.__actual = None


    @pytest.mark.test
    def testShouldPrintDotFormat(self) -> None:
        CommonsGraph.export(self.__actual)\
            .withName("DotFormatGraph")\
            .usingDotNotation()\
            .withVertexLabels(VertexLabelMapper())\
            .withEdgeWeights(EdgeWeightMapper())\
            .withEdgeLabels(EdgeLabelMapper())\
            .to1(sys.stdout)



class GraphConnectionExportTestShouldPrintDotFormat(AbstractGraphConnection):

    def connect0(self) -> None:
        start = self.addVertex(BaseLabeledVertex("start"))
        a = self.addVertex(BaseLabeledVertex("a"))
        b = self.addVertex(BaseLabeledVertex("b"))
        goal = self.addVertex(BaseLabeledVertex("goal"))

        self.addEdge(BaseLabeledWeightedEdge("start <-> a", 1.5))\
            .from_(start)\
            .to(a)
        self.addEdge(BaseLabeledWeightedEdge("a <-> b", 2.0))\
            .from_(a)\
            .to(b)
        self.addEdge(BaseLabeledWeightedEdge("a <-> goal", 2.0))\
            .from_(a)\
            .to(goal)
        self.addEdge(BaseLabeledWeightedEdge("b <-> goal", 2.0))\
            .from_(b)\
            .to(goal)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
