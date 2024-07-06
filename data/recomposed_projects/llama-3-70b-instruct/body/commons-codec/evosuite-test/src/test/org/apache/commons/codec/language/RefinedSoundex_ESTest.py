from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.language.RefinedSoundex import *

# from src.test.org.apache.commons.codec.language.RefinedSoundex_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class RefinedSoundex_ESTest(unittest.TestCase):

    def test25(self) -> None:

        charArray0 = [""] * 17
        refinedSoundex0 = RefinedSoundex(1, "B7#wj/6Yh/", charArray0)

        try:
            refinedSoundex0.difference("B7#wj/6Yh/", "B7#wj/6Yh/")
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError:
            pass

    def test24(self) -> None:

        charArray0 = [""] * 9
        refinedSoundex0 = RefinedSoundex(
            0, "org.apache.commons.codec.EncoderException", charArray0
        )
        char0 = refinedSoundex0.getMappingCode("U")
        self.assertEqual("o", char0)

    def test23(self) -> None:

        refinedSoundex0 = RefinedSoundex(-1, "", None)

    def test22(self) -> None:

        charArray0 = [""] * 17
        refinedSoundex0 = RefinedSoundex(1, "PB[)'zS]s*a2JIM_", charArray0)

        try:
            refinedSoundex0.encode0("PB[)'zS]s*a2JIM_")
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except ArrayIndexOutOfBoundsException:
            pass

    def test21(self) -> None:

        charArray0 = ["\0"] * 17
        refinedSoundex0 = RefinedSoundex(1, "em2_", charArray0)
        char0 = refinedSoundex0.getMappingCode("3")
        self.assertEqual("\0", char0)

    def test19(self) -> None:

        charArray0 = [""] * 17
        refinedSoundex0 = RefinedSoundex(1, "em2_", charArray0)
        string0 = refinedSoundex0.encode1("")
        self.assertEqual("", string0)

    def test18(self) -> None:

        charArray0 = ["\0"] * 17
        charArray0[4] = "."
        refinedSoundex0 = RefinedSoundex(1, "em2_", charArray0)
        string0 = refinedSoundex0.encode1("em2_")
        self.assertEqual("E.", string0)

    def test17(self) -> None:

        refined_soundex0 = RefinedSoundex.US_ENGLISH
        try:
            refined_soundex0.encode0(None)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Parameter supplied to RefinedSoundex encode is not of type java.lang.String
            self.verifyException("org.apache.commons.codec.language.RefinedSoundex", e)

    def test16(self) -> None:

        refinedSoundex0 = RefinedSoundex.US_ENGLISH
        string0 = refinedSoundex0.soundex("")
        self.assertEqual("", string0)

    def test15(self) -> None:

        refinedSoundex0 = RefinedSoundex.US_ENGLISH
        string0 = refinedSoundex0.soundex(None)
        self.assertIsNone(string0)

    def test14(self) -> None:

        refinedSoundex0 = RefinedSoundex.US_ENGLISH
        string0 = refinedSoundex0.US_ENGLISH.soundex("S_A{VA;rY7a9R[Y_T")
        self.assertEqual("S302090906", string0)

    def test13(self) -> None:

        charArray0 = [None] * 17
        refinedSoundex0 = RefinedSoundex(
            1, "org.apache.commons.codec.language.RefinedSoundex", charArray0
        )

        with pytest.raises(ArrayIndexOutOfBoundsException):
            refinedSoundex0.soundex("org.apache.commons.codec.language.RefinedSoundex")

    def test12(self) -> None:

        refinedSoundex0 = None
        try:
            refinedSoundex0 = RefinedSoundex(1, "q", None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("org.apache.commons.codec.language.RefinedSoundex", e)

    def test09(self) -> None:

        charArray0 = ["\0"] * 17
        refinedSoundex0 = RefinedSoundex(0, "h", charArray0)

        with pytest.raises(ArrayIndexOutOfBoundsException):
            refinedSoundex0.encode1("h")

    def test08(self) -> None:

        charArray0 = ["\0"] * 17
        refinedSoundex0 = RefinedSoundex(1, "", charArray0)

        with self.assertRaises(ArrayIndexOutOfBoundsException):
            refinedSoundex0.getMappingCode("x")

    def test07(self) -> None:

        refinedSoundex0 = RefinedSoundex.US_ENGLISH
        int0 = refinedSoundex0.difference('jxcuW`>v8iX"L{MS+(', "S_A{VA;rY7a9R[Y_T")
        self.assertEqual(2, int0)

    def test06(self) -> None:

        refinedSoundex0 = RefinedSoundex.US_ENGLISH
        int0 = refinedSoundex0.difference("01360240043788015936020505", "")
        self.assertEqual(0, int0)

    def test02(self) -> None:

        charArray0 = []
        refinedSoundex0 = RefinedSoundex(2, None, charArray0)
        object0 = refinedSoundex0.encode0("org.apache.commons.codec.EncoderException")
        self.assertEqual("O094010303080830603083060905301608", object0)

    def test01(self) -> None:

        refinedSoundex0 = RefinedSoundex.US_ENGLISH
        string0 = refinedSoundex0.encode1(None)
        self.assertIsNone(string0)

    def test00(self) -> None:

        refinedSoundex0 = RefinedSoundex.US_ENGLISH
        char0 = refinedSoundex0.getMappingCode("K")
        self.assertEqual("3", char0)
