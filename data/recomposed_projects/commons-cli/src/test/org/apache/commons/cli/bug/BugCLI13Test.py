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
    def testCLI13(self) -> None:

        debug_opt = "debug"
        debug = (
            OptionBuilder.with_arg_name(debug_opt)
            .with_description("turn on debugging")
            .with_long_opt(debug_opt)
            .has_arg0()
            .create1("d")
        )
        options = Options()
        options.add_option0(debug)
        command_line = PosixParser().parse0(options, ["-d", "true"])
        self.assertEqual(command_line.get_option_value4(debug_opt), "true")
        self.assertEqual(command_line.get_option_value0("d"), "true")
        self.assertTrue(command_line.has_option0("d"))
        self.assertTrue(command_line.has_option2(debug_opt))

    # Class Methods End
