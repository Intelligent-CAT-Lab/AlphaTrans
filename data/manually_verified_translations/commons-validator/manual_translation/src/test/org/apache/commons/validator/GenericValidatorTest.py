from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.GenericValidator import *


class GenericValidatorTest(unittest.TestCase):

    def testMaxLength(self) -> None:

        self.assertFalse(GenericValidator.maxLength1("12345\n\r", 4, 0))
        self.assertTrue(GenericValidator.maxLength1("12345\n\r", 5, 0))
        self.assertTrue(GenericValidator.maxLength1("12345\n\r", 6, 0))
        self.assertTrue(GenericValidator.maxLength1("12345\n\r", 7, 0))

        self.assertFalse(GenericValidator.maxLength1("12345\n\r", 4, 1))
        self.assertFalse(GenericValidator.maxLength1("12345\n\r", 5, 1))
        self.assertTrue(GenericValidator.maxLength1("12345\n\r", 6, 1))
        self.assertTrue(GenericValidator.maxLength1("12345\n\r", 7, 1))

        self.assertFalse(GenericValidator.maxLength1("12345\n\r", 4, 2))
        self.assertFalse(GenericValidator.maxLength1("12345\n\r", 5, 2))
        self.assertFalse(GenericValidator.maxLength1("12345\n\r", 6, 2))
        self.assertTrue(GenericValidator.maxLength1("12345\n\r", 7, 2))

    def testMinLength(self) -> None:

        self.assertTrue(GenericValidator.minLength1("12345\n\r", 5, 0))
        self.assertFalse(GenericValidator.minLength1("12345\n\r", 6, 0))
        self.assertFalse(GenericValidator.minLength1("12345\n\r", 7, 0))
        self.assertFalse(GenericValidator.minLength1("12345\n\r", 8, 0))

        self.assertTrue(GenericValidator.minLength1("12345\n\r", 5, 1))
        self.assertTrue(GenericValidator.minLength1("12345\n\r", 6, 1))
        self.assertFalse(GenericValidator.minLength1("12345\n\r", 7, 1))
        self.assertFalse(GenericValidator.minLength1("12345\n\r", 8, 1))

        self.assertTrue(GenericValidator.minLength1("12345\n\r", 5, 2))
        self.assertTrue(GenericValidator.minLength1("12345\n\r", 6, 2))
        self.assertTrue(GenericValidator.minLength1("12345\n\r", 7, 2))
        self.assertFalse(GenericValidator.minLength1("12345\n\r", 8, 2))

    def __init__(self, name: str) -> None:
        super().__init__(name)
