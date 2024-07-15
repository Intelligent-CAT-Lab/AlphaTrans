from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.language.Metaphone import *

# from src.test.org.apache.commons.codec.language.Metaphone_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Metaphone_ESTest(unittest.TestCase):

    def test48(self) -> None:
        metaphone0 = Metaphone()
        metaphone0.metaphone(None)
        self.assertEqual(4, metaphone0.getMaxCodeLen())

    def test47(self) -> None:
        metaphone0 = Metaphone()
        string0 = metaphone0.encode1("A!--(,BJU")
        self.assertEqual(string0, "ABJ")
        self.assertEqual(metaphone0.getMaxCodeLen(), 4)

    def test46(self) -> None:
        metaphone0 = Metaphone()
        string0 = metaphone0.encode1("Ku4>w:+UX3~Qbv9e 9s")
        self.assertEqual(string0, "KKSK")

    def test45(self) -> None:

        metaphone0 = Metaphone()
        string0 = metaphone0.metaphone("WhkT<")
        self.assertEqual("K0", string0)
        self.assertEqual(4, metaphone0.getMaxCodeLen())

    def test44(self) -> None:
        metaphone0 = Metaphone()
        string0 = metaphone0.metaphone("AEIOU")
        self.assertEqual(4, metaphone0.getMaxCodeLen())
        self.assertEqual("E", string0)

    def test43(self) -> None:
        metaphone0 = Metaphone()
        string0 = metaphone0.metaphone("wR")
        self.assertEqual(4, metaphone0.getMaxCodeLen())
        self.assertEqual("R", string0)

    def test42(self) -> None:

        metaphone0 = Metaphone()
        string0 = metaphone0.metaphone("Wse[)mb")
        # Unstable assertion: self.assertEqual(4, metaphone0.getMaxCodeLen())
        # Unstable assertion: self.assertEqual("XM", string0)

    def test41(self) -> None:
        metaphone0 = Metaphone()
        string0 = metaphone0.metaphone("SC")
        self.assertEqual(4, metaphone0.getMaxCodeLen())
        self.assertEqual("SK", string0)

    def test40(self) -> None:
        metaphone0 = Metaphone()
        string0 = metaphone0.encode1("y_*C'EscEHJp'vLx,")
        self.assertEqual(string0, "KXJP")

    def test39(self) -> None:

        metaphone0 = Metaphone()
        string0 = metaphone0.metaphone("TsCH")
        self.assertEqual("XSK", string0)
        self.assertEqual(4, metaphone0.getMaxCodeLen())

    def test38(self) -> None:

        metaphone0 = Metaphone()
        string0 = metaphone0.metaphone("CHgE")
        # Unstable assertion: self.assertEqual(4, metaphone0.getMaxCodeLen())
        # Unstable assertion: self.assertEqual("X", string0)

    def test37(self) -> None:
        metaphone0 = Metaphone()
        string0 = metaphone0.metaphone("CH")
        self.assertEqual(4, metaphone0.getMaxCodeLen())
        self.assertEqual("X", string0)

    def test36(self) -> None:
        metaphone0 = Metaphone()
        string0 = metaphone0.metaphone("CHE")
        self.assertEqual("K", string0)
        self.assertEqual(4, metaphone0.getMaxCodeLen())

    def test35(self) -> None:
        metaphone0 = Metaphone()
        object0 = metaphone0.encode0("vS-#Dghx(jKP}3U")
        #  // Unstable assertion: assertEquals("FXTK", object0);
        self.assertEqual("FXTK", object0)

    def test34(self) -> None:
        metaphone0 = Metaphone()
        string0 = metaphone0.encode1("GH")
        self.assertEqual(4, metaphone0.getMaxCodeLen())
        self.assertEqual("", string0)

    def test33(self) -> None:

        metaphone0 = Metaphone()
        string0 = metaphone0.metaphone("2Wbi4GjH*VHiBK0")
        self.assertEqual("BJFH", string0)

    def test32(self) -> None:
        metaphone0 = Metaphone()
        string0 = metaphone0.metaphone("_4OxWCKa`Y")
        self.assertEqual(4, metaphone0.getMaxCodeLen())
        self.assertEqual("KSK", string0)

    def test30(self) -> None:

        metaphone0 = Metaphone()
        string0 = metaphone0.encode1("TPyIA")
        self.assertEqual("XPY", string0)
        self.assertEqual(4, metaphone0.getMaxCodeLen())

    def test29(self) -> None:
        metaphone0 = Metaphone()
        int0 = metaphone0.getMaxCodeLen()
        self.assertEqual(4, int0)

    def test28(self) -> None:
        metaphone0 = Metaphone()
        metaphone0.metaphone("")
        self.assertEqual(4, metaphone0.getMaxCodeLen())

    def test27(self) -> None:
        metaphone0 = Metaphone()
        string0 = metaphone0.metaphone("^")
        self.assertEqual("^", string0)
        self.assertEqual(4, metaphone0.getMaxCodeLen())

    def test26(self) -> None:
        metaphone0 = Metaphone()
        string0 = metaphone0.metaphone("KB")
        self.assertEqual(4, metaphone0.getMaxCodeLen())
        self.assertEqual("KB", string0)

    def test25(self) -> None:

        metaphone0 = Metaphone()
        string0 = metaphone0.metaphone("PLPX")
        self.assertEqual(string0, "PLPK")

    def test24(self) -> None:
        metaphone0 = Metaphone()
        string0 = metaphone0.metaphone("GH")
        self.assertEqual(4, metaphone0.getMaxCodeLen())
        self.assertEqual("", string0)

    def test23(self) -> None:

        metaphone0 = Metaphone()
        string0 = metaphone0.metaphone("X^ x,$Su5M)?")
        # Unstable assertion: self.assertEqual("XKSX", string0)

    def test22(self) -> None:
        metaphone0 = Metaphone()
        string0 = metaphone0.metaphone("GN")
        self.assertEqual(4, metaphone0.getMaxCodeLen())
        self.assertEqual("N", string0)

    def test21(self) -> None:

        metaphone0 = Metaphone()
        string0 = metaphone0.metaphone("A{VN+x4")
        self.assertEqual(string0, "AFNK")

    def test20(self) -> None:
        metaphone0 = Metaphone()
        string0 = metaphone0.metaphone("CYD+Oj")
        self.assertEqual("STJ", string0)
        self.assertEqual(4, metaphone0.getMaxCodeLen())

    def test19(self) -> None:

        metaphone0 = Metaphone()
        string0 = metaphone0.metaphone("EtmB9EE O")
        # Unstable assertion: self.assertEqual(4, metaphone0.getMaxCodeLen())
        # Unstable assertion: self.assertEqual("EXMB", string0)

    def test18(self) -> None:

        metaphone0 = Metaphone()
        string0 = metaphone0.metaphone("fC4No[C")
        self.assertEqual("FXNK", string0)
        self.assertEqual(4, metaphone0.getMaxCodeLen())

    def test17(self) -> None:

        metaphone0 = Metaphone()
        string0 = metaphone0.metaphone("u6bTADI")
        # Unstable assertion: self.assertEqual(4, metaphone0.getMaxCodeLen())
        # Unstable assertion: self.assertEqual("UB0T", string0)

    def test16(self) -> None:

        metaphone0 = Metaphone()
        string0 = metaphone0.metaphone("wDGy?ZTA")
        self.assertEqual("JS0", string0)
        self.assertEqual(4, metaphone0.getMaxCodeLen())

    def test15(self) -> None:

        metaphone0 = Metaphone()
        string0 = metaphone0.metaphone("vS-#Dghx(jKP}3U")
        self.assertEqual("FXTK", string0)

    def test14(self) -> None:

        metaphone0 = Metaphone()
        string0 = metaphone0.metaphone('e;{0=K~GhIZqp"%u ')
        self.assertEqual(string0, "EKKS")

    def test13(self) -> None:
        metaphone0 = Metaphone()
        string0 = metaphone0.metaphone("GE")
        self.assertEqual(4, metaphone0.getMaxCodeLen())
        self.assertEqual("J", string0)

    def test12(self) -> None:
        metaphone0 = Metaphone()
        string0 = metaphone0.metaphone("TG")
        self.assertEqual(4, metaphone0.getMaxCodeLen())
        self.assertEqual("TK", string0)

    def test11(self) -> None:
        metaphone0 = Metaphone()
        string0 = metaphone0.metaphone("hqp")
        self.assertEqual(4, metaphone0.getMaxCodeLen())
        self.assertEqual("KP", string0)

    def test10(self) -> None:
        metaphone0 = Metaphone()
        metaphone0.setMaxCodeLen(83)
        metaphone0.metaphone("org.apache.commons.codec.language.Metaphone")
        self.assertEqual(83, metaphone0.getMaxCodeLen())

    def test09(self) -> None:

        metaphone0 = Metaphone()
        string0 = metaphone0.metaphone("RTLK")
        self.assertEqual("RXLK", string0)
        self.assertEqual(4, metaphone0.getMaxCodeLen())

    def test08(self) -> None:

        metaphone0 = Metaphone()
        string0 = metaphone0.metaphone("/LcTwO}XcqbhQI>XCyB")
        self.assertEqual("LKWK", string0)

    def test07(self) -> None:
        metaphone0 = Metaphone()
        string0 = metaphone0.metaphone("EIY")
        self.assertEqual("E", string0)
        self.assertEqual(4, metaphone0.getMaxCodeLen())

    def test06(self) -> None:
        metaphone0 = Metaphone()
        try:
            metaphone0.encode0(metaphone0)
            self.fail("Expecting exception: Exception")
        except Exception as e:
            # Parameter supplied to Metaphone encode is not of type java.lang.String
            self.verifyException("org.apache.commons.codec.language.Metaphone", e)

    def test03(self) -> None:
        metaphone0 = Metaphone()
        metaphone0.setMaxCodeLen(-2135)
        int0 = metaphone0.getMaxCodeLen()
        self.assertEqual(-2135, int0)

    def test02(self) -> None:
        metaphone0 = Metaphone()
        self.assertEqual(4, metaphone0.getMaxCodeLen())
        metaphone0.setMaxCodeLen(0)
        int0 = metaphone0.getMaxCodeLen()
        self.assertEqual(0, int0)

    def test01(self) -> None:
        metaphone0 = Metaphone()
        self.assertTrue(metaphone0.isMetaphoneEqual("/p", "/p"))
        self.assertEqual(4, metaphone0.getMaxCodeLen())

    def test00(self) -> None:
        metaphone0 = Metaphone()
        boolean0 = metaphone0.isMetaphoneEqual(
            "#jg_hah[Ya|GvHx&gd", "[i$d&Egr.(HJuNUgQ2"
        )
        self.assertEqual(metaphone0.getMaxCodeLen(), 4)
        self.assertFalse(boolean0)
