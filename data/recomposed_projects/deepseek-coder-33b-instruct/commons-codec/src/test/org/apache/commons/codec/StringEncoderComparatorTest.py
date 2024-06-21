from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.StringEncoderComparator import *
from src.main.org.apache.commons.codec.language.DoubleMetaphone import *
from src.main.org.apache.commons.codec.language.Soundex import *


class StringEncoderComparatorTest(unittest.TestCase):

    def testComparatorWithDoubleMetaphoneAndInvalidInput(self) -> None:

        sCompare = StringEncoderComparator(0, DoubleMetaphone())

        compare = sCompare.compare(3.0, 3)
        self.assertEqual(
            "Trying to compare objects that make no sense to the underlying encoder should"
            + " return a zero compare code",
            0,
            compare,
        )

    def testComparatorWithDoubleMetaphone(self) -> None:

        sCompare = StringEncoderComparator(0, DoubleMetaphone())

        testArray = ["Jordan", "Sosa", "Prior", "Pryor"]
        testList = list(testArray)

        controlArray = ["Jordan", "Prior", "Pryor", "Sosa"]

        testList.sort(key=sCompare)

        resultArray = testList

        for i in range(len(resultArray)):
            assert (
                resultArray[i] == controlArray[i]
            ), "Result Array not Equal to Control Array at index: " + str(i)

    def testComparatorWithSoundex(self) -> None:

        sCompare = StringEncoderComparator(0, Soundex(3, False, None, None))

        assert (
            sCompare.compare("O'Brien", "O'Brian") == 0
        ), "O'Brien and O'Brian didn't come out with the same Soundex, something must be wrong here"
