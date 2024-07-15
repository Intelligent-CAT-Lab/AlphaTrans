from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.digest.MurmurHash2 import *

# from src.test.org.apache.commons.codec.digest.MurmurHash2_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class MurmurHash2_ESTest(unittest.TestCase):

    def test40(self) -> None:

        with pytest.raises(RuntimeError):
            MurmurHash2.hash323(None, -180, -180)

    def test39(self) -> None:

        long0 = MurmurHash2.hash643("org.apache.commons.codec.digest.MurmurHash2", 4, 4)
        self.assertEqual((-3131028227372647069), long0)

    def test38(self) -> None:

        byteArray0 = bytearray(7)
        int0 = MurmurHash2.hash321(byteArray0, 1)
        self.assertEqual(375494588, int0)

    def test37(self) -> None:

        int0 = MurmurHash2.hash322('Hnv]qBeD/\!$"zp Vv7')
        self.assertEqual((-1416464607), int0)

    def test36(self) -> None:

        byteArray0 = bytearray(5)
        int0 = MurmurHash2.hash321(byteArray0, (-1756908916))
        self.assertEqual(0, int0)

    def test35(self) -> None:

        long0 = MurmurHash2.hash642('Hnv]qBeD/\!$"zp Vv7')
        self.assertEqual((-3105253281641488939), long0)

    def test34(self) -> None:

        long0 = MurmurHash2.hash642(".Z,V8%")
        self.assertEqual(-7614162413214632062, long0)

    def test33(self) -> None:

        long0 = MurmurHash2.hash642("eAt.phv3h;#}3m6")
        self.assertEqual(3195875775987614497, long0)

    def test32(self) -> None:

        long0 = MurmurHash2.hash640(None, 0, 0)
        self.assertEqual(0, long0)

    def test31(self) -> None:

        byteArray0 = bytearray()
        try:
            MurmurHash2.hash641(byteArray0, 1809)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.verifyException("org.apache.commons.codec.digest.MurmurHash2", e)

    def test30(self) -> None:

        byteArray0 = bytearray(8)
        int0 = MurmurHash2.hash320(byteArray0, 0, 0)
        self.assertEqual(0, int0)

    def test29(self) -> None:

        byteArray0 = bytearray(4)

        try:
            MurmurHash2.hash320(byteArray0, 296, 0)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.assertEqual(str(e), "array index out of bounds")

    def test28(self) -> None:

        byteArray0 = bytearray(2)

        try:
            MurmurHash2.hash320(byteArray0, -2950, 2173)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.assertEqual(str(e), "array index out of range")

    def test27(self) -> None:

        try:
            MurmurHash2.hash320(None, 1, 1)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")
            self.assertEqual(type(e), RuntimeError)

    def test26(self) -> None:

        byteArray0 = bytearray(2)

        try:
            MurmurHash2.hash320(byteArray0, -2965, 2173)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.verifyException("org.apache.commons.codec.digest.MurmurHash2", e)

    def test25(self) -> None:

        try:
            MurmurHash2.hash640(None, 940, 940)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")
            self.assertEqual(type(e), RuntimeError)

    def test24(self) -> None:

        byteArray0 = bytearray(14)

        try:
            MurmurHash2.hash640(byteArray0, -1887, -1887)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.verifyException("org.apache.commons.codec.digest.MurmurHash2", e)

    def test23(self) -> None:

        byteArray0 = bytearray(8)
        long0 = MurmurHash2.hash640(byteArray0, 6, 1)
        self.assertEqual(6496968449332415600, long0)

    def test22(self) -> None:

        byteArray0 = bytearray(4)

        try:
            MurmurHash2.hash640(byteArray0, -294, -78)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except ArrayIndexOutOfBoundsException as e:
            self.verifyException("org.apache.commons.codec.digest.MurmurHash2", e)

    def test21(self) -> None:

        byteArray0 = bytearray(7)

        try:
            MurmurHash2.hash640(byteArray0, -2555, 16)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.verifyException("org.apache.commons.codec.digest.MurmurHash2", e)

    def test20(self) -> None:

        byteArray0 = bytearray(1)

        try:
            MurmurHash2.hash640(byteArray0, -64011636, -64011636)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.verifyException("org.apache.commons.codec.digest.MurmurHash2", e)

    def test19(self) -> None:

        byteArray0 = bytearray(10)

        try:
            MurmurHash2.hash640(byteArray0, -1869, -1869)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.verifyException("org.apache.commons.codec.digest.MurmurHash2", e)

    def test18(self) -> None:

        byteArray0 = bytearray(2)

        try:
            MurmurHash2.hash640(byteArray0, -1, -4173)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except ArrayIndexOutOfBoundsException as e:
            self.verifyException("org.apache.commons.codec.digest.MurmurHash2", e)

    def test17(self) -> None:

        byteArray0 = bytearray()
        try:
            MurmurHash2.hash321(byteArray0, 13)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.verifyException("org.apache.commons.codec.digest.MurmurHash2", e)

    def test16(self) -> None:

        try:
            MurmurHash2.hash321(None, 807)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")
            self.assertEqual(type(e), RuntimeError)

    def test15(self) -> None:

        try:
            MurmurHash2.hash322(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "Expecting exception: RuntimeError")

    def test14(self) -> None:

        with pytest.raises(RuntimeError):
            MurmurHash2.hash641(None, 974)

    def test13(self) -> None:

        try:
            MurmurHash2.hash642(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "Expecting exception: RuntimeError")

    def test12(self) -> None:

        with pytest.raises(RuntimeError):
            MurmurHash2.hash643(None, -94, -94)

    def test11(self) -> None:

        byteArray0 = bytearray(1)
        int0 = MurmurHash2.hash320(byteArray0, 0, 16)
        self.assertEqual(-1121983635, int0)

    def test10(self) -> None:

        byteArray0 = bytearray(4)
        int0 = MurmurHash2.hash320(byteArray0, 0, 54)
        self.assertEqual(1581775328, int0)

    def test09(self) -> None:

        byteArray0 = bytearray(7)
        byteArray0[0] = -108
        int0 = MurmurHash2.hash321(byteArray0, 1)
        self.assertEqual(-40725216, int0)

    def test08(self) -> None:

        int0 = MurmurHash2.hash322(" 3Ux")
        self.assertEqual(40297033, int0)

    def test07(self) -> None:

        int0 = MurmurHash2.hash323("org.apache.commons.codec.digest.MurmurHash2", 7, 7)
        self.assertEqual((-1313868537), int0)

    def test06(self) -> None:

        int0 = MurmurHash2.hash323("org.apache.commons.codec.digest.MurmurHash2", 0, 0)
        self.assertEqual(275646681, int0)

    def test05(self) -> None:

        byteArray0 = bytearray(8)
        byteArray0[0] = 1
        long0 = MurmurHash2.hash640(byteArray0, 6, 1)
        self.assertEqual(-3785491983369535334, long0)

    def test04(self) -> None:
        byteArray0 = bytearray(1)
        long0 = MurmurHash2.hash641(byteArray0, 0)
        self.assertEqual(-7207201254813729732, long0)

    def test03(self) -> None:

        byteArray0 = bytearray(9)
        byteArray0[0] = 101
        long0 = MurmurHash2.hash641(byteArray0, 1)
        self.assertEqual(8982822323587011191, long0)

    def test02(self) -> None:

        long0 = MurmurHash2.hash643(")oXS'jH", 1, 1)
        self.assertEqual(3710105625432625567, long0)

    def test01(self) -> None:

        try:
            MurmurHash2.hash323("", 0, 1717)
            self.fail("Expecting exception: StringIndexOutOfBoundsException")

        except StringIndexOutOfBoundsException:
            pass

    def test00(self) -> None:

        with pytest.raises(StringIndexOutOfBoundsException):
            MurmurHash2.hash643("", (-538903421), 1047936355)
