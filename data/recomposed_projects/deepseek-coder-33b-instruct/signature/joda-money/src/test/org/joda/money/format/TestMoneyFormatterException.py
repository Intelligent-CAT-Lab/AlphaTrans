from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.joda.money.format.MoneyFormatException import *


class TestMoneyFormatterException(unittest.TestCase):

    def test_MoneyFormatException_nonIOException_notRethrown(self) -> None:

        # Create a MoneyFormatException instance
        test = MoneyFormatException("Error", RuntimeError("Inner"))

        # Call the rethrowIOException method
        test.rethrowIOException()

    def test_MoneyFormatException_IOException_notRethrown(self) -> None:

        with pytest.raises(IOException):
            test = MoneyFormatException("Error", IOException("Inner"))
            test.rethrowIOException()
