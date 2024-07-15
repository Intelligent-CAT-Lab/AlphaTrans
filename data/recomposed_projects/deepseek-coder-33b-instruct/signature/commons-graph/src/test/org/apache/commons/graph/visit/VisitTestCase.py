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
            AbstractGraphConnection(
                connect0=lambda: (
                    s := BaseLabeledVertex("S"),
                    a := BaseLabeledVertex("A"),
                    b := BaseLabeledVertex("B"),
                    c := BaseLabeledVertex("C"),
                    d := BaseLabeledVertex("D"),
                    e := BaseLabeledVertex("E"),
                    f := BaseLabeledVertex("F"),
                    g := BaseLabeledVertex("G"),
                    h := BaseLabeledVertex("H"),
                    addVertex(s),
                    addVertex(a),
                    addVertex(b),
                    addVertex(c),
                    addVertex(d),
                    addVertex(e),
                    addVertex(f),
                    addVertex(g),
                    addVertex(h),
                    addEdge(BaseLabeledEdge("S <-> A")).from_(s).to(a),
                    addEdge(BaseLabeledEdge("S <-> B")).from_(s).to(b),
                    addEdge(BaseLabeledEdge("A <-> C")).from_(a).to(c),
                    addEdge(BaseLabeledEdge("A <-> D")).from_(a).to(d),
                    addEdge(BaseLabeledEdge("B <-> E")).from_(b).to(e),
                    addEdge(BaseLabeledEdge("B <-> F")).from_(b).to(f),
                    addEdge(BaseLabeledEdge("E <-> H")).from_(e).to(h),
                    addEdge(BaseLabeledEdge("E <-> G")).from_(e).to(g),
                    expected.append(s),
                    expected.append(b),
                    expected.append(f),
                    expected.append(e),
                    expected.append(g),
                    expected.append(h),
                    expected.append(a),
                    expected.append(d),
                    expected.append(c),
                )
            )
        )

        actual = (
            VisitAlgorithmsSelector(visit(input))
            .from_(BaseLabeledVertex("S"))
            .applyingDepthFirstSearch1(NodeSequenceVisitor())
        )

        self.assertEqual(expected, actual)

    def testVerifyBreadthFirstSearch(self) -> None:

        pass  # LLM could not translate this method

    def testNotExistVertex(self) -> None:

        class TestGraphConnection(AbstractGraphConnection):
            def connect0(self):
                pass

        input = CommonsGraph.newUndirectedMutableGraph(TestGraphConnection())

        with pytest.raises(RuntimeError):
            visit(input).from_(BaseLabeledVertex("NOT EXIST"))
