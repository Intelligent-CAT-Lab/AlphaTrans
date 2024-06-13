# Imports Begin
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.HelpFormatter import *
import unittest
import os
import io

# Imports End


class BugCLI162Test(unittest.TestCase):

    # Class Fields Begin
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

    __OPT_HELP_LONG: str = "help"

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

    __OPT_TRIM_L: str = "trim"

    __OPT_USER: str = "u"

    __OPT_WRITE_TO_FILE: str = "w"

    __PMODE_IN: str = "IN"

    __PMODE_INOUT: str = "INOUT"

    __PMODE_OUT: str = "OUT"

    __PMODE_UNK: str = "Unknown"

    __PMODES: str = __PMODE_IN +\
                    ", " +\
                    __PMODE_INOUT +\
                    ", " +\
                    __PMODE_OUT +\
                    ", " +\
                    __PMODE_UNK
    # Class Fields End

    # Class Methods Begin
    def setUp(self) -> None:
        self.__formatter = HelpFormatter()
        self.__sw = io.StringIO()


    def testInfiniteLoop(self) -> None:
        options = Options()
        options.addOption3("h", "help", False, "This is a looooong description")
        self.__formatter.printHelp2(
            self.__sw,
            20,
            "app",
            None,
            options,
            HelpFormatter.DEFAULT_LEFT_PAD,
            HelpFormatter.DEFAULT_DESC_PAD,
            None,
        )
        expected = "usage: app" +\
                    BugCLI162Test.__CR +\
                    " -h,--help   This is" +\
                    BugCLI162Test.__CR +\
                    "             a" +\
                    BugCLI162Test.__CR +\
                    "             looooon" +\
                    BugCLI162Test.__CR +\
                    "             g" + \
                    BugCLI162Test.__CR +\
                    "             descrip" +\
                    BugCLI162Test.__CR +\
                    "             tion" +\
                    BugCLI162Test.__CR
        self.assertEqual(expected, self.__sw.getvalue())

    
    def testLongLineChunking(self) -> None:
        options = Options()
        options.addOption3(
            "x",
            "extralongarg",
            False,
            "This description has ReallyLongValuesThatAreLongerThanTheWidthOfTheColumns and" +\
                " also other" +\
                " ReallyLongValuesThatAreHugerAndBiggerThanTheWidthOfTheColumnsBob, yes. ",
        )
        self.__formatter.printHelp2(
            self.__sw,
            35,
            type(self).__name__,
            "Header",
            options,
            0,
            5,
            "Footer",
        )
        expected = "usage:" +\
                    BugCLI162Test.__CR +\
                    "       org.apache.commons.cli.bug.B" +\
                    BugCLI162Test.__CR +\
                    "       ugCLI162Test" +\
                    BugCLI162Test.__CR +\
                    "Header" +\
                    BugCLI162Test.__CR +\
                    "-x,--extralongarg     This" +\
                    BugCLI162Test.__CR +\
                    "                      description" +\
                    BugCLI162Test.__CR +\
                    "                      has" +\
                    BugCLI162Test.__CR +\
                    "                      ReallyLongVal" +\
                    BugCLI162Test.__CR +\
                    "                      uesThatAreLon" +\
                    BugCLI162Test.__CR +\
                    "                      gerThanTheWid" +\
                    BugCLI162Test.__CR +\
                    "                      thOfTheColumn" +\
                    BugCLI162Test.__CR +\
                    "                      s and also" +\
                    BugCLI162Test.__CR +\
                    "                      other" +\
                    BugCLI162Test.__CR +\
                    "                      ReallyLongVal" +\
                    BugCLI162Test.__CR +\
                    "                      uesThatAreHug" +\
                    BugCLI162Test.__CR +\
                    "                      erAndBiggerTh" +\
                    BugCLI162Test.__CR +\
                    "                      anTheWidthOfT" +\
                    BugCLI162Test.__CR +\
                    "                      heColumnsBob," +\
                    BugCLI162Test.__CR +\
                    "                      yes." +\
                    BugCLI162Test.__CR +\
                    "Footer" +\
                    BugCLI162Test.__CR
        self.assertEqual(
            expected, self.__sw.getvalue(), "Long arguments did not split as expected"
        )

    
    def testLongLineChunkingIndentIgnored(self) -> None:
        options = Options()
        options.addOption3("x", "extralongarg", False, "This description is Long.")
        self.__formatter.printHelp2(
            self.__sw,
            22,
            type(self).__name__,
            "Header",
            options,
            0,
            5,
            "Footer",
        )
        expected = "usage:" +\
                    BugCLI162Test.__CR +\
                    "       org.apache.commons.cli.bug.Bug" +\
                    BugCLI162Test.__CR +\
                    "       CLI162Test" +\
                    BugCLI162Test.__CR +\
                    "Header" +\
                    BugCLI162Test.__CR +\
                    "-x,--extralongarg" +\
                    BugCLI162Test.__CR +\
                    " This description is" +\
                    BugCLI162Test.__CR +\
                    " Long." +\
                    BugCLI162Test.__CR +\
                    "Footer" +\
                    BugCLI162Test.__CR
        self.assertEqual(
            expected, self.__sw.getvalue(), "Long arguments did not split as expected"
        )

    # Class Methods End
