from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.GnuParser import *

# from src.main.org.apache.commons.cli.GnuParser_ESTest_scaffolding import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.Options import *

# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class GnuParser_ESTest(unittest.TestCase):

    @pytest.mark.test
    def test5(self) -> None:

        gnuParser0 = GnuParser()
        options0 = Options()
        stringArray0 = [""] * 8
        stringArray0[0] = ""
        stringArray0[1] = ""
        stringArray0[2] = "org.apache.commons.cli.GnuParser"
        stringArray0[3] = ""
        stringArray0[4] = "org.apache.commons.cli.GnuParser"
        stringArray0[5] = "--"
        stringArray1 = gnuParser0._flatten(options0, stringArray0, False)
        self.assertEqual(len(stringArray1), 8)

    @pytest.mark.test
    def test4(self) -> None:

        gnuParser0 = GnuParser()
        options0 = Options()
        stringArray0 = ["f", "-", "--", "-"]

        with pytest.raises(NullPointerException):
            gnuParser0._flatten(options0, stringArray0, False)

    @pytest.mark.test
    def test3(self) -> None:

        options0 = Options()
        gnuParser0 = GnuParser()
        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.longOpt(".")
        option0 = option_Builder1.build()
        options0.addOption0(option0)
        stringArray0 = [None] * 1
        stringArray0[0] = "-."
        stringArray1 = gnuParser0._flatten(options0, stringArray0, False)
        self.assertEqual(len(stringArray1), 1)

    @pytest.mark.test
    def test2(self) -> None:

        options0 = Options()
        gnuParser0 = GnuParser()
        stringArray0 = ["-v%0d[C'<=.z?Vp1A"]
        stringArray1 = gnuParser0._flatten(options0, stringArray0, True)
        self.assertEqual(len(stringArray0), len(stringArray1))

    @pytest.mark.test
    def test1(self) -> None:

        gnuParser0 = GnuParser()
        options0 = Options()
        options1 = options0.addOption2("", "l")
        stringArray0 = [""] * 6
        stringArray0[0] = "l"
        stringArray0[1] = ""
        stringArray0[2] = ""
        stringArray0[3] = "--;."
        # Undeclared exception in Java code
        try:
            gnuParser0._flatten(options1, stringArray0, False)
            self.fail("Expecting exception: NullPointerException")

        except Exception as e:
            pass

    @pytest.mark.test
    def test0(self) -> None:

        gnuParser0 = GnuParser()
        stringArray0 = []
        stringArray1 = gnuParser0._flatten(None, stringArray0, True)
        self.assertNotEqual(stringArray1, stringArray0)
