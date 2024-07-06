from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.GnuParser import *

# from src.test.org.apache.commons.cli.GnuParser_ESTest_scaffolding import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.Options import *

# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class GnuParser_ESTest(unittest.TestCase):

    def test5(self) -> None:

        gnuParser0 = GnuParser()
        options0 = Options()
        stringArray0 = ['2*SgaMp@@"c!!Qzz"=', "Cv)w,&9", "-", "", "--"]
        stringArray1 = gnuParser0._flatten(options0, stringArray0, True)
        self.assertEqual(len(stringArray1), 5)

    def test4(self) -> None:

        gnuParser0 = GnuParser()
        options0 = Options()
        options0.addOption3("prM", ",", True, " [ARG]")
        stringArray0 = [",", " [ARG]", " [ARG]", "--,"]
        try:
            gnuParser0.parse0(options0, stringArray0)
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError:
            pass

    def test3(self) -> None:

        gnuParser0 = GnuParser()
        options0 = Options()
        stringArray0 = [None] * 6
        stringArray0[0] = "-="
        stringArray1 = gnuParser0._flatten(options0, stringArray0, True)
        self.assertEqual(len(stringArray1), 6)

    def test2(self) -> None:

        gnuParser0 = GnuParser()
        options0 = Options()
        options0.addOption3("", "", False, "")
        stringArray0 = [""] * 7
        stringArray0[0] = ""
        stringArray0[1] = "-="

        try:
            gnuParser0._flatten(options0, stringArray0, False)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            pass

    def test1(self) -> None:

        options0 = Options()
        gnuParser0 = GnuParser()
        option0 = Option.Option1("", ";A`_E&y2myH>x)#s,$")
        options1 = options0.addOption0(option0)
        stringArray0 = [";A`_E&y2myH>x)#s,$", "--,"]
        commandLine0 = gnuParser0.parse0(options1, stringArray0)
        self.assertIsNotNone(commandLine0)

    def test0(self) -> None:

        gnuParser0 = GnuParser()
        options0 = Options()
        stringArray0 = []
        stringArray1 = gnuParser0._flatten(options0, stringArray0, True)
        self.assertIsNot(stringArray1, stringArray0)
