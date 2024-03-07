# Imports Begin
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.DefaultParser import *
from src.main.org.apache.commons.cli.CommandLine import *
import unittest

# Imports End


class BugCLI265Test(unittest.TestCase):

    # Class Fields Begin
    __parser: DefaultParser = None
    __options: Options = None
    # Class Fields End

    # Class Methods Begin
    def shouldParseShortOptionWithValue(self) -> None:

        short_option_with_value = ["-t1", "path/to/my/db"]
        command_line = self.parser.parse0(self.__options, short_option_with_value)
        self.assertEqual(command_line.getOptionValue4("t1"), "path/to/my/db")
        self.assertFalse(command_line.hasOption2("last"))

    def shouldParseShortOptionWithoutValue(self) -> None:

        two_short_options = ["-t1", "-last"]
        command_line = self.parser.parse0(self.options, two_short_options)
        assert command_line.hasOption2("t1")
        assert command_line.getOptionValue4("t1") != "-last"
        assert command_line.hasOption2("last")

    def shouldParseConcatenatedShortOptions(self) -> None:

        concatenated_short_options = ["-t1", "-ab"]
        command_line = self.__parser.parse0(self.__options, concatenated_short_options)
        assert command_line.hasOption2("t1")
        assert command_line.getOptionValue4("t1") is None
        assert command_line.hasOption2("a")
        assert command_line.hasOption2("b")
        assert not command_line.hasOption2("last")

    def setUp(self) -> None:

        self.__parser = DefaultParser(2, False, None)
        option_t1 = (
            Option.builder1("t1")
            .hasArg0()
            .numberOfArgs(1)
            .optionalArg(True)
            .argName("t1_path")
            .build()
        )
        option_a = Option.builder1("a").hasArg1(False).build()
        option_b = Option.builder1("b").hasArg1(False).build()
        option_last = Option.builder1("last").hasArg1(False).build()
        self.__options = (
            Options()
            .addOption0(option_t1)
            .addOption0(option_a)
            .addOption0(option_b)
            .addOption0(option_last)
        )

    # Class Methods End
