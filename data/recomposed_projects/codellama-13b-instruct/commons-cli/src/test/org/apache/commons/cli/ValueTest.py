# Imports Begin
from src.main.org.apache.commons.cli.PosixParser import *
from src.main.org.apache.commons.cli.Parser import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.CommandLine import *
import unittest
import os

# Imports End


class ValueTest(unittest.TestCase):

    # Class Fields Begin
    __cl: CommandLine = None
    __opts: Options = Options()
    # Class Fields End

    # Class Methods Begin
    def testShortWithArgWithOption(self) -> None:

        pass  # LLM could not translate method body

    def testShortWithArg(self) -> None:

        pass  # LLM could not translate method body

    def testShortOptionalNArgValuesWithOption(self) -> None:

        args = ["-i", "ink", "idea", "isotope", "ice"]
        parser = PosixParser()
        cmd = parser.parse0(self.__opts, args)
        self.assertTrue(cmd.hasOption2("i"))
        self.assertEqual("ink", cmd.getOptionValue2(self.__opts.getOption("i")))
        self.assertEqual("ink", cmd.getOptionValues1(self.__opts.getOption("i"))[0])
        self.assertEqual("idea", cmd.getOptionValues1(self.__opts.getOption("i"))[1])
        self.assertEqual(cmd.getArgs().length, 2)
        self.assertEqual("isotope", cmd.getArgs()[0])
        self.assertEqual("ice", cmd.getArgs()[1])

    def testShortOptionalNArgValues(self) -> None:

        args = ["-i", "ink", "idea", "isotope", "ice"]
        parser = PosixParser()
        cmd = parser.parse0(self.__opts, args)
        assert cmd.hasOption2("i")
        assert cmd.getOptionValue4("i") == "ink"
        assert cmd.getOptionValues2("i")[0] == "ink"
        assert cmd.getOptionValues2("i")[1] == "idea"
        assert len(cmd.getArgs()) == 2
        assert cmd.getArgs()[0] == "isotope"
        assert cmd.getArgs()[1] == "ice"

    def testShortOptionalArgValueWithOption(self) -> None:

        args = ["-e", "everything"]
        parser = PosixParser()
        cmd = parser.parse0(self.__opts, args)
        self.assertTrue(cmd.hasOption1(self.__opts.getOption("e")))
        self.assertEqual("everything", cmd.getOptionValue2(self.__opts.getOption("e")))

    def testShortOptionalArgValuesWithOption(self) -> None:

        args = ["-j", "ink", "idea"]
        parser = PosixParser()
        cmd = parser.parse0(self.__opts, args)
        assert cmd.hasOption1(self.__opts.getOption("j"))
        assert cmd.getOptionValue2(self.__opts.getOption("j")) == "ink"
        assert cmd.getOptionValues1(self.__opts.getOption("j"))[0] == "ink"
        assert cmd.getOptionValues1(self.__opts.getOption("j"))[1] == "idea"
        assert len(cmd.getArgs()) == 0

    def testShortOptionalArgValues(self) -> None:

        args = ["-j", "ink", "idea"]
        parser = PosixParser()
        cmd = parser.parse0(self.__opts, args)
        assert cmd.hasOption2("j")
        assert cmd.getOptionValue4("j") == "ink"
        assert cmd.getOptionValues2("j")[0] == "ink"
        assert cmd.getOptionValues2("j")[1] == "idea"
        assert len(cmd.getArgs()) == 0

    def testShortOptionalArgValue(self) -> None:

        args = ["-e", "everything"]
        parser = PosixParser()
        cmd = parser.parse0(self.__opts, args)
        self.assertTrue(cmd.hasOption2("e"))
        self.assertEqual("everything", cmd.getOptionValue4("e"))

    def testShortOptionalArgNoValueWithOption(self) -> None:

        args = ["-e"]
        parser = PosixParser()
        cmd = parser.parse0(self.__opts, args)
        self.assertTrue(cmd.hasOption1(self.__opts.getOption("e")))
        assertNull(cmd.getOptionValue2(self.__opts.getOption("e")))

    def testShortOptionalArgNoValue(self) -> None:

        args = ["-e"]
        parser = PosixParser()
        cmd = parser.parse0(self.__opts, args)
        assert cmd.hasOption2("e")
        assert cmd.getOptionValue4("e") is None

    def testShortNoArgWithOption(self) -> None:

        assert self.__cl.hasOption1(self.__opts.getOption("a"))
        assert self.__cl.getOptionValue2(self.__opts.getOption("a")) is None

    def testShortNoArg(self) -> None:

        pass  # LLM could not translate method body

    def testLongWithArgWithOption(self) -> None:

        pass  # LLM could not translate method body

    def testLongWithArg(self) -> None:

        pass  # LLM could not translate method body

    def testLongOptionalNoValueWithOption(self) -> None:

        args = ["--fish"]
        parser = PosixParser()
        cmd = parser.parse0(self.__opts, args)
        self.assertTrue(cmd.hasOption1(self.__opts.getOption("fish")))
        assertNull(cmd.getOptionValue2(self.__opts.getOption("fish")))

    def testLongOptionalNoValue(self) -> None:

        args = ["--fish"]
        cmd = self.parse0(self.__opts, args)
        assert cmd.hasOption2("fish")
        assert cmd.getOptionValue4("fish") is None

    def testLongOptionalNArgValuesWithOption(self) -> None:

        args = ["--hide", "house", "hair", "head"]
        parser = PosixParser()
        cmd = parser.parse0(self.__opts, args)
        assert cmd.hasOption1(self.__opts.getOption("hide"))
        assert cmd.getOptionValue2(self.__opts.getOption("hide")) == "house"
        assert cmd.getOptionValues1(self.__opts.getOption("hide"))[0] == "house"
        assert cmd.getOptionValues1(self.__opts.getOption("hide"))[1] == "hair"
        assert len(cmd.getArgs()) == 1
        assert cmd.getArgs()[0] == "head"

    def testLongOptionalNArgValues(self) -> None:

        args = ["--hide", "house", "hair", "head"]
        parser = PosixParser()
        cmd = parser.parse0(self.__opts, args)
        assert cmd.hasOption2("hide")
        assert cmd.getOptionValue4("hide") == "house"
        assert cmd.getOptionValues2("hide")[0] == "house"
        assert cmd.getOptionValues2("hide")[1] == "hair"
        assert len(cmd.getArgs()) == 1
        assert cmd.getArgs()[0] == "head"

    def testLongOptionalArgValueWithOption(self) -> None:

        args = ["--fish", "face"]
        parser = PosixParser()
        cmd = parser.parse0(self.__opts, args)
        self.assertTrue(cmd.hasOption1(self.__opts.getOption("fish")))
        self.assertEqual("face", cmd.getOptionValue2(self.__opts.getOption("fish")))

    def testLongOptionalArgValuesWithOption(self) -> None:

        args = ["--gravy", "gold", "garden"]
        parser = PosixParser()
        cmd = parser.parse0(self.__opts, args)
        assert cmd.hasOption1(self.__opts.getOption("gravy"))
        assert cmd.getOptionValue2(self.__opts.getOption("gravy")) == "gold"
        assert cmd.getOptionValues1(self.__opts.getOption("gravy"))[0] == "gold"
        assert cmd.getOptionValues1(self.__opts.getOption("gravy"))[1] == "garden"
        assert len(cmd.getArgs()) == 0

    def testLongOptionalArgValues(self) -> None:

        args = ["--gravy", "gold", "garden"]
        parser = PosixParser()
        cmd = parser.parse0(self.__opts, args)
        assert cmd.hasOption2("gravy")
        assert cmd.getOptionValue4("gravy") == "gold"
        assert cmd.getOptionValues2("gravy")[0] == "gold"
        assert cmd.getOptionValues2("gravy")[1] == "garden"
        assert len(cmd.getArgs()) == 0

    def testLongOptionalArgValue(self) -> None:

        args = ["--fish", "face"]
        parser = PosixParser()
        cmd = parser.parse0(self.__opts, args)
        assert cmd.hasOption2("fish")
        assert cmd.getOptionValue4("fish") == "face"

    def testLongNoArgWithOption(self) -> None:

        pass  # LLM could not translate method body

    def testLongNoArg(self) -> None:

        assert self.__cl.hasOption2("c")
        assert self.__cl.getOptionValue4("c") is None

    def setUp(self) -> None:

        self.__opts.addOption1("a", False, "toggle -a")
        self.__opts.addOption1("b", True, "set -b")
        self.__opts.addOption3("c", "c", False, "toggle -c")
        self.__opts.addOption3("d", "d", True, "set -d")
        self.__opts.addOption0(OptionBuilder.hasOptionalArg().create1("e"))
        self.__opts.addOption0(
            OptionBuilder.hasOptionalArg().withLongOpt("fish").create0()
        )
        self.__opts.addOption0(
            OptionBuilder.hasOptionalArgs0().withLongOpt("gravy").create0()
        )
        self.__opts.addOption0(
            OptionBuilder.hasOptionalArgs1(2).withLongOpt("hide").create0()
        )
        self.__opts.addOption0(OptionBuilder.hasOptionalArgs1(2).create1("i"))
        self.__opts.addOption0(OptionBuilder.hasOptionalArgs0().create1("j"))
        args = ["-a", "-b", "foo", "--c", "--d", "bar"]
        parser = PosixParser()
        self.__cl = parser.parse0(self.__opts, args)

    # Class Methods End
