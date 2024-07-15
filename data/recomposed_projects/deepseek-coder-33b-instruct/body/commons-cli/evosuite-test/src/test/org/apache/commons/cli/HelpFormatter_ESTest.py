from __future__ import annotations
import time
import locale
import re
import mock
import os
from io import StringIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.HelpFormatter import *

# from src.test.org.apache.commons.cli.HelpFormatter_ESTest_scaffolding import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.Options import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.testdata.EvoSuiteFile import *
# from src.main.org.evosuite.runtime.testdata.FileSystemHandling import *


class HelpFormatter_ESTest(unittest.TestCase):

    def test123(self) -> None:

        helpFormatter0 = HelpFormatter()
        stringBuffer0 = io.StringIO()
        string0 = "["
        helpFormatter0.defaultSyntaxPrefix = "["
        int0 = 881
        options0 = Options()
        string1 = "qV'{Ui"
        boolean0 = False

        try:
            options0.addRequiredOption("qV'{Ui", "", False, "\n")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.apache.commons.cli.OptionValidator", e)

    def test122(self) -> None:

        helpFormatter0 = HelpFormatter()
        string0 = ""
        helpFormatter0.setSyntaxPrefix("")
        string1 = "k{xs;{[P"
        mockPrintWriter0 = None
        try:
            mockPrintWriter0 = MockPrintWriter("usage: ", "k{xs;{[P")
            self.fail("Expecting exception: ValueError")

        except Exception as e:
            # k{xs;{[P
            self.verifyException("org.evosuite.runtime.mock.java.io.MockPrintWriter", e)

    def test121(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.getOptionComparator()
        locale0 = Locale.KOREAN
        objectArray0 = [None] * 6
        objectArray0[0] = helpFormatter0
        helpFormatter0.setLeftPadding(2188)
        options0 = Options()
        options0.addOption3("arg", " ", True, None)
        helpFormatter0.setSyntaxPrefix(None)
        helpFormatter0.findWrapPos("", 2188, 2188)
        helpFormatter0.getArgName()
        self.assertEqual(2188, helpFormatter0.defaultLeftPad)

    def test120(self) -> None:

        helpFormatter0 = HelpFormatter()
        comparator0 = helpFormatter0.getOptionComparator()
        helpFormatter0.setOptionComparator(comparator0)
        helpFormatter0.getNewLine()
        string0 = "--"
        options0 = Options()
        string1 = ""
        options1 = options0.addRequiredOption("", "-", True, "")
        string2 = "spaW_a8 TFA\\uA"
        string3 = "'0-"
        helpFormatter0.defaultWidth = 13
        try:
            options1.addOption3(string2, "'0-", False, "YywJrD%|J")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.apache.commons.cli.OptionValidator", e)

    def test119(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        comparator0 = helpFormatter0.getOptionComparator()
        helpFormatter0.optionComparator = comparator0
        string0 = helpFormatter0._rtrim("org.apache.commons.cli.Option")
        self.assertEqual("usage: ", helpFormatter0.getSyntaxPrefix())
        self.assertEqual("org.apache.commons.cli.Option", string0)
        self.assertEqual(3, helpFormatter0.defaultDescPad)
        self.assertEqual("--", helpFormatter0.getLongOptPrefix())
        self.assertEqual(1, helpFormatter0.defaultLeftPad)
        self.assertEqual("arg", helpFormatter0.getArgName())
        self.assertEqual("-", helpFormatter0.getOptPrefix())
        self.assertEqual(" ", helpFormatter0.getLongOptSeparator())
        self.assertEqual(74, helpFormatter0.defaultWidth)

    def test118(self) -> None:
        helpFormatter0 = HelpFormatter()
        comparator0 = helpFormatter0.getOptionComparator()
        helpFormatter0.setOptionComparator(comparator0)
        helpFormatter0.setLongOptPrefix(":lU/1)h$D")
        helpFormatter0.getOptPrefix()
        self.assertEqual(":lU/1)h$D", helpFormatter0.getLongOptPrefix())

    def test117(self) -> None:

        helpFormatter0 = HelpFormatter()
        int0 = -192
        helpFormatter0.setWidth(int0)
        comparator0 = helpFormatter0.getOptionComparator()
        helpFormatter0.optionComparator = comparator0
        string0 = "Ky:Yl(H_I2A@%\\"
        string1 = "o:M >Welh`/qD`qV^W["
        options0 = Options()
        option0 = Option.Option1("", "")
        options1 = options0.addOption0(option0)
        boolean0 = True
        # Undeclared exception
        try:
            options1.addOption3("usage: ", "-", True, "o:M >Welh`/qD`qV^W[")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # The option 'usage: ' contains an illegal character : ':'
            self.verifyException("org.apache.commons.cli.OptionValidator", e)

    def test116(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.setLeftPadding(-3772)
        try:
            Option.Option1("usage: ", "arg")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # The option 'usage: ' contains an illegal character : ':'
            #
            self.verifyException("org.apache.commons.cli.OptionValidator", e)

    def test115(self) -> None:

        helpFormatter0 = HelpFormatter()
        int0 = -1699
        helpFormatter0.setLeftPadding((-1699))
        mockPrintWriter0 = None
        try:
            mockPrintWriter0 = MockPrintWriter("usage: ", "-")
            self.fail("Expecting exception: ValueError")

        except Exception as e:
            verifyException("org.evosuite.runtime.mock.java.io.MockPrintWriter", e)

    def test114(self) -> None:

        helpFormatter0 = HelpFormatter()

        with pytest.raises(NegativeArraySizeException):
            helpFormatter0.createPadding((-1375))

    def test113(self) -> None:

        helpFormatter0 = HelpFormatter()
        stringBuffer0 = io.StringIO(3131)
        helpFormatter0._renderWrappedText(
            stringBuffer0, 2, 44, "org.apache.commons.cli.Options"
        )

        try:
            helpFormatter0._createPadding((-2))
            self.fail("Expecting exception: NegativeArraySizeException")

        except NegativeArraySizeException as e:
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test112(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()

        try:
            helpFormatter0.printHelp5("", options0, True)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test111(self) -> None:

        helpFormatter0 = HelpFormatter()
        string0 = ""
        helpFormatter0.setSyntaxPrefix("")
        string1 = "zIK9Sre o?ZD~GZ"
        helpFormatter0.defaultNewLine = "zIK9Sre o?ZD~GZ"
        helpFormatter0.getDescPadding()
        boolean0 = True
        helpFormatter0.defaultArgName = "zIK9Sre o?ZD~GZ"
        mockPrintWriter0 = None
        try:
            mockPrintWriter0 = MockPrintWriter(None, True)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("java.io.Writer", e)

    def test110(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        helpFormatter0.printHelp5("org.apache.commons.cli.Options", options0, False)
        stringBuffer0 = io.StringIO()
        helpFormatter0._renderWrappedText(
            stringBuffer0, 0, 0, "org.apache.commons.cli.Options"
        )

    def test109(self) -> None:

        helpFormatter0 = HelpFormatter()
        locale0 = Locale.FRENCH
        helpFormatter1 = HelpFormatter()
        helpFormatter0.getOptionComparator()
        options0 = Options()
        helpFormatter1.printHelp1(3, "--", "usage: ", options0, "usage: ", True)
        helpFormatter0.getLongOptSeparator()

    def test108(self) -> None:
        helpFormatter0 = HelpFormatter()
        helpFormatter0.getWidth()

    def test107(self) -> None:

        helpFormatter0 = HelpFormatter()
        # Undeclared exception in Java code
        try:
            helpFormatter0._findWrapPos("@|bn", 13, -3245)
            self.fail("Expecting exception: StringIndexOutOfBoundsException")

        except IndexError:
            pass

    def test106(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0._rtrim("org.apache.commons.cli.Option")

    def test105(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()

        try:
            helpFormatter0.printUsage1(None, 74, "_4^A*", options0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test104(self) -> None:
        helpFormatter0 = HelpFormatter()
        helpFormatter0.setDescPadding(-3180)
        locale0 = Locale.CHINA
        fileSystemHandling0 = FileSystemHandling()
        stringBuffer0 = StringBuffer(3131)

    def test103(self) -> None:

        helpFormatter0 = HelpFormatter()
        stringBuffer0 = io.StringIO(1)
        helpFormatter1 = HelpFormatter()

        with pytest.raises(IndexError):
            helpFormatter1._renderWrappedText(stringBuffer0, (-1466), 3, "\n")

    def test102(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        helpFormatter1 = HelpFormatter()
        helpFormatter1.setLeftPadding(3)
        options1 = Options()
        options1.addOption3("arg", '~-"G8a,C{4L~C', False, "\n")
        Option.Option1("", "--")
        helpFormatter1.printHelp1(
            8, "arg", "[w( ?wH^RJJ~A^'", options1, "a4N.^Jlev[y$", False
        )

    def test101(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        helpFormatter1 = HelpFormatter()
        helpFormatter1.setLeftPadding(3)
        options1 = Options()
        options1.addOption3("arg", '~-"G8a,C{4L~C', False, "\n")
        option0 = Option.Option1("", "--")
        options0.addOption0(option0)
        helpFormatter1.printHelp7(" ", "-", options1, "", False)

    def test100(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.setDescPadding(-2948)
        helpFormatter0.getWidth()

        try:
            helpFormatter0.printHelp1(
                74, "7fs_C)Ji1Nl", "7fs_C)Ji1Nl", None, "dAN$])9N>PPzV", False
            )
            self.fail("Expecting exception: NegativeArraySizeException")

        except NegativeArraySizeException as e:
            verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test099(self) -> None:

        helpFormatter0 = HelpFormatter()
        comparator0 = helpFormatter0.getOptionComparator()
        helpFormatter0.setOptionComparator(comparator0)
        helpFormatter0.setLongOptPrefix("-P=4e")
        helpFormatter0.findWrapPos("-P=4e", 0, 0)

    def test098(self) -> None:
        helpFormatter0 = HelpFormatter()
        helpFormatter0.setLongOptSeparator("")

    def test097(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        helpFormatter0.printHelp4("&8=Y4Uh*,3}iTl", options0)
        helpFormatter0.getLongOptPrefix()
        helpFormatter0.setLeftPadding((-803))

        try:
            helpFormatter0.printHelp1((-803), "--", "\!F", options0, "", False)
            self.fail("Expecting exception: StringIndexOutOfBoundsException")

        except StringIndexOutOfBoundsException:
            pass

    def test096(self) -> None:
        helpFormatter0 = HelpFormatter()
        helpFormatter0.getLongOptPrefix()

    def test095(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        helpFormatter0.printHelp4("&8=Y4Uh*,3}iTl", options0)
        helpFormatter0.getLongOptPrefix()
        helpFormatter0.setLeftPadding(1)
        helpFormatter0.printHelp1(74, "--", "usage: ", options0, "usage: ", False)
        helpFormatter0.setNewLine('0bx4.8E/g<>n"5z0|')

    def test094(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        helpFormatter0.printHelp4("&8=Y4Uh*,3}iTl", options0)
        helpFormatter0.getLongOptPrefix()
        helpFormatter0.setLeftPadding((-803))

        try:
            helpFormatter0.printHelp1(
                (-803), "&8=Y4Uh*,3}iTl", "", options0, "", False
            )
            self.fail("Expecting exception: StringIndexOutOfBoundsException")

        except StringIndexOutOfBoundsException:
            pass

    def test093(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.getSyntaxPrefix()
        helpFormatter0.setArgName("usage: ")
        helpFormatter0.setDescPadding(-2)
        stringBuffer0 = io.StringIO()
        int1 = 1532
        try:
            helpFormatter0._renderWrappedText(stringBuffer0, -2, 1532, "usage: ")
            self.fail("Expecting exception: StringIndexOutOfBoundsException")

        except IndexError:
            pass

    def test092(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.getOptPrefix()
        int0 = 1
        helpFormatter0.setDescPadding(1)
        helpFormatter0.setArgName("3Y#;%")
        helpFormatter0.getOptionComparator()
        mockPrintWriter0 = MockPrintWriter("3Y#;%")
        string0 = "`z0#>5^pF<Wn<"
        options0 = Options()
        options1 = options0.addOption2("", "3Y#;%")
        optionGroup0 = OptionGroup()
        options1.addOptionGroup(optionGroup0)
        # Undeclared exception handling
        try:
            options1.addOption1("kJb>X{", False, None)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # The option 'kJb>X{' contains an illegal character : '>'
            self.verifyException("org.apache.commons.cli.OptionValidator", e)

    def test091(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0._rtrim("usage: ")

    def test090(self) -> None:

        helpFormatter0 = HelpFormatter()
        string0 = ", "
        options0 = None

        with pytest.raises(RuntimeError):
            helpFormatter0.printHelp4(", ", options0)

    def test089(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.setLongOptSeparator("NS]&amp;!--")
        helpFormatter0.setWidth(375)
        stringWriter0 = io.StringIO()
        mockPrintWriter0 = MockPrintWriter(stringWriter0, False)
        helpFormatter0.printUsage0(mockPrintWriter0, 375, "NS]&amp;!--")
        string0 = "[ARG...]"
        string1 = "lMge!--Sr0Hj;hR"
        options0 = Options()
        string2 = "org.apache.commons.cli.ParseException"
        try:
            Option.Option2("--", False, "org.apache.commons.cli.ParseException")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # The option '--' contains an illegal character : '-'
            #
            self.verifyException("org.apache.commons.cli.OptionValidator", e)

    def test088(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.setLongOptSeparator("B^<D?N")
        helpFormatter0.defaultDescPad = 2641
        helpFormatter0.setNewLine("7")
        string0 = "#v1t=R"
        string1 = "7vUp3Jm?Ec#s3#y"
        options0 = Options()
        boolean0 = True
        try:
            Option.Option2("usage: ", True, "Z^K],5e(j")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # The option 'usage: ' contains an illegal character : ':'
            self.verifyException("org.apache.commons.cli.OptionValidator", e)

    def test087(self) -> None:

        helpFormatter0 = HelpFormatter()
        file0 = MockFile.createTempFile("org.apache.commons.cli.Options", "-")
        mockPrintWriter0 = MockPrintWriter(file0)
        locale0 = Locale.CHINA
        objectArray0 = []
        mockPrintWriter0.format(locale0, "", objectArray0)
        helpFormatter0.setNewLine("org.apache.commons.cli.Options")

    def test086(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.setLeftPadding(3)
        stringWriter0 = io.StringIO()
        stringWriter0.write("=")
        boolean0 = False
        mockPrintWriter0 = MockPrintWriter(stringWriter0, False)
        mockPrintWriter0.write("$")
        options0 = Options()
        string0 = "usage: "
        object0 = "object0"
        mockPrintWriter0.write(object0)
        option_Builder0 = Option.builder0()
        option_Builder0.optionalArg(False)
        option0 = Option(1467, "usage: ", "usage: ", "arg", False, option_Builder0)
        options1 = options0.addOption0(option0)
        int0 = 397
        options0.getOption("--")
        helpFormatter0.printOptions(mockPrintWriter0, 3, options1, 0, 397)
        option_Builder0.hasArgs()
        helpFormatter0.getOptionComparator()
        # Undeclared exception
        try:
            helpFormatter0.printUsage0(mockPrintWriter0, -2, "usage: ")
            self.fail("Expecting exception: StringIndexOutOfBoundsException")

        except StringIndexOutOfBoundsException:
            pass

    def test085(self) -> None:

        helpFormatter0 = HelpFormatter()
        file0 = MockFile.createTempFile("org.apache.commons.cli.Options", "-")
        mockPrintWriter0 = MockPrintWriter(file0)
        locale0 = Locale.CHINA
        objectArray0 = []
        printWriter0 = mockPrintWriter0.format(locale0, "", objectArray0)
        helpFormatter0.printUsage0(printWriter0, 0, "Up]p^HwcDq^yH`lq")

    def test084(self) -> None:

        helpFormatter0 = HelpFormatter()
        comparator0 = helpFormatter0.getOptionComparator()
        helpFormatter0.setOptionComparator(comparator0)
        mockPrintWriter0 = io.StringIO()
        locale0 = "ko_KR"
        objectArray0 = [None] * 6
        objectArray0[0] = helpFormatter0
        objectArray0[1] = helpFormatter0
        objectArray0[2] = comparator0
        object0 = object()
        objectArray0[3] = object0
        objectArray0[4] = comparator0
        objectArray0[5] = locale0
        mockPrintWriter0.write(locale0 + " -- " + " ".join(map(str, objectArray0)))
        helpFormatter0.printUsage0(mockPrintWriter0, 12, "Up]p^HwcDq^yH`lq")
        helpFormatter0.getNewLine()

    def test083(self) -> None:

        helpFormatter0 = HelpFormatter()
        comparator0 = helpFormatter0.getOptionComparator()
        helpFormatter0.setOptionComparator(comparator0)
        helpFormatter0.setLongOptPrefix("(9z")
        helpFormatter1 = HelpFormatter()
        options0 = Options()
        options1 = options0.addOption2(None, "-")
        helpFormatter1.printHelp6("arg", "(9z", options1, "(9z")
        helpFormatter1.getNewLine()
        helpFormatter1.printHelp7(
            "tHF|5lJ@d7S3bn2", None, options0, "W7>QbNh>[_W^k", True
        )

    def test082(self) -> None:

        helpFormatter0 = HelpFormatter()
        file0 = MockFile.createTempFile("org.apache.commons.cli.Options", "-")
        mockPrintWriter0 = MockPrintWriter(file0)
        locale0 = Locale.FRENCH
        helpFormatter1 = HelpFormatter()
        helpFormatter0.getOptionComparator()
        options0 = Options()
        helpFormatter2 = HelpFormatter()
        # Undeclared exception handling is not necessary in Python
        helpFormatter2.printHelp1(
            1,
            "usage: ",
            "VqU>bqb{}J/@+_nT5 ",
            options0,
            "org.apache.commons.cli.Options",
            False,
        )

    def test081(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.getOptionComparator()
        mockPrintWriter0 = io.StringIO()
        options0 = Options()
        helpFormatter0.printUsage1(mockPrintWriter0, 3, "usage: ", options0)

    def test080(self) -> None:

        helpFormatter0 = HelpFormatter()
        comparator0 = helpFormatter0.getOptionComparator()
        helpFormatter0.setOptionComparator(comparator0)
        helpFormatter0.setLongOptPrefix("-P=4e")
        helpFormatter1 = HelpFormatter()
        options0 = Options()
        options1 = options0.addOption2("arg", "")
        helpFormatter1.printHelp6("s9B)]:UGqrO]S0:", 'ZAS,?@A"()lQ', options1, "")
        helpFormatter1.getNewLine()
        helpFormatter0.printHelp7("-:", " ", options1, ',ew"kYN0~xTraJV<(6', True)

    def test079(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        helpFormatter0.printHelp4("&8=Y4Uh*,3}iTl", options0)
        helpFormatter0.getLongOptPrefix()
        helpFormatter0.setLeftPadding(2188)
        byteArray0 = bytearray(3)
        byteArray0[1] = -79
        byteArray0[2] = -103
        option0 = Option.Option2(None, True, "arg")
        options1 = options0.addOption0(option0)
        helpFormatter0.printHelp6("&8=Y4Uh*,3}iTl", "--", options1, "--")
        # FileSystemHandling.appendDataToFile((EvoSuiteFile) null, byteArray0)
        helpFormatter1 = HelpFormatter()
        helpFormatter1.defaultArgName = "LWbH@wD~$>E'%^B9"
        stringBuffer0 = io.StringIO("F")
        # Undeclared exception
        try:
            helpFormatter0._renderWrappedText(
                stringBuffer0, -79, 3, "org.apache.commons.cli.AlreadySelectedException"
            )
            self.fail("Expecting exception: StringIndexOutOfBoundsException")

        except StringIndexOutOfBoundsException:
            pass

    def test078(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.getOptionComparator()
        locale0 = Locale.KOREAN
        helpFormatter0.setLeftPadding(2188)
        options0 = Options()
        options1 = options0.addOption3("arg", " ", True, None)
        helpFormatter1 = HelpFormatter()
        helpFormatter1.printHelp1(2188, "--", None, options1, "", True)

    def test077(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.getOptionComparator()
        mockPrintWriter0 = io.StringIO("\n")
        locale0 = "ko_KR"
        objectArray0 = [None] * 6
        objectArray0[0] = helpFormatter0
        helpFormatter0.setLeftPadding(2188)
        options0 = Options()
        options0.addOption3("arg", " ", True, None)
        option0 = Option.Option1("v", " ")
        options0.addOption0(option0)
        helpFormatter0.setLeftPadding(18)
        helpFormatter0.printHelp7(" ", "", options0, "", False)

    def test076(self) -> None:

        helpFormatter0 = HelpFormatter()
        file0 = MockFile.createTempFile("org.apache.commons.cli.Options", "-")
        mockPrintWriter0 = MockPrintWriter(file0)
        locale0 = Locale.CHINA
        objectArray0 = []
        printWriter0 = mockPrintWriter0.format(locale0, "\n", objectArray0)

        with pytest.raises(StringIndexOutOfBoundsException):
            helpFormatter0.printUsage0(printWriter0, -109, "ie1i|")

    def test075(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.getSyntaxPrefix()
        int0 = 0
        helpFormatter0.setSyntaxPrefix("usage: ")
        helpFormatter0.setDescPadding(0)
        helpFormatter0.setLongOptPrefix("usage: ")
        helpFormatter0.getDescPadding()
        string0 = "JWJ#5C;m~S9k%-|]"
        options0 = Options()
        string1 = "5Kc)]; g]RX"
        # Undeclared exception in Python
        try:
            options0.addOption2("5Kc)]; g]RX", "")
            self.fail("Expecting exception: ValueError")

        except Exception as e:
            #
            # The option '5Kc)]; g]RX' contains an illegal character : ')'
            #
            self.verifyException("org.apache.commons.cli.OptionValidator", e)

    def test074(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        helpFormatter0.printHelp5("cQ6<_Spk=),'ai", options0, False)
        stringBuffer0 = io.StringIO(61)
        helpFormatter0._renderWrappedText(stringBuffer0, 61, 0, "cQ6<_Spk=),'ai")

    def test073(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        stringBuffer0 = io.StringIO()
        helpFormatter0._renderWrappedText(
            stringBuffer0, 0, 0, "9rg.apache.commons.cli.Optio#s"
        )

    def test072(self) -> None:

        helpFormatter0 = HelpFormatter()
        stringBuffer0 = io.StringIO()
        helpFormatter1 = HelpFormatter()
        helpFormatter1._renderWrappedText(stringBuffer0, 74, 4, "")

    def test071(self) -> None:

        helpFormatter0 = HelpFormatter()
        mockPrintStream0 = io.StringIO()
        mockPrintStream0.write(str(helpFormatter0))
        mockPrintWriter0 = io.TextIOWrapper(mockPrintStream0, line_buffering=False)
        printWriter0 = mockPrintWriter0.write("-")
        int0 = 360
        options0 = Options()
        helpFormatter0.printOptions(printWriter0, 360, options0, 360, 360)
        string0 = None
        helpFormatter0.defaultLongOptPrefix = None
        helpFormatter0.setDescPadding(48)
        helpFormatter0.setOptPrefix(None)
        options0.getOption("[ Options: [ short ")
        helpFormatter0.setSyntaxPrefix(None)
        int1 = 0
        helpFormatter0.defaultLeftPad = 0
        # Undeclared exception
        try:
            helpFormatter0.printHelp7("", None, options0, "", True)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # cmdLineSyntax not provided
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test070(self) -> None:

        helpFormatter0 = HelpFormatter()
        locale0 = Locale.CHINA
        options0 = Options()
        optionGroup0 = OptionGroup()
        options0.addOptionGroup(optionGroup0)
        helpFormatter0.printHelp6(
            "org.apache.commons.cli.Options",
            "org.apache.commons.cli.Options",
            options0,
            "org.apache.commons.cli.Options",
        )
        stringBuffer0 = StringBuffer(1)
        helpFormatter0.renderWrappedText(
            stringBuffer0, 44, 44, "org.apache.commons.cli.Options"
        )

    def test069(self) -> None:

        helpFormatter0 = HelpFormatter()
        mockPrintStream0 = io.StringIO()
        mockPrintStream0.write(str(helpFormatter0))
        options0 = Options()
        helpFormatter0.defaultLongOptPrefix = None
        helpFormatter0.setDescPadding(48)
        helpFormatter0.setOptPrefix(None)
        options0.getOption("[ Options: [ short ")
        stringBuffer0 = None
        try:
            stringBuffer0 = io.StringIO(-1)
            self.fail("Expecting exception: NegativeArraySizeException")

        except NegativeArraySizeException as e:
            #
            # -1
            #
            self.verifyException("java.lang.AbstractStringBuilder", e)

    def test068(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()

        try:
            helpFormatter0.printHelp4(None, options0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test067(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.setLongOptPrefix("-P=4e")
        helpFormatter1 = HelpFormatter()
        options0 = Options()
        helpFormatter1.printHelp6("--", "6/", options0, "usage: ")
        helpFormatter1.getNewLine()
        # Undeclared exception
        try:
            helpFormatter1.printHelp7("", "usage: ", options0, "\n", True)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # cmdLineSyntax not provided
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test066(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        helpFormatter0.printHelp5("cQ6<_Spk=),'ai", options0, True)
        stringBuffer0 = io.StringIO(61)
        options0.addOption2("arg", "--")
        helpFormatter0.printHelp1(
            61, "R{ba4P=jY`q]d U}O ", "cQ6<_Spk=),'ai", options0, "i", True
        )

    def test065(self) -> None:

        helpFormatter0 = HelpFormatter()
        comparator0 = helpFormatter0.getOptionComparator()
        helpFormatter0.setOptionComparator(comparator0)
        helpFormatter0.setLongOptPrefix("\n")
        helpFormatter1 = HelpFormatter()
        options0 = Options()
        options1 = options0.addOption2("arg", "")
        helpFormatter1.printHelp6("usage: ", "--", options1, "")
        helpFormatter1.getNewLine()
        helpFormatter0.printHelp7("\n", " ", options1, "usage: ", True)

    def test064(self) -> None:

        helpFormatter0 = HelpFormatter()
        file0 = MockFile.createTempFile("org.apache.commons.cli.Options", "-")
        mockPrintWriter0 = MockPrintWriter(file0)
        locale0 = Locale.CHINA
        helpFormatter0.setLongOptPrefix("m39M&P@*<_R:RNd")
        helpFormatter0.findWrapPos("", (-3653), 23)

    def test063(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.setLeftPadding(3)
        stringWriter0 = io.StringIO()
        stringWriter0.write("=")
        mockPrintWriter0 = MockPrintWriter(stringWriter0, False)
        mockPrintWriter0.write("$")
        options0 = Options()
        option_Builder0 = Option.builder0()
        option_Builder0.optionalArg(False)
        option_Builder0.option("")
        option0 = Option(1467, "usage: ", "usage: ", "arg", False, option_Builder0)
        options1 = options0.addOption0(option0)
        options0.getOption("--")
        helpFormatter0.printOptions(mockPrintWriter0, 3, options1, 0, 397)
        option_Builder0.hasArgs()
        # Undeclared exception
        try:
            helpFormatter0.printHelp3(
                mockPrintWriter0,
                (-1),
                "usage: ",
                "",
                options1,
                (-1),
                (-342),
                "usage: ",
                True,
            )
            self.fail("Expecting exception: NegativeArraySizeException")

        except NegativeArraySizeException as e:
            #
            # -1
            #
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test062(self) -> None:

        helpFormatter0 = HelpFormatter()
        file0 = MockFile.createTempFile("org.apache.commons.cli.Options", "-")
        mockPrintWriter0 = MockPrintWriter(file0)
        locale0 = Locale.CHINA
        objectArray0 = []
        mockPrintWriter0.format(locale0, "", objectArray0)
        options0 = Options()
        helpFormatter0.printHelp7(
            "org.apache.commons.cli.Options", "", options0, "?]$qj_&w", False
        )

    def test061(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.getOptionComparator()
        mockPrintWriter0 = io.StringIO()
        locale0 = "KOREAN"
        options0 = Options()
        helpFormatter0.printUsage1(mockPrintWriter0, 2188, "90iuplHF#Ef;F", options0)
        # Undeclared exception
        try:
            helpFormatter0.printHelp3(
                mockPrintWriter0,
                3,
                "ozVMke.x`",
                'P.l2:"Ue/;""',
                options0,
                -471,
                74,
                "",
                True,
            )
            self.fail("Expecting exception: NegativeArraySizeException")

        except NegativeArraySizeException as e:
            #
            # -471
            #
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test060(self) -> None:

        helpFormatter0 = HelpFormatter()
        file0 = MockFile.createTempFile("org.apache.commons.cli.Options", "-")
        mockPrintWriter0 = MockPrintWriter(file0)
        locale0 = Locale.CHINA
        objectArray0 = []
        mockPrintWriter0.format(locale0, "", objectArray0)
        helpFormatter0.printWrapped1(mockPrintWriter0, 0, "")
        stringBuffer0 = StringBuffer(3131)
        helpFormatter0.renderWrappedText(
            stringBuffer0, 2, 44, "org.apache.commons.cli.Options"
        )

    def test059(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        helpFormatter0.printHelp5("org.apache.commons.cli.Options", options0, False)
        stringBuffer0 = StringIO()
        helpFormatter1 = HelpFormatter()

        try:
            helpFormatter1.printHelp1(
                74, " ", ",>qE(i8V$mkki", None, "Qssnyp{wg*", False
            )
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test058(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.getOptionComparator()
        locale0 = "ko_KR"
        helpFormatter0.setLeftPadding(2188)
        options0 = Options()
        options1 = options0.addOption3("arg", " ", True, None)

        try:
            helpFormatter0.printHelp1(2188, None, None, options1, "<", True)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test057(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        helpFormatter0.printHelp4("&8=Y4Uh*,3}iTl", options0)
        helpFormatter0.getLongOptPrefix()
        options0.helpOptions()
        helpFormatter0.setLeftPadding((-803))
        helpFormatter0.getOptPrefix()
        helpFormatter0.getLongOptSeparator()
        # Undeclared exception in Java code
        try:
            helpFormatter0.printHelp1((-803), "--", "F", options0, "", False)
            self.fail("Expecting exception: StringIndexOutOfBoundsException")

        except StringIndexOutOfBoundsException:
            pass

    def test056(self) -> None:

        helpFormatter0 = HelpFormatter()
        stringBuffer0 = io.StringIO(3131)
        helpFormatter0.renderWrappedText(
            stringBuffer0, 2, 44, "org.apache.commons.cli.Options"
        )
        self.assertEqual(86, stringBuffer0.tell())
        self.assertEqual(
            "or\n g\n .\n a\n p\n a\n c\n h\n e\n .\n c\n o\n m\n m\n o\n n\n s\n .\n c\n l\n i\n .\n O\n p\n t\n i\n o\n n\n s",
            stringBuffer0.getvalue(),
        )

        helpFormatter0.getLongOptSeparator()

    def test055(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.setLongOptSeparator("NS]&amp;!--")
        helpFormatter0.setWidth(375)
        stringWriter0 = io.StringIO()
        stringWriter0.close()
        mockPrintWriter0 = MockPrintWriter(stringWriter0, False)
        helpFormatter0.printUsage0(mockPrintWriter0, 375, "NS]&amp;!--")
        string0 = "[ARG...]"
        string1 = "lMge!--Sr0Hj;hR"
        options0 = Options()
        string2 = "org.apache.commons.cli.ParseException"
        helpFormatter0.getArgName()
        try:
            Option.Option2("--", False, "org.apache.commons.cli.ParseException")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # The option '--' contains an illegal character : '-'
            #
            self.verifyException("org.apache.commons.cli.OptionValidator", e)

    def test054(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        helpFormatter0.printHelp5("cQ6<_Spk=),'ai", options0, True)
        stringBuffer0 = io.StringIO(61)
        options1 = Options()
        helpFormatter0.printHelp1(
            61, "R{ba4P=jY`q]d U}O ", "cQ6<_Spk=),'ai", options0, "i", True
        )
        helpFormatter0.getArgName()

    def test053(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        helpFormatter0.printHelp4("&8=Y4Uh*,3}iTl", options0)
        helpFormatter0.getLongOptPrefix()
        helpFormatter1 = HelpFormatter()
        helpFormatter1.setLeftPadding(2188)
        helpFormatter0.printHelp1(-1, "wq", "--", options0, "wq", False)
        helpFormatter2 = HelpFormatter()
        helpFormatter0._rtrim("")
        helpFormatter1.getDescPadding()

    def test052(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        helpFormatter0.printHelp5("cQ6<_Spk=),'ai", options0, False)
        helpFormatter0.setSyntaxPrefix("&=r?(hL")
        helpFormatter0.printHelp7("<", "6-l$y:vI'@VO", options0, None, False)
        FileSystemHandling.shouldThrowIOException(None)
        helpFormatter0.setSyntaxPrefix("arg")
        mockFile0 = MockFile("-", "\n")
        mockPrintWriter0 = MockPrintWriter(mockFile0)
        printWriter0 = mockPrintWriter0.format("&=r?(hL", None)
        mockPrintWriter1 = MockPrintWriter(printWriter0, True)
        helpFormatter0.printWrapped0(mockPrintWriter1, 0, 0, "")
        helpFormatter0.printUsage1(mockPrintWriter1, -1, "<", options0)
        stringBuffer0 = StringBuffer()
        helpFormatter0.renderOptions(stringBuffer0, -1, options0, 0, 0)
        try:
            helpFormatter0.printHelp2(
                printWriter0, -230, ", ", ", ", options0, -230, -230, "arg"
            )
            self.fail("Expecting exception: StringIndexOutOfBoundsException")
        except StringIndexOutOfBoundsException:
            pass

    def test051(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        helpFormatter1 = HelpFormatter()
        options1 = Options()
        options1.addOption3("arg", '~-"G8a,C{4L~C', False, "\n")
        helpFormatter1.printHelp1(
            3, "arg", "[w( ?wH^RJJ~A^'", options1, "a4N.^Jlev[y$", False
        )
        mockPrintWriter0 = MockPrintWriter(" :: ")
        printWriter0 = mockPrintWriter0.append("--")
        # Undeclared exception handling
        try:
            helpFormatter1.printHelp2(
                printWriter0, -8, "--", "arg", options1, -2035, 74, ""
            )
            self.fail("Expecting exception: StringIndexOutOfBoundsException")

        except StringIndexOutOfBoundsException:
            pass

    def test050(self) -> None:

        helpFormatter0 = HelpFormatter()
        comparator0 = helpFormatter0.getOptionComparator()
        helpFormatter0.setOptionComparator(comparator0)
        mockPrintWriter0 = io.StringIO()
        helpFormatter0.setLeftPadding(2188)
        options0 = Options()
        options0.getOptionGroups()
        options1 = options0.addOption2("", "")
        options2 = options1.addOption3("arg", "-", True, None)
        helpFormatter0.printHelp1(
            44,
            "' was specified but an option from this group has already been selected: '",
            "cmdLineSyntax not provided",
            options2,
            "cmdLineSyntax not provided",
            False,
        )
        helpFormatter1 = HelpFormatter()
        helpFormatter1.setNewLine("\n")
        helpFormatter1.getOptionComparator()
        helpFormatter0.printUsage1(
            mockPrintWriter0,
            74,
            "org.apache.commons.cli.AlreadySelectedException",
            options1,
        )

    def test049(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()

        try:
            helpFormatter0.printUsage1(None, -37, "_4^A*", options0)
            self.fail("Expecting exception: StringIndexOutOfBoundsException")

        except StringIndexOutOfBoundsException:
            pass

    def test048(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        helpFormatter1 = HelpFormatter()
        helpFormatter1.setLeftPadding(3)
        options0.addOption3("arg", '~-"G8a,C{4L~C', False, "\n")
        option0 = Option.Option1("", "--")
        options0.addOption0(option0)
        helpFormatter1.printHelp7(" ", "-", options0, "", False)

    def test047(self) -> None:

        helpFormatter0 = HelpFormatter()
        comparator0 = helpFormatter0.getOptionComparator()
        helpFormatter0.setOptionComparator(comparator0)
        mockPrintWriter0 = io.StringIO()
        locale0 = "ko_KR"
        objectArray0 = [None] * 6
        objectArray0[0] = helpFormatter0
        helpFormatter0.setLeftPadding(2188)
        options0 = Options()
        options1 = options0.addOption2("", "")
        options2 = options1.addOption3("arg", "-", True, None)
        helpFormatter0.printHelp1(
            44,
            "' was specified but an option from this group has already been selected: '",
            "F",
            options2,
            "cmdLineSyntax not provided",
            False,
        )
        helpFormatter1 = HelpFormatter()
        helpFormatter1.setNewLine("\n")

    def test046(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        helpFormatter0.printHelp5("(AfqMLkPKQFZ", options0, False)
        stringBuffer0 = io.StringIO()
        helpFormatter0._renderWrappedText(stringBuffer0, 21, 61, "")

    def test045(self) -> None:

        helpFormatter0 = HelpFormatter()
        comparator0 = helpFormatter0.getOptionComparator()
        helpFormatter0.setOptionComparator(comparator0)
        mockPrintWriter0 = io.StringIO()
        locale0 = "ko_KR"
        objectArray0 = [None] * 6
        objectArray0[0] = helpFormatter0
        objectArray0[1] = helpFormatter0
        objectArray0[2] = comparator0
        object0 = object()
        objectArray0[3] = object0
        string0 = "cmdLineSyntax not provided"
        try:
            helpFormatter0.printWrapped1(
                mockPrintWriter0, -858, "cmdLineSyntax not provided"
            )
            self.fail("Expecting exception: StringIndexOutOfBoundsException")
        except IndexError:
            pass

    def test044(self) -> None:

        helpFormatter0 = HelpFormatter()
        locale0 = Locale.FRENCH
        helpFormatter1 = HelpFormatter()
        helpFormatter0.getOptionComparator()
        options0 = Options()
        helpFormatter2 = HelpFormatter()

        try:
            helpFormatter2.printHelp1(74, "", "arg", options0, "7>nn7mx6", False)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test043(self) -> None:

        helpFormatter0 = HelpFormatter()
        comparator0 = helpFormatter0.getOptionComparator()
        helpFormatter0.setOptionComparator(comparator0)
        helpFormatter0.setLongOptPrefix("-P=4e")
        helpFormatter0.findWrapPos("-P=4e", 0, 3)

    def test042(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        helpFormatter0.printHelp5("arg", options0, False)
        int0 = 61
        stringBuffer0 = StringIO(61)
        writer0 = io.StringIO()
        mockPrintWriter0 = MockPrintWriter(writer0, False)
        int1 = -2
        try:
            helpFormatter0.printWrapped0(mockPrintWriter0, -2, 61, "4Sc:'")
            self.fail("Expecting exception: StringIndexOutOfBoundsException")
        except StringIndexOutOfBoundsException:
            pass

    def test041(self) -> None:

        helpFormatter0 = HelpFormatter()
        file0 = MockFile.createTempFile("org.apache.commons.cli.Options", "-")
        mockPrintWriter0 = MockPrintWriter(file0)
        locale0 = Locale.CHINA
        objectArray0 = []
        mockPrintWriter0.format(locale0, "-", objectArray0)
        helpFormatter0.printWrapped1(mockPrintWriter0, 0, "")
        stringBuffer0 = StringBuffer(3115)
        # Undeclared exception
        try:
            helpFormatter0.renderWrappedText(
                stringBuffer0, 2, (-30), "org.apache.commons.cli.Options"
            )
            self.fail("Expecting exception: NegativeArraySizeException")

        except NegativeArraySizeException as e:
            #
            # -30
            #
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test040(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.setNewLine("")
        helpFormatter0.createPadding(0)
        helpFormatter0.getLongOptPrefix()

        try:
            helpFormatter0.printHelp1(0, "--", "--", None, None, True)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test039(self) -> None:

        helpFormatter0 = HelpFormatter()
        stringWriter0 = io.StringIO()
        stringWriter0.write("=")
        mockPrintWriter0 = MockPrintWriter(stringWriter0, False)
        mockPrintWriter0.write("$")
        options0 = Options()
        object0 = object()
        mockPrintWriter0.print(object0)
        option_Builder0 = Option.builder0()
        option_Builder0.optionalArg(False)
        option_Builder0.option("")
        option0 = Option(1467, "usage: ", "usage: ", "arg", False, option_Builder0)
        options1 = options0.addOption0(option0)
        options0.getOption("--")
        helpFormatter0.printOptions(mockPrintWriter0, 3, options1, 0, 397)
        option_Builder0.hasArgs()
        # Undeclared exception
        try:
            helpFormatter0.printHelp3(
                mockPrintWriter0,
                (-1),
                "usage: ",
                "",
                options1,
                (-1),
                (-342),
                "usage: ",
                False,
            )
            self.fail("Expecting exception: NegativeArraySizeException")

        except NegativeArraySizeException as e:
            #
            # -1
            #
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test038(self) -> None:

        helpFormatter0 = HelpFormatter()
        stringWriter0 = io.StringIO()
        stringWriter0.write("=")
        mockPrintWriter0 = MockPrintWriter(stringWriter0, False)
        mockPrintWriter0.write("$")
        options0 = Options()
        object0 = "usage: "
        mockPrintWriter0.print(object0)
        option_Builder0 = Option.builder0()
        option_Builder0.optionalArg(False)
        option_Builder0.option("")
        option0 = Option(1467, "usage: ", "usage: ", "arg", False, option_Builder0)
        options1 = options0.addOption0(option0)
        # FileSystemHandling.shouldThrowIOException((EvoSuiteFile) null);
        options0.getOption("--")
        helpFormatter0.printOptions(mockPrintWriter0, 3, options1, 0, 397)
        option0.setRequired(True)
        option_Builder0.hasArgs()
        # Undeclared exception
        try:
            helpFormatter0.printHelp3(
                mockPrintWriter0,
                (-1),
                "usage: ",
                "",
                options1,
                (-1),
                (-342),
                "usage: ",
                True,
            )
            self.fail("Expecting exception: NegativeArraySizeException")

        except NegativeArraySizeException as e:
            #
            # -1
            #
            # verifyException("org.apache.commons.cli.HelpFormatter", e);
            pass

    def test037(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        helpFormatter1 = HelpFormatter()
        helpFormatter1.setLeftPadding(3)
        options0.addOption3("arg", '~-"G8a,C{4L~C', False, "\n")
        option0 = Option.Option1("", "--")
        options0.addOption0(option0)
        helpFormatter1.printHelp7(" ", 'eQSc7v"mC;1PC[C@j=c', options0, "-", True)

    def test036(self) -> None:

        helpFormatter0 = HelpFormatter()
        comparator0 = helpFormatter0.getOptionComparator()
        helpFormatter0.setOptionComparator(comparator0)
        helpFormatter0.setWidth(3231)
        helpFormatter0.setLongOptPrefix("-P=4e")
        helpFormatter1 = HelpFormatter()
        string0 = "s9B)]:UGqrO]S0:"
        options0 = Options()
        options1 = options0.addOption2(
            "", "org.apache.commons.cli.HelpFormatter$OptionComparator"
        )
        try:
            helpFormatter1.printHelp6("", "IX", options1, "s9B)]:UGqrO]S0:")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test035(self) -> None:

        helpFormatter0 = HelpFormatter()
        file0 = MockFile.createTempFile("k=|<0KIztbIA+7Ab", "")
        mockPrintWriter0 = MockPrintWriter(file0)
        locale0 = Locale.CHINA
        objectArray0 = [None] * 3
        objectArray0[0] = locale0
        objectArray0[1] = file0
        objectArray0[2] = mockPrintWriter0
        mockPrintWriter0.format(locale0, "arg", objectArray0)
        # Undeclared exception
        helpFormatter0.printWrapped1(mockPrintWriter0, 0, "X0Y}$oEsk}XD")

    def test034(self) -> None:

        helpFormatter0 = HelpFormatter()
        string0 = "org.apache.commons.cli.Options"
        file0 = MockFile.createTempFile("org.apache.commons.cli.Options", "-")
        mockPrintWriter0 = MockPrintWriter(file0)
        locale0 = Locale.CHINA
        objectArray0 = []
        mockPrintWriter0.format(locale0, "", objectArray0)
        # Undeclared exception
        helpFormatter0.printWrapped1(mockPrintWriter0, 0, "-")

    def test033(self) -> None:

        FileSystemHandling.shouldAllThrowIOExceptions()
        helpFormatter0 = HelpFormatter()
        helpFormatter0.setLongOptPrefix("")
        helpFormatter0.getArgName()
        helpFormatter0.getLongOptPrefix()
        helpFormatter0.getOptionComparator()
        stringBuffer0 = StringBuffer("")
        stringBuffer1 = helpFormatter0.renderWrappedText(
            stringBuffer0, 63, (-55), "org.apache.commons.cli.HelpFormatter$1"
        )
        # Undeclared exception in Python
        try:
            helpFormatter0.renderOptions(stringBuffer1, 9, None, 415, 9)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            #
            # no message in exception (getMessage() returned null)
            #
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test032(self) -> None:

        helpFormatter0 = HelpFormatter()
        comparator0 = helpFormatter0.getOptionComparator()
        helpFormatter0.setOptionComparator(comparator0)
        helpFormatter0.setLeftPadding(2188)
        options0 = Options()
        options1 = options0.addOption2("", "")
        options2 = options1.addOption3("arg", "-", True, None)
        helpFormatter0.printHelp1(
            44,
            "' was specified but an option from this group has already been selected: '",
            "cmdLineSyntax not provided",
            options2,
            "cmdLineSyntax not provided",
            False,
        )
        helpFormatter1 = HelpFormatter()
        helpFormatter1.setLeftPadding(2188)
        helpFormatter1.setNewLine("\n")
        helpFormatter1.createPadding(805)

    def test031(self) -> None:

        helpFormatter0 = HelpFormatter()
        comparator0 = helpFormatter0.getOptionComparator()
        helpFormatter0.setOptionComparator(comparator0)
        helpFormatter0.setLongOptPrefix("-P=4e")
        helpFormatter1 = HelpFormatter()
        options0 = Options()
        options1 = options0.addOption2("arg", "")
        helpFormatter1.printHelp6("s9B)]:UGqrO]S0:", "arg", options1, "")
        helpFormatter1.getNewLine()
        stringBuffer0 = io.StringIO(133)
        stringBuffer1 = helpFormatter1.renderWrappedText(stringBuffer0, 3, 74, "--")
        stringBuffer2 = helpFormatter0.renderWrappedText(
            stringBuffer1, 3, 0, "s9B)]:UGqrO]S0:"
        )
        helpFormatter1.renderOptions(stringBuffer2, 1, options1, 63, 133)

    def test030(self) -> None:

        helpFormatter0 = HelpFormatter()
        string0 = "org.apache.commons.cli.Options"
        int0 = 2
        stringBuffer0 = io.StringIO("\n")
        stringBuffer0.write(chr(3))
        # Undeclared exception in Java code
        try:
            helpFormatter0.printHelp0(
                2,
                "org.apache.commons.cli.Options",
                "org.apache.commons.cli.Options",
                None,
                "C*v/TNc",
            )
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test029(self) -> None:

        helpFormatter0 = HelpFormatter()
        comparator0 = helpFormatter0.getOptionComparator()
        helpFormatter0.setOptionComparator(comparator0)
        options0 = Options()

        try:
            helpFormatter0.printHelp0(-1941, "'w1=`5P00Y+", None, options0, "")
            self.fail("Expecting exception: StringIndexOutOfBoundsException")
        except StringIndexOutOfBoundsException:
            pass

    def test028(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.getOptionComparator()
        options0 = Options()
        string0 = ""
        try:
            helpFormatter0.printHelp0(-1968, "'w1=`5P00Y+", None, options0, "")
            self.fail("Expecting exception: StringIndexOutOfBoundsException")

        except StringIndexOutOfBoundsException:
            pass

    def test027(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.getOptionComparator()
        mockPrintWriter0 = io.StringIO()
        locale0 = "ko_KR"
        objectArray0 = [None] * 6
        objectArray0[0] = helpFormatter0
        helpFormatter0.setLeftPadding(2188)
        int0 = 44
        options0 = Options()
        options1 = options0.addOption2("", "")
        options2 = options1.addOption3("arg", "-", True, None)
        helpFormatter0.printUsage1(mockPrintWriter0, 2188, "90iuplHF#Ef;F", options1)
        stringBuffer0 = io.StringIO()
        helpFormatter0.renderOptions(stringBuffer0, 9, options1, 9, 44)
        int1 = -878
        try:
            helpFormatter0.printHelp2(
                mockPrintWriter0,
                9,
                "90iuplHF#Ef;F",
                "Cannot add value, list full.",
                options2,
                -878,
                2188,
                ", ",
            )
            self.fail("Expecting exception: NegativeArraySizeException")

        except NegativeArraySizeException as e:
            verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test026(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.getOptionComparator()
        mockPrintWriter0 = io.StringIO()
        locale0 = "ko_KR"
        objectArray0 = [None] * 6
        objectArray0[0] = helpFormatter0
        mockPrintWriter0.write(locale0 + " " + " ".join(map(str, objectArray0)))
        options0 = Options()
        options1 = options0.addOption2("", "")
        helpFormatter0.printUsage1(mockPrintWriter0, 2188, "90iuplHF#Ef;F", options1)
        int0 = -878
        try:
            helpFormatter0.printHelp2(
                mockPrintWriter0,
                9,
                "90iuplHF#Ef;F",
                "Cannot add value, list full.",
                options1,
                -878,
                2188,
                ", ",
            )
            self.fail("Expecting exception: NegativeArraySizeException")

        except NegativeArraySizeException as e:
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test025(self) -> None:

        helpFormatter0 = HelpFormatter()
        locale0 = Locale.CHINA
        objectArray0 = []
        stringBuffer0 = StringBuffer(3131)

        try:
            helpFormatter0.renderWrappedText(None, 48, 44, "|s=8>L9;@:cZeHMiN")
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test024(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.getOptionComparator()
        mockPrintWriter0 = io.StringIO()
        locale0 = "ko_KR"
        objectArray0 = [None] * 6
        objectArray0[0] = helpFormatter0
        helpFormatter0.setLeftPadding(2188)
        int0 = 44
        options0 = Options()
        options0.addOption2("", "")
        mockPrintWriter1 = io.StringIO(mockPrintWriter0.getvalue())
        int1 = 61
        # Undeclared exception
        try:
            helpFormatter0.printWrapped0(
                mockPrintWriter0,
                61,
                (-24),
                "' was specified but an option from this group has already been selected: '",
            )
            self.fail("Expecting exception: NegativeArraySizeException")

        except NegativeArraySizeException as e:
            #
            # -24
            #
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test023(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.setDescPadding(-3232)
        comparator0 = helpFormatter0.optionComparator
        helpFormatter0.setOptionComparator(comparator0)
        helpFormatter0.getDescPadding()
        helpFormatter0.getSyntaxPrefix()
        mockFile0 = MockFile("arg", "arg")

        try:
            MockFile.createTempFile(None, "-", mockFile0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.evosuite.runtime.vfs.VirtualFileSystem", e)

    def test022(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.getOptionComparator()
        mockPrintWriter0 = io.StringIO("\n")
        locale0 = "ko_KR"
        objectArray0 = [None] * 6
        objectArray0[0] = helpFormatter0
        helpFormatter0.setLeftPadding(2188)
        options0 = Options()
        options0.addOption3("arg", "-", True, None)
        option0 = Option.Option1("v", " ")
        options0.addOption0(option0)
        # Undeclared exception in Java code
        try:
            helpFormatter0.printHelp2(
                None,
                70,
                None,
                "",
                options0,
                -1696,
                -2,
                "' contains an illegal character : '",
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # cmdLineSyntax not provided
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test021(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()

        try:
            helpFormatter0.printHelp0(2155, "", "'w1=`5P00Y+", options0, "")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test020(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.getOptionComparator()
        helpFormatter0.setOptionComparator(None)
        string0 = "-P=4e"
        helpFormatter0.setLongOptPrefix("-P=4e")
        string1 = "s9B)]:UGqrO]S0:"
        options0 = Options()
        options1 = options0.addOption2("arg", "")
        helpFormatter0.printHelp6("s9B)]:UGqrO]S0:", 'ZAS,?@A"()lQ', options1, "")
        string2 = "cmdLineSyntax not provided"
        string3 = "A"
        # Undeclared exception
        try:
            helpFormatter0.printHelp1(1, "", "-P=4e", options1, "A", False)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # cmdLineSyntax not provided
            #
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test019(self) -> None:

        helpFormatter0 = HelpFormatter()
        stringWriter0 = io.StringIO()
        mockPrintWriter0 = MockPrintWriter(stringWriter0, False)
        printWriter0 = mockPrintWriter0.append("$")
        options0 = Options()
        object0 = object()
        mockPrintWriter0.print(object0)
        option_Builder0 = Option.builder0()
        option_Builder0.optionalArg(False)
        option_Builder0.option("")
        options0.getOption("--")
        helpFormatter0.printHelp2(
            printWriter0,
            (-1),
            "cmdLineSyntax not provided",
            "",
            options0,
            4,
            18,
            "cmdLineSyntax not provided",
        )
        helpFormatter0.getOptPrefix()
        helpFormatter0.getLeftPadding()
        helpFormatter0.printUsage1(mockPrintWriter0, 1018, "-", options0)

    def test018(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.getOptionComparator()
        locale0 = "ko_KR"
        objectArray0 = [None] * 6
        objectArray0[0] = helpFormatter0
        helpFormatter0.setLeftPadding(2188)
        options0 = Options()
        options0.addOption3("arg", " ", True, None)
        option0 = Option.Option1("v", " ")
        options0.addOption0(option0)
        helpFormatter0.printHelp7(" ", "", options0, "", True)

    def test017(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.getOptionComparator()
        mockPrintWriter0 = io.StringIO()
        locale0 = "ko_KR"
        objectArray0 = [None] * 6
        objectArray0[0] = helpFormatter0
        mockPrintWriter0.write(locale0.format("", "", objectArray0))
        options0 = Options()
        options1 = options0.addOption2("", "")
        helpFormatter0.printUsage1(mockPrintWriter0, 2188, "90iuplHF#Ef;F", options1)
        # Undeclared exception
        try:
            helpFormatter0.printHelp3(
                mockPrintWriter0,
                3,
                "ozVMke.x`",
                'P.l2:"Ue/;""',
                options1,
                -471,
                44,
                "",
                True,
            )
            self.fail("Expecting exception: NegativeArraySizeException")

        except NegativeArraySizeException as e:
            #
            # -471
            #
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test016(self) -> None:

        helpFormatter0 = HelpFormatter()
        comparator0 = helpFormatter0.getOptionComparator()
        helpFormatter0.setOptionComparator(comparator0)
        mockPrintWriter0 = io.StringIO()
        locale0 = "ko_KR"
        objectArray0 = [None] * 6
        objectArray0[0] = helpFormatter0
        options0 = Options()
        options0.getOptionGroups()
        options1 = options0.addOption2("", "")
        options2 = options1.addOption3("arg", "", True, None)
        helpFormatter0.printHelp1(
            44,
            "' was specified but an option from this group has already been selected: '",
            "cmdLineSyntax not provided",
            options2,
            "cmdLineSyntax not provided",
            False,
        )
        helpFormatter1 = HelpFormatter()
        helpFormatter1.printHelp3(
            mockPrintWriter0,
            1,
            " *eqTk-k",
            "usage: ",
            options0,
            74,
            1,
            " *eqTk-k",
            False,
        )

    def test015(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.getOptionComparator()
        locale0 = "ko_KR"
        objectArray0 = [None] * 6
        objectArray0[0] = helpFormatter0
        helpFormatter0.setLeftPadding(74)
        options0 = Options()
        options0.addOption3("arg", " ", True, None)
        option0 = Option.Option2("arg", True, "v")
        options0.addOption0(option0)
        helpFormatter0.defaultArgName = ""
        helpFormatter0.printHelp7(" ", "", options0, "", True)
        helpFormatter0.getLeftPadding()

    def test014(self) -> None:

        helpFormatter0 = HelpFormatter()
        stringWriter0 = io.StringIO()
        stringWriter0.write("=")
        mockPrintWriter0 = MockPrintWriter(stringWriter0, False)
        mockPrintWriter0.write("$")
        options0 = Options()
        object0 = object()
        mockPrintWriter0.print(object0)
        option_Builder0 = Option.builder0()
        option_Builder0.optionalArg(False)
        option_Builder0.option("")
        option0 = Option(1467, "usage: ", "-", "arg", False, option_Builder0)
        options1 = options0.addOption0(option0)
        options0.getOption("--")
        helpFormatter0.printOptions(mockPrintWriter0, 3, options1, 0, 397)
        option_Builder0.hasArgs()
        int0 = -2
        # Undeclared exception in Java code
        try:
            helpFormatter0.printHelp3(
                mockPrintWriter0,
                -2,
                "",
                None,
                options0,
                61,
                397,
                "*QE p8 >= E4:?dq",
                False,
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # cmdLineSyntax not provided
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test013(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()

        try:
            helpFormatter0.printHelp3(
                None,
                1413,
                "",
                "NO_ARGS_ALLOWED",
                options0,
                1585,
                1585,
                "Cd:'&c>LjI+~<]fPk",
                True,
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test012(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        options0.hasShortOption("")
        helpFormatter0.printHelp4("&8=Y4Uh*,3}iTl", options0)
        helpFormatter0.getLongOptPrefix()
        helpFormatter0.setLeftPadding(2188)
        locale0 = Locale.CHINA
        stringWriter0 = StringWriter(3)
        mockPrintWriter0 = MockPrintWriter(stringWriter0, True)
        FileSystemHandling.setPermissions(None, True, False, True)
        helpFormatter0.printHelp0(2188, " ", " ", options0, None)
        objectArray0 = [None] * 7
        objectArray0[0] = helpFormatter0
        objectArray0[1] = None
        objectArray0[2] = "--"
        objectArray0[3] = "--"
        objectArray0[4] = mockPrintWriter0
        objectArray0[5] = ""
        objectArray0[6] = mockPrintWriter0
        mockPrintWriter0.format(locale0, "g+mdXNiuo85*!!", objectArray0)

    def test011(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.getOptionComparator()
        locale0 = Locale.KOREAN
        objectArray0 = [None] * 6
        objectArray0[0] = helpFormatter0
        helpFormatter0.setLeftPadding(2188)
        helpFormatter0.defaultDescPad = -1111
        options0 = Options()
        options0.addOption3("arg", " ", True, None)
        option0 = Option.Option1("v", " ")
        options1 = options0.addOption0(option0)

        try:
            helpFormatter0.printHelp7(" ", "", options1, "", True)
            self.fail("Expecting exception: NegativeArraySizeException")

        except NegativeArraySizeException as e:
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test010(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.getOptionComparator()
        mockPrintWriter0 = io.StringIO("\n")
        locale0 = "ko_KR"
        helpFormatter0.setLongOptPrefix("$Uz?US`7G")
        helpFormatter1 = HelpFormatter()
        options0 = Options()
        options0.addOption2("", "$9i{z]A")
        helpFormatter1.printHelp6(
            "7l:hc%<nJ8*jEE:&/|", "7l:hc%<nJ8*jEE:&/|", options0, "%GfUd()?}A8."
        )
        helpFormatter0.getNewLine()
        helpFormatter0.printHelp7("\n", ">", options0, "-", True)

    def test009(self) -> None:

        helpFormatter0 = HelpFormatter()
        file0 = MockFile.createTempFile("org.apache.commons.cli.Options", "-")
        mockPrintWriter0 = MockPrintWriter(file0)
        file0.getAbsoluteFile()
        locale0 = Locale.CHINA
        file0.getAbsoluteFile()
        objectArray0 = []
        mockPrintWriter0.format(locale0, "", objectArray0)
        # Undeclared exception
        try:
            helpFormatter0.printHelp7("'E,A(eG310V[", "'E,A(eG310V[", None, "", True)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # no message in exception (getMessage() returned null)
            verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test008(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.getOptionComparator()
        mockPrintWriter0 = io.StringIO()
        locale0 = "ko_KR"
        helpFormatter0.setLongOptPrefix("$Uz?US`7G")
        helpFormatter1 = HelpFormatter()
        options0 = Options()
        options0.addOption2("", "$9i{z]A")
        helpFormatter1.printHelp6(
            "7l:hc%<nJ8*jEE:&/|", "7l:hc%<nJ8*jEE:&/|", options0, "%GfUd()?}A8."
        )
        helpFormatter0.getNewLine()
        # Undeclared exception in Java code
        try:
            helpFormatter0.printUsage0(mockPrintWriter0, 1, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            #
            # no message in exception (getMessage() returned null)
            #
            self.verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test007(self) -> None:

        helpFormatter0 = HelpFormatter()
        FileSystemHandling.appendLineToFile(None, 'SRUVNsr-B"')
        options0 = Options()

        try:
            helpFormatter0.printHelp5("usage: ", None, False)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test006(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.getOptionComparator()
        mockPrintWriter0 = io.StringIO()
        locale0 = "it_IT"
        objectArray0 = [None] * 6
        objectArray0[0] = helpFormatter0
        mockPrintWriter0.write(locale0 + " " + " ".join(map(str, objectArray0)))
        options0 = Options()
        options1 = options0.addOption2("", "")
        helpFormatter0.printUsage1(mockPrintWriter0, 74, "90iuplHF#Ef;F", options1)
        helpFormatter0.printHelp3(
            mockPrintWriter0, 3, "ozVMke.x`", 'P.l2:"Ue/;""', options1, 1, 74, "", True
        )

    def test005(self) -> None:

        helpFormatter0 = HelpFormatter()
        options0 = Options()
        helpFormatter1 = HelpFormatter()
        helpFormatter1.setLeftPadding(3)
        options1 = Options()
        options1.addOption3("arg", '~-"G8a,C{4L~C', False, "\n")
        option0 = Option.Option1("", "--")
        options0.addOption0(option0)
        stringBuffer0 = io.StringIO("--")
        int0 = -27
        try:
            helpFormatter0._renderOptions(
                stringBuffer0.getvalue(), -27, options1, 1406, 1
            )
            self.fail("Expecting exception: StringIndexOutOfBoundsException")
        except IndexError:
            pass

    def test004(self) -> None:

        string0 = ""
        FileSystemHandling.appendLineToFile(None, "")
        FileSystemHandling.appendStringToFile(None, "")
        FileSystemHandling.shouldThrowIOException(None)
        helpFormatter0 = HelpFormatter()
        comparator0 = helpFormatter0.optionComparator
        fileSystemHandling0 = FileSystemHandling()
        helpFormatter0.optionComparator = comparator0
        helpFormatter0.optionComparator = comparator0
        helpFormatter0.getNewLine()
        helpFormatter0.getOptionComparator()
        helpFormatter0.getLongOptSeparator()
        helpFormatter0.getNewLine()
        FileSystemHandling.createFolder(None)
        helpFormatter0.getSyntaxPrefix()
        helpFormatter0.getLongOptSeparator()
        helpFormatter0.getSyntaxPrefix()
        helpFormatter0.getOptPrefix()
        int0 = -3118
        try:
            helpFormatter0.findWrapPos(None, -2685, -3118)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.cli.HelpFormatter", e)

    def test003(self) -> None:

        helpFormatter0 = HelpFormatter()
        comparator0 = helpFormatter0.optionComparator
        mockPrintWriter0 = io.StringIO()
        locale0 = "en_GB"
        options0 = Options()
        helpFormatter0.printUsage1(mockPrintWriter0, 2188, None, options0)
        # Undeclared exception handling
        try:
            helpFormatter0.printHelp3(
                mockPrintWriter0,
                -3021,
                "90iuplHF#Ef;F",
                "",
                options0,
                -3021,
                -3021,
                "Iv",
                True,
            )
            self.fail("Expecting exception: StringIndexOutOfBoundsException")

        except StringIndexOutOfBoundsException:
            pass

    def test002(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.getOptionComparator()
        mockPrintWriter0 = io.StringIO("\n")
        locale0 = "ko_KR"
        helpFormatter0.setLongOptPrefix("$Uz?US`7G")
        helpFormatter1 = HelpFormatter()
        options0 = Options()
        options0.addOption2("", "$9i{z]A")
        helpFormatter0.getNewLine()
        helpFormatter0.printHelp7("\n", ">", options0, "-", True)

    def test001(self) -> None:

        helpFormatter0 = HelpFormatter()
        helpFormatter0.getOptionComparator()
        mockPrintWriter0 = io.StringIO()
        locale0 = "ko_KR"
        options0 = Options()
        options1 = options0.addOption2("TahItvRD", "arg")
        helpFormatter0.printUsage1(mockPrintWriter0, 74, "line.separator", options0)
        helpFormatter0.printHelp3(
            mockPrintWriter0, 74, 'P.l2:"Ue/;""', "", options1, 0, 0, "-", True
        )

    def test000(self) -> None:

        helpFormatter0 = HelpFormatter()
        self.assertEqual("arg", helpFormatter0.getArgName())
        self.assertEqual(1, helpFormatter0.defaultLeftPad)
        self.assertEqual(" ", helpFormatter0.getLongOptSeparator())
        self.assertEqual(74, helpFormatter0.defaultWidth)
        self.assertEqual("usage: ", helpFormatter0.getSyntaxPrefix())
        self.assertEqual("-", helpFormatter0.getOptPrefix())
        self.assertEqual("--", helpFormatter0.getLongOptPrefix())
        self.assertEqual(3, helpFormatter0.defaultDescPad)

        helpFormatter0.getOptionComparator()
        mockPrintWriter0 = io.StringIO()
        locale0 = "ko_KR"
        options0 = Options()
        helpFormatter0.printUsage1(mockPrintWriter0, 2188, " | ", options0)
        helpFormatter1 = HelpFormatter()
        helpFormatter2 = HelpFormatter()
        # Undeclared exception in Python, so we can't translate this line
        # helpFormatter2.printUsage1(mockPrintWriter0, 1, "arg", options0)
