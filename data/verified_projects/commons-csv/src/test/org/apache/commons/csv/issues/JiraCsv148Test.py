import pytest

from src.main.org.apache.commons.csv.QuoteMode import *
from src.main.org.apache.commons.csv.CSVFormat import *
import unittest


class JiraCsv148Test(unittest.TestCase):

    @pytest.mark.test
    def testWithIgnoreSurroundingSpacesEmpty(self) -> None:
        format = CSVFormat.DEFAULT\
            .builder()\
            .setQuoteMode(QuoteMode.ALL)\
            .setIgnoreSurroundingSpaces(True)\
            .build()
        try:
            try:
                output = format.format(
                    "",
                    " ",
                    " Single space on the left",
                    "Single space on the right ",
                    " Single spaces on both sides ",
                    "   Multiple spaces on the left",
                    "Multiple spaces on the right   ",
                    "  Multiple spaces on both sides     "
                )
            except TypeError:
                output = format.format(
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
                )
        except AttributeError:
            try:
                output = format.format_(
                    "",
                    " ",
                    " Single space on the left",
                    "Single space on the right ",
                    " Single spaces on both sides ",
                    "   Multiple spaces on the left",
                    "Multiple spaces on the right   ",
                    "  Multiple spaces on both sides     "
                )
            except TypeError:
                output = format.format_(
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
                )
        self.assertEqual(
            "\"\",\" \",\" Single space on the left\",\"Single space on the right \",\" Single" +\
                " spaces on both sides \",\"   Multiple spaces on the left\",\"Multiple" + \
                " spaces on the right   \",\"  Multiple spaces on both sides     \"",
            output
        )
    
    
    @pytest.mark.test
    def testWithTrimEmpty(self) -> None:
        format = CSVFormat.DEFAULT.builder()\
            .setQuoteMode(QuoteMode.ALL)\
            .setTrim(True)\
            .build()
        try:
            try:
                output = format.format(
                    "",
                    " ",
                    " Single space on the left",
                    "Single space on the right ",
                    " Single spaces on both sides ",
                    "   Multiple spaces on the left",
                    "Multiple spaces on the right   ",
                    "  Multiple spaces on both sides     ",
                )
            except TypeError:
                output = format.format(
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
                )
        except AttributeError:
            try:
                output = format.format_(
                    "",
                    " ",
                    " Single space on the left",
                    "Single space on the right ",
                    " Single spaces on both sides ",
                    "   Multiple spaces on the left",
                    "Multiple spaces on the right   ",
                    "  Multiple spaces on both sides     ",
                )
            except TypeError:
                output = format.format_(
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
                )
        self.assertEqual(
            "\"\",\"\",\"Single space on the left\",\"Single space on the right\"," +\
                "\"Single spaces on both sides\",\"Multiple spaces on the left\"," +\
                "\"Multiple spaces on the right\",\"Multiple spaces on both sides\"",
            output
        )
