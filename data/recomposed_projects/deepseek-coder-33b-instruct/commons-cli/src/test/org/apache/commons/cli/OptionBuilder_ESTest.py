from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionBuilder import *

# from src.main.org.apache.commons.cli.OptionBuilder_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class OptionBuilder_ESTest(unittest.TestCase):

    @pytest.mark.test
    def test28(self) -> None:

        OptionBuilder.hasArgs1(0)
        option0 = OptionBuilder.create2("")
        self.assertEqual(0, option0.getArgs())

    @pytest.mark.test
    def test27(self) -> None:

        OptionBuilder.hasArg0()
        option0 = OptionBuilder.create2("l")
        self.assertEqual(1, option0.getArgs())

    @pytest.mark.test
    def test26(self) -> None:
        optionBuilder0 = OptionBuilder.withType1(None)
        assert optionBuilder0 is not None

    @pytest.mark.test
    def test25(self) -> None:

        OptionBuilder.isRequired0()
        option0 = OptionBuilder.create2(None)
        self.assertEqual(-1, option0.getArgs())
        self.assertTrue(option0.isRequired())

    @pytest.mark.test
    def test24(self) -> None:

        optionBuilder0 = OptionBuilder.hasOptionalArg()
        self.assertIsNotNone(optionBuilder0)

    @pytest.mark.test
    def test23(self) -> None:

        OptionBuilder.hasOptionalArgs0()
        option0 = OptionBuilder.create2(None)
        self.assertEqual(-2, option0.getArgs())
        self.assertTrue(option0.hasOptionalArg())

    @pytest.mark.test
    def test22(self) -> None:

        OptionBuilder.withValueSeparator0()
        option0 = OptionBuilder.create1("f")
        self.assertEqual(-1, option0.getArgs())
        self.assertEqual("=", option0.getValueSeparator())
        self.assertEqual(102, option0.getId())

    @pytest.mark.test
    def test21(self) -> None:
        optionBuilder0 = OptionBuilder.withDescription(
            "Either opt or longOpt must be specified"
        )
        assert optionBuilder0 is not None

    @pytest.mark.test
    def test20(self) -> None:

        OptionBuilder.hasOptionalArgs1(61)
        OptionBuilder.withLongOpt("Either opt or longOpt must be specified")
        option0 = OptionBuilder.create0()
        self.assertTrue(option0.hasOptionalArg())
        self.assertEqual(61, option0.getArgs())

    @pytest.mark.test
    def test19(self) -> None:
        optionBuilder0 = OptionBuilder.hasArgs0()
        assert optionBuilder0 is not None

    @pytest.mark.test
    def test18(self) -> None:

        try:
            OptionBuilder.create0()
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # must specify longopt
            self.verifyException("org.apache.commons.cli.OptionBuilder", e)

    @pytest.mark.test
    def test17(self) -> None:
        optionBuilder0 = OptionBuilder.hasArg1(False)
        assert optionBuilder0 is not None

    @pytest.mark.test
    def test16(self) -> None:

        OptionBuilder.hasArg1(True)
        option0 = OptionBuilder.create1("o")
        self.assertEqual(1, option0.getArgs())
        self.assertEqual("o", option0.getOpt())

    @pytest.mark.test
    def test15(self) -> None:

        try:
            OptionBuilder.create2("b)<f~]v")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # The option 'b)<f~]v' contains an illegal character : ')'
            self.verifyException("org.apache.commons.cli.OptionValidator", e)

    @pytest.mark.test
    def test14(self) -> None:
        class0 = object
        optionBuilder0 = OptionBuilder.withType0(class0)
        self.assertIsNotNone(optionBuilder0)

    @pytest.mark.test
    def test13(self) -> None:

        try:
            OptionBuilder.create1(".")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # Illegal option name '.'
            #
            self.verifyException("org.apache.commons.cli.OptionValidator", e)

    @pytest.mark.test
    def test12(self) -> None:

        try:
            OptionBuilder.withType1("must specify longopt")
            self.fail("Expecting exception: ClassCastException")

        except ClassCastException as e:
            verifyException("org.apache.commons.cli.OptionBuilder", e)

    @pytest.mark.test
    def test11(self) -> None:

        OptionBuilder.hasOptionalArgs1(0)
        OptionBuilder.withLongOpt("w2:?em'uh^H*h8")
        option0 = OptionBuilder.create0()
        self.assertEqual(0, option0.getArgs())
        self.assertTrue(option0.hasOptionalArg())

    @pytest.mark.test
    def test10(self) -> None:

        OptionBuilder.withLongOpt("Either opt or longOpt must be specified")
        OptionBuilder.withArgName("Either opt or longOpt must be specified")
        option0 = OptionBuilder.create0()
        self.assertEqual(-1, option0.getArgs())

    @pytest.mark.test
    def test09(self) -> None:

        OptionBuilder.withLongOpt("Either opt or longOpt must be specified")
        OptionBuilder.withValueSeparator0()
        option0 = OptionBuilder.create0()
        self.assertEqual(-1, option0.getArgs())
        self.assertEqual("=", option0.getValueSeparator())

    @pytest.mark.test
    def test08(self) -> None:

        OptionBuilder.withLongOpt("Either opt or longOpt must be specified")
        OptionBuilder.isRequired0()
        option0 = OptionBuilder.create0()
        self.assertTrue(option0.isRequired())
        self.assertEqual(-1, option0.getArgs())

    @pytest.mark.test
    def test07(self) -> None:

        OptionBuilder.hasOptionalArgs1(0)
        option0 = OptionBuilder.create1("r")
        self.assertEqual(0, option0.getArgs())
        self.assertTrue(option0.hasOptionalArg())
        self.assertEqual(114, option0.getId())

    @pytest.mark.test
    def test06(self) -> None:

        OptionBuilder.withArgName("HC")
        option0 = OptionBuilder.create1("o")
        self.assertEqual(-1, option0.getArgs())
        self.assertEqual("o", option0.getOpt())

    @pytest.mark.test
    def test05(self) -> None:

        OptionBuilder.hasArgs1(70)
        option0 = OptionBuilder.create1("f")
        self.assertEqual(70, option0.getArgs())
        self.assertEqual(102, option0.getId())

    @pytest.mark.test
    def test04(self) -> None:

        OptionBuilder.withLongOpt("")
        option0 = OptionBuilder.create1("u")
        self.assertEqual(-1, option0.getArgs())
        self.assertEqual("u", option0.getOpt())

    @pytest.mark.test
    def test03(self) -> None:

        OptionBuilder.isRequired1(True)
        option0 = OptionBuilder.create1("i")
        self.assertEqual(-1, option0.getArgs())
        self.assertEqual("i", option0.getOpt())

    @pytest.mark.test
    def test02(self) -> None:

        OptionBuilder.withArgName('n,7"p2i`')
        option0 = OptionBuilder.create2("")
        self.assertEqual((-1), option0.getArgs())

    @pytest.mark.test
    def test01(self) -> None:

        OptionBuilder.withLongOpt("")
        option0 = OptionBuilder.create2("")
        self.assertEqual(-1, option0.getArgs())

    @pytest.mark.test
    def test00(self) -> None:

        OptionBuilder.withValueSeparator1("c")
        option0 = OptionBuilder.create2("l")
        self.assertEqual(-1, option0.getArgs())
        self.assertEqual("c", option0.getValueSeparator())
