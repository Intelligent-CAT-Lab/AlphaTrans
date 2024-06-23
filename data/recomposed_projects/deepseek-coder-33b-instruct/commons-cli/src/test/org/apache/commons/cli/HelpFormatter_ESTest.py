from __future__ import annotations
import re
import mock
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.HelpFormatter import *

# from src.main.org.apache.commons.cli.HelpFormatter_ESTest_scaffolding import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.Options import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class HelpFormatter_ESTest(unittest.TestCase):

    @pytest.mark.test
    def test75(self) -> None:
        helpFormatter0 = HelpFormatter()
        helpFormatter0.setLongOptPrefix('^vyLtU)E#_"P|=DT')
        self.assertEqual('^vyLtU)E#_"P|=DT', helpFormatter0.getLongOptPrefix())

    @pytest.mark.test
    def test74(self) -> None:

        helpFormatter0 = HelpFormatter()
        # Undeclared exception in Java code
        try:
            helpFormatter0.printWrapped1(
                None, 79, "org.apache.commons.cli.ParseException"
            )
            self.fail("Expecting exception: NullPointerException")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    @pytest.mark.test
    def test73(self) -> None:
        helpFormatter0 = HelpFormatter()
        helpFormatter0.setLongOptSeparator("ez^9DJ~")
        self.assertEqual("ez^9DJ~", helpFormatter0.getLongOptSeparator())

    @pytest.mark.test
    def test72(self) -> None:
        helpFormatter0 = HelpFormatter()
        helpFormatter0.setLeftPadding(-999)
        self.assertEqual(-999, helpFormatter0.defaultLeftPad)

    @pytest.mark.test
    def test71(self) -> None:

        helpFormatter0 = HelpFormatter()
        # Undeclared exception
        try:
            helpFormatter0.printHelp6('jz>["', "", None, "\!uOkt:<M#QMgd")
            self.fail("Expecting exception: NullPointerException")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    @pytest.mark.test
    def test70(self) -> None:

        helpFormatter0 = HelpFormatter()
        self.assertEqual("arg", helpFormatter0.getArgName())

        helpFormatter0.setArgName("")
        self.assertEqual("", helpFormatter0.getArgName())

    @pytest.mark.test
    def test69(self) -> None:
        helpFormatter0 = HelpFormatter()
        helpFormatter0.setSyntaxPrefix("org.apache.commons.cli.OptionGroup")
        self.assertEqual(
            "org.apache.commons.cli.OptionGroup", helpFormatter0.getSyntaxPrefix()
        )

    @pytest.mark.test
    def test68(self) -> None:

        helpFormatter0 = HelpFormatter()
        string0 = helpFormatter0.getLongOptSeparator()
        self.assertEqual("usage: ", helpFormatter0.getSyntaxPrefix())
        self.assertEqual(" ", string0)
        self.assertEqual("arg", helpFormatter0.getArgName())
        self.assertEqual(74, helpFormatter0.defaultWidth)
        self.assertEqual("--", helpFormatter0.getLongOptPrefix())
        self.assertEqual("-", helpFormatter0.getOptPrefix())
        self.assertEqual(1, helpFormatter0.defaultLeftPad)
        self.assertEqual(3, helpFormatter0.defaultDescPad)

    @pytest.mark.test
    def test67(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        helpFormatter0.printHelp0(1, "(m'LohC]", " ", options0, "[")

    @pytest.mark.test
    def test66(self) -> None:
        helpFormatter0 = HelpFormatter()
        helpFormatter0.setWidth(0)

    @pytest.mark.test
    def test65(self) -> None:
        helpFormatter0 = HelpFormatter()
        helpFormatter0.setOptPrefix('-g-1`WSCvk}n<<-x"')

    @pytest.mark.test
    def test64(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        options1 = options0.addOption1("", True, "usage: ")
        helpFormatter0.printHelp5("d1CQTo-XYLQIPCKe", options1, False)

    @pytest.mark.test
    def test63(self) -> None:
        helpFormatter0 = HelpFormatter()
        helpFormatter0.setDescPadding(-1437)

    @pytest.mark.test
    def test62(self) -> None:

        helpFormatter0 = HelpFormatter()
        mockPrintWriter0 = io.StringIO()
        # Undeclared exception in Java, so we use try-except in Python
        try:
            helpFormatter0.printHelp2(
                mockPrintWriter0, -2, ")[@oYif'LZ^+J#S", "--", None, 2, 64, ""
            )
            self.fail("Expecting exception: StringIndexOutOfBoundsException")

        except IndexError as e:
            pass

    @pytest.mark.test
    def test61(self) -> None:
        helpFormatter0 = HelpFormatter()
        helpFormatter0.getLongOptPrefix()

    @pytest.mark.test
    def test60(self) -> None:
        helpFormatter0 = HelpFormatter()
        options0 = Options()
        helpFormatter0.printHelp4(" | ", options0)

    @pytest.mark.test
    def test59(self) -> None:
        helpFormatter0 = HelpFormatter()
        comparator0 = helpFormatter0.getOptionComparator()
        helpFormatter0.setOptionComparator(comparator0)

    @pytest.mark.test
    def test58(self) -> None:

        helpFormatter0 = HelpFormatter()
        mockPrintWriter0 = io.StringIO()
        options0 = Options()
        options1 = options0.addOption3("arg", "25 ", False, "jR/~8u[/.MeKn")
        options2 = options1.addOption1("", False, "")
        helpFormatter0.printUsage1(mockPrintWriter0, 765, "", options2)

    @pytest.mark.test
    def test57(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        options0.addRequiredOption("arg", "ST2wD)FV", True, "usage: ")
        helpFormatter0.printHelp5("k#5e-gE\u0006aD].DfY", options0, True)

    @pytest.mark.test
    def test56(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        mockPrintWriter0 = io.StringIO()
        option_Builder0 = Option.builder0()
        option0 = Option(63, "usage: ", "-", "", True, option_Builder0)
        options1 = options0.addOption0(option0)
        helpFormatter0.printHelp3(
            mockPrintWriter0, 44, "arg", "arg", options1, 1, 74, "", True
        )

    @pytest.mark.test
    def test55(self) -> None:

        helpFormatter0 = HelpFormatter()
        stringBuffer0 = io.StringIO(" ")

        try:
            helpFormatter0._renderWrappedText(stringBuffer0, -676, 3, "\n")
            self.fail("Expecting exception: StringIndexOutOfBoundsException")

        except StringIndexOutOfBoundsException:
            pass

    @pytest.mark.test
    def test54(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()

        try:
            helpFormatter0.printHelp1(
                (-456), None, 'wni"FjW_SK_b', options0, None, True
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    @pytest.mark.test
    def test53(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()

        try:
            helpFormatter0.printHelp5("", options0, False)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    @pytest.mark.test
    def test52(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        mockPrintWriter0 = io.StringIO()

        try:
            helpFormatter0.printHelp3(
                mockPrintWriter0,
                3,
                " ",
                "org.apache.commons.cli.OptionGroup",
                options0,
                1486,
                (-962),
                "T;81Q@_O>96T%''`",
                True,
            )
            self.fail("Expecting exception: NegativeArraySizeException")

        except NegativeArraySizeException:
            self.verifyException("org.apache.commons.cli.HelpFormatter")

    @pytest.mark.test
    def test51(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        helpFormatter0.printHelp0(
            13, "k#5e-gE\u0006aD].DfY", '}ga "ziiC7}x', options0, ""
        )

    @pytest.mark.test
    def test50(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()

        try:
            helpFormatter0.printUsage1(None, 3, "\n", options0)
            self.fail("Expecting exception: NullPointerException")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    @pytest.mark.test
    def test49(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0._rtrim("")

    @pytest.mark.test
    def test48(self) -> None:
        helpFormatter0 = HelpFormatter()
        helpFormatter0.getDescPadding()

    @pytest.mark.test
    def test47(self) -> None:

        helpFormatter0 = HelpFormatter()
        mockPrintWriter0 = io.StringIO()
        helpFormatter0.printUsage0(mockPrintWriter0, 61, "")

    @pytest.mark.test
    def test46(self) -> None:
        helpFormatter0 = HelpFormatter()
        helpFormatter0.getOptPrefix()

    @pytest.mark.test
    def test45(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()

        try:
            helpFormatter0.printHelp7("", "", options0, "", False)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    @pytest.mark.test
    def test44(self) -> None:
        helpFormatter0 = HelpFormatter()
        helpFormatter0.getSyntaxPrefix()

    @pytest.mark.test
    def test43(self) -> None:
        helpFormatter0 = HelpFormatter()
        helpFormatter0.getArgName()

    @pytest.mark.test
    def test42(self) -> None:

        helpFormatter0 = HelpFormatter()
        mockPrintWriter0 = io.StringIO()

        try:
            helpFormatter0.printOptions(mockPrintWriter0, -1348, None, -1586, -3428)
            self.fail("Expecting exception: NegativeArraySizeException")

        except NegativeArraySizeException:
            # verifyException("org.apache.commons.cli.HelpFormatter", e)
            pass

    @pytest.mark.test
    def test41(self) -> None:
        helpFormatter0 = HelpFormatter()
        helpFormatter0.getLeftPadding()

    @pytest.mark.test
    def test40(self) -> None:
        helpFormatter0 = HelpFormatter()
        helpFormatter0.getWidth()

    @pytest.mark.test
    def test39(self) -> None:
        helpFormatter0 = HelpFormatter()
        helpFormatter0.getNewLine()

    @pytest.mark.test
    def test38(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        mockPrintWriter0 = io.StringIO()

        try:
            helpFormatter0.printHelp3(
                mockPrintWriter0, 1, "", "", options0, 12, 776, "@)v@A", False
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    @pytest.mark.test
    def test37(self) -> None:

        helpFormatter0 = HelpFormatter()
        mockPrintWriter0 = io.StringIO()

        try:
            helpFormatter0.printHelp3(
                mockPrintWriter0, -2, "--", "--", None, -2, 10, "--", False
            )
            self.fail("Expecting exception: StringIndexOutOfBoundsException")

        except StringIndexOutOfBoundsException:
            pass

    @pytest.mark.test
    def test36(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        mockPrintWriter0 = io.StringIO()
        helpFormatter0.printHelp3(
            mockPrintWriter0, 3, "arg", None, options0, 10, 1, "--", True
        )

    @pytest.mark.test
    def test35(self) -> None:

        helpFormatter0 = HelpFormatter()
        try:
            helpFormatter0._createPadding((-18))
            self.fail("Expecting exception: NegativeArraySizeException")

        except NegativeArraySizeException:
            # verifyException("org.apache.commons.cli.HelpFormatter", e)
            pass

    @pytest.mark.test
    def test34(self) -> None:

        helpFormatter0 = HelpFormatter()
        # Undeclared exception
        try:
            helpFormatter0._findWrapPos(None, 3, 74)
            self.fail("Expecting exception: NullPointerException")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    @pytest.mark.test
    def test33(self) -> None:

        helpFormatter0 = HelpFormatter()
        # Undeclared exception in Java code
        try:
            helpFormatter0.printHelp0(-994, "", "", None, "fj6v_%ruoPdl:PsoqC0")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # cmdLineSyntax not provided
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    @pytest.mark.test
    def test32(self) -> None:

        helpFormatter0 = HelpFormatter()
        # Undeclared exception
        try:
            helpFormatter0.printHelp0(9, "         ", "", None, "         ")
            self.fail("Expecting exception: NullPointerException")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    @pytest.mark.test
    def test31(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        # Undeclared exception
        try:
            helpFormatter0.printHelp0(
                -663,
                "org.apache.commons.cli.OptionValidator",
                "BEi}YU&?K-",
                options0,
                "BEi}YU&?K-",
            )
            self.fail("Expecting exception: StringIndexOutOfBoundsException")

        except StringIndexOutOfBoundsException:
            pass

    @pytest.mark.test
    def test30(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        helpFormatter0.printHelp1(1, " ", "", options0, "", False)

    @pytest.mark.test
    def test29(self) -> None:

        helpFormatter0 = HelpFormatter()
        mockPrintWriter0 = io.StringIO()

        try:
            helpFormatter0.printHelp2(mockPrintWriter0, 3, "", "]", None, 3, 3, "R{[m")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # cmdLineSyntax not provided
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    @pytest.mark.test
    def test28(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        mockPrintWriter0 = io.StringIO("usage: ")
        helpFormatter0.printHelp2(
            mockPrintWriter0, 1, "-", "usage: ", options0, 94, 802, "':/FPY'gOW."
        )

    @pytest.mark.test
    def test27(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        mockPrintWriter0 = io.StringIO()
        helpFormatter0.printHelp3(
            mockPrintWriter0,
            1,
            ">",
            "arg",
            options0,
            (-1),
            1,
            "tJ u2BJfta0j*@$H",
            True,
        )

    @pytest.mark.test
    def test26(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()

        try:
            helpFormatter0.printHelp4("", options0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    @pytest.mark.test
    def test25(self) -> None:

        helpFormatter0 = HelpFormatter()
        # Undeclared exception
        try:
            helpFormatter0.printHelp5("--", None, True)
            self.fail("Expecting exception: NullPointerException")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    @pytest.mark.test
    def test24(self) -> None:

        helpFormatter0 = HelpFormatter()

        try:
            helpFormatter0.printUsage0(None, 63, "")
            self.fail("Expecting exception: NullPointerException")

        except Exception as e:
            self.assertEqual(str(e), "")
            self.assertEqual(type(e).__name__, "NullPointerException")

    @pytest.mark.test
    def test23(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        helpFormatter0.printUsage1(None, 1, "iEM6]uk", options0)

    @pytest.mark.test
    def test22(self) -> None:

        helpFormatter0 = HelpFormatter()
        stringBuffer0 = io.StringIO()
        options0 = Options()

        try:
            helpFormatter0._renderOptions(stringBuffer0, (-1), options0, (-1), 3036)
            self.fail("Expecting exception: NegativeArraySizeException")

        except NegativeArraySizeException as e:
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    @pytest.mark.test
    def test21(self) -> None:

        helpFormatter0 = HelpFormatter()
        stringBuffer0 = io.StringIO("\n")

        try:
            helpFormatter0._renderOptions(stringBuffer0, 1, None, 74, 1)
            self.fail("Expecting exception: NullPointerException")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    @pytest.mark.test
    def test20(self) -> None:

        helpFormatter0 = HelpFormatter()
        stringBuffer0 = io.StringIO()

        try:
            helpFormatter0._renderWrappedText(stringBuffer0, 1, (-662), "--")
            self.fail("Expecting exception: NegativeArraySizeException")

        except NegativeArraySizeException as e:
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    @pytest.mark.test
    def test19(self) -> None:

        helpFormatter0 = HelpFormatter()

        try:
            helpFormatter0._renderWrappedText(None, 1, 1, " ")
            self.fail("Expecting exception: NullPointerException")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    @pytest.mark.test
    def test18(self) -> None:

        helpFormatter0 = HelpFormatter()
        stringBuffer0 = io.StringIO()
        helpFormatter0._renderWrappedText(stringBuffer0, 1, 9, "k#5e-gE\u0006aD].DfY")

    @pytest.mark.test
    def test17(self) -> None:
        helpFormatter0 = HelpFormatter()
        helpFormatter0._createPadding(0)

    @pytest.mark.test
    def test16(self) -> None:
        helpFormatter0 = HelpFormatter()
        helpFormatter0._createPadding(1)

    @pytest.mark.test
    def test15(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0._findWrapPos(")[@oYif'LZ^+J#S", -1592, 936)

    @pytest.mark.test
    def test14(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0._findWrapPos("n2O,lK%rk", -3, 9)

    @pytest.mark.test
    def test13(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0._findWrapPos(">", 0, 0)

    @pytest.mark.test
    def test12(self) -> None:
        helpFormatter0 = HelpFormatter()
        helpFormatter0.defaultArgName = ""
        helpFormatter0.getArgName()

    @pytest.mark.test
    def test11(self) -> None:
        helpFormatter0 = HelpFormatter()
        helpFormatter0.setNewLine("")
        helpFormatter0.getNewLine()

    @pytest.mark.test
    def test10(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        stringBuffer0 = io.StringIO()
        helpFormatter0._renderOptions(stringBuffer0, 74, options0, 1, 1)

    @pytest.mark.test
    def test09(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        helpFormatter0._renderOptions(None, -17, options0, 24, 24)

    @pytest.mark.test
    def test08(self) -> None:

        helpFormatter0 = HelpFormatter()
        stringBuffer0 = io.StringIO()
        helpFormatter0._renderWrappedText(stringBuffer0, 213, 213, "")

    @pytest.mark.test
    def test07(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0._rtrim("--")

    @pytest.mark.test
    def test06(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        mockPrintWriter0 = io.StringIO()
        helpFormatter0.printHelp2(
            mockPrintWriter0, 256, "KW2~<", "--", options0, 1, 1, ""
        )

    @pytest.mark.test
    def test05(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        helpFormatter0.printHelp6("YIZC;", "", options0, "")

    @pytest.mark.test
    def test04(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        helpFormatter0.printHelp1(44, " ", "", options0, "", False)

    @pytest.mark.test
    def test03(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        helpFormatter0.printHelp7(
            "ST2wD)FV", "k#5e-gE\u0006aD].DfY", options0, "arg", False
        )

    @pytest.mark.test
    def test02(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        mockPrintWriter0 = io.StringIO()
        helpFormatter0.printOptions(mockPrintWriter0, 44, options0, 23, 44)

    @pytest.mark.test
    def test01(self) -> None:

        helpFormatter0 = HelpFormatter()
        mockFile0 = io.StringIO()
        helpFormatter0.printWrapped1(mockFile0, 2162, "G")

    @pytest.mark.test
    def test00(self) -> None:

        helpFormatter0 = HelpFormatter()
        stringBuffer0 = io.StringIO("-")
        helpFormatter0._renderWrappedText(stringBuffer0, 9, 9, "\!uOkt:<M#QMgd")
