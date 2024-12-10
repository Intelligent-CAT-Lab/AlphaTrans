from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.QuoteMode import *


class JiraCsv148Test(unittest.TestCase):

    def testWithTrimEmpty(self) -> None:

        format_ = (
            CSVFormat.DEFAULT.builder()
            .setQuoteMode(QuoteMode.ALL)
            .setTrim(True)
            .build()
        )

        self.assertEqual(
            '"","","Single space on the left","Single space on the right",'
            + '"Single spaces on both sides","Multiple spaces on the left",'
            + '"Multiple spaces on the right","Multiple spaces on both sides"',
            format_.format_(
                [
                    "",
                    " ",
                    " Single space on the left",
                    "Single space on the right ",
                    " Single spaces on both sides ",
                    "   Multiple spaces on the left",
                    "Multiple spaces on the right   ",
                    "  Multiple spaces on both sides     "
                ]
            ),
        )

    def testWithIgnoreSurroundingSpacesEmpty(self) -> None:

        format_ = (
            CSVFormat.DEFAULT.builder()
            .setQuoteMode(QuoteMode.ALL)
            .setIgnoreSurroundingSpaces(True)
            .build()
        )

        self.assertEqual(
            '""," "," Single space on the left","Single space on the right "," Single'
            + ' spaces on both sides ","   Multiple spaces on the left","Multiple'
            + ' spaces on the right   ","  Multiple spaces on both sides     "',
            format_.format_(
                [
                    "",
                    " ",
                    " Single space on the left",
                    "Single space on the right ",
                    " Single spaces on both sides ",
                    "   Multiple spaces on the left",
                    "Multiple spaces on the right   ",
                    "  Multiple spaces on both sides     "
                ]
            ),
        )
