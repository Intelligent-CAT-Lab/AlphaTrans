from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.language.DoubleMetaphone import *

# from src.test.org.apache.commons.codec.language.DoubleMetaphone_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class DoubleMetaphone_ESTest(unittest.TestCase):

    def test142(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.doubleMetaphone1("KNMVWOGHXG", True)
        self.assertEqual(string0, "NMFK")

    def test141(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone0.setMaxCodeLen(489)
        self.assertEqual(489, doubleMetaphone0.getMaxCodeLen())

        string0 = doubleMetaphone0.doubleMetaphone1(
            "org.apache.commons.codec.EncoderException", False
        )
        self.assertEqual("ARKPXKMNSKTKNKTRKSPXN", string0)

    def test140(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.doubleMetaphone1("WICZ", True)
        self.assertEqual("FKTS", string0)
        self.assertIsNotNone(string0)
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())

    def test137(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone0.encode1(None)
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())

    def test134(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.doubleMetaphone1('}vJ"8auQ`ZY<djr|', False)
        assert string0 is not None
        assert string0 == "FJKS"

    def test133(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.doubleMetaphone1(")y{T,", False)
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())
        self.assertEqual("T", string0)

    def test132(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.encode1("Joq@4Bb{.+;|")
        self.assertEqual("JKP", string0)
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())

    def test131(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.encode1('gv%FFsz"0cgmXN|ADT')
        self.assertEqual("KFFS", string0)
        self.assertIsNotNone(string0)

    def test130(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.doubleMetaphone1("KNNLNP", True)
        assert string0 is not None
        assert string0 == "NLNP"

    def test129(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.doubleMetaphone1("~_w)WYAvH_EQQ#5p6", False)
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())
        self.assertEqual("FKP", string0)
        self.assertIsNotNone(string0)

    def test128(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        try:
            doubleMetaphone0.encode0(doubleMetaphone0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # DoubleMetaphone encode parameter is not of type String
            self.verifyException("org.apache.commons.codec.language.DoubleMetaphone", e)

    def test127(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.doubleMetaphone0("CHIA")
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())
        self.assertIsNotNone(string0)
        self.assertEqual("K", string0)

    def test126(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.doubleMetaphone0("CAESAR")
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())
        self.assertEqual("SSR", string0)
        self.assertIsNotNone(string0)

    def test125(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.encode1("ni8&a=%/Cz4Z")
        self.assertEqual("NSS", string0)
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())

    def test123(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.encode1("wb,M5CkfYOfe7Z5/Sf/")
        self.assertEqual(string0, "PMKF")

    def test122(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.doubleMetaphone0("Y4P1CI}YkHun9r%:|h")
        self.assertEqual(string0, "APSK")

    def test119(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        object0 = doubleMetaphone0.encode0("CCE")
        self.assertEqual("X", object0)

    def test117(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.encode1("CHORE")
        self.assertEqual(string0, "XR")
        self.assertIsNotNone(string0)

    def test116(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.encode1("MCHR")
        self.assertEqual("MKR", string0)

    def test115(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.encode1("DG")
        self.assertEqual("TK", string0)
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())

    def test114(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.doubleMetaphone0("KNDGY")
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())
        self.assertEqual("NJ", string0)
        self.assertIsNotNone(string0)

    def test113(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.encode1("$DD5*dUAY;")
        self.assertEqual("TT", string0)
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())

    def test112(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.encode1("oGN:")
        self.assertEqual("AKN", string0)
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())
        self.assertIsNotNone(string0)

    def test111(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        boolean0 = doubleMetaphone0.isDoubleMetaphoneEqual1(
            "8gnQDJ\u0002", "8gnQDJ\u0002", False
        )
        self.assertTrue(boolean0)

    def test110(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.encode1("GeBkap]=pBcMW'd")
        self.assertEqual(string0, "KPKP")

    def test109(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.encode1("MANGER")
        self.assertEqual(string0, "MNJR")

    def test108(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.doubleMetaphone1("OGY", True)
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())
        self.assertEqual("AK", string0)

    def test107(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.doubleMetaphone0("KN?GY")
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())
        self.assertEqual("NK", string0)

    def test105(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.encode1("GHjt4")
        self.assertEqual(string0, "KT")

    def test103(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.encode1("IGhniX%*(#")
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())
        self.assertEqual("ANKS", string0)
        self.assertIsNotNone(string0)

    def test102(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        boolean0 = doubleMetaphone0.isDoubleMetaphoneEqual0(None, "HO J~&G*:u,>.NW0A#")
        self.assertEqual(doubleMetaphone0.getMaxCodeLen(), 4)
        self.assertFalse(boolean0)

    def test100(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.doubleMetaphone0("JOSE")
        self.assertEqual(string0, "HS")

    def test097(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.doubleMetaphone0("iB}>I&f:}YJ@mB^3-6W")
        self.assertEqual("APFJ", string0)

    def test095(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone0.setMaxCodeLen(2556)
        doubleMetaphone0.doubleMetaphone1(" a *r,bvP]3g#2coJj<", False)
        self.assertEqual(2556, doubleMetaphone0.getMaxCodeLen())

    def test094(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.doubleMetaphone0("Z@,WOlJHhS")
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())
        self.assertEqual("SLS", string0)

    def test093(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.doubleMetaphone1("WRILLA", True)
        self.assertEqual("R", string0)
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())

    def test092(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.doubleMetaphone0("ALLwE")
        assert string0 is not None
        self.assertEqual(doubleMetaphone0.getMaxCodeLen(), 4)
        self.assertEqual(string0, "AL")

    def test091(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.doubleMetaphone0("?FgphvCi")
        self.assertEqual("FKFF", string0)
        self.assertIsNotNone(string0)

    def test090(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        boolean0 = doubleMetaphone0.isDoubleMetaphoneEqual0("WR", "KNPP")
        self.assertEqual(doubleMetaphone0.getMaxCodeLen(), 4)
        self.assertFalse(boolean0)

    def test085(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.encode1("s;zM]sH)b|4")
        self.assertEqual(string0, "SSMX")

    def test083(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.doubleMetaphone0("SIA")
        self.assertEqual("S", string0)
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())

    def test082(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.encode1("SN")
        self.assertEqual("SN", string0)
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())

    def test081(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone0.isDoubleMetaphoneEqual0("PSCH", "PSCH")
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())

    def test079(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.doubleMetaphone0("SCH")
        self.assertEqual("X", string0)
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())
        self.assertIsNotNone(string0)

    def test078(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.encode1("SCy")
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())
        self.assertIsNotNone(string0)
        self.assertEqual("S", string0)

    def test077(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.encode1("TCH")
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())
        self.assertEqual("X", string0)

    def test073(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.encode1("WH")
        assert string0 is not None
        self.assertEqual("A", string0)
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())

    def test072(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone0.isDoubleMetaphoneEqual0("t->mow ", "t->mow ")
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())

    def test070(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        boolean0 = doubleMetaphone0.isDoubleMetaphoneEqual1(
            "\!`t^+vtmI", "OWSKI", False
        )
        self.assertFalse(boolean0)

    def test067(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.doubleMetaphone0("o6zppx")
        self.assertEqual(string0, "ASPK")

    def test066(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.encode1("aA$Zh&LxS1wZp1}s2aJ")
        self.assertEqual(string0, "AJLK")

    def test065(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.doubleMetaphone0("I0zzyi")
        self.assertEqual("AS", string0)
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())

    def test064(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone0.isDoubleMetaphoneEqual1("KNACH", "", False)
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())

    def test061(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.encode1("ACH")
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())
        self.assertEqual("AK", string0)

    def test059(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.doubleMetaphone1("UMB", True)
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())
        self.assertEqual("AM", string0)

    def test058(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.encode1('>>UMB3]RX1tm~0&"')
        self.assertEqual(string0, "MPRK")

    def test057(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.doubleMetaphone1("W", False)
        self.assertEqual("", string0)
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())
        self.assertIsNotNone(string0)

    def test056(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone_DoubleMetaphoneResult0 = doubleMetaphone0.DoubleMetaphoneResult(
            4
        )
        doubleMetaphone_DoubleMetaphoneResult0.append3("GQXQp}+}2_X#", "K")
        boolean0 = doubleMetaphone_DoubleMetaphoneResult0.isComplete()
        self.assertEqual("K", doubleMetaphone_DoubleMetaphoneResult0.getAlternate())
        self.assertFalse(boolean0)

    def test055(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone_DoubleMetaphoneResult0 = DoubleMetaphone.DoubleMetaphoneResult(
            1
        )
        doubleMetaphone_DoubleMetaphoneResult0.getAlternate()
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())

    def test054(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone_DoubleMetaphoneResult0 = DoubleMetaphoneResult(1)
        doubleMetaphone_DoubleMetaphoneResult0.append2("WZ7f")
        self.assertEqual("W", doubleMetaphone_DoubleMetaphoneResult0.getAlternate())

    def test053(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone_DoubleMetaphoneResult0 = DoubleMetaphone.DoubleMetaphoneResult(
            1
        )
        doubleMetaphone_DoubleMetaphoneResult0.getPrimary()
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())

    def test052(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        int0 = doubleMetaphone0.getMaxCodeLen()
        self.assertEqual(4, int0)

    def test051(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone_DoubleMetaphoneResult0 = doubleMetaphone0.DoubleMetaphoneResult(
            (-450)
        )
        doubleMetaphone_DoubleMetaphoneResult0.append0("P")
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())
        self.assertEqual("", doubleMetaphone_DoubleMetaphoneResult0.getAlternate())
        self.assertEqual("", doubleMetaphone_DoubleMetaphoneResult0.getPrimary())

    def test050(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone_DoubleMetaphoneResult0 = doubleMetaphone0.DoubleMetaphoneResult(
            (-450)
        )
        doubleMetaphone_DoubleMetaphoneResult0.append1("J", "$")
        self.assertEqual("", doubleMetaphone_DoubleMetaphoneResult0.getPrimary())
        self.assertEqual("", doubleMetaphone_DoubleMetaphoneResult0.getAlternate())
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())

    def test049(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone0.doubleMetaphone1(None, False)
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())

    def test048(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.doubleMetaphone1("`?,I'Kh*CRChT^oq", False)
        self.assertEqual("KKRK", string0)

    def test047(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.doubleMetaphone1("sEGbbG4+$,z o", False)
        self.assertEqual("SKPK", string0)

    def test046(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.doubleMetaphone1("d'ffr?%du)\"", True)
        self.assertEqual("TFRT", string0)
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())

    def test045(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.doubleMetaphone1("AKKS", False)
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())
        self.assertEqual("AKS", string0)

    def test044(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.doubleMetaphone1("(4'He)4FAf7VvcC~", True)
        self.assertEqual("FFFK", string0)

    def test043(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone_DoubleMetaphoneResult0 = doubleMetaphone0.DoubleMetaphoneResult(
            5
        )
        doubleMetaphone_DoubleMetaphoneResult0.appendPrimary0("1")
        self.assertEqual("1", doubleMetaphone_DoubleMetaphoneResult0.getPrimary())

    def test042(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone_DoubleMetaphoneResult0 = doubleMetaphone0.DoubleMetaphoneResult(
            5
        )
        doubleMetaphone_DoubleMetaphoneResult0.append3(
            "2^hR}&vk%=i", 'OPp"cBJ3Yl00uC%D'
        )
        doubleMetaphone_DoubleMetaphoneResult0.appendAlternate0("1")
        self.assertEqual("2^hR}", doubleMetaphone_DoubleMetaphoneResult0.getPrimary())

    def test041(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone_DoubleMetaphoneResult0 = DoubleMetaphoneResult(83)
        doubleMetaphone_DoubleMetaphoneResult0.appendAlternate0("A")
        self.assertEqual("A", doubleMetaphone_DoubleMetaphoneResult0.getAlternate())

    def test040(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone_DoubleMetaphoneResult0 = DoubleMetaphone.DoubleMetaphoneResult(
            83
        )
        doubleMetaphone_DoubleMetaphoneResult0.appendPrimary1("")
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())

    def test039(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone_DoubleMetaphoneResult0 = DoubleMetaphoneResult(0)
        doubleMetaphone_DoubleMetaphoneResult0.appendPrimary1("y'%5A6i")
        self.assertEqual("", doubleMetaphone_DoubleMetaphoneResult0.getPrimary())
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())

    def test038(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone_DoubleMetaphoneResult0 = doubleMetaphone0.DoubleMetaphoneResult(
            1
        )
        doubleMetaphone_DoubleMetaphoneResult0.appendAlternate1('i~49,5M">bBIj`6{C$R')
        self.assertEqual("i", doubleMetaphone_DoubleMetaphoneResult0.getAlternate())

    def test037(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone_DoubleMetaphoneResult0 = DoubleMetaphone.DoubleMetaphoneResult(
            1904
        )
        doubleMetaphone_DoubleMetaphoneResult0.appendAlternate1("")
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())

    def test036(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone_DoubleMetaphoneResult0 = DoubleMetaphoneResult(4)
        boolean0 = doubleMetaphone_DoubleMetaphoneResult0.isComplete()
        self.assertFalse(boolean0)
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())

    def test035(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone_DoubleMetaphoneResult0 = DoubleMetaphoneResult((-4040))
        boolean0 = doubleMetaphone_DoubleMetaphoneResult0.isComplete()
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())
        self.assertTrue(boolean0)

    def test034(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        try:
            doubleMetaphone0._charAt(None, 86)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            pass

    def test033(self) -> None:

        try:
            DoubleMetaphone.contains(None, 3001, -1, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            pass

    def test032(self) -> None:

        stringArray0 = []
        try:
            DoubleMetaphone.contains("{,M", 2, (-3127), stringArray0)
            self.fail("Expecting exception: StringIndexOutOfBoundsException")

        except StringIndexOutOfBoundsException:
            pass

    def test031(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone0.setMaxCodeLen(-153869933)

        try:
            doubleMetaphone0.doubleMetaphone0("Hens(DH.P:dW1<")
            self.fail("Expecting exception: NegativeArraySizeException")

        except NegativeArraySizeException:
            self.verifyException("java.lang.AbstractStringBuilder")

    def test030(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone0.setMaxCodeLen(-545)

        try:
            doubleMetaphone0.doubleMetaphone1("M`U", False)
            self.fail("Expecting exception: NegativeArraySizeException")

        except NegativeArraySizeException:
            self.verifyException("java.lang.AbstractStringBuilder")

    def test026(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone0.setMaxCodeLen(-3036)

        try:
            doubleMetaphone0.encode0("org.apache.commons.codec.binary.StringUtils")
            self.fail("Expecting exception: NegativeArraySizeException")

        except NegativeArraySizeException:
            self.verifyException("java.lang.AbstractStringBuilder")

    def test025(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone0.setMaxCodeLen(-1)

        try:
            doubleMetaphone0.encode1("w ~mpSH")
            self.fail("Expecting exception: NegativeArraySizeException")

        except NegativeArraySizeException:
            self.verifyException("java.lang.AbstractStringBuilder")

    def test024(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone0.setMaxCodeLen(-53786696)

        with pytest.raises(NegativeArraySizeException):
            doubleMetaphone0.isDoubleMetaphoneEqual0(
                "KNJT8=]%J]@NZWHWTQCI", "KNJT8=]%J]@NZWHWTQCI"
            )

    def test023(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone0.setMaxCodeLen(-1742)

        with pytest.raises(NegativeArraySizeException):
            doubleMetaphone0.isDoubleMetaphoneEqual1("2'G?gT \"", ": ", False)

    def test022(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        char0 = doubleMetaphone0._charAt("8&Rhj1s},ogZD]1~", 4)
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())
        self.assertEqual("j", char0)

    def test021(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        char0 = doubleMetaphone0._charAt("]gC;9Vy8h", 4)
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())
        self.assertEqual("9", char0)

    def test020(self) -> None:

        stringArray0 = []
        boolean0 = DoubleMetaphone._contains("9o +gSm>o/(vTN[$c@", -1, -1, stringArray0)
        self.assertFalse(boolean0)

    def test019(self) -> None:

        stringArray0 = [""] * 3
        boolean0 = DoubleMetaphone._contains("", 0, 0, stringArray0)
        self.assertTrue(boolean0)

    def test018(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.doubleMetaphone0("/")
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())
        self.assertIsNotNone(string0)

    def test017(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone0.doubleMetaphone0(None)
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())

    def test013(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        object0 = doubleMetaphone0.encode0("")
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())
        self.assertIsNone(object0)

    def test012(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.encode1("4")
        assert string0 is not None
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())

    def test011(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone0.setMaxCodeLen(-1501)
        int0 = doubleMetaphone0.getMaxCodeLen()
        self.assertEqual(-1501, int0)

    def test010(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())

        doubleMetaphone0.setMaxCodeLen(0)
        int0 = doubleMetaphone0.getMaxCodeLen()
        self.assertEqual(0, int0)

    def test008(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.encode1("4IGhnX%*(")
        self.assertEqual(string0, "NKS")
        self.assertIsNotNone(string0)

    def test004(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        boolean0 = doubleMetaphone0.isDoubleMetaphoneEqual0("Z|z", "c*MU`#R%u Y_gI")
        self.assertFalse(boolean0)

    def test003(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        boolean0 = doubleMetaphone0.isDoubleMetaphoneEqual0("_Zb^s46tSWs-", "WRWZZ7F")
        self.assertEqual(doubleMetaphone0.getMaxCodeLen(), 4)
        self.assertFalse(boolean0)

    def test002(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        string0 = doubleMetaphone0.doubleMetaphone1("ALL", False)
        self.assertEqual("AL", string0)
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())

    def test001(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        char0 = doubleMetaphone0._charAt("+~5PB", 1538)
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())
        self.assertEqual("\x00", char0)

    def test000(self) -> None:

        doubleMetaphone0 = DoubleMetaphone()
        doubleMetaphone_DoubleMetaphoneResult0 = DoubleMetaphoneResult(0)
        doubleMetaphone_DoubleMetaphoneResult0.appendPrimary0("&")
        self.assertEqual(4, doubleMetaphone0.getMaxCodeLen())
        self.assertEqual("", doubleMetaphone_DoubleMetaphoneResult0.getPrimary())
