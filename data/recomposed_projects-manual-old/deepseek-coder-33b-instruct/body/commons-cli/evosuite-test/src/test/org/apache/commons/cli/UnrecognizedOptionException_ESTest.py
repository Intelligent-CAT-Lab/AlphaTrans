from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.UnrecognizedOptionException import *

# from src.test.org.apache.commons.cli.UnrecognizedOptionException_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class UnrecognizedOptionException_ESTest(unittest.TestCase):

    def test2(self) -> None:
        unrecognizedOptionException0 = (
            UnrecognizedOptionException.UnrecognizedOptionException1("")
        )
        string0 = unrecognizedOptionException0.getOption()
        self.assertIsNone(string0)

    def test1(self) -> None:
        unrecognizedOptionException0 = UnrecognizedOptionException("", "")
        string0 = unrecognizedOptionException0.getOption()
        self.assertEqual("", string0)

    def test0(self) -> None:
        unrecognizedOptionException0 = UnrecognizedOptionException(
            "org.apache.commons.cli.ParseException",
            "org.apache.commons.cli.ParseException",
        )
        string0 = unrecognizedOptionException0.getOption()
        self.assertEqual("org.apache.commons.cli.ParseException", string0)
