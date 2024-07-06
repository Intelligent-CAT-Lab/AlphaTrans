from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.joda.money.IllegalCurrencyException import *


class TestIllegalCurrencyException(unittest.TestCase):

    def test_String_nullString(self) -> None:
        test = IllegalCurrencyException(None)
        self.assertEqual(None, test.getMessage())
        self.assertEqual(None, test.getCause())

    def test_String(self) -> None:
        test = IllegalCurrencyException("PROBLEM")
        self.assertEqual("PROBLEM", test.getMessage())
        self.assertEqual(None, test.getCause())
