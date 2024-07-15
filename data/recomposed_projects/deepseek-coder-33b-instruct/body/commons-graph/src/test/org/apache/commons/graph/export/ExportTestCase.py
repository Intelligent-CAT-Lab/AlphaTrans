from __future__ import annotations
import re
from io import StringIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.export.DotExporter import *
from src.test.org.apache.commons.graph.export.EdgeLabelMapper import *
from src.test.org.apache.commons.graph.export.EdgeWeightMapper import *
from src.main.org.apache.commons.graph.export.ExportSelector import *
from src.main.org.apache.commons.graph.export.NamedExportSelector import *
from src.test.org.apache.commons.graph.export.VertexLabelMapper import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *


class ExportTestCase(unittest.TestCase):

    __actual: UndirectedMutableGraph[
        BaseLabeledVertex, BaseLabeledWeightedEdge[float]
    ] = None

    def testShouldPrintDotFormat(self) -> None:

        # Create a StringIO object to capture the output
        output = io.StringIO()

        # Call the export method
        CommonsGraph.export(self.__actual).withName(
            "DotFormatGraph"
        ).usingDotNotation().withVertexLabels(VertexLabelMapper()).withEdgeWeights(
            EdgeWeightMapper()
        ).withEdgeLabels(
            EdgeLabelMapper()
        ).to1(
            output
        )

        # Get the captured output
        captured_output = output.getvalue()

        # Print the captured output
        print(captured_output)

    def tearDown(self) -> None:
        self.__actual = None

    def setUp(self) -> None:

        self.__actual = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledWeightedEdge[float]]()
            .addVertex(BaseLabeledVertex("start"))
            .addVertex(BaseLabeledVertex("a"))
            .addVertex(BaseLabeledVertex("b"))
            .addVertex(BaseLabeledVertex("goal"))
            .addEdge(BaseLabeledWeightedEdge[float]("start <-> a", 1.5))
            .from_(self.__actual.getVertex("start"))
            .to(self.__actual.getVertex("a"))
            .addEdge(BaseLabeledWeightedEdge[float]("a <-> b", 2))
            .from_(self.__actual.getVertex("a"))
            .to(self.__actual.getVertex("b"))
            .addEdge(BaseLabeledWeightedEdge[float]("a <-> goal", 2))
            .from_(self.__actual.getVertex("a"))
            .to(self.__actual.getVertex("goal"))
            .addEdge(BaseLabeledWeightedEdge[float]("b <-> goal", 2))
            .from_(self.__actual.getVertex("b"))
            .to(self.__actual.getVertex("goal"))
        )
