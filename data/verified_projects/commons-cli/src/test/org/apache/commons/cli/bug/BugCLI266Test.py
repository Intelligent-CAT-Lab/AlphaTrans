# Imports Begin
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.HelpFormatter import *
import unittest
from typing import *

# Imports End


class BugCLI266Test(unittest.TestCase):

    # Class Methods Begin
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__insertedOrder = ["h", "d", "f", "x", "s", "p", "t", "w", "o"]
        self.__sortOrder = ["d", "f", "h", "o", "p", "s", "t", "w", "x"]


    def __buildOptionsGroup(self, options: Options) -> None:
        firstGroup = OptionGroup()
        secondGroup = OptionGroup()
        firstGroup.setRequired(True)
        secondGroup.setRequired(True)

        firstGroup.addOption(
            Option.builder1("d").longOpt("db").hasArg0().argName("table-name").build()
        )
        firstGroup.addOption(
            Option.builder1("f")\
                .longOpt("flat-file")\
                .hasArg0()\
                .argName("input.csv")\
                .build()\
        )
        options.addOptionGroup(firstGroup)
        secondGroup.addOption(Option.builder1("x").hasArg0().argName("arg1").build())
        secondGroup.addOption(Option.builder1("s").build())
        secondGroup.addOption(Option.builder1("p").hasArg0().argName("arg1").build())
        options.addOptionGroup(secondGroup)

    
    def __getOptions(self) -> Options:
        options = Options()
        help = Option.builder1("h")\
            .longOpt("help")\
            .desc("Prints this help message")\
            .build()
        options.addOption0(help)

        self.__buildOptionsGroup(options)

        t = Option.builder1("t").required0().hasArg0().argName("file").build()
        w = Option.builder1("w").required0().hasArg0().argName("word").build()
        o = Option.builder1("o").hasArg0().argName("directory").build()
        options.addOption0(t)
        options.addOption0(w)
        options.addOption0(o)
        return options

    
    def testOptionComparatorDefaultOrder(self) -> None:
        formatter = HelpFormatter()
        options = list(self.__getOptions().getOptions())
        options.sort(key=formatter.getOptionComparator())
        i = 0
        for o in options:
            self.assertEqual(o.getOpt(), self.__sortOrder[i])
            i += 1

    
    def testOptionComparatorInsertedOrder(self) -> None:
        options = self.__getOptions().getOptions()
        i = 0
        for o in options:
            self.assertEqual(o.getOpt(), self.__insertedOrder[i])
            i += 1

    # Class Methods End
