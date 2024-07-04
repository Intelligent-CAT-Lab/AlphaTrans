from __future__ import annotations
import time
import re
import mock
import os
import unittest
import pytest
import io
import unittest

# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
from src.main.org.joda.money.format.MoneyFormatException import *

# from src.test.org.joda.money.format.MoneyFormatException_ESTest_scaffolding import *


class MoneyFormatException_ESTest(unittest.TestCase):

    def test1(self) -> None:

        moneyFormatException0 = MoneyFormatException.MoneyFormatException1("")
        moneyFormatException0.rethrowIOException()

    def test0(self) -> None:

        mock_io_exception = io.IOException()
        money_format_exception = MoneyFormatException(None, mock_io_exception)
        try:
            money_format_exception.rethrowIOException()
            self.fail("Expecting exception: IOException")

        except io.IOException:
            pass
