from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.joda.money.IllegalCurrencyException import *


class TestIllegalCurrencyException(unittest.TestCase):

    def test_String_nullString(self) -> None:

        # Create an instance of IllegalCurrencyException with a null string
        test = IllegalCurrencyException(None)

        # Assert that the message and cause are both None
        self.assertIsNone(test.getMessage())
        self.assertIsNone(test.getCause())

    def test_String(self) -> None:

        test = IllegalCurrencyException("PROBLEM")
        self.assertEqual("PROBLEM", test.getMessage())
        self.assertEqual(None, test.getCause())
