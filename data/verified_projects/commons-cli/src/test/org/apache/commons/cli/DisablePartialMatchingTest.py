import pytest

# Imports Begin
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.DefaultParser import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.CommandLine import *
import unittest

# Imports End


class DisablePartialMatchingTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    @pytest.mark.test
    def testDisablePartialMatching(self) -> None:
        try:
            parser = DefaultParser(0, False, None)
            options = Options()
            options.addOption0(Option(0, "d", "debug", "Turn on debug.", False, None))
            options.addOption0(Option(0, "e", "extract", "Turn on extract.", False, None))
            options.addOption0(
                Option(0, "o", "option", "Turn on option with argument.", True, None)
            )
            line = parser.parse0(options, ["-de", "--option=foobar"])
            self.assertTrue(
                line.hasOption2("debug"), "There should be an option debug in any case..."
            )
            self.assertTrue(
                line.hasOption2("extract"),
                "There should be an extract option because partial matching is off"
            )
            self.assertTrue(
                line.hasOption2("option"),
                "There should be an option option with a argument value"
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @pytest.mark.test
    def testRegularPartialMatching(self) -> None:
        try:
            parser = DefaultParser(2, False, None)
            options = Options()
            options.addOption0(Option(0, "d", "debug", "Turn on debug.", False, None))
            options.addOption0(Option(0, "e", "extract", "Turn on extract.", False, None))
            options.addOption0(
                Option(0, "o", "option", "Turn on option with argument.", True, None)
            )
            line = parser.parse0(options, ["-de", "--option=foobar"])
            self.assertTrue(
                line.hasOption2("debug"), "There should be an option debug in any case..."
            )
            self.assertFalse(
                line.hasOption2("extract"),
                "There should not be an extract option because partial matching only selects debug"
            )
            self.assertTrue(
                line.hasOption2("option"),
                "There should be an option option with a argument value"
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    # Class Methods End
