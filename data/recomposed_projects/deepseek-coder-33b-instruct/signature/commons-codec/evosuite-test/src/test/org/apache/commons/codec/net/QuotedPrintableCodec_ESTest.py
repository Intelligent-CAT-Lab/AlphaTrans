from __future__ import annotations
import time
import re
import os
import typing
from typing import *
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.net.QuotedPrintableCodec import *

# from src.test.org.apache.commons.codec.net.QuotedPrintableCodec_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class QuotedPrintableCodec_ESTest(unittest.TestCase):

    def test96(self) -> None:

        charset0 = "UTF-8"
        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec2(charset0)
        string0 = quotedPrintableCodec0.getDefaultCharset()
        self.assertEqual("UTF-8", string0)

    def test95(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec(-8, "iN pCfDd'A#ZY(e", None, True)
        try:
            quotedPrintableCodec0.decode3("org.apache.commons.codec.binary.StringUtils")
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError:
            pass

    def test94(self) -> None:

        byteArray0 = bytearray(1)
        bitSet0 = BitSet.from_bytes(byteArray0)
        byteArray1 = QuotedPrintableCodec.encodeQuotedPrintable1(bitSet0, None)
        self.assertIsNone(byteArray1)

    def test93(self) -> None:

        try:
            QuotedPrintableCodec.QuotedPrintableCodec0("tnm5")
            self.fail("Expecting exception: UnsupportedCharsetException")

        except UnsupportedCharsetException as e:
            #
            # tnm5
            #
            self.verifyException("java.nio.charset.Charset", e)

    def test88(self) -> None:
        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec3(True)
        byteArray0 = [0] * 9
        byteArray0[6] = -103
        byteArray1 = quotedPrintableCodec0.encode0(byteArray0)
        self.assertEqual(27, len(byteArray1))

    def test87(self) -> None:

        byteArray0 = [0] * 2
        byteArray0[1] = 9
        byteArray1 = QuotedPrintableCodec.encodeQuotedPrintable2(
            None, byteArray0, False
        )
        byteArray2 = QuotedPrintableCodec.encodeQuotedPrintable2(None, byteArray1, True)
        self.assertEqual(8, len(byteArray2))
        self.assertListEqual([61, 51, 68, 48, 48, 61, 48, 57], byteArray2)

    def test85(self) -> None:

        byteArray0 = [0] * 56
        byteArray1 = QuotedPrintableCodec.encodeQuotedPrintable2(None, byteArray0, True)
        byteArray2 = QuotedPrintableCodec.encodeQuotedPrintable2(None, byteArray1, True)
        self.assertEqual(310, len(byteArray2))
        self.assertEqual(174, len(byteArray1))

    def test84(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4()
        byteArray0 = [0] * 2
        byteArray0[1] = -17
        byteArray1 = quotedPrintableCodec0.encode0(byteArray0)
        self.assertEqual(byteArray1, [61, 48, 48, 61, 69, 70])

    def test83(self) -> None:

        byteArray0 = QuotedPrintableCodec.decodeQuotedPrintable(None)
        self.assertIsNone(byteArray0)

    def test82(self) -> None:

        byteArray0 = [0] * 56
        byteArray1 = QuotedPrintableCodec.encodeQuotedPrintable2(None, byteArray0, True)
        byteArray2 = QuotedPrintableCodec.decodeQuotedPrintable(byteArray1)
        self.assertEqual(56, len(byteArray2))
        self.assertEqual(174, len(byteArray1))

    def test81(self) -> None:

        byteArray0 = bytearray(2)
        byteArray0[0] = 13
        byteArray1 = QuotedPrintableCodec.decodeQuotedPrintable(byteArray0)
        self.assertEqual(bytearray([0]), byteArray1)

    def test79(self) -> None:

        charset0 = "UTF-8"
        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec2(charset0)
        string0 = quotedPrintableCodec0.decode2("UTF-8", "UTF-8")
        assert string0 is not None
        self.assertEqual("UTF-8", string0)

    def test78(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4()
        string0 = quotedPrintableCodec0.decode2(None, None)
        self.assertIsNone(string0)

    def test77(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4()
        object0 = quotedPrintableCodec0.encode2(None)
        self.assertIsNone(object0)

    def test76(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4()
        object0 = quotedPrintableCodec0.decode4(None)
        self.assertIsNone(object0)

    def test75(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec(49, "", None, False)

        try:
            quotedPrintableCodec0.decode4("")
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError:
            pass

    def test74(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4()
        charset0 = "UTF-8"
        string0 = quotedPrintableCodec0.encode3(None, charset0)
        self.assertIsNone(string0)

    def test73(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4()
        try:
            quotedPrintableCodec0.encode4("", "")
            self.fail("Expecting exception: ValueError")

        except ValueError:
            pass

    def test72(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4()
        string0 = quotedPrintableCodec0.encode4(None, None)
        self.assertIsNone(string0)

    def test71(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec2(None)
        charset0 = quotedPrintableCodec0.getCharset()
        self.assertIsNone(charset0)

    def test70(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4()
        byteArray0 = bytearray(4)
        byteArray1 = quotedPrintableCodec0.decode0(byteArray0)
        self.assertEqual(bytearray([0, 0, 0, 0]), byteArray1)

    def test69(self) -> None:
        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec3(True)
        try:
            quotedPrintableCodec0.encode1("")
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")
        except IndexError:
            pass

    def test67(self) -> None:

        byteArray0 = QuotedPrintableCodec.encodeQuotedPrintable2(None, None, True)
        self.assertIsNone(byteArray0)

    def test66(self) -> None:

        longArray0 = [0] * 2
        longArray0[0] = -2208
        bitSet0 = BitSet.valueOf(longArray0)
        byteArray0 = [0] * 3
        byteArray0[0] = 9
        byteArray1 = QuotedPrintableCodec.encodeQuotedPrintable2(
            bitSet0, byteArray0, True
        )
        self.assertEqual(byteArray1, [9, 61, 48, 48, 61, 48, 48])
        self.assertEqual(len(byteArray1), 7)

    def test65(self) -> None:

        byteArray0 = bytearray(10)
        byteArray0[6] = -69
        bitSet0 = BitSet.from_bytes(byteArray0)
        byteArray1 = QuotedPrintableCodec.encodeQuotedPrintable2(
            bitSet0, byteArray0, False
        )
        self.assertIsNot(byteArray0, byteArray1)

    def test64(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4()
        charset0 = "UTF-8"
        string0 = quotedPrintableCodec0.decode1(None, charset0)
        self.assertIsNone(string0)

    def test63(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4()

        try:
            quotedPrintableCodec0.decode1("", None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            pass

    def test62(self) -> None:
        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec3(True)
        try:
            quotedPrintableCodec0.encode2("")
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")
        except ArrayIndexOutOfBoundsException:
            pass

    def test61(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4()
        object0 = object()
        try:
            quotedPrintableCodec0.encode2(object0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Objects of type java.lang.Object cannot be quoted-printable encoded
            self.verifyException("org.apache.commons.codec.net.QuotedPrintableCodec", e)

    def test60(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4()
        try:
            quotedPrintableCodec0.decode4(quotedPrintableCodec0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Objects of type org.apache.commons.codec.net.QuotedPrintableCodec cannot be quoted-printable decoded
            self.verifyException("org.apache.commons.codec.net.QuotedPrintableCodec", e)

    def test59(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4()
        try:
            quotedPrintableCodec0.encode3("S>", None)
            self.fail("Expecting exception: RuntimeError")
        except TypeError:
            pass

    def test58(self) -> None:

        try:
            QuotedPrintableCodec.QuotedPrintableCodec0(None)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Null charset name
            self.verifyException("java.nio.charset.Charset", e)

    def test57(self) -> None:

        try:
            QuotedPrintableCodec.QuotedPrintableCodec0("-,2Ay4V<^}~8]uf/")
            self.fail("Expecting exception: IllegalCharsetNameException")

        except IllegalCharsetNameException as e:
            #
            # -,2Ay4V<^}~8]uf/
            #
            self.verifyException("java.nio.charset.Charset", e)

    def test53(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4()
        byteArray0 = bytearray(4)
        byteArray0[0] = 61
        try:
            quotedPrintableCodec0.decode0(byteArray0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Invalid URL encoding: not a valid digit (radix 16): 0
            #
            self.verifyException("org.apache.commons.codec.net.Utils", e)

    def test52(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4()
        charset0 = "UTF-8"
        try:
            quotedPrintableCodec0.decode1("<_qb:='", charset0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Invalid URL encoding: not a valid digit (radix 16): 39
            #
            self.verifyException("org.apache.commons.codec.net.Utils", e)

    def test51(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4()
        try:
            quotedPrintableCodec0.decode2(
                "org.apache.commons.codec.DecoderException",
                "org.apache.commons.codec.DecoderException",
            )
            self.fail("Expecting exception: ValueError")

        except ValueError:
            pass

    def test50(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4()

        with pytest.raises(RuntimeError):
            quotedPrintableCodec0.decode2("}XBHta:K ", None)

    def test49(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4()
        try:
            quotedPrintableCodec0.decode2("-ph1=9#--", "-ph1=9#--")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Invalid URL encoding: not a valid digit (radix 16): 35
            #
            self.verifyException("org.apache.commons.codec.net.Utils", e)

    def test48(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec3(True)
        try:
            quotedPrintableCodec0.decode3("=")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Invalid quoted-printable encoding
            #
            self.verifyException("org.apache.commons.codec.net.QuotedPrintableCodec", e)

    def test47(self) -> None:

        byteArray0 = bytearray(3)
        byteArray0[1] = 61

        try:
            QuotedPrintableCodec.decodeQuotedPrintable(byteArray0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            self.verifyException("org.apache.commons.codec.net.Utils", e)

    def test41(self) -> None:
        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec3(True)
        byteArray0 = bytearray(1)
        try:
            quotedPrintableCodec0.encode0(byteArray0)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")
        except IndexError:
            pass

    def test40(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec(13, "", None, False)

        with pytest.raises(RuntimeError):
            quotedPrintableCodec0.encode1(
                "org.apache.commons.codec.net.QuotedPrintableCodec"
            )

    def test39(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec2(None)
        try:
            quotedPrintableCodec0.encode2(
                "Invalid URL encoding: not a valid digit (radix 16): "
            )
            self.fail("Expecting exception: RuntimeError")
        except Exception as e:
            pass

    def test38(self) -> None:
        charset0 = "UTF-8"
        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec3(True)
        try:
            quotedPrintableCodec0.encode3("", charset0)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")
        except ArrayIndexOutOfBoundsException:
            pass

    def test37(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4()
        try:
            quotedPrintableCodec0.encode4("", None)
            self.fail("Expecting exception: RuntimeError")
        except Exception as e:
            pass

    def test36(self) -> None:

        byteArray0 = bytearray(1)
        try:
            QuotedPrintableCodec.encodeQuotedPrintable2(None, byteArray0, True)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except ArrayIndexOutOfBoundsException:
            pass

    def test35(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec2(None)
        try:
            quotedPrintableCodec0.getDefaultCharset()
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e.__class__), "<class 'RuntimeError'>")

    def test34(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec0("UTF-8")
        self.assertEqual("UTF-8", quotedPrintableCodec0.getDefaultCharset())

    def test27(self) -> None:

        charset0 = "utf-8"
        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec2(charset0)
        byteArray0 = bytearray()
        byteArray1 = quotedPrintableCodec0.decode0(byteArray0)
        byteArray2 = quotedPrintableCodec0.encode0(byteArray1)
        self.assertEqual(bytearray(), byteArray2)

    def test26(self) -> None:

        charset0 = "utf-8"
        quotedPrintableCodec0 = QuotedPrintableCodec(-1, "", charset0, True)
        byteArray0 = quotedPrintableCodec0.decode0(None)
        self.assertIsNone(byteArray0)

    def test25(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec3(True)
        charset0 = "UTF-8"
        string0 = quotedPrintableCodec0.decode1("", charset0)
        self.assertEqual("", string0)

    def test24(self) -> None:

        charset0 = "utf-8"  # Charset.defaultCharset()
        quotedPrintableCodec0 = QuotedPrintableCodec(-1284, "Km]", charset0, True)
        string0 = quotedPrintableCodec0.decode1("Km]", charset0)
        self.assertEqual("Km]", string0)

    def test23(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4()
        string0 = quotedPrintableCodec0.decode3("")
        self.assertEqual("", string0)

    def test22(self) -> None:

        charset0 = "utf-8"
        quotedPrintableCodec0 = QuotedPrintableCodec(
            1, "qhq*k+CvFO}esh&}=", charset0, True
        )
        string0 = quotedPrintableCodec0.decode3("s6nqDamy:")
        self.assertEqual("s6nqDamy:", string0)

    def test21(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec(2, "", None, True)
        string0 = quotedPrintableCodec0.decode3(None)
        self.assertIsNone(string0)

    def test20(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4()
        object0 = quotedPrintableCodec0.decode4(",1lm{[Z@O8[ewQ3WkiV")
        self.assertEqual(",1lm{[Z@O8[ewQ3WkiV", object0)

    def test19(self) -> None:

        byteArray0 = bytearray()
        byteArray1 = QuotedPrintableCodec.decodeQuotedPrintable(byteArray0)
        self.assertFalse(byteArray1 == byteArray0)

    def test13(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4()
        byteArray0 = quotedPrintableCodec0.encode0(None)
        self.assertIsNone(byteArray0)

    def test12(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4()
        string0 = quotedPrintableCodec0.encode1("")
        self.assertEqual("", string0)

    def test11(self) -> None:

        charset0 = "UTF-8"
        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec2(charset0)
        string0 = quotedPrintableCodec0.encode1(";")
        self.assertEqual(";", string0)

    def test10(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4()
        string0 = quotedPrintableCodec0.encode1(None)
        self.assertIsNone(string0)

    def test09(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4()
        object0 = quotedPrintableCodec0.encode2("")
        self.assertEqual("", object0)

    def test08(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4()
        charset0 = "UTF-8"
        string0 = quotedPrintableCodec0.encode3("", charset0)
        self.assertEqual("", string0)

    def test07(self) -> None:
        charset0 = "UTF-8"
        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec3(True)
        string0 = quotedPrintableCodec0.encode3("NR;.(2W'_8anFu", charset0)
        self.assertEqual("NR;.(2W'_8anFu", string0)

    def test06(self) -> None:
        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec3(False)
        string0 = quotedPrintableCodec0.encode4("-t*y`", "UTF-8")
        self.assertEqual("-t*y`", string0)

    def test05(self) -> None:

        byteArray0 = bytearray()
        bitSet0 = set()
        byteArray1 = QuotedPrintableCodec.encodeQuotedPrintable1(bitSet0, byteArray0)
        self.assertIsNot(byteArray0, byteArray1)

    def test04(self) -> None:

        longArray0 = [0] * 8
        bitSet0 = BitSet.valueOf(longArray0)
        byteArray0 = [0] * 6
        byteArray1 = QuotedPrintableCodec.encodeQuotedPrintable1(bitSet0, byteArray0)
        self.assertEqual(18, len(byteArray1))

    def test03(self) -> None:

        bitSet0 = [False] * 256
        byteArray0 = bytearray()
        byteArray1 = QuotedPrintableCodec.encodeQuotedPrintable2(
            bitSet0, byteArray0, False
        )
        self.assertIsNot(byteArray0, byteArray1)

    def test02(self) -> None:

        quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4()
        charset0 = quotedPrintableCodec0.getCharset()
        self.assertEqual("UTF-8", charset0)

    def test01(self) -> None:

        byteArray0 = [0] * 8
        longArray0 = [0] * 8
        longArray0[0] = 85
        bitSet0 = BitSet.valueOf(longArray0)
        byteArray1 = QuotedPrintableCodec.encodeQuotedPrintable2(
            bitSet0, byteArray0, True
        )
        self.assertEqual([0] * 8, byteArray1)
        self.assertEqual(8, len(byteArray1))

    def test00(self) -> None:

        byteArray0 = [0] * 9
        bitSet0 = [False] * 32
        byteArray1 = QuotedPrintableCodec.encodeQuotedPrintable2(
            bitSet0, byteArray0, True
        )
        byteArray2 = QuotedPrintableCodec.encodeQuotedPrintable2(
            bitSet0, byteArray1, True
        )
        byteArray3 = QuotedPrintableCodec.decodeQuotedPrintable(byteArray2)
        self.assertEqual(27, len(byteArray3))
        self.assertEqual(84, len(byteArray2))
