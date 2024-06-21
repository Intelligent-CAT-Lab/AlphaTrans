from __future__ import annotations
import io
from src.main.org.joda.money.IllegalCurrencyException import *


class TestIllegalCurrencyException:

    def test_String_nullString(self) -> None:

        test = IllegalCurrencyException(None)
        assert test.getMessage() is None
        assert test.getCause() is None

    def test_String(self) -> None:

        test = IllegalCurrencyException("PROBLEM")
        assert "PROBLEM" == test.getMessage()
        assert None == test.getCause()
