from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.BasicParser import *

# from src.test.org.apache.commons.cli.BasicParser_ESTest_scaffolding import *
from src.main.org.apache.commons.cli.Options import *

# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class BasicParser_ESTest(unittest.TestCase):

    def test2(self) -> None:

        basicParser0 = BasicParser()
        stringArray0 = [None] * 8
        stringArray1 = basicParser0.flatten(None, stringArray0, False)
        self.assertIs(stringArray0, stringArray1)

    def test1(self) -> None:

        basicParser0 = BasicParser()
        stringArray0 = []
        stringArray1 = basicParser0.flatten(None, stringArray0, True)
        self.assertEqual(0, len(stringArray1))

    def test0(self) -> None:

        basicParser0 = BasicParser()
        stringArray0 = basicParser0._flatten(None, None, False)
        self.assertIsNone(stringArray0)
