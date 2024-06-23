from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.PosixParser import *

# from src.main.org.apache.commons.cli.PosixParser_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class PosixParser_ESTest(unittest.TestCase):

    @pytest.mark.test
    def test13(self) -> None:

        options0 = Options()
        posixParser0 = PosixParser()
        stringArray0 = [""]

        try:
            posixParser0._flatten(options0, stringArray0, True)
            self.fail("Expecting exception: NullPointerException")

        except NullPointerException:
            pass

    @pytest.mark.test
    def test12(self) -> None:

        posixParser0 = PosixParser()
        posixParser0._burstToken("", False)

    @pytest.mark.test
    def test11(self) -> None:

        posixParser0 = PosixParser()

        try:
            posixParser0._burstToken("--", False)
            self.fail("Expecting exception: NullPointerException")

        except Exception as e:
            self.assertEqual(str(e), "")
            self.assertEqual(type(e).__name__, "NullPointerException")

    @pytest.mark.test
    def test10(self) -> None:

        options0 = Options()
        posixParser0 = PosixParser()
        stringArray0 = ["--;0)+oeGp"]
        posixParser0._flatten(options0, stringArray0, True)
        posixParser0._burstToken("--", False)

    @pytest.mark.test
    def test09(self) -> None:

        options0 = Options()
        posixParser0 = PosixParser()
        stringArray0 = ["", ""]
        stringArray0[0] = "-H0n"
        options1 = options0.addOption2("H", "-H0n")
        stringArray1 = posixParser0._flatten(options1, stringArray0, True)
        self.assertEqual(len(stringArray1), 3)

    @pytest.mark.test
    def test08(self) -> None:

        options0 = Options()
        posixParser0 = PosixParser()
        stringArray0 = ["-"]

        with pytest.raises(NullPointerException):
            posixParser0.parse0(options0, stringArray0)

    @pytest.mark.test
    def test07(self) -> None:

        options0 = Options()
        posixParser0 = PosixParser()
        stringArray0 = ["--;0)+oeGp", "--;0)+oeGp", "--"]
        stringArray1 = posixParser0._flatten(options0, stringArray0, False)
        self.assertEqual(len(stringArray1), 3)

    @pytest.mark.test
    def test06(self) -> None:

        options0 = Options()
        posixParser0 = PosixParser()
        stringArray0 = ["", "", ""]
        stringArray0[0] = ")"
        stringArray0[1] = ")"
        stringArray0[2] = "---4^oY=~VK(8"
        stringArray1 = posixParser0._flatten(options0, stringArray0, False)
        self.assertEqual(len(stringArray1), 3)

    @pytest.mark.test
    def test05(self) -> None:

        options0 = Options()
        posixParser0 = PosixParser()
        options1 = options0.addOption1("H", True, "H")
        stringArray0 = ["", ""]
        stringArray0[0] = "-H0n"
        stringArray1 = posixParser0._flatten(options0, stringArray0, True)
        stringArray2 = posixParser0._flatten(options1, stringArray1, True)
        self.assertEqual(len(stringArray2), 2)
        self.assertEqual(len(stringArray1), 2)

    @pytest.mark.test
    def test04(self) -> None:

        options0 = Options()
        posixParser0 = PosixParser()
        stringArray0 = ["-HZ,:n"]
        stringArray1 = posixParser0._flatten(options0, stringArray0, True)
        self.assertEqual(len(stringArray1), 3)

    @pytest.mark.test
    def test03(self) -> None:

        options0 = Options()
        posixParser0 = PosixParser()
        stringArray0 = ["-*"]
        try:
            posixParser0.parse0(options0, stringArray0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Unrecognized option: -*
            self.verifyException("org.apache.commons.cli.Parser", e)

    @pytest.mark.test
    def test02(self) -> None:

        options0 = Options()
        posixParser0 = PosixParser()
        stringArray0 = ["-."]
        stringArray1 = posixParser0._flatten(options0, stringArray0, True)
        self.assertEqual(len(stringArray1), 4)

    @pytest.mark.test
    def test01(self) -> None:

        options0 = Options()
        options0.addOption1("", True, "H")
        posixParser0 = PosixParser()
        stringArray0 = [""] * 4
        stringArray0[0] = ""
        stringArray0[1] = ""
        stringArray0[2] = "H"
        stringArray0[3] = "1"
        posixParser0.parse0(options0, stringArray0)
        posixParser0._burstToken("--", True)

    @pytest.mark.test
    def test00(self) -> None:

        posixParser0 = PosixParser()
        stringArray0 = []
        stringArray1 = posixParser0._flatten(None, stringArray0, True)
        self.assertIsNot(stringArray0, stringArray1)
