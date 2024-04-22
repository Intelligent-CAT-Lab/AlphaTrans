# Imports Begin
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.Option import *
import unittest
from typing import *
# Imports End


class OptionBuilderTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def test_BaseOptionCharOpt(self) -> None:
        base = OptionBuilder.withDescription("option description").create1('o')
        self.assertEqual("o", base.getOpt())
        self.assertEqual("option description", base.getDescription())
        self.assertFalse(base.hasArg())

    
    def test_BaseOptionStringOpt(self) -> None:
        base = OptionBuilder.withDescription("option description").create2("o")
        self.assertEqual("o", base.getOpt())
        self.assertEqual("option description", base.getDescription())
        self.assertFalse(base.hasArg())

    
    def test_BuilderIsResettedAlways(self) -> None:
        try:
            OptionBuilder.withDescription("JUnit").create1('"')
            self.fail("ValueError expected")
        except ValueError:
            pass
        self.assertIsNone(
            OptionBuilder.create1("x").getDescription(), "we inherited a description"
        )
        try:
            OptionBuilder.withDescription("JUnit").create0()
            self.fail("ValueError expected")
        except ValueError:
            pass
        self.assertIsNone(
            OptionBuilder.create1("x").getDescription(), "we inherited a description"
        )


    def test_CompleteOption(self) -> None:
        simple = OptionBuilder.withLongOpt("simple option")\
                              .hasArg0()\
                              .isRequired0()\
                              .hasArgs0()\
                              .withType0(float)\
                              .withDescription("this is a simple option")\
                              .create1('s')
        self.assertEqual("s", simple.getOpt())
        self.assertEqual("simple option", simple.getLongOpt())
        self.assertEqual("this is a simple option", simple.getDescription())
        self.assertEqual(simple.getType, float)
        self.assertTrue(simple.hasArg())
        self.assertTrue(simple.isRequired())
        self.assertTrue(simple.hasArgs())


    def test_CreateIncompleteOption(self) -> None:
        with self.assertRaises(ValueError):
            OptionBuilder.hasArg0().create0()
        OptionBuilder.create2("opt")


    def test_IllegalOptions(self) -> None:
        try:
            OptionBuilder.withDescription("option description").create1('"')
            self.fail("ValueError not caught")
        except ValueError:
            pass
        try:
            OptionBuilder.create2("opt`")
            self.fail("IllegalArgumentException not caught")
        except ValueError:
            pass
        try:
            OptionBuilder.create2("opt")
        except ValueError:
            self.fail("IllegalArgumentException caught")


    def test_OptionArgNumbers(self) -> None:
        opt = OptionBuilder.withDescription("option description").hasArgs1(2).create1('o')
        self.assertEqual(2, opt.getArgs())
    
    
    def test_SpecialOptChars(self) -> None:
        try:
            opt1 = OptionBuilder.withDescription("help options").create1("?")
            self.assertEqual("?", opt1.getOpt())

            opt2 = OptionBuilder.withDescription("read from stdin").create1("@")
            self.assertEqual("@", opt2.getOpt())

            try:
                OptionBuilder.create1(' ')
                self.fail("IllegalArgumentException not caught")
            except ValueError:
                pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    def test_TwoCompleteOptions(self) -> None:

        simple = OptionBuilder.withLongOpt("simple option")\
                              .hasArg0()\
                              .isRequired0()\
                              .hasArgs0()\
                              .withType0(float)\
                              .withDescription("this is a simple option")\
                              .create1("s")
        
        self.assertEqual("s", simple.getOpt())
        self.assertEqual("simple option", simple.getLongOpt())
        self.assertEqual("this is a simple option", simple.getDescription())
        self.assertEqual(simple.getType(), float)
        self.assertTrue(simple.hasArg())
        self.assertTrue(simple.isRequired())
        self.assertTrue(simple.hasArgs())

        simple = OptionBuilder.withLongOpt("dimple option")\
                              .hasArg0()\
                              .withDescription("this is a dimple option")\
                              .create1("d")
        
        self.assertEqual("d", simple.getOpt())
        self.assertEqual("dimple option", simple.getLongOpt())
        self.assertEqual("this is a dimple option", simple.getDescription())
        self.assertEqual(str, simple.getType())
        self.assertTrue(simple.hasArg())
        self.assertFalse(simple.isRequired())
        self.assertFalse(simple.hasArgs())

    # Class Methods End
