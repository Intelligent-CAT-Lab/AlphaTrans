from __future__ import annotations
import time
import re
import mock
import os
from io import StringIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.digest.B64 import *

# from src.test.org.apache.commons.codec.digest.B64_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class B64_ESTest(unittest.TestCase):

    def test9(self) -> None:
        b64_0 = B64()

    def test8(self) -> None:

        stringBuilder0 = io.StringIO()
        B64.b64from24bit(0, 69, 77, 77, stringBuilder0)
        self.assertEqual(
            "BJ2..........................................................................",
            stringBuilder0.getvalue(),
        )

    def test7(self) -> None:

        mockRandom0 = MockRandom(2083)
        string0 = B64.getRandomSalt(2083, mockRandom0)
        self.assertIsNotNone(string0)

    def test6(self) -> None:

        try:
            B64.b64from24bit(63, 63, 63, 63, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            pass

    def test5(self) -> None:

        stringBuilder0 = []
        B64.b64from24bit(65, 65, 65, 16777215, stringBuilder0)

    def test4(self) -> None:

        with pytest.raises(NegativeArraySizeException):
            B64.getRandomSalt(-545, None)

    def test3(self) -> None:

        with pytest.raises(RuntimeError):
            B64.getRandomSalt(63, None)

    def test2(self) -> None:

        mockRandom0 = MockRandom(65535)
        B64.getRandomSalt(65535, mockRandom0)

    def test1(self) -> None:

        mockRandom0 = MockRandom(0)
        string0 = B64.getRandomSalt(0, mockRandom0)
        self.assertEqual("", string0)

    def test0(self) -> None:

        B64.b64from24bit(-120, -120, -120, -120, None)
