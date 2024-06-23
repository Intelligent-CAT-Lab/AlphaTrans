from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.CommandLine import *

# from src.main.org.apache.commons.cli.CommandLine_ESTest_scaffolding import *
from src.main.org.apache.commons.cli.Option import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class CommandLine_ESTest(unittest.TestCase):

    @pytest.mark.test
    def test79(self) -> None:
        commandLine_Builder0 = Builder()
        commandLine0 = commandLine_Builder0.build()
        boolean0 = commandLine0.hasOption0("b")
        self.assertFalse(boolean0)

    @pytest.mark.test
    def test78(self) -> None:
        commandLine_Builder0 = Builder()
        commandLine0 = commandLine_Builder0.build()
        iterator0 = commandLine0.iterator()
        self.assertIsNotNone(iterator0)

    @pytest.mark.test
    def test77(self) -> None:
        commandLine_Builder0 = Builder()
        commandLine0 = commandLine_Builder0.build()
        list0 = commandLine0.getArgList()
        self.assertEqual(0, len(list0))

    @pytest.mark.test
    def test76(self) -> None:

        commandLine_Builder0 = Builder()
        commandLine0 = commandLine_Builder0.build()
        string0 = commandLine0.getOptionValue1("8", "qL)(d`NKR1ME/ttD+")
        self.assertEqual(string0, "qL)(d`NKR1ME/ttD+")
        self.assertIsNotNone(string0)

    @pytest.mark.test
    def test75(self) -> None:
        commandLine_Builder0 = Builder()
        commandLine0 = commandLine_Builder0.build()
        object0 = commandLine0.getParsedOptionValue0(">")
        self.assertIsNone(object0)

    @pytest.mark.test
    def test74(self) -> None:
        commandLine_Builder0 = Builder()
        commandLine0 = commandLine_Builder0.build()
        string0 = commandLine0.getOptionValue0("v")
        self.assertIsNone(string0)

    @pytest.mark.test
    def test73(self) -> None:
        commandLine_Builder0 = Builder()
        commandLine0 = commandLine_Builder0.build()
        optionArray0 = commandLine0.getOptions()
        self.assertEqual(0, len(optionArray0))

    @pytest.mark.test
    def test72(self) -> None:

        commandLine_Builder0 = Builder()
        option_Builder0 = Option.builder1("d")
        option0 = Option(
            1939,
            "Either opt or loqgOpt must be specified",
            "Either opt or loqgOpt must be specified",
            "d",
            True,
            option_Builder0,
        )
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()
        properties0 = commandLine0.getOptionProperties1("DA<@02#DAtWDE")
        self.assertIsNotNone(properties0)

    @pytest.mark.test
    def test71(self) -> None:
        commandLine_Builder0 = Builder()
        commandLine0 = commandLine_Builder0.build()
        stringArray0 = commandLine0.getArgs()
        self.assertEqual(0, len(stringArray0))

    @pytest.mark.test
    def test70(self) -> None:

        commandLine_Builder0 = Builder()
        commandLine0 = commandLine_Builder0.build()
        object0 = commandLine0.getOptionObject0("v")
        self.assertIsNone(object0)

    @pytest.mark.test
    def test69(self) -> None:

        commandLine_Builder0 = Builder()
        option0 = Option.Option2("", False, "")
        commandLine_Builder1 = commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder1.build()
        properties0 = commandLine0.getOptionProperties0(None)
        self.assertIsNotNone(properties0)

    @pytest.mark.test
    def test68(self) -> None:

        commandLine_Builder0 = Builder(
            0,
            "true",
            "true",
            "org.apache.commons.cli.Option$Builder",
            True,
            Builder.builder1("true"),
        )
        option_Builder0 = Builder.builder1("true")
        option_Builder1 = option_Builder0.numberOfArgs(1873)
        option0 = Option(
            0,
            "true",
            "true",
            "org.apache.commons.cli.Option$Builder",
            True,
            option_Builder1,
        )
        option0.addValueForProcessing("true")
        option0.addValueForProcessing("true")
        commandLine_Builder1 = commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder1.build()
        properties0 = commandLine0.getOptionProperties0(option0)
        assert properties0 is not None

    @pytest.mark.test
    def test67(self) -> None:

        commandLine_Builder0 = Builder()
        option0 = Option.Option2("", True, "")
        option0.addValueForProcessing("")
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()
        properties0 = commandLine0.getOptionProperties0(option0)
        self.assertIsNotNone(properties0)

    @pytest.mark.test
    def test66(self) -> None:

        option0 = Option.Option1("D", "D")
        option0.setLongOpt('zP6"$-')
        commandLine_Builder0 = Builder()
        commandLine_Builder1 = commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder1.build()
        properties0 = commandLine0.getOptionProperties1('zP6"$-')
        self.assertIsNotNone(properties0)

    @pytest.mark.test
    def test65(self) -> None:

        pass  # LLM could not translate this method

    @pytest.mark.test
    def test64(self) -> None:

        commandLine_Builder0 = Builder(
            0,
            "true",
            "true",
            ":@[[znsXqJUs/HfS",
            True,
            Builder.builder1("true").numberOfArgs(1879),
        )
        option0 = Option(
            0,
            "true",
            "true",
            ":@[[znsXqJUs/HfS",
            True,
            Builder.builder1("true").numberOfArgs(1879),
        )
        option0.addValueForProcessing("true")
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()
        properties0 = commandLine0.getOptionProperties1("true")
        self.assertIsNotNone(properties0)

    @pytest.mark.test
    def test63(self) -> None:

        commandLine_Builder0 = Builder()
        option_Builder0 = Option.builder1("truje")
        option0 = Option(
            1873,
            "truje",
            "truje",
            "org.apache.commons.cli.Option$Builder",
            False,
            option_Builder0,
        )
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()
        object0 = commandLine0.getParsedOptionValue2("truje")
        self.assertIsNone(object0)

    @pytest.mark.test
    def test62(self) -> None:

        pass  # LLM could not translate this method

    @pytest.mark.test
    def test61(self) -> None:

        commandLine_Builder0 = Builder()
        option0 = Option.Option2("", True, "")
        option0.addValueForProcessing("")
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()
        string0 = commandLine0.getOptionValue5("", "")
        self.assertEqual("", string0)

    @pytest.mark.test
    def test60(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder1("")
        option0 = option_Builder0.build()
        commandLine_Builder1 = commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder1.build()
        stringArray0 = commandLine0.getOptionValues0("l")
        self.assertIsNone(stringArray0)

    @pytest.mark.test
    def test59(self) -> None:

        commandLine_Builder0 = Builder()
        option_Builder0 = Option.builder1("truje")
        option0 = Option(
            1873,
            "truje",
            "truje",
            "org.apache.commons.cli.Option$Builder",
            False,
            option_Builder0,
        )
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()
        boolean0 = commandLine0.hasOption2("truje")
        self.assertTrue(boolean0)

    @pytest.mark.test
    def test58(self) -> None:

        option0 = Option.Option1("D", "D")
        option0.setLongOpt("fF")
        commandLine_Builder0 = Builder()
        commandLine_Builder1 = commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder1.build()
        object0 = commandLine0.getOptionObject1("fF")
        self.assertIsNone(object0)

    @pytest.mark.test
    def test57(self) -> None:

        commandLine_Builder0 = Builder()
        commandLine0 = commandLine_Builder0.build()
        string0 = commandLine0.getOptionValue4("")
        self.assertIsNone(string0)

    @pytest.mark.test
    def test56(self) -> None:
        commandLine_Builder0 = Builder()
        commandLine0 = commandLine_Builder0.build()
        stringArray0 = commandLine0.getOptionValues2("0smVT a^e")
        self.assertIsNone(stringArray0)

    @pytest.mark.test
    def test55(self) -> None:
        commandLine_Builder0 = Builder()
        commandLine0 = commandLine_Builder0.build()
        string0 = commandLine0.getOptionValue2(None)
        self.assertIsNone(string0)

    @pytest.mark.test
    def test54(self) -> None:

        commandLine_Builder0 = Builder(
            0,
            "true",
            "true",
            "org.apache.commons.cli.Option$Builder",
            True,
            Builder.builder1("true").numberOfArgs(1873),
        )
        option0 = Option(
            0,
            "true",
            "true",
            "org.apache.commons.cli.Option$Builder",
            True,
            commandLine_Builder0.numberOfArgs(1873),
        )
        option0.addValueForProcessing("true")
        commandLine_Builder1 = commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder1.build()
        string0 = commandLine0.getOptionValue2(option0)
        self.assertEqual("true", string0)

    @pytest.mark.test
    def test53(self) -> None:

        commandLine_Builder0 = Builder()
        option0 = Option.Option2("", True, "")
        option0.addValueForProcessing("")
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()
        string0 = commandLine0.getOptionValue3(option0, "")
        self.assertEqual("", string0)

    @pytest.mark.test
    def test52(self) -> None:
        commandLine0 = CommandLine()
        commandLine0._addOption(None)
        try:
            commandLine0.getOptionValues1(None)
            self.fail("Expecting exception: NullPointerException")
        except Exception as e:
            self.verifyException("org.apache.commons.cli.CommandLine", e)

    @pytest.mark.test
    def test51(self) -> None:

        commandLine_Builder0 = Builder()
        commandLine0 = commandLine_Builder0.build()
        option_Builder0 = Option.builder1("")
        option0 = Option(-1800, "", "w 1I?", None, True, option_Builder0)
        commandLine_Builder0.addOption(option0)
        option_Builder1 = Option.builder0()
        option1 = Option(
            -672,
            "org.apache.commons.cli.CommandLine$Builder",
            "",
            "",
            False,
            option_Builder1,
        )
        stringArray0 = commandLine0.getOptionValues1(option1)
        self.assertIsNone(stringArray0)

    @pytest.mark.test
    def test50(self) -> None:

        commandLine_Builder0 = Builder(
            0,
            "true",
            "true",
            "org.apache.commons.cli.Option$Builder",
            True,
            Builder.builder1("true").numberOfArgs(1873),
        )
        option0 = Option(
            0,
            "true",
            "true",
            "org.apache.commons.cli.Option$Builder",
            True,
            commandLine_Builder0.numberOfArgs(1873),
        )
        option0.addValueForProcessing("true")
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()
        stringArray0 = commandLine0.getOptionValues1(option0)
        self.assertEqual(1, len(stringArray0))

    @pytest.mark.test
    def test49(self) -> None:
        commandLine_Builder0 = Builder()
        commandLine0 = commandLine_Builder0.build()
        object0 = commandLine0.getParsedOptionValue1(None)
        self.assertIsNone(object0)

    @pytest.mark.test
    def test48(self) -> None:

        option0 = Option.Option1("", "")
        commandLine0 = CommandLine()
        object0 = commandLine0.getParsedOptionValue1(option0)
        self.assertIsNone(object0)

    @pytest.mark.test
    def test47(self) -> None:

        commandLine_Builder0 = Builder(
            0,
            "true",
            "true",
            "org.apache.commons.cli.Option$Builder",
            True,
            Builder.builder1("true").numberOfArgs(1873),
        )
        option0 = Option(
            0,
            "true",
            "true",
            "org.apache.commons.cli.Option$Builder",
            True,
            Builder.builder1("true").numberOfArgs(1873),
        )
        option0.addValueForProcessing("true")
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()
        object0 = commandLine0.getParsedOptionValue1(option0)
        self.assertEqual("true", object0)

    @pytest.mark.test
    def test46(self) -> None:
        commandLine0 = CommandLine()
        boolean0 = commandLine0.hasOption1(None)
        self.assertFalse(boolean0)

    @pytest.mark.test
    def test45(self) -> None:
        commandLine0 = CommandLine()
        commandLine0._addOption(None)
        boolean0 = commandLine0.hasOption1(None)
        self.assertTrue(boolean0)

    @pytest.mark.test
    def test44(self) -> None:

        commandLine_Builder0 = Builder()
        commandLine_Builder0.addOption(None)
        commandLine0 = commandLine_Builder0.build()

        with self.assertRaises(NullPointerException):
            commandLine0.getOptionObject0("a")

    @pytest.mark.test
    def test43(self) -> None:

        commandLine_Builder0 = Builder()
        commandLine_Builder1 = commandLine_Builder0.addOption(None)
        commandLine0 = commandLine_Builder1.build()

        try:
            commandLine0.getOptionObject1("C")
            self.fail("Expecting exception: NullPointerException")

        except NullPointerException as e:
            self.verifyException("org.apache.commons.cli.CommandLine", e)

    @pytest.mark.test
    def test42(self) -> None:

        commandLine_Builder0 = Builder()
        commandLine_Builder1 = commandLine_Builder0.addOption(None)
        commandLine0 = commandLine_Builder1.build()

        try:
            commandLine0.getOptionProperties0(None)
            self.fail("Expecting exception: NullPointerException")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.CommandLine", e)

    @pytest.mark.test
    def test41(self) -> None:

        option0 = Option.Option1(None, None)
        commandLine_Builder0 = Builder()
        commandLine_Builder1 = commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder1.build()

        try:
            commandLine0.getOptionProperties1(None)
            self.fail("Expecting exception: NullPointerException")

        except Exception as e:
            self.assertEqual(str(e), "Expecting exception: NullPointerException")

    @pytest.mark.test
    def test40(self) -> None:

        commandLine_Builder0 = Builder()
        commandLine_Builder1 = commandLine_Builder0.addOption(None)
        commandLine0 = commandLine_Builder1.build()

        try:
            commandLine0.getOptionValue0("a")
            self.fail("Expecting exception: NullPointerException")

        except NullPointerException as e:
            self.verifyException("org.apache.commons.cli.CommandLine", e)

    @pytest.mark.test
    def test39(self) -> None:

        commandLine_Builder0 = Builder()
        commandLine_Builder1 = commandLine_Builder0.addOption(None)
        commandLine0 = commandLine_Builder1.build()

        try:
            commandLine0.getOptionValue1("8", "qL)(d`NKR1ME/ttD+")
            self.fail("Expecting exception: NullPointerException")

        except NullPointerException as e:
            verifyException("org.apache.commons.cli.CommandLine", e)

    @pytest.mark.test
    def test38(self) -> None:

        commandLine_Builder0 = Builder()
        commandLine_Builder0.addOption(None)
        option0 = Option.Option2("", True, "")
        commandLine0 = commandLine_Builder0.build()

        with pytest.raises(NullPointerException):
            commandLine0.getOptionValue2(option0)

    @pytest.mark.test
    def test37(self) -> None:

        option0 = Option.Option2(None, False, None)
        commandLine_Builder0 = Builder()
        commandLine_Builder0.addOption(None)
        commandLine0 = commandLine_Builder0.build()

        try:
            commandLine0.getOptionValue3(option0, None)
            self.fail("Expecting exception: NullPointerException")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.CommandLine", e)

    @pytest.mark.test
    def test36(self) -> None:

        commandLine_Builder0 = Builder()
        commandLine_Builder1 = commandLine_Builder0.addOption(None)
        commandLine0 = commandLine_Builder1.build()

        try:
            commandLine0.getOptionValue4("C")
            self.fail("Expecting exception: NullPointerException")

        except NullPointerException as e:
            self.verifyException("org.apache.commons.cli.CommandLine", e)

    @pytest.mark.test
    def test35(self) -> None:

        commandLine_Builder0 = Builder()
        commandLine_Builder1 = commandLine_Builder0.addOption(None)
        commandLine0 = commandLine_Builder1.build()

        try:
            commandLine0.getOptionValue5("O", "O")
            self.fail("Expecting exception: NullPointerException")

        except NullPointerException as e:
            self.verifyException("org.apache.commons.cli.CommandLine", e)

    @pytest.mark.test
    def test34(self) -> None:

        commandLine_Builder0 = Builder()
        commandLine_Builder1 = commandLine_Builder0.addOption(None)
        commandLine0 = commandLine_Builder1.build()

        try:
            commandLine0.getOptionValues0("/")
            self.fail("Expecting exception: NullPointerException")

        except NullPointerException as e:
            verifyException("org.apache.commons.cli.CommandLine", e)

    @pytest.mark.test
    def test33(self) -> None:

        commandLine_Builder0 = Builder()
        commandLine_Builder1 = commandLine_Builder0.addOption(None)
        commandLine0 = commandLine_Builder1.build()

        try:
            commandLine0.getOptionValues2("0smVT a^e")
            self.fail("Expecting exception: NullPointerException")

        except NullPointerException as e:
            verifyException("org.apache.commons.cli.CommandLine", e)

    @pytest.mark.test
    def test32(self) -> None:

        commandLine0 = CommandLine()
        commandLine0._addOption(None)

        try:
            commandLine0.getParsedOptionValue0("<")
            self.fail("Expecting exception: NullPointerException")

        except Exception as e:
            self.assertEqual(str(type(e)), "<class 'NullPointerException'>")

    @pytest.mark.test
    def test31(self) -> None:

        commandLine_Builder0 = Builder()
        option0 = Option.Option2("", True, "")
        option0.addValueForProcessing("")
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()
        class0 = Option
        option0.setType0(class0)
        try:
            commandLine0.getParsedOptionValue0("-")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.TypeHandler", e)

    @pytest.mark.test
    def test30(self) -> None:

        commandLine_Builder0 = Builder()
        commandLine_Builder0.addOption(None)
        option0 = Option.Option2("", True, "")
        commandLine0 = commandLine_Builder0.build()

        try:
            commandLine0.getParsedOptionValue1(option0)
            self.fail("Expecting exception: NullPointerException")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.CommandLine", e)

    @pytest.mark.test
    def test29(self) -> None:

        commandLine_Builder0 = Builder("true")
        option_Builder0 = Option.builder1("true")
        class0 = Option
        option_Builder0.type(class0)
        option_Builder1 = option_Builder0.numberOfArgs(1873)
        option0 = Builder(
            0,
            "true",
            "true",
            "org.apache.commons.cli.Option$Builder",
            True,
            option_Builder1,
        )
        option0.addValueForProcessing("true")
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()
        try:
            commandLine0.getParsedOptionValue1(option0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.TypeHandler", e)

    @pytest.mark.test
    def test28(self) -> None:

        commandLine_Builder0 = Builder()
        option0 = Option.Option1("truve", "truve")
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()

        with pytest.raises(NullPointerException):
            commandLine0.getParsedOptionValue2(None)

    @pytest.mark.test
    def test27(self) -> None:

        commandLine_Builder0 = Builder("truje")
        option_Builder0 = Option.builder1("truje")
        option_Builder1 = option_Builder0.numberOfArgs(1873)
        option0 = Option(
            1873,
            "truje",
            "truje",
            "org.apache.commons.cli.Option$Builder",
            False,
            option_Builder1,
        )
        option0.addValueForProcessing("truje")
        class0 = Option
        option0.setType0(class0)
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()
        try:
            commandLine0.getParsedOptionValue2("truje")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.TypeHandler", e)

    @pytest.mark.test
    def test26(self) -> None:
        commandLine_Builder0 = Builder()
        commandLine_Builder1 = commandLine_Builder0.addOption(None)
        commandLine0 = commandLine_Builder1.build()
        try:
            commandLine0.hasOption0("j")
            self.fail("Expecting exception: NullPointerException")
        except NullPointerException as e:
            self.verifyException("org.apache.commons.cli.CommandLine", e)

    @pytest.mark.test
    def test25(self) -> None:
        commandLine0 = CommandLine()
        commandLine0._addOption(None)
        try:
            commandLine0.hasOption2("org.apache.commons.cli.CommandLine$Builder")
            self.fail("Expecting exception: NullPointerException")
        except Exception as e:
            self.verifyException("org.apache.commons.cli.CommandLine", e)

    @pytest.mark.test
    def test24(self) -> None:
        commandLine_Builder0 = Builder()
        commandLine0 = commandLine_Builder0.build()
        commandLine_Builder0.addArg("The option '")
        list0 = commandLine0.getArgList()
        self.assertTrue("The option '" in list0)

    @pytest.mark.test
    def test23(self) -> None:
        commandLine0 = CommandLine()
        commandLine0._addArg("true")
        stringArray0 = commandLine0.getArgs()
        self.assertEqual(1, len(stringArray0))

    @pytest.mark.test
    def test22(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder1("d")
        option_Builder0.numberOfArgs(1939)
        option0 = Option(
            1939,
            "Either opt or loqgOpt must be specified",
            "Either opt or loqgOpt must be specified",
            "d",
            True,
            option_Builder0,
        )
        option0.addValueForProcessing("d")
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()
        object0 = commandLine0.getOptionObject0("d")
        self.assertEqual("d", object0)

    @pytest.mark.test
    def test21(self) -> None:

        commandLine_Builder0 = Builder()
        option0 = Option.Option2("", True, "")
        option0.addValueForProcessing("")
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()
        object0 = commandLine0.getOptionObject1("")
        self.assertEqual("", object0)

    @pytest.mark.test
    def test20(self) -> None:

        commandLine_Builder0 = Builder(
            0,
            "",
            "",
            "ocg.apache.commons.cli.Option$Buil der",
            True,
            Builder.builder1(""),
        )
        option_Builder0 = commandLine_Builder0.numberOfArgs(1888)
        option0 = Option(
            0, "", "", "ocg.apache.commons.cli.Option$Buil der", True, option_Builder0
        )
        option0.addValueForProcessing("")
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()
        string0 = commandLine0.getOptionValue0("-")
        self.assertEqual("", string0)

    @pytest.mark.test
    def test19(self) -> None:

        commandLine0 = CommandLine()
        string0 = commandLine0.getOptionValue1("7", "")
        assert string0 is not None
        assert string0 == ""

    @pytest.mark.test
    def test18(self) -> None:
        commandLine0 = CommandLine()
        string0 = commandLine0.getOptionValue1("{", None)
        self.assertIsNone(string0)

    @pytest.mark.test
    def test17(self) -> None:

        commandLine_Builder0 = Builder(
            0,
            "true",
            "true",
            "org.apache.commons.cli.Option$Builder",
            True,
            Builder.builder1("true").numberOfArgs(1873),
        )
        option0 = Option(
            0,
            "true",
            "true",
            "org.apache.commons.cli.Option$Builder",
            True,
            commandLine_Builder0.numberOfArgs(1873),
        )
        option0.addValueForProcessing("")
        commandLine_Builder1 = commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder1.build()
        string0 = commandLine0.getOptionValue2(option0)
        self.assertEqual("", string0)

    @pytest.mark.test
    def test16(self) -> None:

        commandLine0 = CommandLine()
        option_Builder0 = Option.builder1("true")
        option0 = Option(
            1873, "true", "SKE;Fw|7qNIb[}A", ":@[[znsXqJUs/HfS", True, option_Builder0
        )
        string0 = commandLine0.getOptionValue3(option0, "{")
        self.assertEqual("{", string0)

    @pytest.mark.test
    def test15(self) -> None:

        commandLine0 = CommandLine()
        option0 = Option.Option1(None, None)
        string0 = commandLine0.getOptionValue3(option0, None)
        self.assertIsNone(string0)

    @pytest.mark.test
    def test14(self) -> None:

        commandLine_Builder0 = Builder(
            0,
            "",
            "",
            "ocg.apache.commons.cli.Option$Buil der",
            True,
            Builder.builder1(""),
        )
        option_Builder0 = commandLine_Builder0.numberOfArgs(1885)
        option0 = Option(
            0, "", "", "ocg.apache.commons.cli.Option$Buil der", True, option_Builder0
        )
        option0.addValueForProcessing("")
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()
        string0 = commandLine0.getOptionValue4("")
        self.assertEqual("", string0)

    @pytest.mark.test
    def test13(self) -> None:

        commandLine_Builder0 = Builder()
        option_Builder0 = Option.builder1("")
        option_Builder0.numberOfArgs(1873)
        option0 = Option(1, "e,", "", "7", True, option_Builder0)
        option0.addValueForProcessing("-")
        commandLine_Builder1 = commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder1.build()
        string0 = commandLine0.getOptionValue4("")
        self.assertEqual("-", string0)

    @pytest.mark.test
    def test12(self) -> None:

        commandLine0 = CommandLine()
        string0 = commandLine0.getOptionValue5(
            "Either opt or longOpt must be specified",
            "A CloneNotSupportedException was thrown: ",
        )
        self.assertEqual(string0, "A CloneNotSupportedException was thrown: ")
        self.assertIsNotNone(string0)

    @pytest.mark.test
    def test11(self) -> None:
        commandLine0 = CommandLine()
        string0 = commandLine0.getOptionValue5(None, None)
        self.assertIsNone(string0)

    @pytest.mark.test
    def test10(self) -> None:

        commandLine_Builder0 = Builder()
        option0 = Option.Option2("", True, "")
        option0.addValueForProcessing("")
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()
        stringArray0 = commandLine0.getOptionValues0("-")
        self.assertEqual(len(stringArray0), 1)

    @pytest.mark.test
    def test09(self) -> None:

        commandLine_Builder0 = Builder(
            0, "true", "true", ":@[[znsXqJUs/HfS", True, Builder.builder1("true")
        )
        option0 = Option(
            2874, "true", "true", ":@[[znsXqJUs/HfS", False, commandLine_Builder0
        )
        option0.addValueForProcessing("true")
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()
        stringArray0 = commandLine0.getOptionValues2("true")
        self.assertEqual(len(stringArray0), 1)

    @pytest.mark.test
    def test08(self) -> None:

        commandLine_Builder0 = Builder("")
        option_Builder0 = Option.builder1("")
        option0 = option_Builder0.build()
        commandLine_Builder1 = commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder1.build()
        optionArray0 = commandLine0.getOptions()
        self.assertEqual(len(optionArray0), 1)

    @pytest.mark.test
    def test07(self) -> None:

        commandLine_Builder0 = Builder()
        option0 = Option.Option2("", True, "")
        option0.addValueForProcessing("")
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()
        object0 = commandLine0.getParsedOptionValue0("-")
        self.assertEqual("", object0)

    @pytest.mark.test
    def test06(self) -> None:

        commandLine0 = CommandLine()
        option_Builder0 = Option.builder1("i")
        option0 = Option(-852, None, None, None, False, option_Builder0)
        commandLine0.addOption(option0)
        boolean0 = commandLine0.hasOption0("i")
        self.assertTrue(boolean0)

    @pytest.mark.test
    def test05(self) -> None:
        commandLine0 = CommandLine()
        boolean0 = commandLine0.hasOption2("?ZglCu3VLViVg")
        self.assertFalse(boolean0)

    @pytest.mark.test
    def test04(self) -> None:

        commandLine_Builder0 = Builder(
            0,
            "true",
            "true",
            "true",
            False,
            Builder(0, "true", "true", "true", False, None),
        )
        option_Builder0 = Option.builder1("true")
        option_Builder1 = option_Builder0.hasArgs()
        option0 = Option(2874, "true", "true", "true", False, option_Builder1)
        option0.addValueForProcessing("true")
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()
        object0 = commandLine0.getOptionObject1("true")
        self.assertIsNone(object0)

    @pytest.mark.test
    def test03(self) -> None:

        option_Builder0 = Option.builder0()
        option0 = Option(2065, "[ option: ", "7/[:_", "-", False, option_Builder0)
        commandLine_Builder0 = Builder()
        option1 = Option(-1, "-", "", "", False, option_Builder0)
        commandLine_Builder1 = commandLine_Builder0.addOption(option1)
        commandLine0 = commandLine_Builder1.build()
        properties0 = commandLine0.getOptionProperties0(option0)
        self.assertIsNotNone(properties0)

    @pytest.mark.test
    def test02(self) -> None:

        commandLine_Builder0 = Builder(
            0,
            "true",
            "true",
            "org.apache.commons.cli.Option$Builder",
            True,
            Builder.builder1("true").numberOfArgs(1873),
        )
        option0 = Option(
            0,
            "true",
            "true",
            "org.apache.commons.cli.Option$Builder",
            True,
            Builder.builder1("true").numberOfArgs(1873),
        )
        option0.addValueForProcessing("true")
        option0.addValueForProcessing("true")
        option0.addValueForProcessing("org.apache.commons.cli.Option$Builder")
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()
        properties0 = commandLine0.getOptionProperties0(option0)
        self.assertIsNotNone(properties0)

    @pytest.mark.test
    def test01(self) -> None:

        commandLine_Builder0 = Builder("")
        option_Builder0 = Option.builder1("")
        option_Builder1 = option_Builder0.valueSeparator1(">")
        option_Builder1.numberOfArgs(1873)
        option0 = option_Builder1.build()
        option0.addValueForProcessing("2Jwg5>")
        option0.addValueForProcessing("org.apache.commons.cli.Option$Builder")
        commandLine_Builder1 = commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder1.build()
        properties0 = commandLine0.getOptionProperties1("")
        self.assertIsNotNone(properties0)

    @pytest.mark.test
    def test00(self) -> None:

        commandLine_Builder0 = Builder()
        option_Builder0 = Option.builder1("true")
        option0 = Option(
            1873,
            "true",
            "true",
            "org.apache.commons.cli.Option$Builder",
            True,
            option_Builder0,
        )
        option1 = Option(
            -26,
            "org.apache.commons.cli.Option$Builder",
            "true",
            "org.apache.commons.cli.CommandLine",
            True,
            option_Builder0,
        )
        commandLine_Builder1 = commandLine_Builder0.addOption(option1)
        commandLine0 = commandLine_Builder1.build()
        string0 = commandLine0.getOptionValue2(option0)
        self.assertIsNone(string0)
