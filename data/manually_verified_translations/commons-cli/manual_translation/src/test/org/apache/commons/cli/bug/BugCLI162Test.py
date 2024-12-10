from __future__ import annotations
import re
import os
import unittest
import pytest
from io import StringIO
import io
import unittest
from src.main.org.apache.commons.cli.HelpFormatter import *
from src.main.org.apache.commons.cli.Options import *


class BugCLI162Test(unittest.TestCase):

    __sw: io.StringIO = None

    __formatter: HelpFormatter = None

    __PMODE_UNK: str = "Unknown"
    __PMODE_OUT: str = "OUT"
    __PMODE_INOUT: str = "INOUT"
    __PMODE_IN: str = "IN"
    __OPT_WRITE_TO_FILE: str = "w"
    __OPT_USER: str = "u"
    __OPT_TRIM_L: str = "trim"
    __OPT_TIMING: str = "g"
    __OPT_STACK_TRACE: str = "t"
    __OPT_SQL_L: str = "sql"
    __OPT_SQL: str = "s"
    __OPT_PASSWORD_L: str = "password"
    __OPT_PASSWORD: str = "p"
    __OPT_PARAM_TYPES_NAME: str = "Y"
    __OPT_PARAM_TYPES_INT: str = "y"
    __OPT_PARAM_NAMES: str = "a"
    __OPT_PARAM_MODES_NAME: str = "O"
    __OPT_PARAM_MODES_INT: str = "o"
    __OPT_METADATA: str = "m"
    __OPT_JDBC_TO_SFMD_L: str = "jdbc2sfmd"
    __OPT_JDBC_TO_SFMD: str = "2"
    __OPT_INTERACTIVE: str = "i"
    __OPT_HELP_LONG: str = "help"
    __OPT_HELP: str = "h"
    __OPT_FILE_SFMD: str = "f"
    __OPT_FILE_JDBC: str = "j"
    __OPT_FILE_BINDING: str = "b"
    __OPT_DRIVER_INFO: str = "n"
    __OPT_DRIVER: str = "d"
    __OPT_DESCRIPTION: str = "e"
    __OPT_CONNECTION: str = "c"
    __OPT_COLUMN_NAMES: str = "l"
    __OPT: str = "-"
    __CR: str = os.linesep

    __PMODES: str = __PMODE_IN + ", " + __PMODE_INOUT + ", " + __PMODE_OUT + ", " + __PMODE_UNK

    def testLongLineChunkingIndentIgnored(self) -> None:

        options = Options()
        options.addOption3("x", "extralongarg", False, "This description is Long.")
        self.__formatter.printHelp2(
            self.__sw, 22, "org.apache.commons.cli.bug.BugCLI162Test", "Header", options, 0, 5, "Footer"
        )
        expected = (
            "usage:"
            + self.__CR
            + "       org.apache.comm"
            + self.__CR
            + "       ons.cli.bug.Bug"
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
            expected, self.__sw.getvalue(), "Long arguments did not split as expected"
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
            self.__sw,
            35,
            "org.apache.commons.cli.bug.BugCLI162Test",
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
            expected, self.__sw.getvalue(), "Long arguments did not split as expected"
        )

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
        self.__sw = io.StringIO()
