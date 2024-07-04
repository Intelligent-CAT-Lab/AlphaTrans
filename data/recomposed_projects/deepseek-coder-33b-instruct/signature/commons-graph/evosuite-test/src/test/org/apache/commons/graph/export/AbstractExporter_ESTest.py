from __future__ import annotations
import time
import re
import mock
import os
from io import BytesIO
from io import StringIO
import pathlib
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *

# from src.test.org.apache.commons.graph.export.AbstractExporter_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.export.DotExporter import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.InMemoryPath import *
from src.main.org.apache.commons.graph.model.InMemoryWeightedPath import *
from src.main.org.apache.commons.graph.model.RevertedGraph import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.weight.Monoid import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class AbstractExporter_ESTest(unittest.TestCase):

    def test9(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        revertedGraph0 = RevertedGraph(directedMutableGraph0)
        dotExporter0 = DotExporter(revertedGraph0, "")
        mockFile0 = MockFile("]RtFv**]S")
        dotExporter0.to0(mockFile0)
        self.assertEqual(84, mockFile0.length())

    def test8(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        dotExporter0 = DotExporter(undirectedMutableGraph0, None)

        try:
            dotExporter0.to2(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertIsInstance(e, RuntimeError)
            # Impossibe to export the graph in a null stream
            self.assertTrue(
                str(e).startswith("org.apache.commons.graph.utils.Assertions")
            )

    def test5(self) -> None:

        buffered_output_stream0 = io.BufferedWriter(io.StringIO())
        object_output_stream0 = io.StringIO()
        integer0 = 2094
        monoid0 = unittest.mock.Mock(spec=Monoid)
        monoid0.identity.return_value = None
        mapper0 = unittest.mock.Mock(spec=Mapper)
        in_memory_weighted_path0 = InMemoryWeightedPath(
            integer0, integer0, monoid0, mapper0
        )
        dot_exporter0 = DotExporter(in_memory_weighted_path0, "--")

        with pytest.raises(RuntimeError):
            dot_exporter0.to1(object_output_stream0)
            unittest.TestCase.fail(self, "Expecting exception: RuntimeError")

    def test4(self) -> None:

        string_writer0 = io.StringIO(2094)
        in_memory_path0 = InMemoryPath(string_writer0, (string_writer0, string_writer0))
        dot_exporter0 = DotExporter(in_memory_path0, "%;DLVS~/i;E!")

        with pytest.raises(RuntimeError):
            dot_exporter0.to0(None)
            pytest.fail("Expecting exception: RuntimeError")

    def test3(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        dotExporter0 = DotExporter(directedMutableGraph0, "")
        mockFile0 = MockFile("")

        with pytest.raises(RuntimeError):
            dotExporter0.to0(mockFile0)
            self.fail("Expecting exception: RuntimeError")

        verifyException(
            "org.apache.commons.graph.export.AbstractExporter", RuntimeError
        )

    def test2(self) -> None:

        string_writer0 = io.StringIO(new_line="\n")
        in_memory_path0 = InMemoryPath(string_writer0, (string_writer0, string_writer0))
        dot_exporter0 = DotExporter(in_memory_path0, "%;DLVS~/i;E!")

        with pytest.raises(RuntimeError):
            dot_exporter0.to1(None)
            pytest.fail("Expecting exception: RuntimeError")

    def test0(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[StringIO, StringIO]()
        dotExporter0 = DotExporter[StringIO, StringIO](
            directedMutableGraph0,
            "org.apache.commons.graph.export.GraphExportException",
        )
        pipedInputStream0 = io.BytesIO()
        pipedOutputStream0 = io.BytesIO()
        dotExporter0.to1(pipedOutputStream0)
        dotExporter0.to1(pipedOutputStream0)
        self.assertEqual(136, len(pipedInputStream0.getvalue()))
