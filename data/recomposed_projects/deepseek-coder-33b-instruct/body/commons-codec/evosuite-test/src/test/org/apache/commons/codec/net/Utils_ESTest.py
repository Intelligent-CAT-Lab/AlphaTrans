from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.net.Utils import *

# from src.test.org.apache.commons.codec.net.Utils_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Utils_ESTest(unittest.TestCase):

    def test5(self) -> None:
        utils0 = Utils()

    def test4(self) -> None:

        char0 = Utils.hexDigit(48)
        self.assertEqual("0", char0)

    def test3(self) -> None:
        int0 = Utils.digit16(48)
        self.assertEqual(0, int0)

    def test2(self) -> None:
        try:
            Utils.digit16(77)
            self.fail("Expecting exception: Exception")
        except Exception as e:
            # Invalid URL encoding: not a valid digit (radix 16): 77
            self.verifyException("org.apache.commons.codec.net.Utils", e)

    def test1(self) -> None:
        int0 = Utils.digit16(66)
        self.assertEqual(11, int0)

    def test0(self) -> None:
        char0 = Utils.hexDigit(-1)
        self.assertEqual("F", char0)
