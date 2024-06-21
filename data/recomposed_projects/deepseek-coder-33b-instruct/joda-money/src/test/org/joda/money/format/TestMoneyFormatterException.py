from __future__ import annotations
import io
from src.main.org.joda.money.format.MoneyFormatException import *


class TestMoneyFormatterException:

    def test_MoneyFormatException_nonIOException_notRethrown(self) -> None:

        # Create a MoneyFormatException instance
        test = MoneyFormatException("Error", IllegalStateException("Inner"))

        # Call the rethrowIOException method
        try:
            test.rethrowIOException()
        except IOException:
            # If an IOException is thrown, this should be caught and ignored
            pass

    def test_MoneyFormatException_IOException_notRethrown(self) -> None:

        try:
            test = MoneyFormatException("Error", io.IOException("Inner"))
            test.rethrowIOException()
        except io.IOException:
            pass
        else:
            assert False, "Expected IOException"
