from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.language.MatchRatingApproachEncoder import *

# from src.test.org.apache.commons.codec.language.MatchRatingApproachEncoder_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class MatchRatingApproachEncoder_ESTest(unittest.TestCase):

    def test52(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        object0 = matchRatingApproachEncoder0.encode0("1%Nc'cR@b:b")
        self.assertEqual("1%NB:B", object0)

    def test51(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        string0 = matchRatingApproachEncoder0.encode1(None)
        self.assertEqual("", string0)

    def test49(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        string0 = matchRatingApproachEncoder0.encode1("&")
        self.assertEqual("", string0)

    def test48(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        boolean0 = matchRatingApproachEncoder0.isEncodeEquals("-o@l", "Jt|M")
        self.assertFalse(boolean0)

    def test47(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        int0 = matchRatingApproachEncoder0.getMinRating(-1)
        self.assertEqual(5, int0)

    def test46(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        boolean0 = matchRatingApproachEncoder0.isEncodeEquals("PX#6", "pX#'6")
        self.assertTrue(boolean0)

    def test45(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        boolean0 = matchRatingApproachEncoder0.isEncodeEquals(
            "org.apache.commons.codec.EncoderException", "Z}%6*)M"
        )
        self.assertFalse(boolean0)

    def test44(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        int0 = matchRatingApproachEncoder0.getMinRating(31)
        self.assertEqual(1, int0)

    def test43(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        boolean0 = matchRatingApproachEncoder0.isEncodeEquals(None, None)
        self.assertFalse(boolean0)

    def test42(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        boolean0 = matchRatingApproachEncoder0.isEncodeEquals("", "")
        self.assertFalse(boolean0)

    def test41(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        boolean0 = matchRatingApproachEncoder0.isEncodeEquals(" ", "%5lh3a}w_")
        self.assertFalse(boolean0)

    def test40(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        boolean0 = matchRatingApproachEncoder0.isEncodeEquals(":/", None)
        self.assertFalse(boolean0)

    def test39(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        boolean0 = matchRatingApproachEncoder0.isEncodeEquals("1E[{rd1", "")
        self.assertFalse(boolean0)

    def test38(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        boolean0 = matchRatingApproachEncoder0.isEncodeEquals('~p0)"k', " ")
        self.assertFalse(boolean0)

    def test37(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        boolean0 = matchRatingApproachEncoder0.isEncodeEquals("k/Q+}AeK ", "k/Q+}AeK ")
        self.assertFalse(boolean0)

    def test36(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        boolean0 = matchRatingApproachEncoder0.isEncodeEquals("4f)", "n")
        self.assertFalse(boolean0)

    def test35(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        boolean0 = matchRatingApproachEncoder0.isEncodeEquals("b+c", "b+c")
        self.assertTrue(boolean0)

    def test32(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        string0 = matchRatingApproachEncoder0.removeVowels("upc1@|{3(")
        self.assertEqual("uupc1@|{3(", string0)

    def test31(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        boolean0 = matchRatingApproachEncoder0.isEncodeEquals(
            "org.apache.ommons.cdec.EncodrExcepti=n", "J}$ru"
        )
        self.assertFalse(boolean0)

    def test30(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        string0 = matchRatingApproachEncoder0.removeAccents(None)
        self.assertIsNone(string0)

    def test29(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        string0 = matchRatingApproachEncoder0.encode1(
            "�àÈèÌìÒòÙ��áéÉèÍìÓòÚ�Ý�ÂêÊîÎôÔ�Ý�ÃãÕ�ÑñÇçÑñÅåÑñÆæØ�Ý�ÄäËëÏïÖ�Ü�Ÿ�Ååß"
        )
        self.assertEqual("AYYNYC", string0)

    def test28(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        try:
            matchRatingApproachEncoder0.encode0(matchRatingApproachEncoder0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Parameter supplied to Match Rating Approach encoder is not of type java.lang.String
            self.verifyException(
                "org.apache.commons.codec.language.MatchRatingApproachEncoder", e
            )

    def test27(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        string0 = matchRatingApproachEncoder0.encode1("")
        self.assertEqual("", string0)

    def test26(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        string0 = matchRatingApproachEncoder0.encode1(" ")
        self.assertEqual("", string0)

    def test25(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()

        try:
            matchRatingApproachEncoder0.cleanName(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException(
                "org.apache.commons.codec.language.MatchRatingApproachEncoder", e
            )

    def test23(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        # Undeclared exception
        try:
            matchRatingApproachEncoder0.getFirst3Last3(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException(
                "org.apache.commons.codec.language.MatchRatingApproachEncoder", e
            )

    def test22(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        # Undeclared exception in Java, so we'll use a try-except block
        try:
            matchRatingApproachEncoder0.isEncodeEquals("-,", "TT")
            self.fail("Expecting exception: StringIndexOutOfBoundsException")
        except StringIndexOutOfBoundsException:
            pass

    def test21(self) -> None:
        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        with self.assertRaises(RuntimeError):
            matchRatingApproachEncoder0.isVowel(None)

    def test20(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()

        try:
            matchRatingApproachEncoder0.leftToRightThenRightToLeftProcessing(
                None, "NZ3rt+;XmI"
            )
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException(
                "org.apache.commons.codec.language.MatchRatingApproachEncoder", e
            )

    def test19(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        # Undeclared exception
        try:
            matchRatingApproachEncoder0.removeDoubleConsonants(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException(
                "org.apache.commons.codec.language.MatchRatingApproachEncoder", e
            )

    def test18(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()

        with self.assertRaises(RuntimeError):
            matchRatingApproachEncoder0.removeVowels(None)

    def test17(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()

        with pytest.raises(IndexError):
            matchRatingApproachEncoder0.removeVowels("")

    def test16(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        string0 = matchRatingApproachEncoder0.cleanName("")
        self.assertEqual("", string0)

    def test15(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        string0 = matchRatingApproachEncoder0.cleanName("8")
        self.assertEqual("8", string0)

    def test13(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        string0 = matchRatingApproachEncoder0.getFirst3Last3("")
        self.assertEqual("", string0)

    def test12(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        string0 = matchRatingApproachEncoder0.getFirst3Last3(";{wHwQS)Y'6I<\"B")
        self.assertEqual(';{w<"B', string0)

    def test11(self) -> None:
        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        boolean0 = matchRatingApproachEncoder0.isVowel("QQ")
        self.assertFalse(boolean0)

    def test10(self) -> None:
        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        boolean0 = matchRatingApproachEncoder0.isVowel("I")
        self.assertTrue(boolean0)

    def test09(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        int0 = matchRatingApproachEncoder0.leftToRightThenRightToLeftProcessing(
            "HX]NWH", 'Hx]lY2"snxKnWh'
        )
        self.assertEqual(6, int0)

    def test08(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        int0 = matchRatingApproachEncoder0.leftToRightThenRightToLeftProcessing(
            "PJm(OV", "<@c-Ks"
        )
        self.assertEqual(0, int0)

    def test07(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        string0 = matchRatingApproachEncoder0.removeAccents("")
        self.assertEqual("", string0)

    def test06(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        string0 = matchRatingApproachEncoder0.removeAccents(
            "org.apache.commons.codec.language.MatchRatingApproachEncoder"
        )
        self.assertEqual(
            "org.apache.commons.codec.language.MatchRatingApproachEncoder", string0
        )

    def test05(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        string0 = matchRatingApproachEncoder0.removeDoubleConsonants("")
        self.assertEqual("", string0)

    def test04(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        string0 = matchRatingApproachEncoder0.removeDoubleConsonants("E")
        self.assertEqual("E", string0)

    def test03(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        boolean0 = matchRatingApproachEncoder0.isEncodeEquals("QE", "b+c")
        self.assertFalse(boolean0)

    def test02(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        int0 = matchRatingApproachEncoder0.getMinRating(6)
        self.assertEqual(4, int0)

    def test01(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        boolean0 = matchRatingApproachEncoder0.isEncodeEquals("=]DG9?", "S )R2B")
        self.assertFalse(boolean0)

    def test00(self) -> None:

        matchRatingApproachEncoder0 = MatchRatingApproachEncoder()
        boolean0 = matchRatingApproachEncoder0.isEncodeEquals(
            "8p!!@r^+{|]X;%*HL", "[,]"
        )
        self.assertFalse(boolean0)
