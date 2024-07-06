from __future__ import annotations
import time
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.PosixParser import *

# from src.test.org.apache.commons.cli.PosixParser_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class PosixParser_ESTest(unittest.TestCase):

    def test12(self) -> None:

        options0 = Options()
        posixParser0 = PosixParser()
        stringArray0 = [""]

        try:
            posixParser0._flatten(options0, stringArray0, True)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError:
            pass

    def test11(self) -> None:

        options0 = Options()
        options0.addOption3("", "--", True, None)
        posixParser0 = PosixParser()
        stringArray0 = ["--org.apache.commons.cli.PosixParser"]
        posixParser0._flatten(options0, stringArray0, True)
        posixParser0._burstToken("--", True)
        posixParser0._burstToken(">+DmEH", True)

    def test10(self) -> None:

        options0 = Options()
        options0.addOption3("", "--", False, None)
        posixParser0 = PosixParser()
        stringArray0 = ["--org.apache.commons.cli.PosixParser"]
        posixParser0._flatten(options0, stringArray0, False)
        posixParser0._burstToken("--", True)

    def test09(self) -> None:

        options0 = Options()
        options0.addOption3("", "--", True, None)
        posixParser0 = PosixParser()
        stringArray0 = ["--org.apache.commons.cli.PosixParser"]
        posixParser0._flatten(options0, stringArray0, True)
        posixParser0._burstToken("--org.apache.commons.cli.PosixParser", True)

    def test08(self) -> None:

        options0 = Options()
        posixParser0 = PosixParser()
        stringArray0 = ["-"]

        with pytest.raises(RuntimeError):
            posixParser0.parse0(options0, stringArray0)

    def test07(self) -> None:

        options0 = Options()
        posixParser0 = PosixParser()
        stringArray0 = ["--org.apache.commons.cli.PosixParser"]
        stringArray1 = posixParser0._flatten(options0, stringArray0, True)
        stringArray2 = posixParser0._flatten(options0, stringArray1, True)
        self.assertEqual(len(stringArray2), 3)
        self.assertEqual(len(stringArray1), 2)

    def test06(self) -> None:

        posixParser0 = PosixParser()
        options0 = Options()
        stringArray0 = ["-N"]
        stringArray1 = posixParser0._flatten(options0, stringArray0, True)
        self.assertEqual(len(stringArray1), 4)

    def test05(self) -> None:

        posixParser0 = PosixParser()
        options0 = Options()
        stringArray0 = ["-N", "gQk$Sz", "-N", "-N", "5I", "--c_=ibaY|~}yw"]
        stringArray1 = posixParser0._flatten(options0, stringArray0, False)
        self.assertEqual(len(stringArray1), 6)

    def test04(self) -> None:

        posixParser0 = PosixParser()
        options0 = Options()
        stringArray0 = [None] * 8
        stringArray0[0] = "--org.apache.commons.cli.PosixParser"
        stringArray0[1] = "Pd.`J-sm4L#:ZvB"
        stringArray0[2] = "`Tj:~U nm8askt"
        stringArray0[3] = "-mu"
        properties0 = {}

        try:
            posixParser0.parse2(options0, stringArray0, properties0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")

    def test03(self) -> None:

        options0 = Options()
        options0.addOption3("", "--", False, None)
        posixParser0 = PosixParser()
        stringArray0 = ["--org.apache.commons.cli.PosixParser"]
        posixParser0._flatten(options0, stringArray0, False)
        posixParser0._burstToken("--org.apache.commons.cli.PosixParser", True)

    def test02(self) -> None:

        posixParser0 = PosixParser()

        try:
            posixParser0._burstToken("NO_ARGS_ALLOWED", False)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.PosixParser", e)

    def test01(self) -> None:

        posixParser0 = PosixParser()
        stringArray0 = []
        stringArray1 = posixParser0._flatten(None, stringArray0, True)
        self.assertEqual(len(stringArray1), 0)

    def test00(self) -> None:

        posixParser0 = PosixParser()
        posixParser0._burstToken("", False)
