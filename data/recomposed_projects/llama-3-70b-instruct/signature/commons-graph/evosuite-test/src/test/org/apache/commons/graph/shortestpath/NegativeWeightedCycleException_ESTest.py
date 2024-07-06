from __future__ import annotations
import time
import re
import mock
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.shortestpath.NegativeWeightedCycleException import *

# from src.test.org.apache.commons.graph.shortestpath.NegativeWeightedCycleException_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class NegativeWeightedCycleException_ESTest(unittest.TestCase):

    def test1(self) -> None:

        objectArray0 = [None] * 9
        negativeWeightedCycleException0 = NegativeWeightedCycleException(
            None, None, objectArray0
        )
        mockThrowable0 = MockThrowable("qlp$", negativeWeightedCycleException0)
        negativeWeightedCycleException1 = None
        try:
            negativeWeightedCycleException1 = NegativeWeightedCycleException(
                None, mockThrowable0, objectArray0
            )
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            pass

    def test0(self) -> None:

        mockThrowable0 = MockThrowable("")
        objectArray0 = [None] * 3
        negativeWeightedCycleException0 = None
        try:
            negativeWeightedCycleException0 = NegativeWeightedCycleException(
                "a%mGB+4,$>", mockThrowable0, objectArray0
            )
            self.fail("Expecting exception: UnknownFormatConversionException")

        except UnknownFormatConversionException as e:
            #
            # Conversion = 'm'
            #
            self.verifyException("java.util.Formatter$FormatSpecifier", e)
