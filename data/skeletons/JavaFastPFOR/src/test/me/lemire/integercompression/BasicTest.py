from __future__ import annotations

# Imports Begin
from src.main.me.lemire.integercompression.synth.ClusteredDataGenerator import *
from src.main.me.lemire.integercompression.differential.XorBinaryPacking import *
from src.main.me.lemire.integercompression.differential.IntegratedVariableByte import *
from src.main.me.lemire.integercompression.differential.IntegratedIntegerCODEC import *
from src.main.me.lemire.integercompression.differential.IntegratedComposition import *
from src.main.me.lemire.integercompression.differential.IntegratedBinaryPacking import *
from src.main.me.lemire.integercompression.differential.Delta import *
from src.main.me.lemire.integercompression.VariableByte import *
from src.test.me.lemire.integercompression.TestUtils import *
from src.main.me.lemire.integercompression.Simple9 import *
from src.main.me.lemire.integercompression.Simple16 import *
from src.main.me.lemire.integercompression.OptPFDS9 import *
from src.main.me.lemire.integercompression.OptPFDS16 import *
from src.main.me.lemire.integercompression.OptPFD import *
from src.main.me.lemire.integercompression.NewPFDS9 import *
from src.main.me.lemire.integercompression.NewPFDS16 import *
from src.main.me.lemire.integercompression.NewPFD import *
from src.main.me.lemire.integercompression.JustCopy import *
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.GroupSimple9 import *
from src.main.me.lemire.integercompression.FastPFOR128 import *
from src.main.me.lemire.integercompression.FastPFOR import *
from src.main.me.lemire.integercompression.DeltaZigzagVariableByte import *
from src.main.me.lemire.integercompression.DeltaZigzagBinaryPacking import *
from src.main.me.lemire.integercompression.Composition import *
from src.main.me.lemire.integercompression.BitPacking import *
from src.main.me.lemire.integercompression.BinaryPacking import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class BasicTest(unittest.TestCase):

    # Class Fields Begin
    codecs: typing.List[IntegerCODEC] = None
    # Class Fields End

    # Class Methods Begin
    def fastPfor128Test_test3_decomposed(self) -> None:
        pass

    def fastPfor128Test_test2_decomposed(self) -> None:
        pass

    def fastPfor128Test_test1_decomposed(self) -> None:
        pass

    def fastPfor128Test_test0_decomposed(self) -> None:
        pass

    def fastPforTest_test3_decomposed(self) -> None:
        pass

    def fastPforTest_test2_decomposed(self) -> None:
        pass

    def fastPforTest_test1_decomposed(self) -> None:
        pass

    def fastPforTest_test0_decomposed(self) -> None:
        pass

    def testUnsortedExample_test44_decomposed(self) -> None:
        pass

    def testUnsortedExample_test43_decomposed(self) -> None:
        pass

    def testUnsortedExample_test42_decomposed(self) -> None:
        pass

    def testUnsortedExample_test41_decomposed(self) -> None:
        pass

    def testUnsortedExample_test40_decomposed(self) -> None:
        pass

    def testUnsortedExample_test39_decomposed(self) -> None:
        pass

    def testUnsortedExample_test38_decomposed(self) -> None:
        pass

    def testUnsortedExample_test37_decomposed(self) -> None:
        pass

    def testUnsortedExample_test36_decomposed(self) -> None:
        pass

    def testUnsortedExample_test35_decomposed(self) -> None:
        pass

    def testUnsortedExample_test34_decomposed(self) -> None:
        pass

    def testUnsortedExample_test33_decomposed(self) -> None:
        pass

    def testUnsortedExample_test32_decomposed(self) -> None:
        pass

    def testUnsortedExample_test31_decomposed(self) -> None:
        pass

    def testUnsortedExample_test30_decomposed(self) -> None:
        pass

    def testUnsortedExample_test29_decomposed(self) -> None:
        pass

    def testUnsortedExample_test28_decomposed(self) -> None:
        pass

    def testUnsortedExample_test27_decomposed(self) -> None:
        pass

    def testUnsortedExample_test26_decomposed(self) -> None:
        pass

    def testUnsortedExample_test25_decomposed(self) -> None:
        pass

    def testUnsortedExample_test24_decomposed(self) -> None:
        pass

    def testUnsortedExample_test23_decomposed(self) -> None:
        pass

    def testUnsortedExample_test22_decomposed(self) -> None:
        pass

    def testUnsortedExample_test21_decomposed(self) -> None:
        pass

    def testUnsortedExample_test20_decomposed(self) -> None:
        pass

    def testUnsortedExample_test19_decomposed(self) -> None:
        pass

    def testUnsortedExample_test18_decomposed(self) -> None:
        pass

    def testUnsortedExample_test17_decomposed(self) -> None:
        pass

    def testUnsortedExample_test16_decomposed(self) -> None:
        pass

    def testUnsortedExample_test15_decomposed(self) -> None:
        pass

    def testUnsortedExample_test14_decomposed(self) -> None:
        pass

    def testUnsortedExample_test13_decomposed(self) -> None:
        pass

    def testUnsortedExample_test12_decomposed(self) -> None:
        pass

    def testUnsortedExample_test11_decomposed(self) -> None:
        pass

    def testUnsortedExample_test10_decomposed(self) -> None:
        pass

    def testUnsortedExample_test9_decomposed(self) -> None:
        pass

    def testUnsortedExample_test8_decomposed(self) -> None:
        pass

    def testUnsortedExample_test7_decomposed(self) -> None:
        pass

    def testUnsortedExample_test6_decomposed(self) -> None:
        pass

    def testUnsortedExample_test5_decomposed(self) -> None:
        pass

    def testUnsortedExample_test4_decomposed(self) -> None:
        pass

    def testUnsortedExample_test3_decomposed(self) -> None:
        pass

    def testUnsortedExample_test2_decomposed(self) -> None:
        pass

    def testUnsortedExample_test1_decomposed(self) -> None:
        pass

    def testUnsortedExample_test0_decomposed(self) -> None:
        pass

    def zeroinzerouttest_test26_decomposed(self) -> None:
        pass

    def zeroinzerouttest_test25_decomposed(self) -> None:
        pass

    def zeroinzerouttest_test24_decomposed(self) -> None:
        pass

    def zeroinzerouttest_test23_decomposed(self) -> None:
        pass

    def zeroinzerouttest_test22_decomposed(self) -> None:
        pass

    def zeroinzerouttest_test21_decomposed(self) -> None:
        pass

    def zeroinzerouttest_test20_decomposed(self) -> None:
        pass

    def zeroinzerouttest_test19_decomposed(self) -> None:
        pass

    def zeroinzerouttest_test18_decomposed(self) -> None:
        pass

    def zeroinzerouttest_test17_decomposed(self) -> None:
        pass

    def zeroinzerouttest_test16_decomposed(self) -> None:
        pass

    def zeroinzerouttest_test15_decomposed(self) -> None:
        pass

    def zeroinzerouttest_test14_decomposed(self) -> None:
        pass

    def zeroinzerouttest_test13_decomposed(self) -> None:
        pass

    def zeroinzerouttest_test12_decomposed(self) -> None:
        pass

    def zeroinzerouttest_test11_decomposed(self) -> None:
        pass

    def zeroinzerouttest_test10_decomposed(self) -> None:
        pass

    def zeroinzerouttest_test9_decomposed(self) -> None:
        pass

    def zeroinzerouttest_test8_decomposed(self) -> None:
        pass

    def zeroinzerouttest_test7_decomposed(self) -> None:
        pass

    def zeroinzerouttest_test6_decomposed(self) -> None:
        pass

    def zeroinzerouttest_test5_decomposed(self) -> None:
        pass

    def zeroinzerouttest_test4_decomposed(self) -> None:
        pass

    def zeroinzerouttest_test3_decomposed(self) -> None:
        pass

    def zeroinzerouttest_test2_decomposed(self) -> None:
        pass

    def zeroinzerouttest_test1_decomposed(self) -> None:
        pass

    def zeroinzerouttest_test0_decomposed(self) -> None:
        pass

    def spuriousouttest_test11_decomposed(self) -> None:
        pass

    def spuriousouttest_test10_decomposed(self) -> None:
        pass

    def spuriousouttest_test9_decomposed(self) -> None:
        pass

    def spuriousouttest_test8_decomposed(self) -> None:
        pass

    def spuriousouttest_test7_decomposed(self) -> None:
        pass

    def spuriousouttest_test6_decomposed(self) -> None:
        pass

    def spuriousouttest_test5_decomposed(self) -> None:
        pass

    def spuriousouttest_test4_decomposed(self) -> None:
        pass

    def spuriousouttest_test3_decomposed(self) -> None:
        pass

    def spuriousouttest_test2_decomposed(self) -> None:
        pass

    def spuriousouttest_test1_decomposed(self) -> None:
        pass

    def spuriousouttest_test0_decomposed(self) -> None:
        pass

    def basictest_test0_decomposed(self) -> None:
        pass

    def verifyWithExceptions_test0_decomposed(self) -> None:
        pass

    def verifyWithoutMask_test0_decomposed(self) -> None:
        pass

    def verifyBitPacking_test0_decomposed(self) -> None:
        pass

    def checkXorBinaryPacking3_test2_decomposed(self) -> None:
        pass

    def checkXorBinaryPacking3_test1_decomposed(self) -> None:
        pass

    def checkXorBinaryPacking3_test0_decomposed(self) -> None:
        pass

    def checkXorBinaryPacking2_test1_decomposed(self) -> None:
        pass

    def checkXorBinaryPacking2_test0_decomposed(self) -> None:
        pass

    def checkXorBinaryPacking1_test1_decomposed(self) -> None:
        pass

    def checkXorBinaryPacking1_test0_decomposed(self) -> None:
        pass

    def checkXorBinaryPacking_test1_decomposed(self) -> None:
        pass

    def checkXorBinaryPacking_test0_decomposed(self) -> None:
        pass

    def checkDeltaZigzagPacking_test7_decomposed(self) -> None:
        pass

    def checkDeltaZigzagPacking_test6_decomposed(self) -> None:
        pass

    def checkDeltaZigzagPacking_test5_decomposed(self) -> None:
        pass

    def checkDeltaZigzagPacking_test4_decomposed(self) -> None:
        pass

    def checkDeltaZigzagPacking_test3_decomposed(self) -> None:
        pass

    def checkDeltaZigzagPacking_test2_decomposed(self) -> None:
        pass

    def checkDeltaZigzagPacking_test1_decomposed(self) -> None:
        pass

    def checkDeltaZigzagPacking_test0_decomposed(self) -> None:
        pass

    def checkDeltaZigzagVB_test3_decomposed(self) -> None:
        pass

    def checkDeltaZigzagVB_test2_decomposed(self) -> None:
        pass

    def checkDeltaZigzagVB_test1_decomposed(self) -> None:
        pass

    def checkDeltaZigzagVB_test0_decomposed(self) -> None:
        pass

    def varyingLengthTest2_test0_decomposed(self) -> None:
        pass

    def varyingLengthTest_test0_decomposed(self) -> None:
        pass

    def saulTest_test0_decomposed(self) -> None:
        pass

    def testUnsorted(self, codec: IntegerCODEC) -> None:
        pass

    @staticmethod
    def maskArray(array: typing.List[int], mask: int) -> None:
        pass

    def __testUnsorted3(self, codec: IntegerCODEC) -> None:
        pass

    def __testUnsorted2(self, codec: IntegerCODEC) -> None:
        pass

    @staticmethod
    def __testCodec(
        c: IntegerCODEC,
        co: IntegerCODEC,
        data: typing.List[typing.List[int]],
        max_: int,
    ) -> None:
        pass

    @staticmethod
    def __test1(N: int, nbr: int) -> None:
        pass

    @staticmethod
    def __test0(c: IntegerCODEC, co: IntegerCODEC, N: int, nbr: int) -> None:
        pass

    @staticmethod
    def __testZeroInZeroOut(c: IntegerCODEC) -> None:
        pass

    @staticmethod
    def __testSpurious(c: IntegerCODEC) -> None:
        pass

    # Class Methods End
