from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.language.ColognePhonetic import *

# from src.test.org.apache.commons.codec.language.ColognePhonetic_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class ColognePhonetic_ESTest(unittest.TestCase):

    def test22(self) -> None:

        colognePhonetic0 = ColognePhonetic()
        string0 = colognePhonetic0.colognePhonetic("Cr}zYk/R{;i0az<Z?o")
        self.assertEqual("478478", string0)

    def test21(self) -> None:
        colognePhonetic0 = ColognePhonetic()
        boolean0 = colognePhonetic0.isEncodeEqual("[xL]-Kivs$O^bBhz", 'c[b,g9"b}U1')
        self.assertFalse(boolean0)

    def test18(self) -> None:

        colognePhonetic0 = ColognePhonetic()
        string0 = colognePhonetic0.encode1(None)
        self.assertIsNone(string0)

    def test17(self) -> None:

        colognePhonetic0 = ColognePhonetic()
        string0 = colognePhonetic0.colognePhonetic(
            "org.apache.commons.codec.language.ColognePhonetic$CologneOutputBuffer"
        )
        self.assertEqual("074144668285644454636284546212137", string0)

    def test16(self) -> None:

        colognePhonetic0 = ColognePhonetic()
        object0 = colognePhonetic0.encode0("<EWVtcAaI$g.J[$IC")
        self.assertEqual("038448", object0)

    def test15(self) -> None:

        colognePhonetic0 = ColognePhonetic()
        string0 = colognePhonetic0.colognePhonetic("iJm_R$9qcx")
        self.assertEqual("06748", string0)

    def test14(self) -> None:

        colognePhonetic0 = ColognePhonetic()
        string0 = colognePhonetic0.colognePhonetic(None)
        self.assertIsNone(string0)

    def test13(self) -> None:

        colognePhonetic0 = ColognePhonetic()
        string0 = colognePhonetic0.colognePhonetic("?%DZ ")
        self.assertEqual("8", string0)

    def test12(self) -> None:

        colognePhonetic0 = ColognePhonetic()
        string0 = colognePhonetic0.colognePhonetic(
            "org.apache.commons.codec.EncoderException"
        )
        self.assertEqual("07414466828642748126", string0)

    def test11(self) -> None:

        colognePhonetic0 = ColognePhonetic()
        string0 = colognePhonetic0.colognePhonetic('c[b,g9"b}U1')
        self.assertEqual("8141", string0)

    def test10(self) -> None:

        colognePhonetic0 = ColognePhonetic()

        try:
            colognePhonetic0.encode0(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.codec.language.ColognePhonetic", e)

    def test08(self) -> None:

        colognePhonetic0 = ColognePhonetic()
        object0 = object()
        try:
            colognePhonetic0.encode0(object0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # This method's parameter was expected to be of the type java.lang.String. But actually it was of the type java.lang.Object.
            self.verifyException("org.apache.commons.codec.language.ColognePhonetic", e)

    def test07(self) -> None:

        colognePhonetic0 = ColognePhonetic()
        try:
            colognePhonetic0.isEncodeEqual(None, None)
            self.fail("Expecting exception: RuntimeError")
        except Exception as e:
            self.assertEqual(str(e), "Expecting exception: RuntimeError")

    def test06(self) -> None:

        colognePhonetic0 = ColognePhonetic()
        string0 = colognePhonetic0.colognePhonetic("03")
        self.assertEqual("", string0)

    def test02(self) -> None:

        colognePhonetic0 = ColognePhonetic()
        string0 = colognePhonetic0.encode1("+3,")
        self.assertEqual("", string0)

    def test01(self) -> None:

        colognePhonetic0 = ColognePhonetic()
        string0 = colognePhonetic0.encode1("A@xLt=oZG0D`m:'")
        self.assertEqual("048528426", string0)

    def test00(self) -> None:
        colognePhonetic0 = ColognePhonetic()
        boolean0 = colognePhonetic0.isEncodeEqual('c[b,g9"b}U1', 'c[b,g9"b}U1')
        self.assertTrue(boolean0)
