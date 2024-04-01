# Imports Begin
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.HelpFormatter import *
import unittest
import os
import io

# Imports End


class BugCLI162Test(unittest.TestCase):

    # Class Fields Begin
    __PMODES: str = "PMODE_IN, PMODE_INOUT, PMODE_OUT, PMODE_UNK"
    __formatter: HelpFormatter = None
    __sw: io.StringIO = None
    __CR: str = os.linesep
    __OPT: str = "-"
    __OPT_COLUMN_NAMES: str = "l"
    __OPT_CONNECTION: str = "c"
    __OPT_DESCRIPTION: str = "e"
    __OPT_DRIVER: str = "d"
    __OPT_DRIVER_INFO: str = "n"
    __OPT_FILE_BINDING: str = "b"
    __OPT_FILE_JDBC: str = "j"
    __OPT_FILE_SFMD: str = "f"
    __OPT_HELP: str = "h"
    __OPT_HELP_LONG: str = ""  # LLM could not translate field
    __OPT_INTERACTIVE: str = "i"
    __OPT_JDBC_TO_SFMD: str = "2"
    __OPT_JDBC_TO_SFMD_L: str = "jdbc2sfmd"
    __OPT_METADATA: str = "m"
    __OPT_PARAM_MODES_INT: str = "o"
    __OPT_PARAM_MODES_NAME: str = "O"
    __OPT_PARAM_NAMES: str = "a"
    __OPT_PARAM_TYPES_INT: str = "y"
    __OPT_PARAM_TYPES_NAME: str = "Y"
    __OPT_PASSWORD: str = "p"
    __OPT_PASSWORD_L: str = "password"
    __OPT_SQL: str = "s"
    __OPT_SQL_L: str = "sql"
    __OPT_STACK_TRACE: str = "t"
    __OPT_TIMING: str = "g"
    __OPT_TRIM_L: str = ""  # LLM could not translate field
    __OPT_USER: str = ""  # LLM could not translate field
    __OPT_WRITE_TO_FILE: str = "w"
    __PMODE_IN: str = "IN"
    __PMODE_INOUT: str = "INOUT"
    __PMODE_OUT: str = "OUT"
    __PMODE_UNK: str = "Unknown"
    # Class Fields End

    # Class Methods Begin
    def testLongLineChunkingIndentIgnored(self) -> None:

        options = Options()
        options.addOption3("x", "extralongarg", False, "This description is Long.")
        self.__formatter.printHelp2(
            io.StringIO(),
            22,
            self.__class__.__name__,
            "Header",
            options,
            0,
            5,
            "Footer",
        )
        expected = (
            "usage:"
            + self.__CR
            + "       org.apache.commons.cli.bug.Bug"
            + self.__CR
            + "       CLI162Test"
            + self.__CR
            + "Header"
            + self.__CR
            + "-x,--extralongarg"
            + self.__CR
            + " This description is"
            + self.__CR
            + " Long."
            + self.__CR
            + "Footer"
            + self.__CR
        )
        self.assertEqual(
            "Long arguments did not split as expected", expected, self.__sw.getvalue()
        )

    def testLongLineChunking(self) -> None:

        options = Options()
        options.addOption3(
            "x",
            "extralongarg",
            False,
            "This description has ReallyLongValuesThatAreLongerThanTheWidthOfTheColumns and"
            + " also other"
            + " ReallyLongValuesThatAreHugerAndBiggerThanTheWidthOfTheColumnsBob, yes. ",
        )
        self.__formatter.printHelp2(
            io.TextIOWrapper(self.__sw),
            35,
            self.getClass().getName(),
            "Header",
            options,
            0,
            5,
            "Footer",
        )
        expected = (
            "usage:"
            + self.__CR
            + "       org.apache.commons.cli.bug.B"
            + self.__CR
            + "       ugCLI162Test"
            + self.__CR
            + "Header"
            + self.__CR
            + "-x,--extralongarg     This"
            + self.__CR
            + "                      description"
            + self.__CR
            + "                      has"
            + self.__CR
            + "                      ReallyLongVal"
            + self.__CR
            + "                      uesThatAreLon"
            + self.__CR
            + "                      gerThanTheWid"
            + self.__CR
            + "                      thOfTheColumn"
            + self.__CR
            + "                      s and also"
            + self.__CR
            + "                      other"
            + self.__CR
            + "                      ReallyLongVal"
            + self.__CR
            + "                      uesThatAreHug"
            + self.__CR
            + "                      erAndBiggerTh"
            + self.__CR
            + "                      anTheWidthOfT"
            + self.__CR
            + "                      heColumnsBob,"
            + self.__CR
            + "                      yes."
            + self.__CR
            + "Footer"
            + self.__CR
        )
        self.assertEqual(
            "Long arguments did not split as expected", expected, self.__sw.toString()
        )

    def testInfiniteLoop(self) -> None:

        options = Options()
        options.addOption3("h", "help", False, "This is a looooong description")
        self.__formatter.printHelp2(
            io.TextIOWrapper(self.__sw),
            20,
            "app",
            None,
            options,
            HelpFormatter.DEFAULT_LEFT_PAD,
            HelpFormatter.DEFAULT_DESC_PAD,
            None,
        )
        expected = (
            "usage: app"
            + self.__CR
            + " -h,--help   This is"
            + self.__CR
            + "             a"
            + self.__CR
            + "             looooon"
            + self.__CR
            + "             g"
            + self.__CR
            + "             descrip"
            + self.__CR
            + "             tion"
            + self.__CR
        )
        self.assertEqual(expected, self.__sw.getvalue())

    def setUp(self) -> None:

        self.__formatter = HelpFormatter()
        self.__sw = StringWriter()

    # Class Methods End
