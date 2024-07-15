from __future__ import annotations
import time
import re
import mock
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.export.DefaultExportSelector import *

# from src.test.org.apache.commons.graph.export.DefaultExportSelector_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.export.DotExporter import *
from src.main.org.apache.commons.graph.export.ExportSelector import *
from src.main.org.apache.commons.graph.model.MutableSpanningTree import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.weight.Monoid import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class DefaultExportSelector_ESTest(unittest.TestCase):

    def test3(self) -> None:

        defaultExportSelector0 = DefaultExportSelector[str, str](None)

        try:
            defaultExportSelector0.usingDotNotation()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.export.DotExporter", e)

    def test2(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        defaultExportSelector0 = DefaultExportSelector(undirectedMutableGraph0)
        exportSelector0 = defaultExportSelector0.withName(
            "org.apache.commons.graph.export.DefaultExportSelector"
        )
        assert exportSelector0 is not None

    def test1(self) -> None:

        monoid0 = unittest.mock.Mock(spec=Monoid)
        monoid0.identity.return_value = None
        mapper0 = unittest.mock.Mock(spec=Mapper)
        mutableSpanningTree0 = MutableSpanningTree(monoid0, mapper0)
        defaultExportSelector0 = DefaultExportSelector(mutableSpanningTree0)
        dotExporter0 = defaultExportSelector0.usingDotNotation()
        self.assertIsNotNone(dotExporter0)

    def test0(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        defaultExportSelector0 = DefaultExportSelector(undirectedMutableGraph0)

        try:
            defaultExportSelector0.withName(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.utils.Assertions", e)
