from __future__ import annotations
import functools
import re
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.cli.HelpFormatter import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.Options import *


class BugCLI266Test(unittest.TestCase):

    __sortOrder: typing.List[str] = ["d", "f", "h", "o", "p", "s", "t", "w", "x"]
    __insertedOrder: List[str] = ["h", "d", "f", "x", "s", "p", "t", "w", "o"]

    def testOptionComparatorInsertedOrder(self) -> None:

        options = self.__getOptions().getOptions()
        i = 0
        for o in options:
            self.assertEqual(o.getOpt(), self.__insertedOrder[i])
            i += 1

    def testOptionComparatorDefaultOrder(self) -> None:

        formatter = HelpFormatter()
        options = list(self.__getOptions().getOptions())
        options.sort(key=functools.cmp_to_key(formatter.getOptionComparator()))
        i = 0
        for o in options:
            self.assertEqual(o.getOpt(), self.__sortOrder[i])
            i += 1

    def __getOptions(self) -> Options:

        options = Options()
        help = (
            Option.builder1("h")
            .longOpt("help")
            .desc("Prints this help message")
            .build()
        )
        options.addOption0(help)

        self.__buildOptionsGroup(options)

        t = Option.builder1("t").required0().hasArg0().argName("file").build()
        w = Option.builder1("w").required0().hasArg0().argName("word").build()
        o = Option.builder1("o").hasArg0().argName("directory").build()
        options.addOption0(t)
        options.addOption0(w)
        options.addOption0(o)
        return options

    def __buildOptionsGroup(self, options: Options) -> None:

        firstGroup = OptionGroup()
        secondGroup = OptionGroup()
        firstGroup.setRequired(True)
        secondGroup.setRequired(True)

        firstGroup.addOption(
            Option.builder1("d").longOpt("db").hasArg0().argName("table-name").build()
        )
        firstGroup.addOption(
            Option.builder1("f")
            .longOpt("flat-file")
            .hasArg0()
            .argName("input.csv")
            .build()
        )
        options.addOptionGroup(firstGroup)
        secondGroup.addOption(Option.builder1("x").hasArg0().argName("arg1").build())
        secondGroup.addOption(Option.builder1("s").build())
        secondGroup.addOption(Option.builder1("p").hasArg0().argName("arg1").build())
        options.addOptionGroup(secondGroup)
