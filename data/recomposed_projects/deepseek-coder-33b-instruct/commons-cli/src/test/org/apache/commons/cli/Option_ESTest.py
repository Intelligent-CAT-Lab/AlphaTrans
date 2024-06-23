from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.Option import *

# from src.main.org.apache.commons.cli.Option_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Option_ESTest(unittest.TestCase):

    @pytest.mark.test
    def test104(self) -> None:
        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.valueSeparator0()
        self.assertIs(option_Builder1, option_Builder0)

    @pytest.mark.test
    def test103(self) -> None:
        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.hasArg0()
        self.assertEqual(option_Builder1, option_Builder0)

    @pytest.mark.test
    def test102(self) -> None:
        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.required0()
        self.assertIs(option_Builder0, option_Builder1)

    @pytest.mark.test
    def test101(self) -> None:
        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.optionalArg(True)
        self.assertIs(option_Builder0, option_Builder1)

    @pytest.mark.test
    def test100(self) -> None:
        option_Builder0 = Option.builder1(None)
        option_Builder1 = option_Builder0.desc("")
        self.assertIs(option_Builder1, option_Builder0)

    @pytest.mark.test
    def test099(self) -> None:

        option_Builder0 = Option.builder1(None)
        option_Builder0.hasArgs()
        option0 = Option(-829, "1Ax(s", "fUX0x-z3rr3W", "", False, option_Builder0)
        boolean0 = option0.hasArg()
        self.assertTrue(boolean0)
        self.assertEqual(-2, option0.getArgs())

    @pytest.mark.test
    def test098(self) -> None:
        option_Builder0 = Option.builder0()
        class0 = object
        option_Builder1 = option_Builder0.type(class0)
        self.assertEqual(option_Builder0, option_Builder1)

    @pytest.mark.test
    def test097(self) -> None:

        option_Builder0 = Option.builder0()
        option0 = Option(
            -831, "", "", "org.apache.commons.cli.Option$Builder", True, option_Builder0
        )
        option0.getArgName()
        self.assertEqual(-1, option0.getArgs())

    @pytest.mark.test
    def test096(self) -> None:

        option0 = Option.Option1("", "")
        option0.setType1(None)
        option0.getType()
        self.assertFalse(option0.hasLongOpt())
        self.assertEqual(-1, option0.getArgs())

    @pytest.mark.test
    def test095(self) -> None:

        option0 = Option.Option2("", True, "")
        option0.getValuesList()
        self.assertEqual("\u0000", option0.getValueSeparator())
        self.assertFalse(option0.hasLongOpt())
        self.assertTrue(option0.hasArg())

    @pytest.mark.test
    def test094(self) -> None:

        option0 = Option.Option1(None, None)
        try:
            option0.getId()
            self.fail("Expecting exception: NullPointerException")

        except Exception as e:
            self.assertEqual(str(e), "")

    @pytest.mark.test
    def test093(self) -> None:

        option0 = Option.Option2("NO_ARGS_ALLOWED", False, "NO_ARGS_ALLOWED")
        option1 = option0.clone()
        self.assertFalse(option1.hasLongOpt())
        self.assertEqual(-1, option1.getArgs())
        self.assertIsNot(option1, option0)

    @pytest.mark.test
    def test092(self) -> None:

        option0 = Option.Option1("", "")
        option0.setDescription("")
        self.assertFalse(option0.hasLongOpt())
        self.assertEqual(-1, option0.getArgs())

    @pytest.mark.test
    def test091(self) -> None:

        option0 = Option.Option1("", "")
        boolean0 = option0.requiresArg()
        self.assertFalse(option0.hasLongOpt())
        self.assertEqual(-1, option0.getArgs())
        self.assertFalse(boolean0)

    @pytest.mark.test
    def test090(self) -> None:

        option0 = Option.Option1("", "")
        option0.clearValues()
        self.assertEqual(-1, option0.getArgs())
        self.assertFalse(option0.hasLongOpt())

    @pytest.mark.test
    def test089(self) -> None:

        option0 = Option.Option1("@", "@")
        int0 = option0.getArgs()
        self.assertEqual((-1), int0)
        self.assertFalse(option0.hasLongOpt())

    @pytest.mark.test
    def test088(self) -> None:

        option0 = Option.Option2(None, True, None)
        string0 = option0.getDescription()
        self.assertIsNone(string0)
        self.assertTrue(option0.hasArg())

    @pytest.mark.test
    def test087(self) -> None:

        option_Builder0 = Option.builder0()
        option0 = Option(-1, None, "", "", True, option_Builder0)
        boolean0 = option0.isRequired()
        self.assertEqual("0", option0.getValueSeparator())
        self.assertTrue(option0.hasArg())
        self.assertFalse(boolean0)
        self.assertFalse(option0.hasOptionalArg())

    @pytest.mark.test
    def test086(self) -> None:

        option0 = Option.Option2("NO_ARGS_ALLOWED", False, "NO_ARGS_ALLOWED")
        option0.hashCode()
        self.assertEqual((-1), option0.getArgs())
        self.assertFalse(option0.hasLongOpt())

    @pytest.mark.test
    def test085(self) -> None:

        option0 = Option.Option1("", "")
        string0 = option0.getLongOpt()
        self.assertIsNone(string0)
        self.assertEqual(-1, option0.getArgs())

    @pytest.mark.test
    def test084(self) -> None:

        option0 = Option.Option1("", "")
        try:
            option0.addValue("")
            self.fail("Expecting exception: NotImplementedError")

        except Exception as e:
            self.assertTrue(
                "The addValue method is not intended for client use. "
                + "Subclasses should use the addValueForProcessing method instead. "
                in str(e)
            )

    @pytest.mark.test
    def test083(self) -> None:

        option0 = Option.Option1("", "")
        option0.getType()
        self.assertFalse(option0.hasLongOpt())
        self.assertEqual(-1, option0.getArgs())

    @pytest.mark.test
    def test082(self) -> None:

        option0 = Option.Option2("NO_ARGS_ALLOWED", False, "NO_ARGS_ALLOWED")
        string0 = option0.getOpt()
        self.assertEqual(-1, option0.getArgs())
        self.assertFalse(option0.hasLongOpt())
        self.assertIsNotNone(string0)

    @pytest.mark.test
    def test081(self) -> None:

        option0 = Option.Option1("", "")
        self.assertFalse(option0.hasLongOpt())

        option0.setLongOpt("")
        string0 = option0.toString()
        self.assertEqual("[ option:    ::  :: class java.lang.String ]", string0)

    @pytest.mark.test
    def test080(self) -> None:

        option_Builder0 = Option.builder0()

        try:
            option_Builder0.build()
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.apache.commons.cli.Option$Builder", e)

    @pytest.mark.test
    def test079(self) -> None:

        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.longOpt("3I1")
        option0 = option_Builder1.build()

        self.assertEqual(-1, option0.getArgs())
        self.assertTrue(option0.hasLongOpt())

    @pytest.mark.test
    def test078(self) -> None:
        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.hasArg1(False)
        self.assertEqual(option_Builder0, option_Builder1)

    @pytest.mark.test
    def test077(self) -> None:

        option0 = Option.Option1("", "")
        option0.setOptionalArg(True)
        boolean0 = option0.acceptsArg()
        self.assertTrue(option0.hasOptionalArg())
        self.assertTrue(boolean0)

    @pytest.mark.test
    def test076(self) -> None:

        option0 = Option.Option2("f", True, "f")
        option0.addValueForProcessing("f")
        # Undeclared exception in Java code
        try:
            option0.addValueForProcessing("f")
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # Cannot add value, list full.
            self.assertEqual(str(e), "NO_ARGS_ALLOWED")

    @pytest.mark.test
    def test075(self) -> None:

        option0 = Option.Option1("z", "z")
        try:
            option0.addValueForProcessing("z")
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.assertEqual(str(e), "NO_ARGS_ALLOWED")

    @pytest.mark.test
    def test074(self) -> None:

        option0 = Option.Option2("", True, "")
        object0 = object()
        boolean0 = option0.equals(object0)
        self.assertEqual("\u0000", option0.getValueSeparator())
        self.assertFalse(option0.hasLongOpt())
        self.assertTrue(option0.hasArg())
        self.assertFalse(boolean0)

    @pytest.mark.test
    def test073(self) -> None:

        option0 = Option.Option1("Q", "Q")
        boolean0 = option0.equals(option0)
        self.assertTrue(boolean0)
        self.assertEqual(-1, option0.getArgs())
        self.assertFalse(option0.hasLongOpt())

    @pytest.mark.test
    def test072(self) -> None:

        option0 = Option.Option1("", "")
        option1 = Option.Option1("", "")
        boolean0 = option0.equals(option1)
        self.assertTrue(boolean0)
        self.assertFalse(option1.hasLongOpt())
        self.assertEqual(-1, option1.getArgs())

    @pytest.mark.test
    def test071(self) -> None:

        option0 = Option.Option2("", True, "")
        option_Builder0 = Option.builder1("")
        option_Builder0.longOpt("")
        option1 = option_Builder0.build()
        boolean0 = option0.equals(option1)
        self.assertFalse(boolean0)
        self.assertFalse(option0.hasValueSeparator())
        self.assertEqual(-1, option1.getArgs())
        self.assertTrue(option0.hasArg())
        self.assertTrue(option1.hasLongOpt())

    @pytest.mark.test
    def test070(self) -> None:

        option0 = Option.Option1("z", "z")
        option1 = Option.Option1("", "z")
        boolean0 = option1.equals(option0)
        self.assertEqual("z", option1.getDescription())
        self.assertEqual(-1, option1.getArgs())
        self.assertFalse(option1.hasLongOpt())
        self.assertFalse(boolean0)

    @pytest.mark.test
    def test069(self) -> None:

        option0 = Option.Option1("", "")
        try:
            option0.getId()
            self.fail("Expecting exception: StringIndexOutOfBoundsException")

        except StringIndexOutOfBoundsException:
            pass

    @pytest.mark.test
    def test068(self) -> None:

        option0 = Option.Option2("", True, "")
        self.assertTrue(option0.hasArg())

        option0.addValueForProcessing("")
        option0.getValue2("")
        self.assertFalse(option0.hasValueSeparator())
        self.assertFalse(option0.hasLongOpt())

    @pytest.mark.test
    def test067(self) -> None:

        option0 = Option.Option1("jdyw", "jdyw")
        string0 = option0.getValue2("jdyw")
        self.assertIsNotNone(string0)
        self.assertFalse(option0.hasLongOpt())
        self.assertEqual(-1, option0.getArgs())

    @pytest.mark.test
    def test066(self) -> None:

        option0 = Option.Option2("", True, "")
        option0.addValueForProcessing("")
        string0 = option0.getValue1(0)
        self.assertFalse(option0.hasLongOpt())
        self.assertIsNotNone(string0)
        self.assertFalse(option0.hasValueSeparator())

    @pytest.mark.test
    def test065(self) -> None:

        option0 = Option.Option2("NO_ARGS_ALLOWED", False, "NO_ARGS_ALLOWED")
        option0.getValue1(-1962)
        self.assertFalse(option0.hasLongOpt())
        self.assertEqual(-1, option0.getArgs())

    @pytest.mark.test
    def test064(self) -> None:

        option0 = Option.Option2("", True, "")
        option0.addValueForProcessing("")
        stringArray0 = option0.getValues()
        self.assertFalse(option0.hasLongOpt())
        self.assertIsNotNone(stringArray0)
        self.assertFalse(option0.hasValueSeparator())

    @pytest.mark.test
    def test063(self) -> None:

        option0 = Option.Option1("", "")
        stringArray0 = option0.getValues()
        self.assertIsNone(stringArray0)
        self.assertEqual(-1, option0.getArgs())
        self.assertFalse(option0.hasLongOpt())

    @pytest.mark.test
    def test062(self) -> None:

        option0 = Option.Option1(None, "")
        boolean0 = option0.hasArgName()
        self.assertEqual(-1, option0.getArgs())
        self.assertFalse(option0.hasLongOpt())
        self.assertFalse(boolean0)

    @pytest.mark.test
    def test061(self) -> None:

        option0 = Option.Option1("AB", "AB")
        option0.setArgName("AB")
        boolean0 = option0.hasArgName()
        self.assertTrue(boolean0)

    @pytest.mark.test
    def test060(self) -> None:

        option0 = Option.Option1("", "")
        option0.setArgName("")
        boolean0 = option0.hasArgName()
        self.assertFalse(boolean0)
        self.assertFalse(option0.hasLongOpt())
        self.assertEqual(-1, option0.getArgs())

    @pytest.mark.test
    def test059(self) -> None:

        option0 = Option.Option1("", "")
        option0.setArgs(63)
        boolean0 = option0.hasArgs()
        self.assertEqual(63, option0.getArgs())
        self.assertTrue(boolean0)

    @pytest.mark.test
    def test058(self) -> None:

        option0 = Option.Option1(None, "")
        self.assertFalse(option0.hasArgs())

        option0.setArgs(-2)
        option0.toString()
        self.assertEqual(-2, option0.getArgs())

    @pytest.mark.test
    def test057(self) -> None:

        option0 = Option.Option1("", "")
        boolean0 = option0.hasLongOpt()
        self.assertEqual(-1, option0.getArgs())
        self.assertFalse(boolean0)

    @pytest.mark.test
    def test056(self) -> None:

        option_Builder0 = Option.builder1(None)
        option_Builder0.longOpt("Cannot add value, list full.")
        option0 = Option(-2, "", "", "<IQ*JK", True, option_Builder0)
        boolean0 = option0.hasLongOpt()
        self.assertTrue(boolean0)
        self.assertEqual(-1, option0.getArgs())

    @pytest.mark.test
    def test055(self) -> None:

        option0 = Option.Option2("k", True, "The option '")
        option0.setValueSeparator("T")
        option0.addValueForProcessing("The option '")
        self.assertEqual("T", option0.getValueSeparator())

    @pytest.mark.test
    def test054(self) -> None:

        option0 = Option.Option1("zZ", "zZ")
        option0.setArgs((-2))
        option0.setValueSeparator("s")
        option0.addValueForProcessing("Either opt or longOpt must be specified")
        self.assertEqual("s", option0.getValueSeparator())

    @pytest.mark.test
    def test053(self) -> None:

        option0 = Option.Option1("", "")
        option0.setOptionalArg(True)
        boolean0 = option0.requiresArg()
        self.assertTrue(option0.hasOptionalArg())
        self.assertFalse(boolean0)

    @pytest.mark.test
    def test052(self) -> None:

        option0 = Option.Option1(None, "")
        self.assertFalse(option0.hasArgs())

        option0.setArgs(-2)
        boolean0 = option0.requiresArg()
        self.assertTrue(boolean0)

    @pytest.mark.test
    def test051(self) -> None:

        option0 = Option.Option1(None, "")
        self.assertFalse(option0.hasArgs())

        option0.setArgs(-2)
        option0.addValueForProcessing("")
        boolean0 = option0.requiresArg()
        self.assertFalse(boolean0)

    @pytest.mark.test
    def test050(self) -> None:

        option0 = Option.Option2("", True, "")
        string0 = option0.toString()
        self.assertEqual("[ option:   [ARG] ::  :: class java.lang.String ]", string0)

    @pytest.mark.test
    def test049(self) -> None:

        option0 = Option.Option1(None, None)
        option0.setType1(None)
        string0 = option0.toString()
        self.assertEqual("[ option: None  :: None ]", string0)
        self.assertEqual(-1, option0.getArgs())

    @pytest.mark.test
    def test048(self) -> None:

        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.option("")
        self.assertEqual(option_Builder1, option_Builder0)

    @pytest.mark.test
    def test047(self) -> None:

        option0 = Option.Option1("", "")
        option0.hasOptionalArg()
        self.assertEqual((-1), option0.getArgs())
        self.assertFalse(option0.hasLongOpt())

    @pytest.mark.test
    def test046(self) -> None:

        option_Builder0 = Option.builder1(None)
        option0 = Option(-2, "", "", "<IQ*JK", True, option_Builder0)
        class0 = object
        option0.setType0(class0)
        self.assertEqual(-1, option0.getArgs())

    @pytest.mark.test
    def test045(self) -> None:

        option_Builder0 = Option.builder0()
        option0 = Option(3233, "U:_drWoR", "", "C`", True, option_Builder0)
        char0 = option0.getValueSeparator()
        self.assertEqual(-1, option0.getArgs())
        self.assertEqual("\u0000", char0)

    @pytest.mark.test
    def test044(self) -> None:

        option_Builder0 = Option.builder0()
        option0 = None
        try:
            option0 = Option(
                0, "=ghNUw_.9yX?", "=ghNUw_.9yX?", "=ghNUw_.9yX?", True, option_Builder0
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # The option '=ghNUw_.9yX?' contains an illegal character : '='
            self.verifyException("org.apache.commons.cli.OptionValidator", e)

    @pytest.mark.test
    def test043(self) -> None:

        option_Builder0 = Option.builder0()
        option0 = Option(0, "MX", "", "", False, option_Builder0)
        self.assertEqual("MX", option0.getOpt())
        self.assertEqual("", option0.getLongOpt())
        self.assertEqual("", option0.getDescription())
        self.assertEqual(-1, option0.getArgs())

    @pytest.mark.test
    def test042(self) -> None:

        option_Builder0 = Option.builder0()
        option0 = Option(3233, "U:_drWoR", "", "C`", True, option_Builder0)
        option0.getValue0()
        self.assertEqual((-1), option0.getArgs())

    @pytest.mark.test
    def test041(self) -> None:

        option0 = Option.Option2("", False, "")
        self.assertFalse(option0.hasArg())

        option0.setArgs(1)
        option0.addValueForProcessing("")
        option0.getValue0()
        self.assertEqual(1, option0.getArgs())

    @pytest.mark.test
    def test040(self) -> None:

        option0 = Option.Option1("Q", "Q")
        boolean0 = option0.hasArg()
        self.assertFalse(boolean0)
        self.assertFalse(option0.hasLongOpt())
        self.assertEqual(-1, option0.getArgs())

    @pytest.mark.test
    def test039(self) -> None:

        option0 = Option.Option1("", "")
        option0.setArgs(6806)
        option0.hasArg()
        self.assertEqual(6806, option0.getArgs())

    @pytest.mark.test
    def test038(self) -> None:

        option0 = Option.Option1(None, "")
        self.assertEqual(-1, option0.getArgs())

        option0.setArgs(-2)
        boolean0 = option0.hasArgs()
        self.assertTrue(boolean0)

    @pytest.mark.test
    def test037(self) -> None:

        option0 = Option.Option1("", "")
        boolean0 = option0.hasArgs()
        self.assertFalse(boolean0)
        self.assertEqual(-1, option0.getArgs())
        self.assertFalse(option0.hasLongOpt())

    @pytest.mark.test
    def test036(self) -> None:

        option0 = Option.Option1("", "")
        boolean0 = option0.hasValueSeparator()
        self.assertFalse(option0.hasLongOpt())
        self.assertEqual(-1, option0.getArgs())
        self.assertFalse(boolean0)

    @pytest.mark.test
    def test035(self) -> None:

        option0 = Option.Option1("k", "k")
        option0.setValueSeparator("n")
        boolean0 = option0.hasValueSeparator()
        self.assertEqual("n", option0.getValueSeparator())
        self.assertTrue(boolean0)

    @pytest.mark.test
    def test034(self) -> None:

        option0 = None
        try:
            option0 = Option(
                868,
                "A CloneNotSupportedException was thrown: ",
                "A CloneNotSupportedException was thrown: ",
                "A CloneNotSupportedException was thrown: ",
                False,
                None,
            )
            self.fail("Expecting exception: NullPointerException")

        except NullPointerException as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("org.apache.commons.cli.Option$Builder", e)

    @pytest.mark.test
    def test033(self) -> None:

        try:
            Option.Option1("@ZfONsDKq", "@ZfONsDKq")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # The option '@ZfONsDKq' contains an illegal character : '@'
            self.verifyException("org.apache.commons.cli.OptionValidator", e)

    @pytest.mark.test
    def test032(self) -> None:

        try:
            Option.Option2(
                "org.apache.commons.cli.OptionValidator",
                False,
                "org.apache.commons.cli.OptionValidator",
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # The option 'org.apache.commons.cli.OptionValidator' contains an illegal character : '.'
            self.verifyException("org.apache.commons.cli.OptionValidator", e)

    @pytest.mark.test
    def test031(self) -> None:

        option0 = Option.Option2("4f", True, None)
        option0.setValueSeparator("F")
        try:
            option0.addValueForProcessing(None)
            self.fail("Expecting exception: NullPointerException")

        except Exception as e:
            self.assertEqual(str(type(e)), "<class 'NullPointerException'>")

    @pytest.mark.test
    def test030(self) -> None:

        try:
            Option.builder1(" ")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # Illegal option name ' '
            #
            self.verifyException("org.apache.commons.cli.OptionValidator", e)

    @pytest.mark.test
    def test029(self) -> None:

        option0 = Option.Option2("", True, "")
        option0.addValueForProcessing("")
        try:
            option0.getValue1(63)
            self.fail("Expecting exception: IndexOutOfBoundsException")

        except IndexError as e:
            pass

    @pytest.mark.test
    def test028(self) -> None:

        option0 = Option.Option1("", "")
        try:
            option0.setType1("")
            self.fail("Expecting exception: ClassCastException")

        except ClassCastException as e:
            self.verifyException("org.apache.commons.cli.Option", e)

    @pytest.mark.test
    def test027(self) -> None:

        option_Builder0 = Option.builder1("")
        option_Builder0.argName("")
        option0 = option_Builder0.build()
        string0 = option0.getArgName()
        assert string0 is not None
        self.assertEqual(-1, option0.getArgs())

    @pytest.mark.test
    def test026(self) -> None:

        option_Builder0 = Option.builder1("")
        option_Builder0.argName("The option '")
        option0 = Option(-63, "<IQ*JK", "", "^MYCq,IO%V<o[7g?$Q", True, option_Builder0)
        option0.getArgName()
        self.assertEqual(-1, option0.getArgs())

    @pytest.mark.test
    def test025(self) -> None:

        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.hasArg1(True)
        option0 = Option(
            -3246,
            "l9&+8x?q% A)bynyQ}:",
            "l9&+8x?q% A)bynyQ}:",
            "",
            True,
            option_Builder1,
        )
        int0 = option0.getArgs()
        self.assertEqual("\u0000", option0.getValueSeparator())
        self.assertEqual(1, int0)

    @pytest.mark.test
    def test024(self) -> None:

        option0 = Option.Option1("@", "@")
        self.assertEqual(-1, option0.getArgs())

        option0.setArgs(0)
        int0 = option0.getArgs()
        self.assertEqual(0, int0)

    @pytest.mark.test
    def test023(self) -> None:

        option0 = Option.Option1("", "")
        string0 = option0.getDescription()
        self.assertFalse(option0.hasLongOpt())
        self.assertIsNotNone(string0)
        self.assertEqual(-1, option0.getArgs())

    @pytest.mark.test
    def test022(self) -> None:

        option0 = Option.Option1("", "b>ROpA^diHY]s~")
        string0 = option0.getDescription()
        self.assertEqual(-1, option0.getArgs())
        self.assertFalse(option0.hasLongOpt())
        self.assertEqual("b>ROpA^diHY]s~", string0)
        self.assertIsNotNone(string0)

    @pytest.mark.test
    def test021(self) -> None:

        option0 = Option.Option2("I", True, "")
        self.assertEqual("\u0000", option0.getValueSeparator())

        option0.getId()
        self.assertEqual("", option0.getDescription())
        self.assertFalse(option0.hasLongOpt())

    @pytest.mark.test
    def test020(self) -> None:

        option0 = Option.Option1("", "")
        option0.getKey()
        self.assertFalse(option0.hasLongOpt())
        self.assertEqual(-1, option0.getArgs())

    @pytest.mark.test
    def test019(self) -> None:

        option_Builder0 = Option.builder1(None)
        option_Builder0.longOpt("Cannot add value, list full.")
        option0 = Option(-2, "", "", "<IQ*JK", True, option_Builder0)
        option0.getKey()
        self.assertEqual(-1, option0.getArgs())

    @pytest.mark.test
    def test018(self) -> None:

        option_Builder0 = Option.builder1(None)
        option0 = Option(-2, "", "", "<IQ*JK", True, option_Builder0)
        option0.getKey()
        self.assertEqual(-1, option0.getArgs())

    @pytest.mark.test
    def test017(self) -> None:

        option0 = Option.Option1("", "")
        self.assertFalse(option0.hasLongOpt())

        option0.setLongOpt("")
        option0.getLongOpt()
        self.assertEqual(-1, option0.getArgs())

    @pytest.mark.test
    def test016(self) -> None:

        option_Builder0 = Option.builder0()
        option0 = Option(0, "IRUuhDd", "@Mu~", "IRUuhDd", True, option_Builder0)
        string0 = option0.getLongOpt()
        self.assertEqual("IRUuhDd", option0.getDescription())
        self.assertEqual("@Mu~", string0)

    @pytest.mark.test
    def test015(self) -> None:

        option0 = Option.Option2("", True, "")
        option0.getOpt()
        self.assertFalse(option0.hasLongOpt())

    @pytest.mark.test
    def test014(self) -> None:

        option_Builder0 = Option.builder0()
        option0 = Option(3233, "U:_drWoR", "", "C`", True, option_Builder0)
        option0.getOpt()
        self.assertEqual((-1), option0.getArgs())

    @pytest.mark.test
    def test013(self) -> None:

        option0 = Option.Option2("", False, "")
        self.assertFalse(option0.hasArg())

        option0.setArgs(1)
        option0.addValueForProcessing("'")
        option0.getValue0()
        self.assertFalse(option0.hasValueSeparator())

    @pytest.mark.test
    def test012(self) -> None:

        option0 = Option.Option1("c", "c")
        self.assertFalse(option0.hasArgs())

        option0.setArgs(-2)
        option0.addValueForProcessing("c")
        option0.getValue1(0)
        self.assertTrue(option0.hasArg())

    @pytest.mark.test
    def test011(self) -> None:

        option_Builder0 = Option.builder0()
        option0 = Option(3233, "U:_drWoR", "", "C`", True, option_Builder0)
        option0.getValue2(None)
        self.assertEqual(-1, option0.getArgs())

    @pytest.mark.test
    def test010(self) -> None:

        option0 = Option.Option2("", False, "")
        option0.setValueSeparator("V")
        char0 = option0.getValueSeparator()
        self.assertEqual("V", char0)

    @pytest.mark.test
    def test009(self) -> None:

        option_Builder0 = Option.builder0()
        option0 = Option(-1, "|fn?HSat*", "", "", True, option_Builder0)
        char0 = option0.getValueSeparator()
        self.assertFalse(option0.hasOptionalArg())
        self.assertEqual("0", char0)
        self.assertFalse(option0.isRequired())
        self.assertEqual(1, option0.getArgs())

    @pytest.mark.test
    def test008(self) -> None:

        option0 = Option.Option2("", True, "")
        option0.addValueForProcessing("NzhRXN,?+/kI7")
        option0.getValuesList()
        self.assertFalse(option0.hasLongOpt())
        self.assertFalse(option0.hasValueSeparator())

    @pytest.mark.test
    def test007(self) -> None:

        option0 = Option.Option1("", "")
        option0.setOptionalArg(True)
        boolean0 = option0.hasOptionalArg()
        self.assertTrue(boolean0)

    @pytest.mark.test
    def test006(self) -> None:

        option0 = Option.Option2("", False, "")
        option0.setRequired(True)
        boolean0 = option0.isRequired()
        self.assertTrue(boolean0)

    @pytest.mark.test
    def test005(self) -> None:
        option_Builder0 = Option.builder1("")
        option_Builder1 = option_Builder0.required1(False)
        self.assertIs(option_Builder1, option_Builder0)

    @pytest.mark.test
    def test004(self) -> None:
        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.valueSeparator1("*")
        self.assertIs(option_Builder0, option_Builder1)

    @pytest.mark.test
    def test003(self) -> None:

        option0 = Option.Option2("", False, "")
        option0.setArgs(0)
        # Undeclared exception in Java code
        try:
            option0.addValueForProcessing("")
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # Cannot add value, list full.
            self.assertEqual(str(e), "NO_ARGS_ALLOWED")

    @pytest.mark.test
    def test002(self) -> None:

        option_Builder0 = Option.builder0()
        option_Builder0.numberOfArgs(-916)
        option0 = Option(1, "", "", "", True, option_Builder0)
        boolean0 = option0.acceptsArg()
        self.assertFalse(boolean0)
        self.assertEqual(-916, option0.getArgs())

    @pytest.mark.test
    def test001(self) -> None:

        option0 = Option.Option2("", False, "")
        option0.setArgs(447)
        option0.setValueSeparator("=")
        option0.addValueForProcessing('7p[ZV|="b:')
        self.assertEqual(447, option0.getArgs())

    @pytest.mark.test
    def test000(self) -> None:

        option_Builder0 = Option.builder0()
        option_Builder0.numberOfArgs(-916)
        option0 = Option(
            -916,
            "gOUhx",
            "Illegal option name '",
            "Illegal option name '",
            False,
            option_Builder0,
        )
        boolean0 = option0.requiresArg()
        self.assertFalse(boolean0)
        self.assertEqual(-916, option0.getArgs())
