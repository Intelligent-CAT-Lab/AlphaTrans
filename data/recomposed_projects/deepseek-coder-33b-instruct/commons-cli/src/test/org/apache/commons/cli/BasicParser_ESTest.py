from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.BasicParser import *

# from src.main.org.apache.commons.cli.BasicParser_ESTest_scaffolding import *
from src.main.org.apache.commons.cli.Options import *

# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class BasicParser_ESTest(unittest.TestCase):

    @pytest.mark.test
    def test2(self) -> None:

        basicParser0 = BasicParser()
        stringArray0 = []
        stringArray1 = basicParser0._flatten(None, stringArray0, False)
        self.assertEqual(stringArray0, stringArray1)

    @pytest.mark.test
    def test1(self) -> None:

        # Create an instance of BasicParser
        basicParser0 = BasicParser()

        # Create an instance of Options
        options0 = Options()

        # Create an array of strings
        stringArray0 = [""] * 4

        # Call the flatten method
        stringArray1 = basicParser0._flatten(options0, stringArray0, True)

        # Assert that the returned array is the same as the input array
        self.assertIs(stringArray1, stringArray0)

    @pytest.mark.test
    def test0(self) -> None:

        # Create an instance of BasicParser
        basicParser0 = BasicParser()

        # Create an instance of Options
        options0 = Options()

        # Call the flatten method
        stringArray0 = basicParser0._flatten(options0, None, True)

        # Assert that the result is None
        self.assertIsNone(stringArray0)
