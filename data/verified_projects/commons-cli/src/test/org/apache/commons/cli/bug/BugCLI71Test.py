import pytest

from src.main.org.apache.commons.cli.PosixParser import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.MissingArgumentException import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.CommandLine import *
import unittest


class BugCLI71Test(unittest.TestCase):

    def setUp(self) -> None:
        self.__options = Options()

        algorithm = Option(
            0, "a", "algo", "the algorithm which it to perform executing", True, None
        )
        algorithm.setArgName("algorithm name")
        self.__options.addOption0(algorithm)

        key = Option(
            0, "k", "key", "the key the setted algorithm uses to process", True, None
        )
        algorithm.setArgName("value")
        self.__options.addOption0(key)

        self.__parser = PosixParser()
    
    
    @pytest.mark.test
    def testBasic(self) -> None:
        try:
            args = ["-a", "Caesar", "-k", "A"]
            line = self.__parser.parse0(self.__options, args)
            self.assertEqual("Caesar", line.getOptionValue4("a"))
            self.assertEqual("A", line.getOptionValue4("k"))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testGetsDefaultIfOptional(self) -> None:
        try:
            args = ["-k", "-a", "Caesar"]
            self.__options.getOption("k").setOptionalArg(True)
            line = self.__parser.parse0(self.__options, args)

            self.assertEqual("Caesar", line.getOptionValue4("a"))
            self.assertEqual("a", line.getOptionValue1('k', "a"))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testLackOfError(self) -> None:
        try:
            args = ["-k", "-a", "Caesar"]
            try:
                self.__parser.parse0(self.__options, args)
                self.fail("MissingArgumentException expected")
            except MissingArgumentException as e:
                self.assertEqual("k", e.getOption().getOpt(), "option missing an argument")
        except Exception as e:
            self.fail(f"An unexpected exception occurred. Expected MissingArgumentException but got: {e}")

    
    @pytest.mark.test
    def testMistakenArgument(self) -> None:
        try:
            args = ["-a", "Caesar", "-k", "A"]
            line = self.__parser.parse0(self.__options, args)
            args = ["-a", "Caesar", "-k", "a"]
            line = self.__parser.parse0(self.__options, args)
            self.assertEqual("Caesar", line.getOptionValue4("a"))
            self.assertEqual("a", line.getOptionValue4("k"))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

