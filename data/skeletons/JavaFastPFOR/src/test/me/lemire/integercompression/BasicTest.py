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
import typing
from typing import *
import io

# Imports End


class BasicTest(unittest.TestCase):

    # Class Fields Begin
    codecs: typing.List[IntegerCODEC] = None
    # Class Fields End

    # Class Methods Begin
    def fastPfor128Test(self) -> None:
        pass

    def fastPforTest(self) -> None:
        pass

    def testUnsortedExample(self) -> None:
        pass

    def zeroinzerouttest(self) -> None:
        pass

    def spuriousouttest(self) -> None:
        pass

    def basictest(self) -> None:
        pass

    def verifyWithExceptions(self) -> None:
        pass

    def verifyWithoutMask(self) -> None:
        pass

    def verifyBitPacking(self) -> None:
        pass

    def checkXorBinaryPacking3(self) -> None:
        pass

    def checkXorBinaryPacking2(self) -> None:
        pass

    def checkXorBinaryPacking1(self) -> None:
        pass

    def checkXorBinaryPacking(self) -> None:
        pass

    def checkDeltaZigzagPacking(self) -> None:
        pass

    def checkDeltaZigzagVB(self) -> None:
        pass

    def varyingLengthTest2(self) -> None:
        pass

    def varyingLengthTest(self) -> None:
        pass

    def saulTest(self) -> None:
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
    def __test(N: int, nbr: int) -> None:
        pass

    @staticmethod
    def __test(c: IntegerCODEC, co: IntegerCODEC, N: int, nbr: int) -> None:
        pass

    @staticmethod
    def __testZeroInZeroOut(c: IntegerCODEC) -> None:
        pass

    @staticmethod
    def __testSpurious(c: IntegerCODEC) -> None:
        pass

    def fastPfor128Test(self) -> None:
        pass

    def fastPforTest(self) -> None:
        pass

    def testUnsorted(self) -> None:
        pass

    def testUnsortedExample(self) -> None:
        pass

    def zeroinzerouttest(self) -> None:
        pass

    def spuriousouttest(self) -> None:
        pass

    def basictest(self) -> None:
        pass

    def verifyWithExceptions(self) -> None:
        pass

    @staticmethod
    def maskArray() -> None:
        pass

    def verifyWithoutMask(self) -> None:
        pass

    def verifyBitPacking(self) -> None:
        pass

    def checkXorBinaryPacking3(self) -> None:
        pass

    def checkXorBinaryPacking2(self) -> None:
        pass

    def checkXorBinaryPacking1(self) -> None:
        pass

    def checkXorBinaryPacking(self) -> None:
        pass

    def checkDeltaZigzagPacking(self) -> None:
        pass

    def checkDeltaZigzagVB(self) -> None:
        pass

    def varyingLengthTest2(self) -> None:
        pass

    def varyingLengthTest(self) -> None:
        pass

    def saulTest(self) -> None:
        pass

    def __testUnsorted3(self) -> None:
        pass

    def __testUnsorted2(self) -> None:
        pass

    @staticmethod
    def __testCodec() -> None:
        pass

    @staticmethod
    def __test() -> None:
        pass

    @staticmethod
    def __test() -> None:
        pass

    @staticmethod
    def __testZeroInZeroOut() -> None:
        pass

    @staticmethod
    def __testSpurious() -> None:
        pass

    # Class Methods End
