from __future__ import annotations
import unittest
import pytest
import io
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.ParseException import *
from src.main.org.apache.commons.cli.PosixParser import *


class BugCLI13Test(unittest.TestCase):

    def testCLI13(self) -> None:

        debugOpt = "debug"
        debug = (
            OptionBuilder.withArgName(debugOpt)
            .withDescription("turn on debugging")
            .withLongOpt(debugOpt)
            .hasArg0()
            .create1("d")
        )
        options = Options()
        options.addOption0(debug)
        commandLine = PosixParser().parse0(options, ["-d", "true"])

        assert commandLine.getOptionValue4(debugOpt) == "true"
        assert commandLine.getOptionValue0("d") == "true"
        assert commandLine.hasOption0("d")
        assert commandLine.hasOption2(debugOpt)
