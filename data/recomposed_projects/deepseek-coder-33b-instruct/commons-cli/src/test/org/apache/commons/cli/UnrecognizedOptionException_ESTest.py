from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.UnrecognizedOptionException import *

# from src.main.org.apache.commons.cli.UnrecognizedOptionException_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class UnrecognizedOptionException_ESTest(unittest.TestCase):

    @pytest.mark.test
    def test2(self) -> None:
        unrecognizedOptionException0 = UnrecognizedOptionException("", "")
        string0 = unrecognizedOptionException0.getOption()
        self.assertEqual("", string0)

    @pytest.mark.test
    def test1(self) -> None:
        unrecognizedOptionException0 = UnrecognizedOptionException("64rBdz", "64rBdz")
        string0 = unrecognizedOptionException0.getOption()
        self.assertEqual("64rBdz", string0)

    @pytest.mark.test
    def test0(self) -> None:
        unrecognizedOptionException0 = (
            UnrecognizedOptionException.UnrecognizedOptionException1("Z{X")
        )
        string0 = unrecognizedOptionException0.getOption()
        self.assertIsNone(string0)
