from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.cli.Option import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class DefaultOption(Option):

    # Class Fields Begin
    __serialVersionUID: int = None
    __defaultValue: str = None
    # Class Fields End

    # Class Methods Begin
    def getValue0(self) -> str:
        pass

    def __init__(self, opt: str, description: str, defaultValue: str) -> None:
        pass

    # Class Methods End


class TestOption(Option):

    # Class Fields Begin
    __serialVersionUID: int = None
    # Class Fields End

    # Class Methods Begin
    def addValue(self, value: str) -> bool:
        pass

    def __init__(self, opt: str, hasArg: bool, description: str) -> None:
        pass

    # Class Methods End


class OptionTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testSubclass_test3_decomposed(self) -> None:
        pass

    def testSubclass_test2_decomposed(self) -> None:
        pass

    def testSubclass_test1_decomposed(self) -> None:
        pass

    def testSubclass_test0_decomposed(self) -> None:
        pass

    def testHashCode_test15_decomposed(self) -> None:
        pass

    def testHashCode_test14_decomposed(self) -> None:
        pass

    def testHashCode_test13_decomposed(self) -> None:
        pass

    def testHashCode_test12_decomposed(self) -> None:
        pass

    def testHashCode_test11_decomposed(self) -> None:
        pass

    def testHashCode_test10_decomposed(self) -> None:
        pass

    def testHashCode_test9_decomposed(self) -> None:
        pass

    def testHashCode_test8_decomposed(self) -> None:
        pass

    def testHashCode_test7_decomposed(self) -> None:
        pass

    def testHashCode_test6_decomposed(self) -> None:
        pass

    def testHashCode_test5_decomposed(self) -> None:
        pass

    def testHashCode_test4_decomposed(self) -> None:
        pass

    def testHashCode_test3_decomposed(self) -> None:
        pass

    def testHashCode_test2_decomposed(self) -> None:
        pass

    def testHashCode_test1_decomposed(self) -> None:
        pass

    def testHashCode_test0_decomposed(self) -> None:
        pass

    def testHasArgs_test10_decomposed(self) -> None:
        pass

    def testHasArgs_test9_decomposed(self) -> None:
        pass

    def testHasArgs_test8_decomposed(self) -> None:
        pass

    def testHasArgs_test7_decomposed(self) -> None:
        pass

    def testHasArgs_test6_decomposed(self) -> None:
        pass

    def testHasArgs_test5_decomposed(self) -> None:
        pass

    def testHasArgs_test4_decomposed(self) -> None:
        pass

    def testHasArgs_test3_decomposed(self) -> None:
        pass

    def testHasArgs_test2_decomposed(self) -> None:
        pass

    def testHasArgs_test1_decomposed(self) -> None:
        pass

    def testHasArgs_test0_decomposed(self) -> None:
        pass

    def testHasArgName_test6_decomposed(self) -> None:
        pass

    def testHasArgName_test5_decomposed(self) -> None:
        pass

    def testHasArgName_test4_decomposed(self) -> None:
        pass

    def testHasArgName_test3_decomposed(self) -> None:
        pass

    def testHasArgName_test2_decomposed(self) -> None:
        pass

    def testHasArgName_test1_decomposed(self) -> None:
        pass

    def testHasArgName_test0_decomposed(self) -> None:
        pass

    def testGetValue_test7_decomposed(self) -> None:
        pass

    def testGetValue_test6_decomposed(self) -> None:
        pass

    def testGetValue_test5_decomposed(self) -> None:
        pass

    def testGetValue_test4_decomposed(self) -> None:
        pass

    def testGetValue_test3_decomposed(self) -> None:
        pass

    def testGetValue_test2_decomposed(self) -> None:
        pass

    def testGetValue_test1_decomposed(self) -> None:
        pass

    def testGetValue_test0_decomposed(self) -> None:
        pass

    def testClone_test9_decomposed(self) -> None:
        pass

    def testClone_test8_decomposed(self) -> None:
        pass

    def testClone_test7_decomposed(self) -> None:
        pass

    def testClone_test6_decomposed(self) -> None:
        pass

    def testClone_test5_decomposed(self) -> None:
        pass

    def testClone_test4_decomposed(self) -> None:
        pass

    def testClone_test3_decomposed(self) -> None:
        pass

    def testClone_test2_decomposed(self) -> None:
        pass

    def testClone_test1_decomposed(self) -> None:
        pass

    def testClone_test0_decomposed(self) -> None:
        pass

    def testClear_test5_decomposed(self) -> None:
        pass

    def testClear_test4_decomposed(self) -> None:
        pass

    def testClear_test3_decomposed(self) -> None:
        pass

    def testClear_test2_decomposed(self) -> None:
        pass

    def testClear_test1_decomposed(self) -> None:
        pass

    def testClear_test0_decomposed(self) -> None:
        pass

    def testBuilderMethods_test73_decomposed(self) -> None:
        pass

    def testBuilderMethods_test72_decomposed(self) -> None:
        pass

    def testBuilderMethods_test71_decomposed(self) -> None:
        pass

    def testBuilderMethods_test70_decomposed(self) -> None:
        pass

    def testBuilderMethods_test69_decomposed(self) -> None:
        pass

    def testBuilderMethods_test68_decomposed(self) -> None:
        pass

    def testBuilderMethods_test67_decomposed(self) -> None:
        pass

    def testBuilderMethods_test66_decomposed(self) -> None:
        pass

    def testBuilderMethods_test65_decomposed(self) -> None:
        pass

    def testBuilderMethods_test64_decomposed(self) -> None:
        pass

    def testBuilderMethods_test63_decomposed(self) -> None:
        pass

    def testBuilderMethods_test62_decomposed(self) -> None:
        pass

    def testBuilderMethods_test61_decomposed(self) -> None:
        pass

    def testBuilderMethods_test60_decomposed(self) -> None:
        pass

    def testBuilderMethods_test59_decomposed(self) -> None:
        pass

    def testBuilderMethods_test58_decomposed(self) -> None:
        pass

    def testBuilderMethods_test57_decomposed(self) -> None:
        pass

    def testBuilderMethods_test56_decomposed(self) -> None:
        pass

    def testBuilderMethods_test55_decomposed(self) -> None:
        pass

    def testBuilderMethods_test54_decomposed(self) -> None:
        pass

    def testBuilderMethods_test53_decomposed(self) -> None:
        pass

    def testBuilderMethods_test52_decomposed(self) -> None:
        pass

    def testBuilderMethods_test51_decomposed(self) -> None:
        pass

    def testBuilderMethods_test50_decomposed(self) -> None:
        pass

    def testBuilderMethods_test49_decomposed(self) -> None:
        pass

    def testBuilderMethods_test48_decomposed(self) -> None:
        pass

    def testBuilderMethods_test47_decomposed(self) -> None:
        pass

    def testBuilderMethods_test46_decomposed(self) -> None:
        pass

    def testBuilderMethods_test45_decomposed(self) -> None:
        pass

    def testBuilderMethods_test44_decomposed(self) -> None:
        pass

    def testBuilderMethods_test43_decomposed(self) -> None:
        pass

    def testBuilderMethods_test42_decomposed(self) -> None:
        pass

    def testBuilderMethods_test41_decomposed(self) -> None:
        pass

    def testBuilderMethods_test40_decomposed(self) -> None:
        pass

    def testBuilderMethods_test39_decomposed(self) -> None:
        pass

    def testBuilderMethods_test38_decomposed(self) -> None:
        pass

    def testBuilderMethods_test37_decomposed(self) -> None:
        pass

    def testBuilderMethods_test36_decomposed(self) -> None:
        pass

    def testBuilderMethods_test35_decomposed(self) -> None:
        pass

    def testBuilderMethods_test34_decomposed(self) -> None:
        pass

    def testBuilderMethods_test33_decomposed(self) -> None:
        pass

    def testBuilderMethods_test32_decomposed(self) -> None:
        pass

    def testBuilderMethods_test31_decomposed(self) -> None:
        pass

    def testBuilderMethods_test30_decomposed(self) -> None:
        pass

    def testBuilderMethods_test29_decomposed(self) -> None:
        pass

    def testBuilderMethods_test28_decomposed(self) -> None:
        pass

    def testBuilderMethods_test27_decomposed(self) -> None:
        pass

    def testBuilderMethods_test26_decomposed(self) -> None:
        pass

    def testBuilderMethods_test25_decomposed(self) -> None:
        pass

    def testBuilderMethods_test24_decomposed(self) -> None:
        pass

    def testBuilderMethods_test23_decomposed(self) -> None:
        pass

    def testBuilderMethods_test22_decomposed(self) -> None:
        pass

    def testBuilderMethods_test21_decomposed(self) -> None:
        pass

    def testBuilderMethods_test20_decomposed(self) -> None:
        pass

    def testBuilderMethods_test19_decomposed(self) -> None:
        pass

    def testBuilderMethods_test18_decomposed(self) -> None:
        pass

    def testBuilderMethods_test17_decomposed(self) -> None:
        pass

    def testBuilderMethods_test16_decomposed(self) -> None:
        pass

    def testBuilderMethods_test15_decomposed(self) -> None:
        pass

    def testBuilderMethods_test14_decomposed(self) -> None:
        pass

    def testBuilderMethods_test13_decomposed(self) -> None:
        pass

    def testBuilderMethods_test12_decomposed(self) -> None:
        pass

    def testBuilderMethods_test11_decomposed(self) -> None:
        pass

    def testBuilderMethods_test10_decomposed(self) -> None:
        pass

    def testBuilderMethods_test9_decomposed(self) -> None:
        pass

    def testBuilderMethods_test8_decomposed(self) -> None:
        pass

    def testBuilderMethods_test7_decomposed(self) -> None:
        pass

    def testBuilderMethods_test6_decomposed(self) -> None:
        pass

    def testBuilderMethods_test5_decomposed(self) -> None:
        pass

    def testBuilderMethods_test4_decomposed(self) -> None:
        pass

    def testBuilderMethods_test3_decomposed(self) -> None:
        pass

    def testBuilderMethods_test2_decomposed(self) -> None:
        pass

    def testBuilderMethods_test1_decomposed(self) -> None:
        pass

    def testBuilderMethods_test0_decomposed(self) -> None:
        pass

    def testBuilderInvalidOptionName4_test0_decomposed(self) -> None:
        pass

    def testBuilderInvalidOptionName3_test0_decomposed(self) -> None:
        pass

    def testBuilderInvalidOptionName2_test1_decomposed(self) -> None:
        pass

    def testBuilderInvalidOptionName2_test0_decomposed(self) -> None:
        pass

    def testBuilderInvalidOptionName1_test1_decomposed(self) -> None:
        pass

    def testBuilderInvalidOptionName1_test0_decomposed(self) -> None:
        pass

    def testBuilderInsufficientParams2_test2_decomposed(self) -> None:
        pass

    def testBuilderInsufficientParams2_test1_decomposed(self) -> None:
        pass

    def testBuilderInsufficientParams2_test0_decomposed(self) -> None:
        pass

    def testBuilderInsufficientParams1_test2_decomposed(self) -> None:
        pass

    def testBuilderInsufficientParams1_test1_decomposed(self) -> None:
        pass

    def testBuilderInsufficientParams1_test0_decomposed(self) -> None:
        pass

    @staticmethod
    def __checkOption(
        option: Option,
        opt: str,
        description: str,
        longOpt: str,
        numArgs: int,
        argName: str,
        required: bool,
        optionalArg: bool,
        valueSeparator: str,
        cls: typing.Type[typing.Any],
    ) -> None:
        pass

    # Class Methods End
