import pytest

from src.main.org.apache.commons.validator.GenericValidator import *
import unittest


class GenericValidatorTest(unittest.TestCase):

    @pytest.mark.test
    def testMinLength(self) -> None:
        self.assertTrue(GenericValidator.minLength1("12345\n\r", 5, 0), "Min=5 End=0")
        self.assertFalse(GenericValidator.minLength1("12345\n\r", 6, 0), "Min=6 End=0")
        self.assertFalse(GenericValidator.minLength1("12345\n\r", 7, 0), "Min=7 End=0")
        self.assertFalse(GenericValidator.minLength1("12345\n\r", 8, 0), "Min=8 End=0")

        self.assertTrue(GenericValidator.minLength1("12345\n\r", 5, 1), "Min=5 End=1")
        self.assertTrue(GenericValidator.minLength1("12345\n\r", 6, 1), "Min=6 End=1")
        self.assertFalse(GenericValidator.minLength1("12345\n\r", 7, 1), "Min=7 End=1")
        self.assertFalse(GenericValidator.minLength1("12345\n\r", 8, 1), "Min=8 End=1")

        self.assertTrue(GenericValidator.minLength1("12345\n\r", 5, 2), "Min=5 End=2")
        self.assertTrue(GenericValidator.minLength1("12345\n\r", 6, 2), "Min=6 End=2")
        self.assertTrue(GenericValidator.minLength1("12345\n\r", 7, 2), "Min=7 End=2")
        self.assertFalse(GenericValidator.minLength1("12345\n\r", 8, 2), "Min=8 End=2")

    
    @pytest.mark.test
    def testMaxLength(self) -> None:
        self.assertFalse(GenericValidator.maxLength1("12345\n\r", 4, 0), "Max=4 End=0")
        self.assertTrue(GenericValidator.maxLength1("12345\n\r", 5, 0), "Max=5 End=0")
        self.assertTrue(GenericValidator.maxLength1("12345\n\r", 6, 0), "Max=6 End=0")
        self.assertTrue(GenericValidator.maxLength1("12345\n\r", 7, 0), "Max=7 End=0")

        self.assertFalse(GenericValidator.maxLength1("12345\n\r", 4, 1), "Max=4 End=1")
        self.assertFalse(GenericValidator.maxLength1("12345\n\r", 5, 1), "Max=5 End=1")
        self.assertTrue(GenericValidator.maxLength1("12345\n\r", 6, 1), "Max=6 End=1")
        self.assertTrue(GenericValidator.maxLength1("12345\n\r", 7, 1), "Max=7 End=1")

        self.assertFalse(GenericValidator.maxLength1("12345\n\r", 4, 2), "Max=4 End=2")
        self.assertFalse(GenericValidator.maxLength1("12345\n\r", 5, 2), "Max=5 End=2")
        self.assertFalse(GenericValidator.maxLength1("12345\n\r", 6, 2), "Max=6 End=2")
        self.assertTrue(GenericValidator.maxLength1("12345\n\r", 7, 2), "Max=7 End=2")
