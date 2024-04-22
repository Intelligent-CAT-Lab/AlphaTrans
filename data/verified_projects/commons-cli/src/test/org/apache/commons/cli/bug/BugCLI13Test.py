# Imports Begin
from src.main.org.apache.commons.cli.PosixParser import *
from src.main.org.apache.commons.cli.ParseException import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.CommandLine import *
import unittest
import os

# Imports End


class BugCLI13Test(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def test_CLI13(self) -> None:
        try:
            debugOpt = "debug"
            debug = OptionBuilder.withArgName(debugOpt)\
                .withDescription("turn on debugging")\
                .withLongOpt(debugOpt)\
                .hasArg0()\
                .create1('d')
            options = Options()
            options.add_option0(debug)
            commandLine = PosixParser().parse0(options, ["-d", "true"])

            self.assertEqual(commandLine.getOptionValue4(debugOpt), "true")
            self.assertEqual(commandLine.getOptionValue0('d'), "true")
            self.assertTrue(commandLine.hasOption0('d'))
            self.assertTrue(commandLine.hasOption2(debugOpt))
        except ParseException as e:
            self.fail(f"ParseException occurred: {e}")

    # Class Methods End
