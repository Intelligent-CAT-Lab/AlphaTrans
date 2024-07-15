from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *

# from src.test.org.apache.commons.validator.routines.checkdigit.CheckDigitException_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class CheckDigitException_ESTest(unittest.TestCase):

    def test1(self) -> None:
        checkDigitException0 = CheckDigitException.CheckDigitException1("")
        checkDigitException1 = CheckDigitException(
            "2fdA33pTvI61m6L-", checkDigitException0
        )
        self.assertFalse(checkDigitException1 == checkDigitException0)

    def test0(self) -> None:
        checkDigitException0 = CheckDigitException.CheckDigitException2()
        assert checkDigitException0 is not None
