from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.CalendarValidator import *
from src.test.org.apache.commons.validator.routines.AbstractCalendarValidatorTest import *
from src.main.org.apache.commons.validator.routines.AbstractCalendarValidator import *
import unittest
import os
import io

# Imports End


class CalendarValidatorTest(AbstractCalendarValidatorTest, unittest.TestCase):

    # Class Fields Begin
    __DATE_2005_11_23: int = None
    __TIME_12_03_45: int = None
    __calValidator: CalendarValidator = None
    # Class Fields End

    # Class Methods Begin
    def testAdjustToTimeZone_test18_decomposed(self) -> None:
        pass

    def testAdjustToTimeZone_test17_decomposed(self) -> None:
        pass

    def testAdjustToTimeZone_test16_decomposed(self) -> None:
        pass

    def testAdjustToTimeZone_test15_decomposed(self) -> None:
        pass

    def testAdjustToTimeZone_test14_decomposed(self) -> None:
        pass

    def testAdjustToTimeZone_test13_decomposed(self) -> None:
        pass

    def testAdjustToTimeZone_test12_decomposed(self) -> None:
        pass

    def testAdjustToTimeZone_test11_decomposed(self) -> None:
        pass

    def testAdjustToTimeZone_test10_decomposed(self) -> None:
        pass

    def testAdjustToTimeZone_test9_decomposed(self) -> None:
        pass

    def testAdjustToTimeZone_test8_decomposed(self) -> None:
        pass

    def testAdjustToTimeZone_test7_decomposed(self) -> None:
        pass

    def testAdjustToTimeZone_test6_decomposed(self) -> None:
        pass

    def testAdjustToTimeZone_test5_decomposed(self) -> None:
        pass

    def testAdjustToTimeZone_test4_decomposed(self) -> None:
        pass

    def testAdjustToTimeZone_test3_decomposed(self) -> None:
        pass

    def testAdjustToTimeZone_test2_decomposed(self) -> None:
        pass

    def testAdjustToTimeZone_test1_decomposed(self) -> None:
        pass

    def testAdjustToTimeZone_test0_decomposed(self) -> None:
        pass

    def testDateTimeStyle_test3_decomposed(self) -> None:
        pass

    def testDateTimeStyle_test2_decomposed(self) -> None:
        pass

    def testDateTimeStyle_test1_decomposed(self) -> None:
        pass

    def testDateTimeStyle_test0_decomposed(self) -> None:
        pass

    def testCompare_test13_decomposed(self) -> None:
        pass

    def testCompare_test12_decomposed(self) -> None:
        pass

    def testCompare_test11_decomposed(self) -> None:
        pass

    def testCompare_test10_decomposed(self) -> None:
        pass

    def testCompare_test9_decomposed(self) -> None:
        pass

    def testCompare_test8_decomposed(self) -> None:
        pass

    def testCompare_test7_decomposed(self) -> None:
        pass

    def testCompare_test6_decomposed(self) -> None:
        pass

    def testCompare_test5_decomposed(self) -> None:
        pass

    def testCompare_test4_decomposed(self) -> None:
        pass

    def testCompare_test3_decomposed(self) -> None:
        pass

    def testCompare_test2_decomposed(self) -> None:
        pass

    def testCompare_test1_decomposed(self) -> None:
        pass

    def testCompare_test0_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test41_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test40_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test39_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test38_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test37_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test36_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test35_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test34_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test33_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test32_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test31_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test30_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test29_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test28_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test27_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test26_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test25_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test24_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test23_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test22_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test21_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test20_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test19_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test18_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test17_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test16_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test15_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test14_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test13_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test12_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test11_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test10_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test9_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test8_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test7_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test6_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test5_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test4_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test3_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test2_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test1_decomposed(self) -> None:
        pass

    def testCalendarValidatorMethods_test0_decomposed(self) -> None:
        pass

    def testFormat(self) -> None:
        pass

    def setUp(self) -> None:
        pass

    def __init__(self, name: str) -> None:
        pass

    # Class Methods End
