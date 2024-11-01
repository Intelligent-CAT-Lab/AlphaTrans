import pytest

from src.main.org.apache.commons.cli.PosixParser import *
from src.main.org.apache.commons.cli.Parser import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.CommandLine import *
import unittest


class ValueTest(unittest.TestCase):

    __cl = None
    __opts = Options()
    

    def setUp(self) -> None:
        try:
            self.__opts.addOption1("a", False, "toggle -a")
            self.__opts.addOption1("b", True, "set -b")
            self.__opts.addOption3("c", "c", False, "toggle -c")
            self.__opts.addOption3("d", "d", True, "set -d")

            self.__opts.addOption0(OptionBuilder.hasOptionalArg().create1('e'))
            self.__opts.addOption0(
                OptionBuilder.hasOptionalArg().withLongOpt("fish").create0()
            )
            self.__opts.addOption0(
                OptionBuilder.hasOptionalArgs0().withLongOpt("gravy").create0()
            )
            self.__opts.addOption0(
                OptionBuilder.hasOptionalArgs1(2).withLongOpt("hide").create0()
            )
            self.__opts.addOption0(OptionBuilder.hasOptionalArgs1(2).create1('i'))
            self.__opts.addOption0(OptionBuilder.hasOptionalArgs0().create1('j'))

            args = ["-a", "-b", "foo", "--c", "--d", "bar"]

            parser = PosixParser()
            self.__cl = parser.parse0(self.__opts, args)
        except Exception as e:
            self.fail(f"An exception occurred when setting up the test: {e}")
    
    
    @pytest.mark.test
    def testLongNoArg(self) -> None:
        self.assertTrue(self.__cl.hasOption2("c"))
        self.assertIsNone(self.__cl.getOptionValue4("c"))

    
    @pytest.mark.test
    def testLongNoArgWithOption(self) -> None:
        self.assertTrue(self.__cl.hasOption1(self.__opts.getOption("c")))
        self.assertIsNone(self.__cl.getOptionValue2(self.__opts.getOption("c")))
    
    
    @pytest.mark.test
    def testLongOptionalArgValue(self) -> None:
        try:
            args = ["--fish", "face"]

            parser = PosixParser()
            cmd = parser.parse0(self.__opts, args)
            self.assertTrue(cmd.hasOption2("fish"))
            self.assertEqual("face", cmd.getOptionValue4("fish"))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testLongOptionalArgValues(self) -> None:
        try:
            args = ["--gravy", "gold", "garden"]

            parser = PosixParser()
            cmd = parser.parse0(self.__opts, args)
            self.assertTrue(cmd.hasOption2("gravy"))
            self.assertEqual("gold", cmd.getOptionValue4("gravy"))
            self.assertEqual("gold", cmd.getOptionValues2("gravy")[0])
            self.assertEqual("garden", cmd.getOptionValues2("gravy")[1])
            self.assertEqual(len(cmd.getArgs()), 0)
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testLongOptionalArgValuesWithOption(self) -> None:
        try:
            args = ["--gravy", "gold", "garden"]

            parser = PosixParser()
            cmd = parser.parse0(self.__opts, args)
            self.assertTrue(cmd.hasOption1(self.__opts.getOption("gravy")))
            self.assertEqual("gold", cmd.getOptionValue2(self.__opts.getOption("gravy")))
            self.assertEqual("gold", cmd.getOptionValues1(self.__opts.getOption("gravy"))[0])
            self.assertEqual("garden", cmd.getOptionValues1(self.__opts.getOption("gravy"))[1])
            self.assertEqual(len(cmd.getArgs()), 0)
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testLongOptionalArgValueWithOption(self) -> None:
        try:
            args = ["--fish", "face"]

            parser = PosixParser()
            cmd = parser.parse0(self.__opts, args)
            self.assertTrue(cmd.hasOption1(self.__opts.getOption("fish")))
            self.assertEqual("face", cmd.getOptionValue2(self.__opts.getOption("fish")))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    @pytest.mark.test
    def testLongOptionalNArgValues(self) -> None:
        try:
            args = ["--hide", "house", "hair", "head"]

            parser = PosixParser()

            cmd = parser.parse0(self.__opts, args)
            self.assertTrue(cmd.hasOption2("hide"))
            self.assertEqual("house", cmd.getOptionValue4("hide"))
            self.assertEqual("house", cmd.getOptionValues2("hide")[0])
            self.assertEqual("hair", cmd.getOptionValues2("hide")[1])
            self.assertEqual(len(cmd.getArgs()), 1)
            self.assertEqual("head", cmd.getArgs()[0])
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testLongOptionalNArgValuesWithOption(self) -> None:
        try:
            args = ["--hide", "house", "hair", "head"]

            parser = PosixParser()

            cmd = parser.parse0(self.__opts, args)

            self.assertTrue(cmd.hasOption1(self.__opts.getOption("hide")))
            self.assertEqual("house", cmd.getOptionValue2(self.__opts.getOption("hide")))
            self.assertEqual("house", cmd.getOptionValues1(self.__opts.getOption("hide"))[0])
            self.assertEqual("hair", cmd.getOptionValues1(self.__opts.getOption("hide"))[1])
            self.assertEqual(len(cmd.getArgs()), 1)
            self.assertEqual("head", cmd.getArgs()[0])
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testLongOptionalNoValue(self) -> None:
        try:
            args = ["--fish"]

            parser = PosixParser()
            cmd = parser.parse0(self.__opts, args)
            self.assertTrue(cmd.hasOption2("fish"))
            self.assertIsNone(cmd.getOptionValue4("fish"))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testLongOptionalNoValueWithOption(self) -> None:
        try:
            args = ["--fish"]

            parser = PosixParser()
            cmd = parser.parse0(self.__opts, args)
            self.assertTrue(cmd.hasOption1(self.__opts.getOption("fish")))
            self.assertIsNone(cmd.getOptionValue2(self.__opts.getOption("fish")))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    

    @pytest.mark.test
    def testLongWithArg(self) -> None:
        self.assertTrue(self.__cl.hasOption2("d"))
        self.assertIsNotNone(self.__cl.getOptionValue4("d"))
        self.assertEqual(self.__cl.getOptionValue4("d"), "bar")

    
    @pytest.mark.test
    def testLongWithArgWithOption(self) -> None:
        self.assertTrue(self.__cl.hasOption1(self.__opts.getOption("d")))
        self.assertIsNotNone(self.__cl.getOptionValue2(self.__opts.getOption("d")))
        self.assertEqual(self.__cl.getOptionValue2(self.__opts.getOption("d")), "bar")

    
    @pytest.mark.test
    def testShortNoArg(self) -> None:
        self.assertTrue(self.__cl.hasOption2("a"))
        self.assertIsNone(self.__cl.getOptionValue4("a"))

    
    @pytest.mark.test
    def testShortNoArgWithOption(self) -> None:
        self.assertTrue(self.__cl.hasOption1(self.__opts.getOption("a")))
        self.assertIsNone(self.__cl.getOptionValue2(self.__opts.getOption("a")))

    
    @pytest.mark.test
    def testShortOptionalArgNoValue(self) -> None:
        try:
            args = ["-e"]

            parser = PosixParser()
            cmd = parser.parse0(self.__opts, args)
            self.assertTrue(cmd.hasOption2("e"))
            self.assertIsNone(cmd.getOptionValue4("e"))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testShortOptionalArgNoValueWithOption(self) -> None:
        try:
            args = ["-e"]

            parser = PosixParser()
            cmd = parser.parse0(self.__opts, args)
            self.assertTrue(cmd.hasOption1(self.__opts.getOption("e")))
            self.assertIsNone(cmd.getOptionValue2(self.__opts.getOption("e")))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testShortOptionalArgValue(self) -> None:
        try:
            args = ["-e", "everything"]

            parser = PosixParser()
            cmd = parser.parse0(self.__opts, args)
            self.assertTrue(cmd.hasOption2("e"))
            self.assertEqual("everything", cmd.getOptionValue4("e"))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testShortOptionalArgValues(self) -> None:
        try:
            args = ["-j", "ink", "idea"]

            parser = PosixParser()
            cmd = parser.parse0(self.__opts, args)
            self.assertTrue(cmd.hasOption2("j"))
            self.assertEqual("ink", cmd.getOptionValue4("j"))
            self.assertEqual("ink", cmd.getOptionValues2("j")[0])
            self.assertEqual("idea", cmd.getOptionValues2("j")[1])
            self.assertEqual(len(cmd.getArgs()), 0)
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    

    @pytest.mark.test
    def testShortOptionalArgValuesWithOption(self) -> None:
        try:
            args = ["-j", "ink", "idea"]

            parser = PosixParser()
            cmd = parser.parse0(self.__opts, args)
            self.assertTrue(cmd.hasOption1(self.__opts.getOption("j")))
            self.assertEqual("ink", cmd.getOptionValue2(self.__opts.getOption("j")))
            self.assertEqual("ink", cmd.getOptionValues1(self.__opts.getOption("j"))[0])
            self.assertEqual("idea", cmd.getOptionValues1(self.__opts.getOption("j"))[1])
            self.assertEqual(len(cmd.getArgs()), 0)
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testShortOptionalArgValueWithOption(self) -> None:
        try:
            args = ["-e", "everything"]

            parser = PosixParser()
            cmd = parser.parse0(self.__opts, args)
            self.assertTrue(cmd.hasOption1(self.__opts.getOption("e")))
            self.assertEqual("everything", cmd.getOptionValue2(self.__opts.getOption("e")))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testShortOptionalNArgValues(self) -> None:
        try:
            args = ["-i", "ink", "idea", "isotope", "ice"]

            parser = PosixParser()
            cmd = parser.parse0(self.__opts, args)
            self.assertTrue(cmd.hasOption2("i"))
            self.assertEqual("ink", cmd.getOptionValue4("i"))
            self.assertEqual("ink", cmd.getOptionValues2("i")[0])
            self.assertEqual("idea", cmd.getOptionValues2("i")[1])
            self.assertEqual(len(cmd.getArgs()), 2)
            self.assertEqual("isotope", cmd.getArgs()[0])
            self.assertEqual("ice", cmd.getArgs()[1])
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    

    @pytest.mark.test
    def testShortOptionalNArgValuesWithOption(self) -> None:
        try:
            args = ["-i", "ink", "idea", "isotope", "ice"]

            parser = PosixParser()
            cmd = parser.parse0(self.__opts, args)
            self.assertTrue(cmd.hasOption2("i"))
            self.assertEqual("ink", cmd.getOptionValue2(self.__opts.getOption("i")))
            self.assertEqual("ink", cmd.getOptionValues1(self.__opts.getOption("i"))[0])
            self.assertEqual("idea", cmd.getOptionValues1(self.__opts.getOption("i"))[1])
            self.assertEqual(len(cmd.getArgs()), 2)
            self.assertEqual("isotope", cmd.getArgs()[0])
            self.assertEqual("ice", cmd.getArgs()[1])
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testShortWithArg(self) -> None:
        self.assertTrue(self.__cl.hasOption2("b"))
        self.assertIsNotNone(self.__cl.getOptionValue4("b"))
        self.assertEqual(self.__cl.getOptionValue4("b"), "foo")

    
    @pytest.mark.test
    def testShortWithArgWithOption(self) -> None:
        self.assertTrue(self.__cl.hasOption1(self.__opts.getOption("b")))
        self.assertIsNotNone(self.__cl.getOptionValue2(self.__opts.getOption("b")))
        self.assertEqual(self.__cl.getOptionValue2(self.__opts.getOption("b")), "foo")
