from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.language.Caverphone1 import *
from src.main.org.apache.commons.codec.language.DoubleMetaphone import *
from src.main.org.apache.commons.codec.language.Nysiis import *
from src.main.org.apache.commons.codec.language.Soundex import *
from src.main.org.apache.commons.codec.language.SoundexUtils import *

# from src.test.org.apache.commons.codec.language.SoundexUtils_ESTest_scaffolding import *
from src.main.org.apache.commons.codec.net.QuotedPrintableCodec import *
from src.main.org.apache.commons.codec.net.URLCodec import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class SoundexUtils_ESTest(unittest.TestCase):

    def test14(self) -> None:
        soundexUtils0 = SoundexUtils()

    def test13(self) -> None:

        nysiis0 = Nysiis(True)
        int0 = SoundexUtils.difference(nysiis0, None, "+43U")
        self.assertEqual(0, int0)

    def test12(self) -> None:

        string0 = SoundexUtils.clean(None)
        self.assertIsNone(string0)

    def test11(self) -> None:

        string0 = SoundexUtils.clean("")
        self.assertEqual("", string0)

    def test10(self) -> None:

        nysiis0 = Nysiis(True)
        int0 = SoundexUtils.difference(nysiis0, "TT", "a]]T0")
        self.assertEqual(0, int0)

    def test09(self) -> None:

        soundex0 = Soundex.US_ENGLISH_GENEALOGY
        int0 = SoundexUtils.difference(soundex0, "6B3<. lZ#Hvq2}r", None)
        self.assertEqual(0, int0)

    def test08(self) -> None:

        int0 = SoundexUtils.differenceEncoded("w3", "w3")
        self.assertEqual(2, int0)

    def test07(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec3(True)

        try:
            SoundexUtils.difference(quotedPrintableCodec0, "", "")
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.verifyException("org.apache.commons.codec.net.QuotedPrintableCodec", e)

    def test06(self) -> None:

        charArray0 = [""] * 2
        soundex0 = Soundex(0, True, "", charArray0)

        try:
            SoundexUtils.difference(
                soundex0, "re>K3]qov//$BCi*N", "01230120022455012623010202"
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.apache.commons.codec.language.Soundex", e)

    def test05(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone0.setMaxCodeLen(-1767)

        try:
            SoundexUtils.difference(doubleMetaphone0, "D%|5", "G'm//{nD4[7Z4zH3Z/")
            self.fail("Expecting exception: NegativeArraySizeException")

        except NegativeArraySizeException as e:
            self.verifyException("java.lang.AbstractStringBuilder", e)

    def test04(self) -> None:

        try:
            SoundexUtils.difference(
                None, "01230120022455012623010202", "01230120022455012623010202"
            )
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(type(e)), "<class 'RuntimeError'>")
            self.verifyException("org.apache.commons.codec.language.SoundexUtils", e)

    def test03(self) -> None:

        uRLCodec0 = URLCodec("$")
        try:
            SoundexUtils.difference(uRLCodec0, "$", "$")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            self.verifyException("org.apache.commons.codec.net.URLCodec", e)

    def test02(self) -> None:

        string0 = SoundexUtils.clean("^D+mkc^3m+C$Tf*wEV")
        self.assertEqual("DMKCMCTFWEV", string0)

    def test01(self) -> None:

        caverphone1_0 = Caverphone1()
        int0 = SoundexUtils.difference(caverphone1_0, "3kh3", 'oFyd^R@gA"+v')
        self.assertEqual(1, int0)

    def test00(self) -> None:

        int0 = SoundexUtils.differenceEncoded("+;QPb(ml$JI1G.@rw", "")
        self.assertEqual(0, int0)
