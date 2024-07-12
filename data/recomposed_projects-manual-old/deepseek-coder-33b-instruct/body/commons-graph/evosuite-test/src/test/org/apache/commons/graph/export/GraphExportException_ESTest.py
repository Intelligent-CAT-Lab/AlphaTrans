from __future__ import annotations
import time
import re
import mock
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.export.GraphExportException import *

# from src.test.org.apache.commons.graph.export.GraphExportException_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class GraphExportException_ESTest(unittest.TestCase):

    def test2(self) -> None:

        mockThrowable0 = MockThrowable("")
        objectArray0 = [""]
        graphExportException0 = GraphExportException(mockThrowable0, "", objectArray0)

    def test1(self) -> None:

        mockThrowable0 = MockThrowable("")
        objectArray0 = [None]
        graphExportException0 = None
        try:
            graphExportException0 = GraphExportException(
                mockThrowable0, None, objectArray0
            )
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            pass

    def test0(self) -> None:

        mockThrowable0 = MockThrowable()
        objectArray0 = [None] * 7
        graphExportException0 = None
        try:
            graphExportException0 = GraphExportException(
                mockThrowable0, "4r&}Oo+%1#[Z", objectArray0
            )
            self.fail("Expecting exception: UnknownFormatConversionException")

        except UnknownFormatConversionException as e:
            # Conversion = '1'
            self.verifyException("java.util.Formatter", e)
