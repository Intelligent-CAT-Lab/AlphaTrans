# Imports Begin
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.HelpFormatter import *
import unittest
import typing
from typing import *

# Imports End


class BugCLI266Test(unittest.TestCase):

    # Class Fields Begin
    __insertedOrder: List[str] = ["h", "d", "f", "x", "s", "p", "t", "w", "o"]
    __sortOrder: List[str] = ["d", "f", "h", "o", "p", "s", "t", "w", "x"]
    # Class Fields End

    # Class Methods Begin
    def testOptionComparatorInsertedOrder(self) -> None:

        options = self.getOptions().getOptions()
        i = 0
        for o in options:
            Assert.self.assertEqual(o.getOpt(), self.__insertedOrder[i])
            i += 1

    def testOptionComparatorDefaultOrder(self) -> None:

        formatter = HelpFormatter()
        options = list(self.getOptions().getOptions())
        options.sort(key=formatter.getOptionComparator())
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

        first_group = OptionGroup()
        second_group = OptionGroup()
        first_group.setRequired(True)
        second_group.setRequired(True)
        first_group.addOption(
            Option.builder1("d").longOpt("db").hasArg0().argName("table-name").build()
        )
        first_group.addOption(
            Option.builder1("f")
            .longOpt("flat-file")
            .hasArg0()
            .argName("input.csv")
            .build()
        )
        options.addOptionGroup(first_group)
        second_group.addOption(Option.builder1("x").hasArg0().argName("arg1").build())
        second_group.addOption(Option.builder1("s").build())
        second_group.addOption(Option.builder1("p").hasArg0().argName("arg1").build())
        options.addOptionGroup(second_group)

    # Class Methods End
