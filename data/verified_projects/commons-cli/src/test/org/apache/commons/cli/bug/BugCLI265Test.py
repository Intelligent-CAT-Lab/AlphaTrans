# Imports Begin
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.DefaultParser import *
from src.main.org.apache.commons.cli.CommandLine import *
import unittest

# Imports End


class BugCLI265Test(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def setUp(self) -> None:
        self.__parser = DefaultParser(2, False, None)

        optionT1 = Option.builder1("t1")\
                    .hasArg0()\
                    .numberOfArgs(1)\
                    .optionalArg(True)\
                    .argName("t1_path")\
                    .build()
        optionA = Option.builder1("a").hasArg1(False).build()
        optionB = Option.builder1("b").hasArg1(False).build()
        optionLast = Option.builder1("last").hasArg1(False).build()
        self.__options = Options()\
                        .addOption0(optionT1)\
                        .addOption0(optionA)\
                        .addOption0(optionB)\
                        .addOption0(optionLast)

    
    def test_shouldParseConcatenatedShortOptions(self) -> None:
        try:
            concatenatedShortOptions = ["-t1", "-ab"]

            commandLine = self.__parser.parse0(self.__options, concatenatedShortOptions)

            self.assertTrue(commandLine.hasOption2("t1"))
            self.assertIsNone(commandLine.getOptionValue4("t1"))
            self.assertTrue(commandLine.hasOption2("a"))
            self.assertTrue(commandLine.hasOption2("b"))
            self.assertFalse(commandLine.hasOption2("last"))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    def test_shouldParseShortOptionWithoutValue(self) -> None:
        try:
            twoShortOptions = ["-t1", "-last"]

            commandLine = self.__parser.parse0(self.__options, twoShortOptions)

            self.assertTrue(commandLine.hasOption2("t1"))
            self.assertNotEqual(
                "-last",
                commandLine.getOptionValue4("t1"),
                "Second option has been used as value for first option"
            )
            self.assertTrue(commandLine.hasOption2("last"), "Second option has not been detected")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    def test_shouldParseShortOptionWithValue(self) -> None:
        try:
            shortOptionWithValue = ["-t1", "path/to/my/db"]

            commandLine = self.__parser.parse0(self.__options, shortOptionWithValue)

            self.assertEqual("path/to/my/db", commandLine.getOptionValue4("t1"))
            self.assertFalse(commandLine.hasOption2("last"))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    # Class Methods End
