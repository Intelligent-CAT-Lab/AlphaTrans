from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.fileupload.ParameterParser import *

# from src.test.org.apache.commons.fileupload.ParameterParser_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class ParameterParser_ESTest(unittest.TestCase):

    def test21(self) -> None:
        parameterParser0 = ParameterParser()
        boolean0 = parameterParser0.isLowerCaseNames()
        self.assertFalse(boolean0)

    def test20(self) -> None:

        parameterParser0 = ParameterParser()
        parameterParser0.parse1(" \t\r\n", "`")
        self.assertFalse(parameterParser0.isLowerCaseNames())

    def test19(self) -> None:

        parameterParser0 = ParameterParser()
        charArray0 = [""]
        map0 = parameterParser0.parse0("Unknown RFC 2047 encoding: ", charArray0)
        self.assertEqual(1, len(map0))

    def test18(self) -> None:

        parameterParser0 = ParameterParser()
        charArray0 = ["(", ""]
        map0 = parameterParser0.parse0("=8HTjM:*BF_P{F!!-(O", charArray0)
        self.assertFalse(parameterParser0.isLowerCaseNames())
        self.assertEqual(1, len(map0))

    def test17(self) -> None:

        parameterParser0 = ParameterParser()
        parameterParser0.parse0("FN>TZE6|X6KB!!;xr&", None)
        self.assertFalse(parameterParser0.isLowerCaseNames())

    def test16(self) -> None:

        parameterParser0 = ParameterParser()
        charArray0 = []
        parameterParser0.parse0("", charArray0)
        self.assertFalse(parameterParser0.isLowerCaseNames())

    def test15(self) -> None:

        parameterParser0 = ParameterParser()
        charArray0 = ["", ""]
        parameterParser0.parse0(None, charArray0)
        self.assertFalse(parameterParser0.isLowerCaseNames())

    def test14(self) -> None:

        parameterParser0 = ParameterParser()
        charArray0 = ["K", "K"]
        map0 = parameterParser0.parse0('K=""2O~9F', charArray0)
        self.assertFalse(parameterParser0.isLowerCaseNames())
        self.assertTrue(not map0)

    def test13(self) -> None:

        parameterParser0 = ParameterParser()
        parameterParser0.parse2(None, ")")
        self.assertFalse(parameterParser0.isLowerCaseNames())

    def test12(self) -> None:

        parameterParser0 = ParameterParser()
        parameterParser0.parse3(None, 66, 66, "/")
        self.assertFalse(parameterParser0.isLowerCaseNames())

    def test11(self) -> None:

        parameterParser0 = ParameterParser()
        charArray0 = [""] * 6
        charArray0[4] = "?"
        parameterParser0.setLowerCaseNames(True)

        with pytest.raises(IndexError):
            parameterParser0.parse3(charArray0, 0, 107, "?")

    def test10(self) -> None:

        parameterParser0 = ParameterParser()
        map0 = parameterParser0.parse1("J_2IM4Yt=c`", "w")
        self.assertFalse(parameterParser0.isLowerCaseNames())
        self.assertEqual(1, len(map0))

    def test09(self) -> None:

        parameterParser0 = ParameterParser()
        map0 = parameterParser0.parse1('=;Oj|YvQwe"', "V")
        self.assertEqual(0, len(map0))

    def test08(self) -> None:

        parameterParser0 = ParameterParser()
        parameterParser0.parse1(None, "K")
        self.assertFalse(parameterParser0.isLowerCaseNames())

    def test07(self) -> None:

        parameterParser0 = ParameterParser()
        charArray0 = ["", "", ""]
        map0 = parameterParser0.parse2(charArray0, "b")
        self.assertEqual(1, len(map0))
        self.assertFalse(parameterParser0.isLowerCaseNames())

    def test06(self) -> None:

        parameterParser0 = ParameterParser()
        charArray0 = [""] * 8
        map0 = parameterParser0.parse3(charArray0, 0, 2, "d")
        self.assertTrue(bool(map0))
        self.assertFalse(parameterParser0.isLowerCaseNames())

    def test05(self) -> None:

        parameterParser0 = ParameterParser()
        charArray0 = [""] * 8
        charArray0[1] = "="
        map0 = parameterParser0.parse3(charArray0, 0, 2, "d")
        self.assertEqual(1, len(map0))

    def test04(self) -> None:

        parameterParser0 = ParameterParser()
        charArray0 = [""] * 8
        charArray0[0] = "="
        map0 = parameterParser0.parse3(charArray0, 0, 2, "j")
        self.assertTrue(not map0)

    def test03(self) -> None:

        parameterParser0 = ParameterParser()
        self.assertFalse(parameterParser0.isLowerCaseNames())

        parameterParser0.setLowerCaseNames(True)
        boolean0 = parameterParser0.isLowerCaseNames()
        self.assertTrue(boolean0)

    def test02(self) -> None:

        parameterParser0 = ParameterParser()
        charArray0 = [""] * 6
        map0 = parameterParser0.parse3(charArray0, 0, -1, "/")
        self.assertFalse(parameterParser0.isLowerCaseNames())
        self.assertTrue(not map0)

    def test01(self) -> None:

        parameterParser0 = ParameterParser()
        charArray0 = ["="] * 3
        map0 = parameterParser0.parse2(charArray0, "b")
        self.assertTrue(not map0)

    def test00(self) -> None:

        parameterParser0 = ParameterParser()
        charArray0 = [""] * 4
        charArray0[2] = "#"
        charArray0[3] = "3"
        map0 = parameterParser0.parse0("%_NM#dicXH sb>;RR3", charArray0)
        self.assertEqual(2, len(map0))
