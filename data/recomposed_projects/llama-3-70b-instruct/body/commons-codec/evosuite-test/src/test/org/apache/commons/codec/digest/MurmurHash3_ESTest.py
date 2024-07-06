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
from src.main.org.apache.commons.codec.digest.MurmurHash3 import *

# from src.test.org.apache.commons.codec.digest.MurmurHash3_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class MurmurHash3_ESTest(unittest.TestCase):

    def test99(self) -> None:

        byteArray0 = bytearray(7)
        try:
            MurmurHash3.hash326(byteArray0, 630838780)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.verifyException("org.apache.commons.codec.digest.MurmurHash3", e)

    def test98(self) -> None:

        with pytest.raises(RuntimeError):
            MurmurHash3.hash644(None, 1671, -3090)

    def test97(self) -> None:

        int0 = MurmurHash3.hash323(1331, 2046551812)
        self.assertEqual(758345217, int0)

    def test96(self) -> None:

        int0 = MurmurHash3.hash325("^=Ci")
        self.assertEqual(269472428, int0)

    def test95(self) -> None:

        byteArray0 = bytearray(9)
        longArray0 = MurmurHash3.hash128x640(byteArray0)
        self.assertEqual(longArray0, [8297479994805284640, -1010425036434519540])

    def test94(self) -> None:

        try:
            MurmurHash3.hash1281(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertIsInstance(e, RuntimeError)
            self.assertIsNotNone(str(e))

    def test93(self) -> None:

        int0 = MurmurHash3.hash320((-1794), (-1794))
        self.assertEqual((-154936693), int0)

    def test92(self) -> None:

        long0 = MurmurHash3.hash641(-89)
        self.assertEqual(1877368944204863702, long0)

    def test91(self) -> None:

        try:
            MurmurHash3.hash1282(None, -862048943, -862048943, -862048943)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")
            self.assertEqual(type(e).__name__, "RuntimeError")

    def test90(self) -> None:

        byteArray0 = bytearray(4)
        longArray0 = MurmurHash3.hash1280(byteArray0)
        self.assertEqual(longArray0, [4237109858264490658, -3654202066835248170])

    def test89(self) -> None:

        int0 = MurmurHash3.hash322(2046551812)
        self.assertEqual(-1093777662, int0)

    def test88(self) -> None:

        long0 = MurmurHash3.hash640(0)
        self.assertEqual(-8620514229188030809, long0)

    def test87(self) -> None:

        byteArray0 = bytearray(11)

        try:
            MurmurHash3.hash645(byteArray0, 366678052, 366678052, 366678052)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.verifyException("org.apache.commons.codec.digest.MurmurHash3", e)

    def test86(self) -> None:
        murmurHash3_IncrementalHash32x86_0 = MurmurHash3.IncrementalHash32x86()
        int0 = murmurHash3_IncrementalHash32x86_0.end()
        self.assertEqual(0, int0)

    def test85(self) -> None:

        murmurHash3_IncrementalHash32x86_0 = MurmurHash3.IncrementalHash32x86()
        murmurHash3_IncrementalHash32x86_0.start(1109)
        self.assertEqual(1161923513, murmurHash3_IncrementalHash32x86_0.end())

    def test84(self) -> None:

        with pytest.raises(RuntimeError):
            MurmurHash3.hash326(None, -2707)

    def test83(self) -> None:

        byteArray0 = bytearray(7)
        int0 = MurmurHash3.hash32x860(byteArray0)
        self.assertEqual((-720425247), int0)

    def test82(self) -> None:

        byteArray0 = bytearray(8)
        int0 = MurmurHash3.hash32x860(byteArray0)
        self.assertEqual(1669671676, int0)

    def test81(self) -> None:

        byteArray0 = bytearray(11)
        long0 = MurmurHash3.hash644(byteArray0, -1, -920)
        self.assertEqual(-290380851590073214, long0)

    def test80(self) -> None:

        longArray0 = MurmurHash3.hash1281("VH")
        self.assertEqual(longArray0, [1621193727033521071, 8283586221036498362])

    def test79(self) -> None:

        byteArray0 = bytearray(3)
        longArray0 = MurmurHash3.hash128x640(byteArray0)
        self.assertEqual(longArray0, [8779008611884021576, 789792335023450397])

    def test78(self) -> None:

        longArray0 = MurmurHash3.hash1281("KZ;oW")
        self.assertEqual(longArray0, [(-374753840059279731), 2265938371139162254])

    def test77(self) -> None:

        byteArray0 = bytearray(6)
        longArray0 = MurmurHash3.hash1280(byteArray0)
        self.assertEqual(longArray0, [8735115895426159728, 5193896931062123826])

    def test76(self) -> None:
        byteArray0 = bytearray(7)
        longArray0 = MurmurHash3.hash1280(byteArray0)
        self.assertEqual([-2613151768389018909, 2529546424875844979], longArray0)

    def test75(self) -> None:

        byteArray0 = bytearray(10)
        longArray0 = MurmurHash3.hash1280(byteArray0)
        self.assertEqual(longArray0, [7063875085384484892, -6037316431886049400])

    def test74(self) -> None:

        longArray0 = MurmurHash3.hash1281("org.apache.commons.codec.digest.MurmurHash3")
        self.assertEqual([7857037817036204021, 6968258762365418411], longArray0)

    def test73(self) -> None:

        longArray0 = MurmurHash3.hash1281("{T5Eq=bC0uG")
        self.assertEqual(longArray0, [(-5529662467487770005), (-1451557616180753302)])

    def test72(self) -> None:

        byteArray0 = bytearray()
        try:
            MurmurHash3.hash128x641(byteArray0, -19, -19, -19)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.verifyException("org.apache.commons.codec.digest.MurmurHash3", e)

    def test71(self) -> None:

        longArray0 = MurmurHash3.hash1281("HM#t'ZNV2*!/g/O")
        self.assertEqual(longArray0, [8024476854106698359, -8822075722905644794])

    def test70(self) -> None:

        byteArray0 = bytearray(15)
        longArray0 = MurmurHash3.hash128x640(byteArray0)
        self.assertEqual(longArray0, [7845573677149415537, 1826583217152429490])

    def test69(self) -> None:

        byteArray0 = bytearray(9)
        murmurHash3_IncrementalHash32x86_0 = MurmurHash3.IncrementalHash32x86()
        murmurHash3_IncrementalHash32x86_0.add(byteArray0, (-111685489), (-111685489))
        self.assertEqual(9, len(byteArray0))

    def test68(self) -> None:

        byteArray0 = bytearray(15)
        murmurHash3_IncrementalHash32x86_0 = MurmurHash3.IncrementalHash32x86()
        murmurHash3_IncrementalHash32x86_0.add(byteArray0, 4, 4)
        self.assertEqual(593689054, murmurHash3_IncrementalHash32x86_0.end())

    def test67(self) -> None:

        byteArray0 = bytearray(11)
        murmurHash3_IncrementalHash32x86_0 = MurmurHash3.IncrementalHash32x86()
        int0 = murmurHash3_IncrementalHash32x86_0.finalise(1, 1, byteArray0, 366678052)
        self.assertEqual(0, murmurHash3_IncrementalHash32x86_0.end())
        self.assertEqual(1384765200, int0)

    def test66(self) -> None:

        int0 = MurmurHash3.hash321((-589), (-1867), 2422)
        self.assertEqual((-287202861), int0)

    def test65(self) -> None:

        with pytest.raises(TypeError):
            MurmurHash3.hash327(None, 1, -1)

    def test64(self) -> None:

        try:
            MurmurHash3.hash328(None, -154936693, -154936693, -154936693)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.codec.digest.MurmurHash3", e)

    def test63(self) -> None:

        byteArray0 = bytearray(9)

        try:
            MurmurHash3.hash328(byteArray0, 877, 78, -2120)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            # Index 877 out of bounds for length 9
            self.assertEqual(str(e), "array index out of bounds")

    def test62(self) -> None:

        byteArray0 = bytearray(7)

        try:
            MurmurHash3.hash328(byteArray0, 81, 1, 1)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.verifyException("org.apache.commons.codec.digest.MurmurHash3", e)

    def test61(self) -> None:

        byteArray0 = bytearray(5)

        try:
            MurmurHash3.hash328(byteArray0, 4, -3410, -1)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.verifyException("org.apache.commons.codec.digest.MurmurHash3", e)

    def test60(self) -> None:

        byteArray0 = bytearray(4)
        int0 = MurmurHash3.hash328(byteArray0, 0, -332, -332)
        self.assertEqual(0, int0)

    def test59(self) -> None:

        try:
            MurmurHash3.hash32x861(None, -982, 56, 56)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")
            self.assertEqual(type(e), RuntimeError)

    def test58(self) -> None:

        byteArray0 = bytearray(3)

        try:
            MurmurHash3.hash32x861(byteArray0, 0, -1, 920)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except ArrayIndexOutOfBoundsException as e:
            self.verifyException("org.apache.commons.codec.digest.MurmurHash3", e)

    def test57(self) -> None:

        byteArray0 = bytearray(14)
        int0 = MurmurHash3.hash32x861(byteArray0, 51, 0, -1)
        self.assertEqual(-2114883783, int0)

    def test56(self) -> None:

        byteArray0 = bytearray(7)

        try:
            MurmurHash3.hash32x861(byteArray0, 0, -1162, 0)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except ArrayIndexOutOfBoundsException as e:
            self.verifyException("org.apache.commons.codec.digest.MurmurHash3", e)

    def test55(self) -> None:

        byteArray0 = bytearray()

        try:
            MurmurHash3.hash32x861(byteArray0, -1067, 1, -59)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            # Index -1067 out of bounds for length 0
            self.assertEqual(str(e), "array index out of range")

    def test54(self) -> None:

        try:
            MurmurHash3.hash645(None, 7, 7, 7)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")
            self.assertEqual(type(e), RuntimeError)

    def test53(self) -> None:

        byteArray0 = [0] * 7

        try:
            MurmurHash3.hash645(byteArray0, 0, -2, 13)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except ArrayIndexOutOfBoundsException as e:
            self.verifyException("org.apache.commons.codec.digest.MurmurHash3", e)

    def test52(self) -> None:

        byteArray0 = bytearray(5)

        try:
            MurmurHash3.hash645(byteArray0, 16, -2048144789, 0)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.verifyException("org.apache.commons.codec.digest.MurmurHash3", e)

    def test51(self) -> None:

        byteArray0 = bytearray(7)

        try:
            MurmurHash3.hash645(byteArray0, 0, -291, 2658)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.verifyException("org.apache.commons.codec.digest.MurmurHash3", e)

    def test50(self) -> None:

        byteArray0 = bytearray(4)

        try:
            MurmurHash3.hash645(byteArray0, -12, -332, -12)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.verifyException("org.apache.commons.codec.digest.MurmurHash3", e)

    def test49(self) -> None:

        byteArray0 = bytearray(3)
        long0 = MurmurHash3.hash645(byteArray0, 0, 1, 371)
        self.assertEqual(-6112031723299314685, long0)

    def test48(self) -> None:

        byteArray0 = bytearray(1)

        try:
            MurmurHash3.hash645(byteArray0, 21, -3390, -777887350)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.verifyException("org.apache.commons.codec.digest.MurmurHash3", e)

    def test47(self) -> None:

        byteArray0 = bytearray(5)
        long0 = MurmurHash3.hash645(byteArray0, 0, 0, 0)
        self.assertEqual(0, long0)

    def test46(self) -> None:

        with pytest.raises(RuntimeError):
            MurmurHash3.hash1280(None)

    def test45(self) -> None:

        byteArray0 = bytearray(8)
        try:
            MurmurHash3.hash1282(byteArray0, -40, -40, -40)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.assertEqual(str(e), "array index out of range")

    def test44(self) -> None:

        with pytest.raises(RuntimeError):
            MurmurHash3.hash128x640(None)

    def test43(self) -> None:

        with pytest.raises(RuntimeError):
            MurmurHash3.hash128x641(None, 7, -83, -83)

    def test42(self) -> None:

        with pytest.raises(RuntimeError):
            MurmurHash3.hash324(None)

    def test41(self) -> None:

        with pytest.raises(RuntimeError):
            MurmurHash3.hash325(None)

    def test40(self) -> None:

        byteArray0 = bytearray(9)
        try:
            MurmurHash3.hash327(byteArray0, -1, 24)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.verifyException("org.apache.commons.codec.digest.MurmurHash3", e)

    def test39(self) -> None:

        try:
            MurmurHash3.hash32x860(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertIsInstance(e, TypeError)
            self.assertEqual(str(e), "object of type 'NoneType' has no len()")

    def test38(self) -> None:

        try:
            MurmurHash3.hash643(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")
            self.assertEqual(type(e), RuntimeError)

    def test37(self) -> None:

        byteArray0 = bytearray(10)

        try:
            MurmurHash3.hash644(byteArray0, 4684, 4684)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            # Index 4684 out of bounds for length 10
            self.verifyException("org.apache.commons.codec.digest.MurmurHash3", e)

    def test36(self) -> None:
        byteArray0 = bytearray()
        longArray0 = MurmurHash3.hash1282(byteArray0, 0, 0, 0)
        self.assertEqual(longArray0, [0, 0])

    def test35(self) -> None:

        byteArray0 = bytearray(6)
        longArray0 = MurmurHash3.hash128x641(byteArray0, 0, 0, 1)
        self.assertEqual([5048724184180415669, 5864299874987029891], longArray0)

    def test34(self) -> None:

        int0 = MurmurHash3.hash320(1, 1)
        self.assertEqual(1037298354, int0)

    def test33(self) -> None:

        int0 = MurmurHash3.hash321(104729, 12, -35)
        self.assertEqual(428332708, int0)

    def test32(self) -> None:

        int0 = MurmurHash3.hash322(23)
        self.assertEqual(1561548038, int0)

    def test31(self) -> None:

        int0 = MurmurHash3.hash323(1861685801266829510, -3390)
        self.assertEqual(-777887350, int0)

    def test30(self) -> None:

        byteArray0 = bytearray(7)
        byteArray0[4] = -3
        int0 = MurmurHash3.hash324(byteArray0)
        self.assertEqual(-1763601783, int0)

    def test29(self) -> None:

        int0 = MurmurHash3.hash325("")
        self.assertEqual(-965378730, int0)

    def test28(self) -> None:

        byteArray0 = bytearray(9)
        int0 = MurmurHash3.hash326(byteArray0, 6)
        self.assertEqual(-380548134, int0)

    def test27(self) -> None:

        byteArray0 = bytearray(7)
        int0 = MurmurHash3.hash326(byteArray0, 1)
        self.assertEqual(500407381, int0)

    def test26(self) -> None:

        byteArray0 = bytearray(3)
        byteArray0[0] = 1
        int0 = MurmurHash3.hash327(byteArray0, 1, 0)
        self.assertEqual(-463810133, int0)

    def test25(self) -> None:

        byteArray0 = bytearray(6)
        byteArray0[1] = 16
        int0 = MurmurHash3.hash327(byteArray0, 2, -1)
        self.assertEqual(2064155002, int0)

    def test24(self) -> None:

        byteArray0 = bytearray(4)
        int0 = MurmurHash3.hash327(byteArray0, 0, 0)
        self.assertEqual(0, int0)

    def test23(self) -> None:

        byteArray0 = bytearray(1)
        int0 = MurmurHash3.hash328(byteArray0, 32, 0, 908)
        self.assertEqual(-1301097675, int0)

    def test22(self) -> None:

        byteArray0 = bytearray(9)
        int0 = MurmurHash3.hash328(byteArray0, 11, 0, -655)
        self.assertEqual(1603053134, int0)

    def test21(self) -> None:

        byteArray0 = bytearray()
        int0 = MurmurHash3.hash32x860(byteArray0)
        self.assertEqual(0, int0)

    def test20(self) -> None:

        byteArray0 = bytearray(7)
        int0 = MurmurHash3.hash32x861(byteArray0, 111, 0, -1613)
        self.assertEqual(583805940, int0)

    def test19(self) -> None:

        int0 = MurmurHash3.hash32x861(None, -569, 0, 0)
        self.assertEqual(0, int0)

    def test18(self) -> None:

        long0 = MurmurHash3.hash641(3157)
        self.assertEqual(-6634736834468170140, long0)

    def test17(self) -> None:

        byteArray0 = bytearray(6)
        long0 = MurmurHash3.hash644(byteArray0, 12, 0)
        self.assertEqual(8404154273843829576, long0)

    def test16(self) -> None:

        byteArray0 = bytearray(7)
        long0 = MurmurHash3.hash645(byteArray0, 0, 0, -2390)
        self.assertEqual(1593541470847758467, long0)

    def test15(self) -> None:

        byteArray0 = bytearray(7)
        murmurHash3_IncrementalHash32x86_0 = MurmurHash3.IncrementalHash32x86()
        murmurHash3_IncrementalHash32x86_0.add(byteArray0, 1, 1)

        try:
            murmurHash3_IncrementalHash32x86_0.add(byteArray0, 1, 223)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.verifyException("org.apache.commons.codec.digest.MurmurHash3", e)

    def test14(self) -> None:
        byteArray0 = bytearray(7)
        byteArray0[5] = -1 & 0xFF
        byteArray0[6] = 51 & 0xFF
        int0 = MurmurHash3.hash324(byteArray0)
        self.assertEqual(1626078053, int0)

    def test13(self) -> None:
        byteArray0 = bytearray(7)
        byteArray0[4] = -3
        byteArray0[5] = 81
        int0 = MurmurHash3.hash324(byteArray0)
        self.assertEqual(1011453179, int0)

    def test12(self) -> None:

        byteArray0 = bytearray(7)
        byteArray0[6] = 7
        int0 = MurmurHash3.hash32x860(byteArray0)
        self.assertEqual(499142092, int0)

    def test11(self) -> None:

        byteArray0 = bytearray(7)
        byteArray0[5] = 1
        int0 = MurmurHash3.hash32x860(byteArray0)
        self.assertEqual(1920566328, int0)

    def test10(self) -> None:

        long0 = MurmurHash3.hash640(2862933555777941757)
        self.assertEqual(7977142960040688617, long0)

    def test09(self) -> None:

        long0 = MurmurHash3.hash642(1)
        self.assertEqual(-3032679231428807052, long0)

    def test08(self) -> None:

        long0 = MurmurHash3.hash642((-6359 & 0xFFFF))
        self.assertEqual(4148648213518644761, long0)

    def test07(self) -> None:

        byteArray0 = bytearray(16)
        long0 = MurmurHash3.hash643(byteArray0)
        self.assertEqual(-4879355010014097355, long0)

    def test06(self) -> None:

        byteArray0 = bytearray(8)
        byteArray0[3] = -24
        long0 = MurmurHash3.hash643(byteArray0)
        self.assertEqual(-596032900876998572, long0)

    def test05(self) -> None:

        byteArray0 = bytearray(7)
        byteArray0[6] = 12
        long0 = MurmurHash3.hash643(byteArray0)
        self.assertEqual(5685171064728034281, long0)

    def test04(self) -> None:

        murmurHash3_IncrementalHash32x86_0 = MurmurHash3.IncrementalHash32x86()
        byteArray0 = bytearray(3)
        murmurHash3_IncrementalHash32x86_0.add(byteArray0, 0, 0)
        self.assertEqual(0, murmurHash3_IncrementalHash32x86_0.end())

    def test03(self) -> None:

        murmurHash3_IncrementalHash32x86_0 = MurmurHash3.IncrementalHash32x86()
        byteArray0 = bytearray(9)
        byteArray0[2] = 58
        int0 = murmurHash3_IncrementalHash32x86_0.finalise(3, 3, byteArray0, -89)
        self.assertEqual(127983477, int0)

    def test02(self) -> None:

        murmurHash3_IncrementalHash32x86_0 = IncrementalHash32x86()
        byteArray0 = bytearray(2)
        byteArray0[1] = 1
        murmurHash3_IncrementalHash32x86_0.add(byteArray0, 1, 1)
        murmurHash3_IncrementalHash32x86_0.add(byteArray0, 1, 1)
        int0 = murmurHash3_IncrementalHash32x86_0.end()
        self.assertEqual(1107827355, int0)

    def test01(self) -> None:

        murmurHash3_IncrementalHash32x86_0 = MurmurHash3.IncrementalHash32x86()
        byteArray0 = bytearray(2)
        byteArray0[1] = 1
        murmurHash3_IncrementalHash32x86_0.add(byteArray0, 1, 1)
        murmurHash3_IncrementalHash32x86_0.add(byteArray0, 1, 1)

        try:
            murmurHash3_IncrementalHash32x86_0.add(byteArray0, 0, 416)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.assertEqual(str(e), "array index out of range")

    def test00(self) -> None:

        byteArray0 = bytearray(9)
        murmurHash3_IncrementalHash32x86_0 = IncrementalHash32x86()
        byteArray1 = bytearray(8)
        byteArray1[5] = 3
        murmurHash3_IncrementalHash32x86_0.add(byteArray1, 3, 3)
        murmurHash3_IncrementalHash32x86_0.add(byteArray0, 3, 3)
        self.assertEqual(70885486, murmurHash3_IncrementalHash32x86_0.end())
