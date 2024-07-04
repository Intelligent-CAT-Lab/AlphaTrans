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
from src.main.org.apache.commons.cli.OptionBuilder import *

# from src.test.org.apache.commons.cli.OptionBuilder_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class OptionBuilder_ESTest(unittest.TestCase):

    def test30(self) -> None:

        OptionBuilder.hasArgs1(0)
        option0 = OptionBuilder.create1("R")
        self.assertEqual(0, option0.getArgs())
        self.assertEqual(82, option0.getId())

    def test29(self) -> None:

        OptionBuilder.hasArg0()
        OptionBuilder.withLongOpt("U?V(")
        option0 = OptionBuilder.create0()
        self.assertEqual(1, option0.getArgs())

    def test28(self) -> None:
        class0 = str
        optionBuilder0 = OptionBuilder.withType0(class0)
        assert optionBuilder0 is not None

    def test27(self) -> None:

        OptionBuilder.isRequired0()
        option0 = OptionBuilder.create2("")
        self.assertEqual(-1, option0.getArgs())
        self.assertTrue(option0.isRequired())

    def test26(self) -> None:

        OptionBuilder.withArgName("t_K|")
        option0 = OptionBuilder.create1("O")
        self.assertEqual(79, option0.getId())
        self.assertEqual(-1, option0.getArgs())

    def test25(self) -> None:

        optionBuilder0 = OptionBuilder.hasOptionalArg()
        assert optionBuilder0 is not None

    def test24(self) -> None:

        OptionBuilder.hasOptionalArgs0()
        OptionBuilder.withLongOpt("s>&Vg-MR")
        option0 = OptionBuilder.create0()
        self.assertEqual(-2, option0.getArgs())
        self.assertTrue(option0.hasOptionalArg())

    def test23(self) -> None:

        OptionBuilder.withValueSeparator0()
        OptionBuilder.withLongOpt("s>&Vg-MR")
        option0 = OptionBuilder.create0()
        self.assertEqual("=", option0.getValueSeparator())
        self.assertEqual(-1, option0.getArgs())

    def test22(self) -> None:
        optionBuilder0 = OptionBuilder.withDescription("org.apache.commons.cli.Option")
        assert optionBuilder0 is not None

    def test21(self) -> None:
        optionBuilder0 = OptionBuilder.withType1(None)
        assert optionBuilder0 is not None

    def test20(self) -> None:

        OptionBuilder.hasArgs0()
        option0 = OptionBuilder.create2("")
        self.assertEqual(-2, option0.getArgs())

    def test19(self) -> None:

        try:
            OptionBuilder.create0()
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # must specify longopt
            self.verifyException("org.apache.commons.cli.OptionBuilder", e)

    def test18(self) -> None:
        optionBuilder0 = OptionBuilder.hasArg1(False)
        assert optionBuilder0 is not None

    def test17(self) -> None:
        optionBuilder0 = OptionBuilder.hasArg1(True)
        assert optionBuilder0 is not None

    def test16(self) -> None:

        try:
            OptionBuilder.create1("&")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # Illegal option name '&'
            #
            self.verifyException("org.apache.commons.cli.OptionValidator", e)

    def test15(self) -> None:

        try:
            OptionBuilder.create2("A CloneNotSupportedException was thrown: ")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # The option 'A CloneNotSupportedException was thrown: ' contains an illegal character : ' '
            verifyException("org.apache.commons.cli.OptionValidator", e)

    def test14(self) -> None:

        object0 = object()
        try:
            OptionBuilder.withType1(object0)
            self.fail("Expecting exception: ClassCastException")

        except ClassCastException as e:
            self.verifyException("org.apache.commons.cli.OptionBuilder", e)

    def test13(self) -> None:

        OptionBuilder.withLongOpt("")
        OptionBuilder.hasOptionalArgs1(0)
        option0 = OptionBuilder.create0()
        self.assertTrue(option0.hasOptionalArg())
        self.assertEqual(0, option0.getArgs())

    def test12(self) -> None:

        OptionBuilder.withLongOpt("")
        OptionBuilder.withArgName('|Yu2"c<=3@WUEpO')
        option0 = OptionBuilder.create0()
        self.assertEqual((-1), option0.getArgs())

    def test11(self) -> None:

        OptionBuilder.isRequired1(True)
        OptionBuilder.withLongOpt("s>&Vg-MR")
        option0 = OptionBuilder.create0()
        self.assertEqual((-1), option0.getArgs())

    def test10(self) -> None:

        OptionBuilder.hasArg0()
        option0 = OptionBuilder.create1("5")
        self.assertEqual("5", option0.getOpt())
        self.assertEqual(1, option0.getArgs())

    def test09(self) -> None:

        OptionBuilder.hasOptionalArgs0()
        option0 = OptionBuilder.create1("l")
        self.assertEqual(-2, option0.getArgs())
        self.assertEqual(108, option0.getId())
        self.assertTrue(option0.hasOptionalArg())

    def test08(self) -> None:

        OptionBuilder.withLongOpt("U?V(")
        option0 = OptionBuilder.create1("k")
        self.assertEqual(-1, option0.getArgs())
        self.assertEqual(107, option0.getId())

    def test07(self) -> None:

        OptionBuilder.withValueSeparator0()
        option0 = OptionBuilder.create1("O")
        self.assertEqual(-1, option0.getArgs())
        self.assertEqual("=", option0.getValueSeparator())
        self.assertEqual("O", option0.getOpt())

    def test06(self) -> None:

        OptionBuilder.isRequired1(True)
        option0 = OptionBuilder.create1("5")
        self.assertEqual(-1, option0.getArgs())
        self.assertEqual("5", option0.getOpt())

    def test05(self) -> None:

        OptionBuilder.hasArg0()
        option0 = OptionBuilder.create2("")
        self.assertEqual(1, option0.getArgs())

    def test04(self) -> None:

        OptionBuilder.hasOptionalArgs1(0)
        option0 = OptionBuilder.create2("")
        self.assertEqual(0, option0.getArgs())
        self.assertTrue(option0.hasOptionalArg())

    def test03(self) -> None:

        option0 = OptionBuilder.create2("NO_ARGS_ALLOWED")
        self.assertEqual(-1, option0.getArgs())

    def test02(self) -> None:

        OptionBuilder.withArgName("org.apache.commons.cli.Option$Builder")
        option0 = OptionBuilder.create2("")
        self.assertEqual(-1, option0.getArgs())

    def test01(self) -> None:

        OptionBuilder.withLongOpt("")
        option0 = OptionBuilder.create2("")
        self.assertEqual(-1, option0.getArgs())

    def test00(self) -> None:

        OptionBuilder.withValueSeparator1(")")
        option0 = OptionBuilder.create2("")
        self.assertEqual(-1, option0.getArgs())
        self.assertEqual(")", option0.getValueSeparator())
