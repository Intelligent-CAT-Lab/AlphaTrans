from __future__ import annotations
import re
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
        CommonsGraph.export(self.__actual).withName(
            "DotFormatGraph"
        ).usingDotNotation().withVertexLabels(VertexLabelMapper()).withEdgeWeights(
            EdgeWeightMapper()
        ).withEdgeLabels(
            EdgeLabelMapper()
        ).to1(
            System.out
        )

    def tearDown(self) -> None:
        self.__actual = None

    def setUp(self) -> None:

        pass  # LLM could not translate this method
