from __future__ import annotations
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.MissingArgumentException import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.PosixParser import *


class BugCLI71Test(unittest.TestCase):

    __parser: CommandLineParser = None

    __options: Options = None

    def testMistakenArgument(self) -> None:

        args = ["-a", "Caesar", "-k", "A"]
        line = self.parser.parse0(self.options, args)
        self.assertEqual("Caesar", line.getOptionValue4("a"))
        self.assertEqual("A", line.getOptionValue4("k"))

        args = ["-a", "Caesar", "-k", "a"]
        line = self.parser.parse0(self.options, args)
        self.assertEqual("Caesar", line.getOptionValue4("a"))
        self.assertEqual("a", line.getOptionValue4("k"))

    def testLackOfError(self) -> None:

        args = ["-k", "-a", "Caesar"]
        try:
            self.parser.parse0(self.options, args)
            self.fail("MissingArgumentException expected")
        except MissingArgumentException as e:
            self.assertEqual("option missing an argument", "k", e.getOpt())

    def testGetsDefaultIfOptional(self) -> None:

        args = ["-k", "-a", "Caesar"]
        self.options.getOption("k").setOptionalArg(True)
        line = self.parser.parse0(self.options, args)

        self.assertEqual("Caesar", line.getOptionValue4("a"))
        self.assertEqual("a", line.getOptionValue1("k", "a"))

    def testBasic(self) -> None:

        args = ["-a", "Caesar", "-k", "A"]
        line = self.parser.parse0(self.options, args)
        self.assertEqual("Caesar", line.getOptionValue4("a"))
        self.assertEqual("A", line.getOptionValue4("k"))

    def setUp(self) -> None:

        self.options = Options()

        algorithm = Option(
            0, "a", "algo", "the algorithm which it to perform executing", True, None
        )
        algorithm.setArgName("algorithm name")
        self.options.addOption0(algorithm)

        key = Option(
            0, "k", "key", "the key the setted algorithm uses to process", True, None
        )
        key.setArgName("value")
        self.options.addOption0(key)

        self.parser = PosixParser()
