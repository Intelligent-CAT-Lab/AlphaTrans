from __future__ import annotations
import time
import re
import mock
import os
from io import BytesIO
import pathlib
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.export.DotExporter import *

# from src.test.org.apache.commons.graph.export.DotExporter_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.InMemoryPath import *
from src.main.org.apache.commons.graph.model.InMemoryWeightedPath import *
from src.main.org.apache.commons.graph.model.MutableSpanningTree import *
from src.main.org.apache.commons.graph.model.RevertedGraph import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class DotExporter_ESTest(unittest.TestCase):

    def test21(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        revertedGraph0 = RevertedGraph(directedMutableGraph0)
        inMemoryPath0 = InMemoryPath(revertedGraph0, revertedGraph0)
        dotExporter0 = DotExporter(inMemoryPath0, "36.")
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        dotExporter1 = dotExporter0.withEdgeWeights(mapper0)
        self.assertIs(dotExporter1, dotExporter0)

    def test20(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        reverted_graph0 = RevertedGraph(directed_mutable_graph0)
        in_memory_path0 = InMemoryPath(reverted_graph0, reverted_graph0)
        dot_exporter0 = DotExporter(in_memory_path0, "sV")
        byte_array_output_stream0 = io.BytesIO()
        dot_exporter0.to1(byte_array_output_stream0)
        hash_map0 = {"sV": "sV", "%s %s {%n": "sV"}
        dot_exporter0.vertex(reverted_graph0, hash_map0)
        self.assertFalse(bool(hash_map0))

    def test19(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        dotExporter0 = DotExporter(
            undirectedMutableGraph0, "org.apache.commons.graph.model.InMemoryPath"
        )
        dotExporter1 = dotExporter0.with_edge_labels(None)
        assert dotExporter1 == dotExporter0

    def test18(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        revertedGraph0 = RevertedGraph(directedMutableGraph0)
        monoid0 = mock(Monoid, ViolatedAssumptionAnswer())
        monoid0.identity.return_value = None
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        inMemoryWeightedPath0 = InMemoryWeightedPath(
            revertedGraph0, revertedGraph0, monoid0, mapper0
        )
        dotExporter0 = DotExporter(inMemoryWeightedPath0, "weight")
        mapper1 = mock(Mapper, ViolatedAssumptionAnswer())
        dotExporter1 = dotExporter0.withVertexLabels(mapper1)
        self.assertIs(dotExporter0, dotExporter1)

    def test17(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        revertedGraph0 = RevertedGraph(directedMutableGraph0)
        dotExporter0 = DotExporter(revertedGraph0, "")
        class0 = int
        dotExporter0.enlistVerticesProperty("", class0)

    def test16(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        revertedGraph0 = RevertedGraph(directedMutableGraph0)
        inMemoryPath0 = InMemoryPath(revertedGraph0, revertedGraph0)
        dotExporter0 = DotExporter(inMemoryPath0, "36.")
        hashMap0 = {}
        try:
            dotExporter0.vertex(revertedGraph0, hashMap0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("org.apache.commons.graph.export.DotExporter", e)

    def test15(self) -> None:

        integer_weight_base_operations0 = IntegerWeightBaseOperations()
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        mutable_spanning_tree0 = MutableSpanningTree(
            integer_weight_base_operations0, mapper0
        )
        dot_exporter0 = DotExporter(mutable_spanning_tree0, "")
        class0 = int
        dot_exporter0.enlist_edges_property("", class0)

    def test14(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph[int, RevertedGraph[int, int]]()
        integer0 = Integer(-2)
        undirectedMutableGraph0.addVertex(integer0)
        dotExporter0 = DotExporter[int, RevertedGraph[int, int]](
            undirectedMutableGraph0, "L"
        )

    def test13(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph[int, int]()
        reverted_graph0 = RevertedGraph[int, int](directed_mutable_graph0)
        in_memory_path0 = InMemoryPath[
            RevertedGraph[int, int], RevertedGraph[int, int]
        ](reverted_graph0, reverted_graph0)
        dot_exporter0 = DotExporter[RevertedGraph[int, int], RevertedGraph[int, int]](
            in_memory_path0, "36."
        )
        byte_array_output_stream0 = io.BytesIO()
        buffered_output_stream0 = io.BufferedWriter(byte_array_output_stream0)
        dot_exporter0.to1(buffered_output_stream0)
        hash_map0 = dict[str, object]()
        hash_map0["36."] = reverted_graph0
        dot_exporter0.vertex(reverted_graph0, hash_map0)
        self.assertFalse(hash_map0)

    def test12(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        dotExporter0 = DotExporter(
            undirectedMutableGraph0, "org.apache.commons.graph.model.InMemoryPath"
        )

        pipedInputStream0 = PipedInputStream(988)
        pipedOutputStream0 = PipedOutputStream(pipedInputStream0)
        mockPrintStream0 = MockPrintStream(pipedOutputStream0, True)
        dataOutputStream0 = DataOutputStream(mockPrintStream0)

        dotExporter0.to1(dataOutputStream0)

        directedMutableGraph0 = DirectedMutableGraph()
        revertedGraph0 = RevertedGraph(directedMutableGraph0)
        hashMap0 = {}

        dotExporter0.edge(revertedGraph0, revertedGraph0, revertedGraph0, hashMap0)

        self.assertTrue(not hashMap0)

    def test11(self) -> None:

        dotExporter0 = None
        try:
            dotExporter0 = DotExporter[int, str](None, "")
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.export.DotExporter", e)

    def test10(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph[int, int]()
        dotExporter0 = DotExporter[int, int](undirectedMutableGraph0, "")

        try:
            dotExporter0.comment("")
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("org.apache.commons.graph.export.DotExporter", e)

    def test09(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        dotExporter0 = DotExporter(
            undirectedMutableGraph0, "org.apache.commons.graph.model.InMemoryPath"
        )

        try:
            dotExporter0.endGraph()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("org.apache.commons.graph.export.DotExporter", e)

    def test08(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        dotExporter0 = DotExporter(undirectedMutableGraph0, "s{DqL VW")

        try:
            dotExporter0.startGraph("org.apache.commons.graph.model.BaseGraph")
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("org.apache.commons.graph.export.DotExporter", e)

    def test07(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph[int, int]()
        dotExporter0 = DotExporter[int, int](
            undirectedMutableGraph0, "org.apache.commons.graph.model.RevertedGraph"
        )

        try:
            dotExporter0.startSerialization()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("java.io.Writer", e)

    def test06(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        revertedGraph0 = RevertedGraph(directedMutableGraph0)
        inMemoryPath0 = InMemoryPath(revertedGraph0, revertedGraph0)
        dotExporter0 = DotExporter(inMemoryPath0, "I9N:)e?b~jm5tP")
        dotExporter0.endSerialization()

    def test05(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, int]()
        revertedGraph0 = RevertedGraph[int, int](directedMutableGraph0)
        inMemoryPath0 = InMemoryPath[RevertedGraph[int, int], RevertedGraph[int, int]](
            revertedGraph0, revertedGraph0
        )
        dotExporter0 = DotExporter[RevertedGraph[int, int], RevertedGraph[int, int]](
            inMemoryPath0, "36."
        )
        byteArrayOutputStream0 = io.BytesIO()
        bufferedOutputStream0 = io.BufferedWriter(byteArrayOutputStream0)
        dotExporter0.to1(bufferedOutputStream0)
        dotExporter0.comment("^yVN]sQ$/")

    def test04(self) -> None:

        integer0 = Integer(2)
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        mapper0 = mock(Mapper, new=ViolatedAssumptionAnswer())
        inMemoryWeightedPath0 = InMemoryWeightedPath(
            integer0, integer0, integerWeightBaseOperations0, mapper0
        )
        dotExporter0 = DotExporter(inMemoryWeightedPath0, "")
        mockFile0 = MockFile("ZQ[M;^odH", "y@tztKj[._7kz")
        dotExporter0.to0(mockFile0)
        dotExporter0.endGraph()

    def test03(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, int]()
        dotExporter0 = DotExporter[int, int](directedMutableGraph0, "I9N:)e?b~jm5tP")
        byteArrayOutputStream0 = io.BytesIO()
        dotExporter0.to1(byteArrayOutputStream0)
        dotExporter0.startGraph("")

    def test02(self) -> None:

        integer_weight_base_operations0 = IntegerWeightBaseOperations()
        mapper0 = Mock(spec=Mapper)
        mutable_spanning_tree0 = MutableSpanningTree(
            integer_weight_base_operations0, mapper0
        )
        dot_exporter0 = DotExporter(mutable_spanning_tree0, ";-")
        mock_file0 = MockFile("  %s", "")
        mock_print_stream0 = MockPrintStream(mock_file0)
        buffered_output_stream0 = BufferedOutputStream(mock_print_stream0, 2)
        dot_exporter0.to1(buffered_output_stream0)
        dot_exporter0.start_serialization()

    def test01(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        dotExporter0 = DotExporter(undirectedMutableGraph0, "36.")
        integer0 = Integer(1104)
        hashMap0 = {}
        directedMutableGraph0 = DirectedMutableGraph()
        revertedGraph0 = RevertedGraph(directedMutableGraph0)

        try:
            dotExporter0.edge(revertedGraph0, integer0, integer0, hashMap0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.export.DotExporter", e)

    def test00(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        mapper0 = mock(Mapper, new_callable=ViolatedAssumptionAnswer)
        mutableSpanningTree0 = MutableSpanningTree(
            integerWeightBaseOperations0, mapper0
        )
        dotExporter0 = DotExporter(mutableSpanningTree0, 'jAwAG4%I*Sh@6E;y1>"')
        integer0 = Integer(31)
        integer1 = Integer(0)
        hashMap0 = {}
        try:
            dotExporter0.edge(integer0, integer1, integer0, hashMap0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.export.DotExporter", e)
