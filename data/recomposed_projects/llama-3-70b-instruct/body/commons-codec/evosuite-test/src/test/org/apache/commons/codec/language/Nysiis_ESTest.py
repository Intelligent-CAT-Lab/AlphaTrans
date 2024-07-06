from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.language.Nysiis import *

# from src.test.org.apache.commons.codec.language.Nysiis_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Nysiis_ESTest(unittest.TestCase):

    def test25(self) -> None:

        nysiis0 = Nysiis.Nysiis1()
        string0 = nysiis0.nysiis("org.apache.commons.codec.EncoderException")
        self.assertEqual("ORGAPA", string0)
        self.assertIsNotNone(string0)

    def test24(self) -> None:

        nysiis0 = Nysiis.Nysiis1()
        object0 = nysiis0.encode0("c}=[ljGyI?xU<h4{Ui")
        self.assertEqual("CLJGYA", object0)
        self.assertIsNotNone(object0)

    def test23(self) -> None:

        nysiis0 = Nysiis.Nysiis1()
        string0 = nysiis0.encode1("By@EbheBevSR p2+n")
        self.assertEqual("BYABAB", string0)
        self.assertIsNotNone(string0)

    def test22(self) -> None:

        nysiis0 = Nysiis.Nysiis1()
        object0 = nysiis0.encode0("Ybqp-Hd(")
        self.assertTrue(nysiis0.isStrict())
        self.assertEqual("YBGFD", object0)

    def test21(self) -> None:

        nysiis0 = Nysiis.Nysiis1()
        string0 = nysiis0.nysiis(")-ZF*!\u0002'6Jjp}kNy")
        self.assertEqual("ZFJPNY", string0)
        self.assertTrue(nysiis0.isStrict())

    def test20(self) -> None:

        nysiis0 = Nysiis.Nysiis1()
        string0 = nysiis0.encode1("8caW")
        self.assertTrue(nysiis0.isStrict())
        self.assertEqual("C", string0)
        self.assertIsNotNone(string0)

    def test18(self) -> None:

        nysiis0 = Nysiis(False)
        nysiis0.nysiis(None)
        self.assertFalse(nysiis0.isStrict())

    def test17(self) -> None:

        nysiis0 = Nysiis.Nysiis1()
        nysiis0.encode1("")
        self.assertTrue(nysiis0.isStrict())

    def test15(self) -> None:

        nysiis0 = Nysiis(False)
        object0 = nysiis0.encode0("org.apache.commons.codec.EncoderException")
        self.assertEqual(object0, "ORGAPACACANANSCADACANCADARAXCAPTAN")

    def test14(self) -> None:
        nysiis0 = Nysiis.Nysiis1()
        boolean0 = nysiis0.isStrict()
        self.assertTrue(boolean0)

    def test13(self) -> None:

        nysiis0 = Nysiis.Nysiis1()
        try:
            nysiis0.encode0(nysiis0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Parameter supplied to Nysiis encode is not of type java.lang.String
            self.verifyException("org.apache.commons.codec.language.Nysiis", e)

    def test12(self) -> None:

        nysiis0 = Nysiis(False)
        nysiis0.nysiis("")
        self.assertFalse(nysiis0.isStrict())

    def test11(self) -> None:

        nysiis0 = Nysiis.Nysiis1()
        nysiis0.nysiis("N")
        self.assertTrue(nysiis0.isStrict())

    def test10(self) -> None:

        nysiis0 = Nysiis.Nysiis1()
        string0 = nysiis0.nysiis("T2ay`f=A)4z+>/-")
        self.assertEqual("TAYF", string0)
        self.assertTrue(nysiis0.isStrict())

    def test09(self) -> None:

        nysiis0 = Nysiis.Nysiis1()
        string0 = nysiis0.nysiis(":4d2],8DdU<]")
        self.assertTrue(nysiis0.isStrict())
        self.assertEqual("D", string0)

    def test08(self) -> None:

        nysiis0 = Nysiis.Nysiis1()
        string0 = nysiis0.nysiis("(EE|IE)$")
        self.assertEqual("EY", string0)
        self.assertTrue(nysiis0.isStrict())

    def test07(self) -> None:

        nysiis0 = Nysiis(False)
        string0 = nysiis0.nysiis(">X3+b]+v")
        self.assertEqual("XBV", string0)
        self.assertFalse(nysiis0.isStrict())

    def test04(self) -> None:

        nysiis0 = Nysiis(True)
        nysiis0.encode1(None)
        self.assertTrue(nysiis0.isStrict())

    def test03(self) -> None:

        nysiis0 = Nysiis(False)
        boolean0 = nysiis0.isStrict()
        self.assertFalse(boolean0)

    def test01(self) -> None:

        nysiis0 = Nysiis.Nysiis1()
        string0 = nysiis0.nysiis("RClpkggkVkz`Mr?-hN")
        self.assertEqual("RCLPCG", string0)

    def test00(self) -> None:

        nysiis0 = Nysiis(True)
        string0 = nysiis0.encode1("HSCACT")
        self.assertTrue(nysiis0.isStrict())
        self.assertEqual("HSCACT", string0)
