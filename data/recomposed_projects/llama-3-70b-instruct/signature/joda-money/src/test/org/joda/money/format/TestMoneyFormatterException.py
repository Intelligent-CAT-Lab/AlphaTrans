from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.joda.money.format.MoneyFormatException import *


class TestMoneyFormatterException(unittest.TestCase):

    def test_MoneyFormatException_nonIOException_notRethrown(self) -> None:
        test = MoneyFormatException("Error", RuntimeError("Inner"))
        test.rethrowIOException()  # should succeed

    def test_MoneyFormatException_IOException_notRethrown(self) -> None:
        test = MoneyFormatException("Error", io.IOException("Inner"))
        test.rethrowIOException()  # should throw
