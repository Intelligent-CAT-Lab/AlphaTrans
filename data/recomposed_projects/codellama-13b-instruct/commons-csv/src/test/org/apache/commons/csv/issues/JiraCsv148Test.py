# Imports Begin
from src.main.org.apache.commons.csv.QuoteMode import *
from src.main.org.apache.commons.csv.CSVFormat import *
import unittest

# Imports End


class JiraCsv148Test(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testWithTrimEmpty(self) -> None:

        format = (
            CSVFormat.DEFAULT.builder()
            .setQuoteMode(QuoteMode.ALL)
            .setTrim(True)
            .build()
        )
        self.assertEqual(
            '"","","Single space on the left","Single space on the right",'
            + '"Single spaces on both sides","Multiple spaces on the left",'
            + '"Multiple spaces on the right","Multiple spaces on both sides"',
            format.format(
                "",
                " ",
                " Single space on the left",
                "Single space on the right ",
                " Single spaces on both sides ",
                "   Multiple spaces on the left",
                "Multiple spaces on the right   ",
                "  Multiple spaces on both sides     ",
            ),
        )

    def testWithIgnoreSurroundingSpacesEmpty(self) -> None:

        pass  # LLM could not translate method body

    # Class Methods End
