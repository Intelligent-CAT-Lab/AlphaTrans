from __future__ import annotations
import time
import re
import mock
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.GraphException import *

# from src.test.org.apache.commons.graph.GraphException_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class GraphException_ESTest(unittest.TestCase):

    def test2(self) -> None:

        objectArray0 = [None] * 8
        graphException0 = GraphException("3yD", None, objectArray0)
        graphException1 = GraphException('"WaDD1~$b_0', graphException0, objectArray0)
        self.assertFalse(graphException1 == graphException0)

    def test1(self) -> None:

        mockThrowable0 = MockThrowable("org.apache.commons.graph.GraphException")
        objectArray0 = [None]
        graphException0 = GraphException(
            "org.apache.commons.graph.GraphException", mockThrowable0, objectArray0
        )
        graphException1 = None
        try:
            graphException1 = GraphException(None, graphException0, objectArray0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            pass

    def test0(self) -> None:

        mockThrowable0 = MockThrowable(None, None)
        throwableArray0 = mockThrowable0.getSuppressed()
        graphException0 = GraphException("", mockThrowable0, throwableArray0)
        graphException1 = None
        try:
            graphException1 = GraphException(
                "%?A?(S~uPlt", graphException0, throwableArray0
            )
            self.fail("Expecting exception: UnknownFormatConversionException")

        except UnknownFormatConversionException as e:
            #
            # Conversion = '?'
            #
            self.verifyException("java.util.Formatter", e)
