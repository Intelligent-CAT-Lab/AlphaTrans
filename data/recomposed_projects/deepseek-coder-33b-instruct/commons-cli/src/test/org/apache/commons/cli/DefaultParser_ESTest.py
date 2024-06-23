from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.DefaultParser import *

# from src.main.org.apache.commons.cli.DefaultParser_ESTest_scaffolding import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.Options import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class DefaultParser_ESTest(unittest.TestCase):

    @pytest.mark.test
    def test38(self) -> None:

        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()
        options0 = Options()
        stringArray0 = [""]
        try:
            defaultParser0.parse1(options0, stringArray0, True)
            self.fail("Expecting exception: NullPointerException")

        except NullPointerException:
            pass

    @pytest.mark.test
    def test37(self) -> None:

        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser_Builder1 = defaultParser_Builder0.setAllowPartialMatching(False)
        defaultParser0 = defaultParser_Builder1.build()
        options0 = Options()
        properties0 = {}
        stringArray0 = ["-Dg|%Az`l?Gm10=1???"]
        try:
            defaultParser0.parse2(options0, stringArray0, properties0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Unrecognized option: -Dg|%Az`l?Gm10=1???
            self.verifyException("org.apache.commons.cli.DefaultParser", e)

    @pytest.mark.test
    def test36(self) -> None:

        boolean0 = True
        defaultParser0 = DefaultParser(0, boolean0, boolean0)

    @pytest.mark.test
    def test35(self) -> None:

        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()
        options0 = Options()
        options1 = options0.addRequiredOption("", "", True, "")
        stringArray0 = [""] * 1
        stringArray0[0] = "--=-"
        defaultParser0.parse0(options1, stringArray0)
        defaultParser0._handleConcatenatedOptions("--=-")
        defaultParser0._handleConcatenatedOptions("--=-")

    @pytest.mark.test
    def test34(self) -> None:

        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()
        options0 = Options()
        options0.addRequiredOption("", "", True, "")
        stringArray0 = [""] * 1
        stringArray0[0] = "--=-"
        options1 = options0.addOption3("", "--=-", True, "--=-")
        try:
            defaultParser0.parse1(options1, stringArray0, True)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Missing required option:
            #
            self.verifyException("org.apache.commons.cli.MissingOptionException", e)

    @pytest.mark.test
    def test33(self) -> None:

        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser_Builder0.setAllowPartialMatching(False)
        defaultParser0 = defaultParser_Builder0.build()

        options0 = Options()
        options1 = options0.addRequiredOption("", "", True, "")

        stringArray0 = [""] * 1
        stringArray0[0] = "--=-"

        commandLine0 = defaultParser0.parse0(options1, stringArray0)

        self.assertIsNotNone(commandLine0)

    @pytest.mark.test
    def test32(self) -> None:

        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()
        defaultParser0._handleConcatenatedOptions("")

    @pytest.mark.test
    def test31(self) -> None:

        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()
        options0 = Options()
        options1 = options0.addRequiredOption("", "", True, "")
        stringArray0 = [""] * 7
        stringArray0[0] = "--=-"
        stringArray0[1] = "--=-"
        stringArray0[2] = ""
        stringArray0[3] = ""
        stringArray0[4] = ""
        stringArray0[5] = ""
        stringArray0[6] = ""
        defaultParser0.parse0(options1, stringArray0)
        defaultParser0.handleConcatenatedOptions("=-")

    @pytest.mark.test
    def test30(self) -> None:

        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()
        options0 = Options()
        options0.addOption3("1", "1", True, "[ARG...]")
        stringArray0 = ["7DRQ", "g", "g", "--=-", "g", "--=-", "--=-", "--("]
        try:
            defaultParser0.parse0(options0, stringArray0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.DefaultParser", e)

    @pytest.mark.test
    def test29(self) -> None:

        options0 = Options()
        options0.addRequiredOption("g", "g", False, "g")
        stringArray0 = ["g", "--=-"]
        options0.addRequiredOption("g", "--=-", False, "g")
        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()
        try:
            defaultParser0.parse3(options0, stringArray0, None, False)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Ambiguous option: '--'  (could be: 'g', '--=-')
            #
            self.verifyException("org.apache.commons.cli.DefaultParser", e)

    @pytest.mark.test
    def test28(self) -> None:

        options0 = Options()
        options1 = options0.addRequiredOption("g", "g", False, "g")
        stringArray0 = ["g", "--=-"]
        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()
        try:
            defaultParser0.parse0(options1, stringArray0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.DefaultParser", e)

    @pytest.mark.test
    def test27(self) -> None:

        options0 = Options()
        stringArray0 = ["g", "---"]
        options0.addRequiredOption("g", "---", False, "g")
        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()

        try:
            defaultParser0.parse0(options0, stringArray0)
            self.fail("Expecting exception: NullPointerException")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.DefaultParser", e)

    @pytest.mark.test
    def test26(self) -> None:

        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()
        options0 = Options()
        properties0 = Properties(61)
        stringArray0 = [None] * 5
        stringArray0[0] = "-N979:{K%lDG'@&"
        commandLine0 = defaultParser0.parse3(options0, stringArray0, properties0, True)
        self.assertIsNotNone(commandLine0)

    @pytest.mark.test
    def test25(self) -> None:

        boolean0 = bool("}")
        defaultParser0 = DefaultParser(0, boolean0, False)
        options0 = Options()
        stringArray0 = ["org.apache.commons.cli.Options", "}"]
        properties0 = {}
        object0 = object()
        properties0["org.apache.commons.cli.Options"] = object0
        try:
            defaultParser0.parse3(options0, stringArray0, properties0, False)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Default option wasn't defined
            self.verifyException("org.apache.commons.cli.DefaultParser", e)

    @pytest.mark.test
    def test24(self) -> None:

        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()
        options0 = Options()
        stringArray0 = [None] * 6
        stringArray0[0] = "-,"
        defaultParser0.parse1(options0, stringArray0, True)
        defaultParser0.handleConcatenatedOptions("63;dMmT|IsY")

    @pytest.mark.test
    def test23(self) -> None:

        options0 = Options()
        stringArray0 = ["g", "-A=>"]
        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()
        try:
            defaultParser0.parse0(options0, stringArray0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Unrecognized option: -A=>
            self.verifyException("org.apache.commons.cli.DefaultParser", e)

    @pytest.mark.test
    def test22(self) -> None:

        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()
        options0 = Options()
        stringArray0 = ["--"]
        commandLine0 = defaultParser0.parse0(options0, stringArray0)
        self.assertIsNotNone(commandLine0)

    @pytest.mark.test
    def test21(self) -> None:

        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()
        options0 = Options()
        stringArray0 = ["-"]
        commandLine0 = defaultParser0.parse0(options0, stringArray0)
        self.assertIsNotNone(commandLine0)

    @pytest.mark.test
    def test20(self) -> None:

        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()
        options0 = Options()
        stringArray0 = [""] * 6
        optionGroup0 = OptionGroup()
        option0 = Option.Option1("", "-k")
        optionGroup1 = optionGroup0.addOption(option0)
        options1 = options0.addOptionGroup(optionGroup1)

        try:
            defaultParser0.parse0(options1, stringArray0)
            self.fail("Expecting exception: NullPointerException")

        except NullPointerException:
            pass

    @pytest.mark.test
    def test19(self) -> None:

        options0 = Options()
        options1 = options0.addRequiredOption("g", "g", True, "g")
        defaultParser_Builder0 = DefaultParser.builder()
        boolean0 = False
        defaultParser_Builder1 = (
            defaultParser_Builder0.setStripLeadingAndTrailingQuotes(boolean0)
        )
        defaultParser0 = defaultParser_Builder1.build()
        stringArray0 = ["g", "--=-"]
        commandLine0 = defaultParser0.parse1(options1, stringArray0, False)
        self.assertIsNotNone(commandLine0)

    @pytest.mark.test
    def test18(self) -> None:

        options0 = Options()
        options0.addRequiredOption("g", "g", True, "g")

        defaultParser_Builder0 = DefaultParser.builder()
        boolean0 = True
        defaultParser_Builder1 = (
            defaultParser_Builder0.setStripLeadingAndTrailingQuotes(boolean0)
        )
        defaultParser0 = defaultParser_Builder1.build()

        stringArray0 = ["g", "--=-"]
        properties0 = {}

        commandLine0 = defaultParser0.parse2(options0, stringArray0, properties0)

        self.assertIsNotNone(commandLine0)

    @pytest.mark.test
    def test17(self) -> None:

        boolean0 = True
        defaultParser0 = DefaultParser(1, boolean0, boolean0)

    @pytest.mark.test
    def test16(self) -> None:

        boolean0 = True
        defaultParser0 = DefaultParser(1871, True, boolean0)
        properties0 = {}
        options0 = Options()
        optionGroup0 = OptionGroup()
        option_Builder0 = Option.builder0()
        option0 = Option(
            -2473,
            "N979:{K%lDG'@&",
            "N979:{K%lDG'@&",
            "N979:{K%lDG'@&",
            True,
            option_Builder0,
        )
        optionGroup1 = optionGroup0.addOption(option0)
        options1 = options0.addOptionGroup(optionGroup1)
        stringArray0 = [None] * 2

        try:
            defaultParser0.parse3(options1, stringArray0, properties0, True)
            self.fail("Expecting exception: NullPointerException")

        except Exception as e:
            self.assertEqual(str(e), "")

    @pytest.mark.test
    def test15(self) -> None:

        boolean0 = bool("MBm]/B?xX")
        defaultParser0 = DefaultParser(1, boolean0, None)
        options0 = Options()
        properties0 = {}
        defaultParser0.parse3(options0, None, properties0, False)
        defaultParser0._checkRequiredOptions()

    @pytest.mark.test
    def test14(self) -> None:

        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()

        try:
            defaultParser0._checkRequiredOptions()
            self.fail("Expecting exception: MissingOptionException")

        except MissingOptionException.MissingOptionException1:
            pass

    @pytest.mark.test
    def test13(self) -> None:

        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()
        linkedList0 = []
        defaultParser0._expectedOpts = linkedList0
        linkedList0.append(defaultParser0)
        try:
            defaultParser0._checkRequiredOptions()
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Missing required option: org.apache.commons.cli.DefaultParser@2
            #
            self.verifyException("org.apache.commons.cli.MissingOptionException", e)

    @pytest.mark.test
    def test12(self) -> None:

        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()

        try:
            defaultParser0._handleConcatenatedOptions("-]")
            self.fail("Expecting exception: NullPointerException")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.DefaultParser", e)

    @pytest.mark.test
    def test11(self) -> None:

        defaultParser_Builder0 = DefaultParser.builder()
        options0 = Options()
        defaultParser0 = defaultParser_Builder0.build()
        stringArray0 = []
        defaultParser0.parse0(options0, stringArray0)
        try:
            defaultParser0._handleConcatenatedOptions("-x%u`,0D<8Y+{k<]~")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Unrecognized option: -x%u`,0D<8Y+{k<]~
            self.verifyException("org.apache.commons.cli.DefaultParser", e)

    @pytest.mark.test
    def test10(self) -> None:

        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()
        options0 = Options()
        stringArray0 = ["-=-"]

        with pytest.raises(StringIndexOutOfBoundsException):
            defaultParser0.parse0(options0, stringArray0)

    @pytest.mark.test
    def test09(self) -> None:

        options0 = Options()
        options1 = options0.addRequiredOption("g", "g", True, "g")
        stringArray0 = ["g", "--=-"]
        options0.addRequiredOption("g", "--=-", True, "g")
        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()
        try:
            defaultParser0.parse0(options1, stringArray0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.DefaultParser", e)

    @pytest.mark.test
    def test08(self) -> None:

        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()
        options0 = Options()
        stringArray0 = ["-=-"]

        with pytest.raises(StringIndexOutOfBoundsException):
            defaultParser0.parse1(options0, stringArray0, True)

    @pytest.mark.test
    def test07(self) -> None:

        options0 = Options()
        options0.addRequiredOption("g", "g", False, "g")
        stringArray0 = ["g", "--=-"]
        options1 = options0.addRequiredOption("g", "--=-", False, "g")
        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()
        try:
            defaultParser0.parse1(options1, stringArray0, False)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.DefaultParser", e)

    @pytest.mark.test
    def test06(self) -> None:

        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()
        options0 = Options()
        properties0 = {}
        properties0[defaultParser_Builder0] = options0

        try:
            defaultParser0.parse2(options0, None, properties0)
            self.fail("Expecting exception: ClassCastException")

        except ClassCastException as e:
            self.verifyException("java.util.Properties", e)

    @pytest.mark.test
    def test05(self) -> None:

        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()
        options0 = Options()
        properties0 = {}
        stringArray0 = [""]

        try:
            defaultParser0.parse2(options0, stringArray0, properties0)
            self.fail("Expecting exception: NullPointerException")

        except Exception as e:
            self.assertEqual(str(e), "")

    @pytest.mark.test
    def test04(self) -> None:

        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()
        options0 = Options()
        stringArray0 = ["-=-"]
        properties0 = {}

        with pytest.raises(StringIndexOutOfBoundsException):
            defaultParser0.parse2(options0, stringArray0, properties0)

    @pytest.mark.test
    def test03(self) -> None:

        options0 = Options()
        options0.addRequiredOption("g", "g", True, "g")
        stringArray0 = ["g", "--=-"]
        options1 = options0.addRequiredOption("g", "--=-", True, "g")
        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()
        properties0 = {}
        try:
            defaultParser0.parse2(options1, stringArray0, properties0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.DefaultParser", e)

    @pytest.mark.test
    def test02(self) -> None:

        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()
        options0 = Options()
        stringArray0 = []
        properties0 = {}
        function0 = lambda x: x
        properties0.setdefault(
            defaultParser_Builder0, function0(defaultParser_Builder0)
        )

        with pytest.raises(ClassCastException):
            defaultParser0.parse3(options0, stringArray0, properties0, False)
            verifyException("java.util.Properties", ClassCastException)

    @pytest.mark.test
    def test01(self) -> None:

        stringArray0 = ["-=-"]
        defaultParser0 = DefaultParser(0, False, None)
        options0 = Options()
        properties0 = {}

        try:
            defaultParser0.parse3(options0, stringArray0, properties0, False)
            self.fail("Expecting exception: StringIndexOutOfBoundsException")

        except StringIndexOutOfBoundsException:
            pass

    @pytest.mark.test
    def test00(self) -> None:

        boolean0 = bool("---N979:{K%lDG'@&")
        defaultParser0 = DefaultParser(1, False, boolean0)
        options0 = Options()
        properties0 = {}
        stringArray0 = [""] * 9
        stringArray0[0] = "---N979:{K%lDG'@&"
        commandLine0 = defaultParser0.parse3(options0, stringArray0, properties0, True)
        self.assertIsNotNone(commandLine0)
