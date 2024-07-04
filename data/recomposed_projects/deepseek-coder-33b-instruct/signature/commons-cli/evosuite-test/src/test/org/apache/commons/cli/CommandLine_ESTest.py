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
from src.main.org.apache.commons.cli.CommandLine import *

# from src.test.org.apache.commons.cli.CommandLine_ESTest_scaffolding import *
from src.main.org.apache.commons.cli.Option import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class CommandLine_ESTest(unittest.TestCase):

    def test76(self) -> None:
        commandLine_Builder0 = Builder()
        commandLine0 = commandLine_Builder0.build()
        boolean0 = commandLine0.hasOption0("L")
        self.assertFalse(boolean0)

    def test75(self) -> None:
        commandLine_Builder0 = Builder()
        commandLine0 = commandLine_Builder0.build()
        iterator0 = commandLine0.iterator()
        assert iterator0 is not None

    def test74(self) -> None:
        commandLine0 = CommandLine()
        list0 = commandLine0.getArgList()
        self.assertTrue(len(list0) == 0)

    def test73(self) -> None:

        commandLine_Builder0 = Builder()
        commandLine0 = commandLine_Builder0.build()
        string0 = commandLine0.getOptionValue1("/", "<d\rCWue")
        self.assertEqual("<d\rCWue", string0)
        self.assertIsNotNone(string0)

    def test72(self) -> None:
        commandLine_Builder0 = Builder()
        commandLine0 = commandLine_Builder0.build()
        object0 = commandLine0.getParsedOptionValue0("F")
        self.assertIsNone(object0)

    def test71(self) -> None:
        commandLine_Builder0 = Builder()
        commandLine0 = commandLine_Builder0.build()
        string0 = commandLine0.getOptionValue0("7")
        self.assertIsNone(string0)

    def test70(self) -> None:
        commandLine0 = CommandLine()
        optionArray0 = commandLine0.getOptions()
        self.assertEqual(0, len(optionArray0))

    def test69(self) -> None:
        commandLine_Builder0 = Builder()
        commandLine0 = commandLine_Builder0.build()
        stringArray0 = commandLine0.getArgs()
        self.assertEqual(0, len(stringArray0))

    def test68(self) -> None:
        commandLine0 = CommandLine()
        object0 = commandLine0.getOptionObject0("\u001F")
        self.assertIsNone(object0)

    def test67(self) -> None:

        commandLine_Builder0 = Builder()
        option0 = Option.Option1("Y", "Y")
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()
        properties0 = commandLine0.getOptionProperties0(None)
        self.assertIsNotNone(properties0)

    def test66(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.valueSeparator0()
        option_Builder1.longOpt("P z=Y")
        option_Builder1.hasArgs()
        option0 = option_Builder1.build()
        commandLine_Builder0.addOption(option0)
        option0.addValueForProcessing("P z=Y")
        commandLine0 = commandLine_Builder0.build()
        properties0 = commandLine0.getOptionProperties0(option0)
        self.assertIsNotNone(properties0)

    def test65(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.hasArg0()
        option_Builder1.longOpt("P z=Y")
        option0 = option_Builder1.build()
        commandLine_Builder0.addOption(option0)
        option0.addValueForProcessing("P z=Y")
        commandLine0 = commandLine_Builder0.build()
        properties0 = commandLine0.getOptionProperties0(option0)
        self.assertIsNotNone(properties0)

    def test64(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder1("Y")
        option0 = option_Builder0.build()
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()
        properties0 = commandLine0.getOptionProperties1("Y")
        self.assertIsNotNone(properties0)

    def test63(self) -> None:

        commandLine_Builder0 = Builder()
        option0 = Option.Option1("", "")
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()
        properties0 = commandLine0.getOptionProperties1("{4")
        self.assertIsNotNone(properties0)

    def test62(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.valueSeparator0()
        option_Builder1.longOpt("P z=Y")
        option_Builder0.hasArgs()
        option0 = option_Builder1.build()
        commandLine_Builder0.addOption(option0)
        option0.addValueForProcessing("P z=Y")
        commandLine0 = commandLine_Builder0.build()
        properties0 = commandLine0.getOptionProperties1("P z=Y")
        self.assertIsNotNone(properties0)

    def test61(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder1("Y")
        option_Builder1 = option_Builder0.hasArg0()
        option0 = option_Builder1.build()
        commandLine_Builder0.addOption(option0)
        option0.addValueForProcessing("Y")
        commandLine0 = commandLine_Builder0.build()
        properties0 = commandLine0.getOptionProperties1("Y")
        self.assertIsNotNone(properties0)

    def test60(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder0()
        option_Builder0.longOpt("P z=Y")
        option0 = option_Builder0.build()
        commandLine0 = commandLine_Builder0.build()
        object0 = commandLine0.getParsedOptionValue1(option0)
        self.assertIsNone(object0)

    def test59(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.hasArg0()
        option_Builder1.longOpt("P z=Y")
        option0 = option_Builder1.build()
        commandLine_Builder0.addOption(option0)
        option0.addValueForProcessing("P z=Y")
        commandLine0 = commandLine_Builder0.build()
        object0 = commandLine0.getParsedOptionValue1(option0)
        self.assertEqual("P z=Y", object0)

    def test58(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder1("Y")
        option_Builder1 = option_Builder0.hasArg0()
        option0 = option_Builder1.build()
        commandLine_Builder0.addOption(option0)
        option0.addValueForProcessing("Y")
        commandLine0 = commandLine_Builder0.build()
        string0 = commandLine0.getOptionValue5("Y", "Y")
        self.assertEqual("Y", string0)

    def test57(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder0()
        option_Builder0.longOpt("Y")
        option0 = option_Builder0.build()
        commandLine_Builder1 = commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder1.build()
        stringArray0 = commandLine0.getOptionValues0("L")
        self.assertIsNone(stringArray0)

    def test56(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.longOpt("Y")
        option0 = option_Builder1.build()
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()
        boolean0 = commandLine0.hasOption1(option0)
        self.assertTrue(boolean0)

    def test55(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder0()
        option_Builder0.longOpt("P z=Y")
        option0 = option_Builder0.build()
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()
        stringArray0 = commandLine0.getOptionValues2("P z=Y")
        self.assertIsNone(stringArray0)

    def test54(self) -> None:
        commandLine_Builder0 = Builder()
        commandLine0 = commandLine_Builder0.build()
        object0 = commandLine0.getParsedOptionValue2(" $ip")
        self.assertIsNone(object0)

    def test53(self) -> None:
        commandLine_Builder0 = Builder()
        commandLine0 = commandLine_Builder0.build()
        boolean0 = commandLine0.hasOption2('oBl{"?:$tOSy')
        self.assertFalse(boolean0)

    def test52(self) -> None:
        commandLine0 = CommandLine()
        string0 = commandLine0.getOptionValue4("i}m6]H")
        self.assertIsNone(string0)

    def test51(self) -> None:
        commandLine_Builder0 = Builder()
        commandLine0 = commandLine_Builder0.build()
        string0 = commandLine0.getOptionValue2(None)
        self.assertIsNone(string0)

    def test50(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder1("")
        option0 = option_Builder0.build()
        commandLine0 = commandLine_Builder0.build()
        string0 = commandLine0.getOptionValue2(option0)
        self.assertIsNone(string0)

    def test49(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder1("")
        option_Builder1 = option_Builder0.hasArg0()
        option0 = option_Builder1.build()
        commandLine_Builder1 = commandLine_Builder0.addOption(option0)
        option0.addValueForProcessing("")
        commandLine0 = commandLine_Builder1.build()
        string0 = commandLine0.getOptionValue2(option0)
        self.assertEqual("", string0)

    def test48(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.hasArg0()
        option_Builder0.option("Y")
        option0 = option_Builder1.build()
        commandLine_Builder1 = commandLine_Builder0.addOption(option0)
        option0.addValueForProcessing("w[p;")
        commandLine0 = commandLine_Builder1.build()
        string0 = commandLine0.getOptionValue3(option0, "AO5awyh8i6aR{9hp")
        self.assertEqual("w[p;", string0)

    def test47(self) -> None:

        commandLine_Builder0 = Builder()
        commandLine_Builder0.addOption(None)
        commandLine0 = commandLine_Builder0.build()

        try:
            commandLine0.getOptionValues1(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.CommandLine", e)

    def test46(self) -> None:

        commandLine_Builder0 = Builder()
        option0 = Option.Option1(None, None)
        commandLine_Builder1 = commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder1.build()
        stringArray0 = commandLine0.getOptionValues1(None)
        self.assertIsNone(stringArray0)

    def test45(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder1("Y")
        option_Builder1 = option_Builder0.hasArg0()
        option0 = option_Builder1.build()
        commandLine_Builder0.addOption(option0)
        option0.addValueForProcessing("Y")
        commandLine0 = commandLine_Builder0.build()
        stringArray0 = commandLine0.getOptionValues1(option0)
        self.assertEqual(len(stringArray0), 1)

    def test44(self) -> None:
        commandLine0 = CommandLine()
        object0 = commandLine0.getParsedOptionValue1(None)
        self.assertIsNone(object0)

    def test43(self) -> None:

        commandLine0 = CommandLine()
        option0 = CommandLine.Option1("", None)
        boolean0 = commandLine0.hasOption1(option0)
        self.assertFalse(boolean0)

    def test42(self) -> None:

        commandLine0 = CommandLine()
        commandLine0._addOption(None)

        try:
            commandLine0.getOptionObject0("\u001F")
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.cli.CommandLine", e)

    def test41(self) -> None:

        commandLine_Builder0 = Builder()
        option0 = Option.Option1("Y", "Y")
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()

        try:
            commandLine0.getOptionObject1(None)
            self.fail("Expecting exception: RuntimeError")

        except TypeError as e:
            pass

    def test40(self) -> None:

        commandLine_Builder0 = Builder()
        commandLine_Builder1 = commandLine_Builder0.addOption(None)
        commandLine0 = commandLine_Builder1.build()

        try:
            commandLine0.getOptionProperties0(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.CommandLine", e)

    def test39(self) -> None:

        commandLine_Builder0 = Builder()
        commandLine_Builder1 = commandLine_Builder0.addOption(None)
        commandLine0 = commandLine_Builder1.build()

        try:
            commandLine0.getOptionProperties1("Exception found converting ")
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.CommandLine", e)

    def test38(self) -> None:

        commandLine_Builder0 = Builder()
        commandLine_Builder1 = commandLine_Builder0.addOption(None)
        commandLine0 = commandLine_Builder1.build()

        with pytest.raises(RuntimeError):
            commandLine0.getOptionValue0("f")

    def test37(self) -> None:

        commandLine_Builder0 = Builder()
        commandLine_Builder1 = commandLine_Builder0.addOption(None)
        commandLine0 = commandLine_Builder1.build()

        try:
            commandLine0.getOptionValue1("c", 'IhF" _O%X')
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.cli.CommandLine", e)

    def test36(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        commandLine_Builder0.addOption(None)
        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.longOpt("Y")
        option0 = option_Builder1.build()
        commandLine0 = commandLine_Builder0.build()

        try:
            commandLine0.getOptionValue2(option0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.CommandLine", e)

    def test35(self) -> None:

        commandLine_Builder0 = Builder()
        option0 = Option.Option1(None, None)
        commandLine_Builder1 = commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder1.build()

        with pytest.raises(RuntimeError):
            commandLine0.getOptionValue4(None)

    def test34(self) -> None:

        commandLine_Builder0 = Builder()
        option0 = Option.Option1(
            "Y", "[ option: null   [ARG] :: null :: class java.lang.Object ]"
        )
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()

        try:
            commandLine0.getOptionValue5(None, ".")
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            pass

    def test33(self) -> None:

        commandLine_Builder0 = Builder()
        commandLine_Builder1 = commandLine_Builder0.addOption(None)
        commandLine0 = commandLine_Builder1.build()

        with self.assertRaises(RuntimeError):
            commandLine0.getOptionValues0("7")

    def test32(self) -> None:

        commandLine_Builder0 = Builder()
        commandLine_Builder0.addOption(None)
        commandLine0 = commandLine_Builder0.build()

        try:
            commandLine0.getOptionValues2("u_^lb~8=xM>%5")
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.cli.CommandLine", e)

    def test31(self) -> None:

        commandLine_Builder0 = Builder()
        commandLine_Builder1 = commandLine_Builder0.addOption(None)
        commandLine0 = commandLine_Builder1.build()

        with pytest.raises(RuntimeError):
            commandLine0.getParsedOptionValue0("")
            self.fail("Expecting exception: RuntimeError")

        self.verifyException("org.apache.commons.cli.CommandLine", RuntimeError)

    def test30(self) -> None:

        commandLine_Builder0 = Builder()
        commandLine_Builder0.addOption(None)
        option0 = Option.Option1("Y", "Y")
        commandLine0 = commandLine_Builder0.build()

        try:
            commandLine0.getParsedOptionValue1(option0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.CommandLine", e)

    def test29(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.hasArg0()
        option_Builder1.type(Option)
        option_Builder1.longOpt("P z=Y")
        option0 = option_Builder0.build()
        commandLine_Builder1 = commandLine_Builder0.addOption(option0)
        option0.addValueForProcessing("P z=Y")
        commandLine0 = commandLine_Builder1.build()
        try:
            commandLine0.getParsedOptionValue1(option0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.TypeHandler", e)

    def test28(self) -> None:

        commandLine_Builder0 = Builder()
        option0 = Option.Option1("Y", "Y")
        commandLine_Builder1 = commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder1.build()

        try:
            commandLine0.getParsedOptionValue2(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "Expecting exception: RuntimeError")

    def test27(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder1("Y")
        option_Builder1 = option_Builder0.hasArg0()
        option_Builder0.type(Option)
        option0 = option_Builder1.build()
        commandLine_Builder1 = commandLine_Builder0.addOption(option0)
        option0.addValueForProcessing("w[p;")
        commandLine0 = commandLine_Builder1.build()
        try:
            commandLine0.getParsedOptionValue2("Y")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.TypeHandler", e)

    def test26(self) -> None:

        commandLine_Builder0 = Builder()
        commandLine_Builder1 = commandLine_Builder0.addOption(None)
        commandLine0 = commandLine_Builder1.build()

        with self.assertRaises(RuntimeError):
            commandLine0.hasOption0("+")

    def test25(self) -> None:

        commandLine_Builder0 = Builder()
        commandLine_Builder1 = commandLine_Builder0.addOption(None)
        commandLine0 = commandLine_Builder1.build()

        try:
            commandLine0.hasOption2('oBl{"?:$tOSy')
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.apache.commons.cli.CommandLine", e)

    def test24(self) -> None:
        commandLine_Builder0 = Builder()
        commandLine_Builder1 = commandLine_Builder0.addArg("")
        commandLine0 = commandLine_Builder1.build()
        list0 = commandLine0.getArgList()
        self.assertEqual(1, len(list0))

    def test23(self) -> None:
        commandLine_Builder0 = Builder()
        commandLine_Builder1 = commandLine_Builder0.addArg("7")
        commandLine0 = commandLine_Builder1.build()
        stringArray0 = commandLine0.getArgs()
        self.assertEqual(1, len(stringArray0))

    def test22(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder0()
        option_Builder0.hasArg0()
        option_Builder0.longOpt("Y")
        option0 = option_Builder0.build()
        commandLine_Builder1 = commandLine_Builder0.addOption(option0)
        option0.addValueForProcessing("Y")
        commandLine0 = commandLine_Builder1.build()
        object0 = commandLine0.getOptionObject1("Y")
        self.assertEqual("Y", object0)

    def test21(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder1("Y")
        option_Builder1 = option_Builder0.hasArg0()
        option0 = option_Builder1.build()
        commandLine_Builder0.addOption(option0)
        option0.addValueForProcessing("Y")
        commandLine0 = commandLine_Builder0.build()
        string0 = commandLine0.getOptionValue0("Y")
        self.assertEqual("Y", string0)

    def test20(self) -> None:

        commandLine_Builder0 = Builder()
        commandLine0 = commandLine_Builder0.build()
        string0 = commandLine0.getOptionValue1("5", "")
        assert string0 is not None
        assert string0 == ""

    def test19(self) -> None:
        commandLine0 = CommandLine()
        string0 = commandLine0.getOptionValue1("9", None)
        self.assertIsNone(string0)

    def test18(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder0()
        option_Builder0.hasArg0()
        option_Builder0.longOpt("Y")
        option0 = option_Builder0.build()
        commandLine_Builder1 = commandLine_Builder0.addOption(option0)
        option0.addValueForProcessing("Y")
        commandLine0 = commandLine_Builder1.build()
        string0 = commandLine0.getOptionValue2(option0)
        self.assertEqual("Y", string0)

    def test17(self) -> None:

        option_Builder0 = Option.builder0()
        option_Builder0.longOpt("")
        option0 = option_Builder0.build()
        commandLine0 = CommandLine()
        string0 = commandLine0.getOptionValue3(option0, "")
        self.assertEqual("", string0)

    def test16(self) -> None:

        commandLine_Builder0 = Builder()
        option0 = Option.Option1(None, None)
        commandLine0 = commandLine_Builder0.build()
        string0 = commandLine0.getOptionValue3(option0, None)
        self.assertIsNone(string0)

    def test15(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder1("")
        option_Builder1 = option_Builder0.hasArg0()
        option0 = option_Builder1.build()
        commandLine_Builder1 = commandLine_Builder0.addOption(option0)
        option0.addValueForProcessing("")
        commandLine0 = commandLine_Builder1.build()
        string0 = commandLine0.getOptionValue4("")
        self.assertEqual("", string0)

    def test14(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.hasArg0()
        option_Builder0.longOpt("Y")
        option0 = option_Builder1.build()
        commandLine_Builder1 = commandLine_Builder0.addOption(option0)
        option0.addValueForProcessing("Y")
        commandLine0 = commandLine_Builder1.build()
        string0 = commandLine0.getOptionValue4("Y")
        self.assertEqual("Y", string0)

    def test13(self) -> None:

        commandLine0 = CommandLine()
        string0 = commandLine0.getOptionValue5("Jpx]bJzR{{bhe$]Si", "")
        self.assertEqual(string0, "")
        self.assertIsNotNone(string0)

    def test12(self) -> None:
        commandLine0 = CommandLine()
        string0 = commandLine0.getOptionValue5(None, None)
        self.assertIsNone(string0)

    def test11(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder1("Y")
        option_Builder1 = option_Builder0.hasArg0()
        option0 = option_Builder1.build()
        commandLine_Builder0.addOption(option0)
        option0.addValueForProcessing("Y")
        commandLine0 = commandLine_Builder0.build()
        stringArray0 = commandLine0.getOptionValues0("Y")
        self.assertEqual(1, len(stringArray0))

    def test10(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder1("Y")
        option_Builder1 = option_Builder0.hasArg0()
        option0 = option_Builder1.build()
        commandLine_Builder0.addOption(option0)
        option0.addValueForProcessing("Y")
        commandLine0 = commandLine_Builder0.build()
        stringArray0 = commandLine0.getOptionValues2("Y")
        self.assertEqual(len(stringArray0), 1)

    def test09(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.longOpt("")
        option0 = option_Builder1.build()
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()
        optionArray0 = commandLine0.getOptions()
        self.assertEqual(1, len(optionArray0))

    def test08(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder0()
        option_Builder0.longOpt(" $ip")
        option_Builder1 = option_Builder0.hasArg0()
        option0 = option_Builder1.build()
        commandLine_Builder0.addOption(option0)
        option0.addValueForProcessing(" $ip")
        commandLine0 = commandLine_Builder0.build()
        object0 = commandLine0.getParsedOptionValue2(" $ip")
        self.assertEqual(" $ip", object0)

    def test07(self) -> None:

        commandLine_Builder0 = Builder()
        option0 = Option.Option1("Y", "Y")
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()
        boolean0 = commandLine0.hasOption0("Y")
        self.assertTrue(boolean0)

    def test06(self) -> None:

        commandLine_Builder0 = Builder()
        option0 = Option.Option1("Y", "Y")
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()
        boolean0 = commandLine0.hasOption2("Y")
        self.assertTrue(boolean0)

    def test05(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.hasArg0()
        option_Builder1.type(Option)
        option_Builder0.longOpt("Y")
        option0 = option_Builder0.build()
        commandLine_Builder1 = commandLine_Builder0.addOption(option0)
        option0.addValueForProcessing("Y")
        commandLine0 = commandLine_Builder1.build()
        object0 = commandLine0.getOptionObject1("Y")
        self.assertIsNone(object0)

    def test04(self) -> None:
        commandLine0 = CommandLine()
        commandLine0._addArg('l+J,/7dJzJM?GcA"T')

    def test03(self) -> None:

        commandLine_Builder0 = Builder()
        option0 = Option.Option1("", "")
        commandLine_Builder0.addOption(option0)
        commandLine0 = commandLine_Builder0.build()
        option1 = Option.Option2("", True, None)
        properties0 = commandLine0.getOptionProperties0(option1)
        self.assertIsNotNone(properties0)

    def test02(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.valueSeparator0()
        option_Builder1.hasArgs()
        option_Builder1.longOpt("P z=Y")
        option0 = option_Builder0.build()
        commandLine_Builder1 = commandLine_Builder0.addOption(option0)
        option0.addValueForProcessing("P z=Y")
        option0.addValueForProcessing("org.apache.commons.cli.CommandLine")
        commandLine0 = commandLine_Builder1.build()
        properties0 = commandLine0.getOptionProperties0(option0)
        self.assertIsNotNone(properties0)

    def test01(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.valueSeparator0()
        option_Builder1.longOpt("P z=Y")
        option_Builder0.hasArgs()
        option0 = option_Builder0.build()
        commandLine_Builder0.addOption(option0)
        option0.addValueForProcessing("P z=Y")
        commandLine0 = commandLine_Builder0.build()
        option0.addValueForProcessing("P z=Y")
        properties0 = commandLine0.getOptionProperties1("P z=Y")
        self.assertIsNotNone(properties0)

    def test00(self) -> None:

        commandLine_Builder0 = CommandLine.Builder()
        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.option("")
        option0 = option_Builder1.build()
        commandLine_Builder0.addOption(option0)
        option1 = option_Builder0.build()
        commandLine0 = commandLine_Builder0.build()
        stringArray0 = commandLine0.getOptionValues1(option1)
        self.assertIsNone(stringArray0)
