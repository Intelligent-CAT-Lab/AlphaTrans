from __future__ import annotations
import time
import re
import os
import typing
from typing import *
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.MissingOptionException import *

# from src.test.org.apache.commons.cli.MissingOptionException_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class MissingOptionException_ESTest(unittest.TestCase):

    def test6(self) -> None:

        linkedList0 = []
        missingOptionException0 = MissingOptionException.MissingOptionException1(
            1379, linkedList0, "X$k#k=IoA pgf9"
        )
        list0 = missingOptionException0.getMissingOptions()
        self.assertIsNone(list0)

    def test5(self) -> None:

        linkedList0 = []
        missingOptionException0 = MissingOptionException.MissingOptionException1(
            1, linkedList0, ", "
        )
        list0 = missingOptionException0.getMissingOptions()
        self.assertEqual(0, len(list0))

    def test4(self) -> None:

        linkedList0 = [
            "",
        ]
        missingOptionException0 = MissingOptionException.MissingOptionException1(
            1, linkedList0, ""
        )
        self.assertIsNotNone(missingOptionException0)

    def test3(self) -> None:

        list0 = ["6^+dgsR4h5*| 2u6", "6^+dgsR4h5*| 2u6"]
        missingOptionException0 = MissingOptionException.MissingOptionException1(
            1, list0, ""
        )
        self.assertIsNotNone(missingOptionException0)

    def test2(self) -> None:

        linkedList0 = []
        missingOptionException0 = MissingOptionException(-16, linkedList0, None)

    def test1(self) -> None:

        try:
            MissingOptionException.MissingOptionException1(1, None, "3cFAtCi7c4Vm\n-")
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.MissingOptionException", e)

    def test0(self) -> None:

        linkedList0 = LinkedList()
        integer0 = Integer(1)
        linkedList0.add(integer0)
        missingOptionException0 = MissingOptionException(1, linkedList0, None)
        list0 = missingOptionException0.getMissingOptions()
        self.assertFalse(len(list0) == 0)
