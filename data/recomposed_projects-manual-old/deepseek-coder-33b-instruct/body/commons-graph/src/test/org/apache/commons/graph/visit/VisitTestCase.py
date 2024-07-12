from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.visit.GraphVisitHandler import *
from src.test.org.apache.commons.graph.visit.NodeSequenceVisitor import *
from src.main.org.apache.commons.graph.visit.VisitAlgorithmsSelector import *
from src.main.org.apache.commons.graph.visit.VisitSourceSelector import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *


class VisitTestCase(unittest.TestCase):

    def testVerifyDepthFirstSearch(self) -> None:

        expected = []

        input = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection().connect0(
                lambda: [
                    BaseLabeledVertex(label)
                    for label in ["A", "B", "C", "D", "E", "F", "G", "H", "S"]
                ],
                lambda: [
                    BaseLabeledEdge(f"{from_vertex} <-> {to_vertex}")
                    for from_vertex, to_vertex in [
                        ("S", "A"),
                        ("S", "B"),
                        ("A", "C"),
                        ("A", "D"),
                        ("B", "E"),
                        ("B", "F"),
                        ("E", "H"),
                        ("E", "G"),
                    ]
                ],
            )
        )

        actual = (
            VisitAlgorithmsSelector(input)
            .from_(BaseLabeledVertex("S"))
            .applyingDepthFirstSearch1(NodeSequenceVisitor())
        )

        self.assertEqual(expected, actual)

    def testVerifyBreadthFirstSearch(self) -> None:

        pass  # LLM could not translate this method

    def testNotExistVertex(self) -> None:

        input = CommonsGraph.newUndirectedMutableGraph(AbstractGraphConnection())

        with pytest.raises(RuntimeError):
            visit(input).from_(BaseLabeledVertex("NOT EXIST"))
