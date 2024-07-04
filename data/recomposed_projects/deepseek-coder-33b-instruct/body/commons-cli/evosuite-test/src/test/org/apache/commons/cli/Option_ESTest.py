from __future__ import annotations
import time
import re
import os
import typing
from typing import *
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.Option import *

# from src.test.org.apache.commons.cli.Option_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Option_ESTest(unittest.TestCase):

    def test98(self) -> None:
        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.argName("R@@Zf5H#f1)Bzz")
        self.assertIs(option_Builder0, option_Builder1)

    def test97(self) -> None:
        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.valueSeparator0()
        self.assertIs(option_Builder0, option_Builder1)

    def test96(self) -> None:
        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.hasArg0()
        self.assertEqual(option_Builder0, option_Builder1)

    def test95(self) -> None:

        option_Builder0 = Option.builder0()
        option_Builder0.optionalArg(True)
        option_Builder0.longOpt("")
        option0 = option_Builder0.build()
        boolean0 = option0.hasOptionalArg()
        self.assertEqual(-1, option0.getArgs())
        self.assertTrue(boolean0)

    def test94(self) -> None:

        option_Builder0 = Option.builder0()
        option_Builder0.hasArgs()
        option0 = Option(7330, "7CLs[:", None, "f;3$8j#0IWpx:%", True, option_Builder0)
        option0.setValueSeparator(":")
        option0.addValueForProcessing("7CLs[:")
        self.assertEqual(":", option0.getValueSeparator())

    def test93(self) -> None:
        option_Builder0 = Option.builder0()
        class0 = object
        option_Builder1 = option_Builder0.type(class0)
        self.assertEqual(option_Builder1, option_Builder0)

    def test92(self) -> None:

        option0 = Option.Option2("", False, "LDE$IPc0Ine3waBb9x")
        option0.getArgName()
        self.assertEqual("LDE$IPc0Ine3waBb9x", option0.getDescription())
        self.assertFalse(option0.hasLongOpt())
        self.assertEqual(-1, option0.getArgs())
        self.assertEqual("", option0.getOpt())

    def test91(self) -> None:

        option0 = Option.Option1("6", "6")
        option0.setOptionalArg(True)
        boolean0 = option0.acceptsArg()
        self.assertTrue(option0.hasOptionalArg())
        self.assertTrue(boolean0)

    def test90(self) -> None:

        option0 = Option.Option1("X", "X")
        option0.setRequired(True)
        self.assertTrue(option0.isRequired())

    def test89(self) -> None:

        option0 = Option.Option1("", "")
        try:
            option0.setType1("")
            self.fail("Expecting exception: ClassCastException")

        except ClassCastException as e:
            self.verifyException("org.apache.commons.cli.Option", e)

    def test88(self) -> None:

        option0 = Option.Option1("", "")
        option0.getValuesList()
        self.assertEqual(-1, option0.getArgs())
        self.assertFalse(option0.hasLongOpt())

    def test87(self) -> None:

        option0 = Option.Option1(None, None)
        try:
            option0.getId()
            self.fail("Expecting exception: RuntimeError")
        except Exception as e:
            self.assertEqual(str(e), "")

    def test86(self) -> None:

        option0 = Option.Option1("", "")
        option1 = option0.clone()
        boolean0 = option0.equals(option1)
        self.assertIsNot(option1, option0)
        self.assertEqual(-1, option1.getArgs())
        self.assertTrue(boolean0)
        self.assertFalse(option1.hasLongOpt())

    def test85(self) -> None:

        option0 = Option.Option1("6", "6")
        option0.setArgName("6")
        boolean0 = option0.hasArgName()
        self.assertTrue(boolean0)

    def test84(self) -> None:

        option0 = Option.Option1("", "")
        option0.setDescription("")
        self.assertFalse(option0.hasLongOpt())
        self.assertEqual(-1, option0.getArgs())

    def test83(self) -> None:

        option0 = Option.Option1("", "")
        boolean0 = option0.requiresArg()
        self.assertFalse(boolean0)
        self.assertEqual(-1, option0.getArgs())
        self.assertFalse(option0.hasLongOpt())

    def test82(self) -> None:

        option0 = Option.Option1("X", "X")
        option0.clearValues()
        self.assertFalse(option0.hasLongOpt())
        self.assertEqual(-1, option0.getArgs())

    def test81(self) -> None:

        option0 = Option.Option1("", "")
        int0 = option0.getArgs()
        self.assertEqual(-1, int0)
        self.assertFalse(option0.hasLongOpt())

    def test80(self) -> None:

        option_Builder0 = Option.builder1("")
        option0 = Option(48, "", "", "g/SNMWkTVe|,Z$", False, option_Builder0)
        option0.getDescription()
        self.assertEqual((-1), option0.getArgs())

    def test79(self) -> None:

        option_Builder0 = Option.builder1("")
        option0 = Option(48, "", "", "g/SNMWkTVe|,Z$", False, option_Builder0)
        assert not option0.isRequired()
        assert option0.getArgs() == -1

    def test78(self) -> None:

        option0 = Option.Option2("", True, "")
        option0.hashCode()
        self.assertFalse(option0.hasLongOpt())
        self.assertEqual(1, option0.getArgs())
        self.assertFalse(option0.hasValueSeparator())

    def test77(self) -> None:

        option0 = Option(0, "", "", " [ARG]", True, None)
        string0 = option0.getLongOpt()
        self.assertEqual("", string0)
        self.assertEqual(" [ARG]", option0.getDescription())
        self.assertEqual(1, option0.getArgs())

    def test76(self) -> None:

        option0 = Option.Option1("X", "X")
        # Undeclared exception
        try:
            option0.addValue("X")
            self.fail("Expecting exception: NotImplementedError")

        except NotImplementedError as e:
            # The addValue method is not intended for client use. Subclasses should use the addValueForProcessing method instead.
            self.verifyException("org.apache.commons.cli.Option", e)

    def test75(self) -> None:

        option0 = Option.Option1("", "")
        string0 = option0.getOpt()
        self.assertEqual(-1, option0.getArgs())
        self.assertFalse(option0.hasLongOpt())
        self.assertIsNotNone(string0)

    def test74(self) -> None:

        option0 = Option.Option1("6", "6")
        class0 = Option
        option0.setType0(class0)
        self.assertEqual(-1, option0.getArgs())
        self.assertFalse(option0.hasLongOpt())

    def test73(self) -> None:

        option_Builder0 = Option.builder0()

        try:
            option_Builder0.build()
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.apache.commons.cli.Option$Builder", e)

    def test72(self) -> None:
        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.hasArg1(False)
        self.assertEqual(option_Builder1, option_Builder0)

    def test71(self) -> None:

        option0 = Option.Option2("", True, "")
        self.assertTrue(option0.hasArg())

        option0.addValueForProcessing("")
        string0 = option0.getValue1(0)
        self.assertIsNotNone(string0)
        self.assertFalse(option0.hasValueSeparator())
        self.assertFalse(option0.hasLongOpt())

    def test70(self) -> None:

        option0 = Option.Option2("", True, "")
        option0.addValueForProcessing(" [ARG]")
        boolean0 = option0.acceptsArg()
        self.assertFalse(option0.hasLongOpt())
        self.assertFalse(boolean0)
        self.assertFalse(option0.hasValueSeparator())

    def test69(self) -> None:

        option0 = Option.Option1("", "")
        # Undeclared exception in Java code
        try:
            option0.addValueForProcessing("")
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            #
            # NO_ARGS_ALLOWED
            #
            self.assertEqual(str(e), "NO_ARGS_ALLOWED")

    def test68(self) -> None:

        option0 = Option.Option2("", False, "{LDE$3Pc0Ine3wBb9")
        boolean0 = option0.equals(option0)
        self.assertEqual(-1, option0.getArgs())
        self.assertFalse(option0.hasLongOpt())
        self.assertEqual("{LDE$3Pc0Ine3wBb9", option0.getDescription())
        self.assertTrue(boolean0)

    def test67(self) -> None:

        option0 = Option.Option1("", "")
        boolean0 = option0.equals("")
        self.assertEqual(-1, option0.getArgs())
        self.assertFalse(option0.hasLongOpt())
        self.assertFalse(boolean0)

    def test66(self) -> None:

        option0 = Option.Option1("f6", "f6")
        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.longOpt("f6")
        option1 = option_Builder1.build()
        boolean0 = option0.equals(option1)
        self.assertTrue(option1.hasLongOpt())
        self.assertFalse(boolean0)
        self.assertFalse(option0.hasLongOpt())
        self.assertEqual(-1, option0.getArgs())
        self.assertEqual(-1, option1.getArgs())

    def test65(self) -> None:

        option0 = Option.Option1("", "")
        option1 = Option.Option1(None, "")
        boolean0 = option0.equals(option1)
        self.assertFalse(option0.hasLongOpt())
        self.assertEqual(-1, option1.getArgs())
        self.assertFalse(boolean0)

    def test64(self) -> None:

        option0 = Option.Option1("", "")
        # Undeclared exception
        try:
            option0.getId()
            self.fail("Expecting exception: StringIndexOutOfBoundsException")

        except StringIndexOutOfBoundsException:
            pass

    def test63(self) -> None:

        option0 = Option.Option2("", True, "")
        option0.addValueForProcessing(" [ARG]")
        string0 = option0.getValue2("")
        self.assertFalse(option0.hasLongOpt())
        self.assertEqual(" [ARG]", string0)
        self.assertFalse(option0.hasValueSeparator())

    def test62(self) -> None:

        option0 = Option.Option2("", True, "")
        string0 = option0.getValue2("")
        self.assertEqual("\u0000", option0.getValueSeparator())
        self.assertFalse(option0.hasLongOpt())
        self.assertIsNotNone(string0)

    def test61(self) -> None:

        option0 = Option(0, "", "", " [ARG]", True, None)
        option0.getValue1(63)
        self.assertEqual(" [ARG]", option0.getDescription())
        self.assertEqual("", option0.getLongOpt())

    def test60(self) -> None:

        option0 = Option.Option2("", True, "")
        option0.addValueForProcessing("")
        stringArray0 = option0.getValues()
        self.assertIsNotNone(stringArray0)
        self.assertFalse(option0.hasLongOpt())
        self.assertFalse(option0.hasValueSeparator())

    def test59(self) -> None:

        option0 = Option.Option2("", True, "")
        stringArray0 = option0.getValues()
        self.assertIsNone(stringArray0)
        self.assertFalse(option0.hasLongOpt())
        self.assertFalse(option0.hasValueSeparator())

    def test58(self) -> None:

        option0 = Option.Option1("6", "6")
        boolean0 = option0.hasArgName()
        self.assertEqual(-1, option0.getArgs())
        self.assertFalse(option0.hasLongOpt())
        self.assertFalse(boolean0)

    def test57(self) -> None:

        option0 = Option.Option1("", "")
        option0.setArgName("")
        boolean0 = option0.hasArgName()
        self.assertEqual(-1, option0.getArgs())
        self.assertFalse(option0.hasLongOpt())
        self.assertFalse(boolean0)

    def test56(self) -> None:

        option_Builder0 = Option.builder0()
        option_Builder0.hasArgs()
        option0 = Option(7330, "7CLs[:", None, "f;3$8j#0IWpx:%", True, option_Builder0)
        string0 = option0.toString()
        self.assertEqual(
            "[ option: None [ARG...] :: None :: class java.lang.String ]", string0
        )

    def test55(self) -> None:

        option0 = Option.Option2("", True, "")
        boolean0 = option0.hasLongOpt()
        self.assertFalse(boolean0)
        self.assertFalse(option0.hasValueSeparator())

    def test54(self) -> None:

        option0 = Option.Option1("", "")
        self.assertFalse(option0.hasLongOpt())

        option0.setLongOpt("~|}]x'8((y.$0R~Vpz")
        boolean0 = option0.hasLongOpt()
        self.assertTrue(boolean0)

    def test53(self) -> None:

        option0 = Option.Option2("", True, "")
        option0.setValueSeparator(":")
        option0.addValueForProcessing(
            "[ option:   [ARG] ::  :: class java.lang.String ]"
        )
        self.assertEqual(":", option0.getValueSeparator())

    def test52(self) -> None:

        option0 = Option.Option1("6", "6")
        option0.setOptionalArg(True)
        boolean0 = option0.requiresArg()
        self.assertTrue(option0.hasOptionalArg())
        self.assertFalse(boolean0)

    def test51(self) -> None:

        option_Builder0 = Option.builder1("")
        option_Builder1 = option_Builder0.hasArgs()
        option0 = option_Builder1.build()
        boolean0 = option0.requiresArg()
        self.assertTrue(boolean0)
        self.assertEqual(-2, option0.getArgs())

    def test50(self) -> None:

        option_Builder0 = Option.builder1("")
        option_Builder1 = option_Builder0.hasArgs()
        option0 = option_Builder1.build()
        option0.addValueForProcessing("")
        boolean0 = option0.requiresArg()
        self.assertFalse(boolean0)
        self.assertTrue(option0.hasArg())
        self.assertEqual(-2, option0.getArgs())
        self.assertFalse(option0.hasValueSeparator())

    def test49(self) -> None:

        option0 = Option.Option1("", "")
        self.assertFalse(option0.hasLongOpt())

        option0.setLongOpt("")
        string0 = option0.toString()
        self.assertEqual("[ option:    ::  :: class java.lang.String ]", string0)

    def test48(self) -> None:

        option_Builder0 = Option.builder0()
        option0 = Option(-1, "", "", "", False, option_Builder0)
        string0 = option0.toString()
        self.assertFalse(option0.isRequired())
        self.assertEqual("[ option: null  [ARG] ::  ]", string0)
        self.assertEqual("0", option0.getValueSeparator())
        self.assertFalse(option0.hasOptionalArg())

    def test47(self) -> None:

        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.option("")
        self.assertEqual(option_Builder1, option_Builder0)

    def test46(self) -> None:

        option_Builder0 = Option.builder0()
        option_Builder0.longOpt("")
        option0 = option_Builder0.build()
        option0.hasOptionalArg()
        self.assertEqual((-1), option0.getArgs())

    def test45(self) -> None:

        option0 = Option.Option2("", True, "")
        char0 = option0.getValueSeparator()
        self.assertFalse(option0.hasLongOpt())
        self.assertEqual("\u0000", char0)

    def test44(self) -> None:

        option0 = Option(0, "4Yl0", "4Yl0", "4Yl0", False, None)
        self.assertEqual(-1, option0.getArgs())

    def test43(self) -> None:

        option_Builder0 = Option.builder1("")
        option0 = Option(48, "", "", "g/SNMWkTVe|,Z$", False, option_Builder0)
        option0.getValue0()
        self.assertEqual((-1), option0.getArgs())

    def test42(self) -> None:

        option0 = Option.Option2("", True, "")
        option0.addValueForProcessing("")
        string0 = option0.getValue0()
        self.assertFalse(option0.hasLongOpt())
        self.assertIsNotNone(string0)
        self.assertFalse(option0.hasValueSeparator())

    def test41(self) -> None:

        option0 = Option.Option1("5l", "5l")
        boolean0 = option0.hasArg()
        self.assertFalse(boolean0)
        self.assertFalse(option0.hasLongOpt())
        self.assertEqual(-1, option0.getArgs())

    def test40(self) -> None:

        option_Builder0 = Option.builder0()
        option0 = Option(-1, "", "", "", True, option_Builder0)
        boolean0 = option0.hasArg()
        self.assertEqual("0", option0.getValueSeparator())
        self.assertTrue(boolean0)
        self.assertFalse(option0.hasOptionalArg())
        self.assertFalse(option0.isRequired())

    def test39(self) -> None:

        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.hasArgs()
        option0 = Option(1777, "", "", "", True, option_Builder1)
        boolean0 = option0.hasArg()
        self.assertTrue(boolean0)
        self.assertEqual(-2, option0.getArgs())

    def test38(self) -> None:

        option_Builder0 = Option.builder0()
        option_Builder0.longOpt("~wM:b")
        option_Builder1 = option_Builder0.hasArgs()
        option0 = option_Builder1.build()
        boolean0 = option0.hasArgs()
        self.assertTrue(boolean0)

    def test37(self) -> None:

        option_Builder0 = Option.builder0()
        option_Builder0.numberOfArgs(48)
        option0 = Option(48, "", "", "", False, option_Builder0)
        boolean0 = option0.hasArgs()
        self.assertTrue(boolean0)
        self.assertEqual(48, option0.getArgs())

    def test36(self) -> None:

        option0 = Option.Option1("w", "w")
        boolean0 = option0.hasArgs()
        self.assertEqual(-1, option0.getArgs())
        self.assertFalse(option0.hasLongOpt())
        self.assertFalse(boolean0)

    def test35(self) -> None:

        option0 = Option.Option1("", "")
        boolean0 = option0.hasValueSeparator()
        self.assertEqual(-1, option0.getArgs())
        self.assertFalse(boolean0)
        self.assertFalse(option0.hasLongOpt())

    def test34(self) -> None:

        option0 = Option.Option1("", "")
        option0.setValueSeparator("3")
        boolean0 = option0.hasValueSeparator()
        self.assertEqual("3", option0.getValueSeparator())
        self.assertTrue(boolean0)

    def test33(self) -> None:

        option0 = None
        try:
            option0 = Option(0, ">4", ">4", ">4", False, None)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # The option '>4' contains an illegal character : '>'
            self.verifyException("org.apache.commons.cli.OptionValidator", e)

    def test32(self) -> None:

        option0 = None
        try:
            option0 = Option(
                -3,
                "org.apache.commons.cli.OptionValidator",
                "org.apache.commons.cli.OptionValidator",
                "org.apache.commons.cli.OptionValidator",
                True,
                None,
            )
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("org.apache.commons.cli.Option$Builder", e)

    def test31(self) -> None:

        try:
            Option.Option1("P6UGMg;=r~{Ai9~r", "P6UGMg;=r~{Ai9~r")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # The option 'P6UGMg;=r~{Ai9~r' contains an illegal character : ';'
            self.verifyException("org.apache.commons.cli.OptionValidator", e)

    def test30(self) -> None:

        try:
            Option.Option2('m",{Wl:.*:', False, 'm",{Wl:.*:')
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # The option 'm\",{Wl:.*:' contains an illegal character : '\"'
            self.verifyException("org.apache.commons.cli.OptionValidator", e)

    def test29(self) -> None:

        option0 = Option.Option2(None, True, None)
        option0.setValueSeparator("I")

        try:
            option0.addValueForProcessing(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.Option", e)

    def test28(self) -> None:

        # Undeclared exception
        try:
            Option.builder1("*^5MS$s9`|cUF+VY")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # The option '*^5MS$s9`|cUF+VY' contains an illegal character : '*'
            self.verifyException("org.apache.commons.cli.OptionValidator", e)

    def test27(self) -> None:

        option0 = Option.Option2("", True, "")
        option0.addValueForProcessing("")
        try:
            option0.getValue1(2757)
            self.fail("Expecting exception: IndexOutOfBoundsException")

        except IndexError as e:
            pass

    def test26(self) -> None:

        option0 = Option.Option1("", ">}H/I`")
        option0.setArgName("")
        assert option0.getArgName() == ""
        assert not option0.hasLongOpt()
        assert option0.getArgs() == -1
        assert option0.getDescription() == ">}H/I`"

    def test25(self) -> None:

        option0 = Option.Option2("", False, "LDE$IPc0Ine3waBb9x")
        option0.setArgName("Illegal option name '")
        option0.getArgName()
        self.assertEqual("LDE$IPc0Ine3waBb9x", option0.getDescription())
        self.assertFalse(option0.hasLongOpt())
        self.assertEqual(-1, option0.getArgs())

    def test24(self) -> None:

        option_Builder0 = Option.builder0()
        option_Builder0.numberOfArgs(48)
        option0 = Option(48, "", "", "", False, option_Builder0)
        int0 = option0.getArgs()
        self.assertEqual(48, int0)

    def test23(self) -> None:

        option0 = Option.Option1("", "")
        string0 = option0.getDescription()
        self.assertEqual(-1, option0.getArgs())
        self.assertFalse(option0.hasLongOpt())
        self.assertIsNotNone(string0)

    def test22(self) -> None:

        option_Builder0 = Option.builder0()
        option_Builder0.desc("A CloneNotSupportedException was thrown: ")
        option0 = Option(
            -215,
            "A CloneNotSupportedException was thrown: ",
            "A CloneNotSupportedException was thrown: ",
            "A CloneNotSupportedException was thrown: ",
            False,
            option_Builder0,
        )
        option0.getDescription()
        self.assertEqual(-1, option0.getArgs())

    def test21(self) -> None:

        option_Builder0 = Option.builder1(None)
        option_Builder1 = option_Builder0.longOpt("Ul6P5;IM>9m,Q(Rv4")
        option0 = option_Builder1.build()
        int0 = option0.getId()
        self.assertEqual(85, int0)
        self.assertEqual(-1, option0.getArgs())

    def test20(self) -> None:

        option0 = Option.Option2("", False, "LDE$IPc0Ine3waBb9x")
        string0 = option0.getKey()
        self.assertFalse(option0.hasLongOpt())
        self.assertEqual(-1, option0.getArgs())
        self.assertIsNotNone(string0)
        self.assertEqual("LDE$IPc0Ine3waBb9x", option0.getDescription())

    def test19(self) -> None:

        option0 = Option.Option1("j", "")
        string0 = option0.getKey()
        self.assertEqual(-1, option0.getArgs())
        self.assertEqual("", option0.getDescription())
        self.assertFalse(option0.hasLongOpt())
        self.assertIsNotNone(string0)

    def test18(self) -> None:

        option_Builder0 = Option.builder0()
        option0 = Option(
            -664,
            "org.apache.commons.cli.Option$1",
            "org.apache.commons.cli.Option$1",
            "<u0;",
            True,
            option_Builder0,
        )
        option0.getKey()
        self.assertEqual(-1, option0.getArgs())

    def test17(self) -> None:

        option_Builder0 = Option.builder0()
        option_Builder0.longOpt("~wM:b")
        option0 = option_Builder0.build()
        option0.getLongOpt()
        self.assertEqual((-1), option0.getArgs())

    def test16(self) -> None:

        option0 = Option.Option1("", "")
        string0 = option0.getLongOpt()
        self.assertEqual(-1, option0.getArgs())
        self.assertIsNone(string0)

    def test15(self) -> None:

        option0 = Option.Option2("o7", False, "Kd")
        string0 = option0.getOpt()
        self.assertIsNotNone(string0)
        self.assertFalse(option0.hasLongOpt())
        self.assertEqual(-1, option0.getArgs())
        self.assertEqual("Kd", option0.getDescription())

    def test14(self) -> None:

        option_Builder0 = Option.builder1("")
        option0 = Option(-1, "", ">~DUr<`Nbfb/{,", "@;#u#<0I", False, option_Builder0)
        option0.getOpt()
        self.assertEqual("0", option0.getValueSeparator())
        self.assertFalse(option0.hasOptionalArg())
        self.assertFalse(option0.isRequired())
        self.assertEqual(1, option0.getArgs())

    def test13(self) -> None:

        option_Builder0 = Option.builder0()
        option0 = Option(-1, "", "", "", False, option_Builder0)
        self.assertEqual(option0.getType(), None)
        self.assertEqual(option0.getValueSeparator(), "0")
        self.assertFalse(option0.isRequired())
        self.assertFalse(option0.hasOptionalArg())
        self.assertEqual(option0.getArgs(), 1)

    def test12(self) -> None:

        option0 = Option.Option2("", True, "")
        option0.addValueForProcessing(";mn#dgl4w341i3y1q?F")
        string0 = option0.getValue0()
        self.assertFalse(option0.hasValueSeparator())
        self.assertIsNotNone(string0)
        self.assertFalse(option0.hasLongOpt())

    def test11(self) -> None:

        option0 = Option.Option2("", True, "")
        option0.addValueForProcessing(
            "[ option:   [ARG] ::  :: class java.lang.String ]"
        )
        string0 = option0.getValue1(0)
        self.assertFalse(option0.hasLongOpt())
        self.assertFalse(option0.hasValueSeparator())
        self.assertIsNotNone(string0)

    def test10(self) -> None:

        option0 = Option.Option2("", True, "")
        option0.getValue2(None)
        self.assertFalse(option0.hasLongOpt())
        self.assertFalse(option0.hasValueSeparator())

    def test09(self) -> None:

        option0 = Option.Option2("", True, "")
        option0.setValueSeparator("y")
        char0 = option0.getValueSeparator()
        self.assertEqual("y", char0)

    def test08(self) -> None:

        option0 = Option.Option2("", True, None)
        option0.setValueSeparator("3")
        char0 = option0.getValueSeparator()
        self.assertEqual("3", char0)

    def test07(self) -> None:

        option0 = Option.Option2("", True, "")
        option0.addValueForProcessing("")
        option0.getValuesList()
        self.assertFalse(option0.hasValueSeparator())
        self.assertFalse(option0.hasLongOpt())

    def test06(self) -> None:

        option_Builder0 = Option.builder1("")
        option_Builder1 = option_Builder0.required0()
        option0 = Option(48, "", "", "g/SNMWkTVe|,Z$", False, option_Builder1)
        boolean0 = option0.isRequired()
        self.assertTrue(boolean0)
        self.assertEqual(-1, option0.getArgs())

    def test05(self) -> None:

        option0 = Option.Option1("", "")
        object0 = option0.getType()
        option0.setType1(object0)
        self.assertFalse(option0.hasLongOpt())
        self.assertEqual(-1, option0.getArgs())

    def test04(self) -> None:
        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.required1(False)
        self.assertEqual(option_Builder1, option_Builder0)

    def test03(self) -> None:
        option_Builder0 = Option.builder1("")
        option_Builder1 = option_Builder0.valueSeparator1(",")
        self.assertIs(option_Builder0, option_Builder1)

    def test02(self) -> None:

        option_Builder0 = Option.builder1("")
        option_Builder0.numberOfArgs(0)
        option0 = Option(-166, "mnWdglww341i3yRq?F", None, "", True, option_Builder0)

        try:
            option0.addValueForProcessing("")
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.apache.commons.cli.Option", e)

    def test01(self) -> None:

        option0 = Option.Option2("", True, "")
        option0.setValueSeparator("y")
        option0.setArgs(121)
        option0.addValueForProcessing(";mn#dgl4w341i3y1q?F")
        self.assertEqual(121, option0.getArgs())

    def test00(self) -> None:

        option_Builder0 = Option.builder0()
        option0 = Option(
            -266,
            "\!#\)\~\^\=7Qj1M\:\:N\`x",
            'O5"EO5B9F\:4<A',
            "8",
            True,
            option_Builder0,
        )
        option0.setArgs(-266)
        boolean0 = option0.requiresArg()
        self.assertEqual(-266, option0.getArgs())
        self.assertFalse(boolean0)
