from __future__ import annotations
import re
import os
import unittest
import pytest
import io
import unittest
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

        self.assertEqual("true", commandLine.getOptionValue4(debugOpt))
        self.assertEqual("true", commandLine.getOptionValue0("d"))
        self.assertTrue(commandLine.hasOption0("d"))
        self.assertTrue(commandLine.hasOption2(debugOpt))
