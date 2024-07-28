from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.DefaultParser import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.Options import *


class DisablePartialMatchingTest(unittest.TestCase):

    def testRegularPartialMatching(self) -> None:

        parser = DefaultParser(2, False, None)

        options = Options()

        options.addOption0(Option(0, "d", "debug", "Turn on debug.", False, None))
        options.addOption0(Option(0, "e", "extract", "Turn on extract.", False, None))
        options.addOption0(
            Option(0, "o", "option", "Turn on option with argument.", True, None)
        )

        line = parser.parse0(options, ["-de", "--option=foobar"])

        self.assertTrue(
            "There should be an option debug in any case...", line.hasOption2("debug")
        )
        self.assertFalse(
            "There should not be an extract option because partial matching only selects debug",
            line.hasOption2("extract"),
        )
        self.assertTrue(
            "There should be an option option with a argument value",
            line.hasOption2("option"),
        )

    def testDisablePartialMatching(self) -> None:

        parser = DefaultParser(0, False, None)

        options = Options()

        options.addOption0(Option(0, "d", "debug", "Turn on debug.", False, None))
        options.addOption0(Option(0, "e", "extract", "Turn on extract.", False, None))
        options.addOption0(
            Option(0, "o", "option", "Turn on option with argument.", True, None)
        )

        line = parser.parse0(options, ["--debug", "--extract", "--option=foobar"])

        self.assertTrue(line.hasOption2("debug"))
        self.assertTrue(line.hasOption2("extract"))
        self.assertTrue(line.hasOption2("option"))
