from __future__ import annotations
import time
import re
import os
import decimal
import typing
from typing import *
from io import BytesIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.binary.Hex import *

# from src.test.org.apache.commons.codec.binary.Hex_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Hex_ESTest(unittest.TestCase):

    def test78(self) -> None:

        charset0 = Charset.defaultCharset()
        hex0 = Hex(
            61,
            "Output array is not large enough to accommodate decoded data.",
            charset0,
        )

        with pytest.raises(RuntimeError):
            hex0.encode0(None)

    def test77(self) -> None:

        byteArray0 = [0] * 7
        string0 = Hex.encodeHexString1(byteArray0, False)
        self.assertEqual("00000000000000", string0)

    def test76(self) -> None:

        try:
            Hex.encodeHexString3(None, False)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.codec.binary.Hex", e)

    def test73(self) -> None:

        charArray0 = []
        byteArray0 = []
        try:
            Hex.decodeHex1(charArray0, byteArray0, 1298)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Output array is not large enough to accommodate decoded data.
            self.verifyException("org.apache.commons.codec.binary.Hex", e)

    def test72(self) -> None:

        byteArray0 = Hex.decodeHex2("")
        # Undeclared exception in Java code
        try:
            Hex.encodeHex3(byteArray0, 1000, 1000, False)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except ArrayIndexError:
            # no message in exception (getMessage() returned null)
            pass

    def test71(self) -> None:

        byteArray0 = [0] * 2
        charArray0 = [0] * 0

        try:
            Hex.encodeHex4(byteArray0, -78, 891, True, charArray0, 13)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError:
            pass

    def test69(self) -> None:

        hex0 = Hex.Hex0("UTF8")
        byteBuffer0 = bytearray(3326)
        hex0.encode2(byteBuffer0)
        self.assertEqual(3326, len(byteBuffer0))
        self.assertEqual(0, len(byteBuffer0))

    def test68(self) -> None:

        try:
            Hex.encodeHexString2(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.codec.binary.Hex", e)

    def test66(self) -> None:

        try:
            Hex.encodeHex0(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.codec.binary.Hex", e)

    def test65(self) -> None:

        try:
            Hex.encodeHexString0(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.codec.binary.Hex", e)

    def test64(self) -> None:

        try:
            Hex.decodeHex0(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.codec.binary.Hex", e)

    def test63(self) -> None:
        hex0 = Hex.Hex0("UTF-8")
        charset0 = hex0.getCharset()
        self.assertTrue(charset0.canEncode())

    def test62(self) -> None:

        byteArray0 = [0] * 2
        charArray0 = [0] * 5

        try:
            Hex.decodeHex1(charArray0, byteArray0, 6)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Odd number of characters.
            #
            self.verifyException("org.apache.commons.codec.binary.Hex", e)

    def test61(self) -> None:

        byteArray0 = bytearray(2)
        byteBuffer0 = io.BytesIO(byteArray0)
        charArray0 = Hex.encodeHex6(byteBuffer0)
        int0 = Hex.decodeHex1(charArray0, byteArray0, 0)
        self.assertEqual(2, int0)
        self.assertListEqual([0, 0], list(byteArray0))
        self.assertListEqual(["0", "0", "0", "0"], charArray0)

    def test60(self) -> None:

        try:
            Hex.encodeHex1(None, False)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "Expecting exception: RuntimeError")

    def test59(self) -> None:

        byteArray0 = [0] * 3
        charArray0 = Hex.encodeHex1(byteArray0, True)
        self.assertEqual(charArray0, ["0", "0", "0", "0", "0", "0"])
        self.assertEqual(len(charArray0), 6)

    def test58(self) -> None:

        charset0 = "utf-8"
        charArray0 = []
        charBuffer0 = "".join(charArray0)
        byteBuffer0 = charBuffer0.encode(charset0)
        charArray1 = Hex.encodeHex7(byteBuffer0, False)
        self.assertEqual(0, len(charArray1))

    def test57(self) -> None:

        hex0 = Hex.Hex0("UTF8")
        try:
            hex0.decode2("UTF8")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Illegal hexadecimal character U at index 0
            #
            self.verifyException("org.apache.commons.codec.binary.Hex", e)

    def test56(self) -> None:

        charset0 = Charset.defaultCharset()
        hex0 = Hex(7, "(", charset0)
        object0 = hex0.encode2("(")
        self.assertIsNotNone(object0)

    def test55(self) -> None:

        hex0 = Hex(5, "", None)

        try:
            hex0.encode2(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.codec.binary.Hex", e)

    def test54(self) -> None:

        # Undeclared exception
        try:
            Hex.Hex0(None)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Null charset name
            verifyException("java.nio.charset.Charset", e)

    def test53(self) -> None:

        # Undeclared exception
        try:
            Hex.Hex0("")
            self.fail("Expecting exception: IllegalCharsetNameException")

        except IllegalCharsetNameException as e:
            #
            #
            #
            self.verifyException("java.nio.charset.Charset", e)

    def test52(self) -> None:

        # Undeclared exception
        try:
            Hex.Hex0("org.apache.commons.codec.DecoderException")
            self.fail("Expecting exception: UnsupportedCharsetException")

        except UnsupportedCharsetException as e:
            # org.apache.commons.codec.DecoderException
            self.verifyException("java.nio.charset.Charset", e)

    def test49(self) -> None:

        byteArray0 = Hex.decodeHex2("eC")
        charset0 = Charset.defaultCharset()
        hex0 = Hex((-696), "eC", charset0)
        try:
            hex0.decode0(byteArray0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Odd number of characters.
            #
            self.verifyException("org.apache.commons.codec.binary.Hex", e)

    def test48(self) -> None:

        hex0 = Hex.Hex0("UTF8")
        # Undeclared exception in Java code
        try:
            hex0.decode1(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("org.apache.commons.codec.binary.Hex", e)

    def test47(self) -> None:

        hex0 = Hex.Hex0("UTF8")
        byteBuffer0 = bytearray(53)
        try:
            hex0.decode1(byteBuffer0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Odd number of characters.
            #
            self.verifyException("org.apache.commons.codec.binary.Hex", e)

    def test46(self) -> None:

        charArray0 = ["\0"] * 8
        try:
            Hex.decodeHex0(charArray0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Illegal hexadecimal character \u0000 at index 0
            #
            self.verifyException("org.apache.commons.codec.binary.Hex", e)

    def test45(self) -> None:

        byteArray0 = bytearray(3)
        byteBuffer0 = io.BytesIO(byteArray0)
        charArray0 = Hex.encodeHex6(byteBuffer0)

        try:
            Hex.decodeHex1(charArray0, byteArray0, -1728)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.assertEqual(str(e), "array index out of range")

    def test44(self) -> None:

        byteArray0 = bytearray(0)

        try:
            Hex.decodeHex1(None, byteArray0, -1662)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")
            self.assertEqual(type(e).__name__, "RuntimeError")

    def test43(self) -> None:

        try:
            Hex.decodeHex2(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.codec.binary.Hex", e)

    def test42(self) -> None:

        try:
            Hex.decodeHex2(")qv1ia")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Illegal hexadecimal character ) at index 0
            #
            self.assertIsInstance(e, Exception)

    def test39(self) -> None:

        hex0 = Hex.Hex0("UTF8")
        # Undeclared exception in Java code, but RuntimeError is the closest Python equivalent
        try:
            hex0.encode1(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            # verifyException("org.apache.commons.codec.binary.Hex", e)
            # In Python, we can use assert to verify the exception type
            assert isinstance(e, TypeError), "Expecting exception: RuntimeError"

    def test38(self) -> None:

        charset0 = Charset.defaultCharset()
        hex0 = Hex(1687, 'hUP"5}', charset0)
        try:
            hex0.encode2(charset0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            self.verifyException("org.apache.commons.codec.binary.Hex", e)

    def test37(self) -> None:

        byteArray0 = bytearray(1)
        charArray0 = [None] * 0

        try:
            Hex._encodeHex2(byteArray0, Hex.__DIGITS_UPPER)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError:
            pass

    def test36(self) -> None:

        byteBuffer0 = bytearray(1262)
        charArray0 = Hex.encodeHex6(byteBuffer0)

        try:
            Hex.encodeHex2(None, charArray0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.codec.binary.Hex", e)

    def test35(self) -> None:

        byteArray0 = Hex.decodeHex2("")

        try:
            Hex.encodeHex3(byteArray0, -2003, -2003, True)
            self.fail("Expecting exception: NegativeArraySizeException")

        except NegativeArraySizeException as e:
            verifyException("org.apache.commons.codec.binary.Hex", e)

    def test34(self) -> None:

        try:
            Hex.encodeHex3(None, 16, 16, True)
            self.fail("Expecting exception: RuntimeError")

        except TypeError as e:
            # no message in exception (getMessage() returned null)
            pass

    def test33(self) -> None:

        try:
            Hex.encodeHex6(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.codec.binary.Hex", e)

    def test32(self) -> None:

        try:
            Hex.encodeHex7(None, True)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e.__class__), "<class 'NoneType'>")

    def test31(self) -> None:

        byteBuffer0 = bytearray(91)
        charArray0 = [0] * 0

        try:
            Hex._encodeHex8(byteBuffer0, Hex.__DIGITS_UPPER)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError:
            pass

    def test30(self) -> None:

        charArray0 = ["\0"]
        try:
            Hex.encodeHex8(None, charArray0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.codec.binary.Hex", e)

    def test29(self) -> None:

        try:
            Hex.encodeHexString1(None, True)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "Expecting exception: RuntimeError")

    def test28(self) -> None:

        try:
            Hex._toDigit("$", 1061)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Illegal hexadecimal character $ at index 1061
            #
            self.assertIsInstance(e, DecoderException)
            self.assertEqual(str(e), "Illegal hexadecimal character $ at index 1061")

    def test27(self) -> None:

        byteArray0 = bytearray()
        charset0 = "UTF-8"
        hex0 = Hex(12, "UTF-8", charset0)
        byteArray1 = hex0.decode0(byteArray0)
        self.assertFalse(byteArray1 == byteArray0)

    def test26(self) -> None:

        byteBuffer0 = bytearray(246)
        charArray0 = Hex.encodeHex7(byteBuffer0, True)
        byteArray0 = Hex.decodeHex0(charArray0)
        self.assertEqual(246, len(byteArray0))

    def test25(self) -> None:

        byteArray0 = bytearray()
        byteBuffer0 = memoryview(byteArray0)
        charArray0 = Hex.encodeHex6(byteBuffer0)
        byteArray1 = bytearray(2)
        int0 = Hex.decodeHex1(charArray0, byteArray1, -737)
        self.assertEqual(0, int0)

    def test23(self) -> None:

        byteArray0 = bytearray(0)
        charset0 = "UTF-8"
        hex0 = Hex(-520, "UTF-8", charset0)
        byteArray1 = hex0.encode0(byteArray0)
        self.assertEqual(0, len(byteArray1))

    def test22(self) -> None:

        charset0 = Charset.defaultCharset()
        byteArray0 = bytearray(2)
        hex0 = Hex(6, "(", charset0)
        byteArray1 = hex0.encode0(byteArray0)
        self.assertEqual(byteArray1, bytearray([48, 48, 48, 48]))

    def test21(self) -> None:

        byteArray0 = bytearray(2)
        byteBuffer0 = io.BytesIO(byteArray0)
        charArray0 = Hex.encodeHex6(byteBuffer0)
        self.assertEqual(list(charArray0), ["0", "0", "0", "0"])

        charset0 = "utf-8"
        hex0 = Hex(101, "", charset0)
        byteArray1 = hex0.encode1(byteBuffer0)
        self.assertEqual(len(byteArray1), 0)

    def test20(self) -> None:

        byteArray0 = bytearray()
        charArray0 = Hex.encodeHex0(byteArray0)
        self.assertEqual(0, len(charArray0))

    def test19(self) -> None:

        byteArray0 = Hex.decodeHex2("eC")
        charArray0 = Hex.encodeHex0(byteArray0)
        # Unstable assertion: self.assertListEqual(['0', '0'], charArray0)
        # Unstable assertion: self.assertListEqual([-20], byteArray0)

    def test18(self) -> None:

        byteArray0 = bytearray()
        charArray0 = Hex.encodeHex1(byteArray0, False)
        self.assertEqual(0, len(charArray0))

    def test17(self) -> None:

        charArray0 = []
        byteArray0 = Hex.decodeHex0(charArray0)
        charArray1 = Hex._encodeHex2(byteArray0, charArray0)
        assert charArray1 != charArray0

    def test16(self) -> None:

        byteArray0 = [0] * 7
        charArray0 = Hex.encodeHex0(byteArray0)
        charArray1 = Hex._encodeHex2(byteArray0, charArray0)
        self.assertEqual(14, len(charArray1))

    def test15(self) -> None:

        byteArray0 = [0] * 3
        charArray0 = Hex.encodeHex3(byteArray0, 1, 0, False)
        self.assertEqual(0, len(charArray0))

    def test14(self) -> None:

        byteBuffer0 = bytearray(0)
        charArray0 = ["\0"] * 8
        charArray1 = Hex._encodeHex8(byteBuffer0, charArray0)
        self.assertEqual(0, len(charArray1))

    def test13(self) -> None:

        byteBuffer0 = bytearray(65)
        charArray0 = ["\0"]
        charArray1 = Hex._encodeHex8(byteBuffer0, charArray0)
        self.assertEqual(130, len(charArray1))

    def test12(self) -> None:

        charArray0 = []
        byteArray0 = Hex.decodeHex0(charArray0)
        string0 = Hex.encodeHexString0(byteArray0)
        self.assertEqual("", string0)

    def test11(self) -> None:

        byteArray0 = bytearray(3)
        string0 = Hex.encodeHexString0(byteArray0)
        self.assertEqual("000000", string0)

    def test10(self) -> None:

        byteArray0 = bytearray(0)
        string0 = Hex.encodeHexString1(byteArray0, False)
        self.assertEqual("", string0)

    def test09(self) -> None:

        byteBuffer0 = bytearray(200)
        Hex.encodeHex6(byteBuffer0)
        string0 = Hex.encodeHexString2(byteBuffer0)
        self.assertEqual("", string0)

    def test08(self) -> None:

        byteBuffer0 = bytearray(2536)
        string0 = Hex.encodeHexString2(byteBuffer0)
        self.assertIsNotNone(string0)

    def test07(self) -> None:

        byteBuffer0 = bytearray(0)
        string0 = Hex.encodeHexString3(byteBuffer0, False)
        self.assertEqual("", string0)

    def test06(self) -> None:

        byteBuffer0 = bytearray(785)
        string0 = Hex.encodeHexString3(byteBuffer0, True)
        self.assertIsNotNone(string0)

    def test05(self) -> None:

        int0 = Hex._toDigit("a", -1285)
        self.assertEqual(10, int0)

    def test04(self) -> None:

        int0 = Hex._toDigit("0", 2419)
        self.assertEqual(0, int0)

    def test03(self) -> None:

        charset0 = Charset.defaultCharset()
        hex0 = Hex(-5568, "%y&) p 5}yd6|p~b}r", charset0)
        try:
            hex0.decode2(charset0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            self.verifyException("org.apache.commons.codec.binary.Hex", e)

    def test02(self) -> None:

        byteArray0 = [0] * 2
        charArray0 = [0] * 0
        Hex.encodeHex4(byteArray0, 9, (-1213), False, charArray0, 52)
        self.assertEqual([], charArray0)

    def test01(self) -> None:

        hex0 = Hex(1, "", None)
        string0 = hex0.toString()
        self.assertIsNotNone(string0)
