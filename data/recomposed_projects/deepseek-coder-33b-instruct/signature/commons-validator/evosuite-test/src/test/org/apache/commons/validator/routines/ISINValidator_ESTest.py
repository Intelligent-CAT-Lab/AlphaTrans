from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.routines.ISINValidator import *

# from src.test.org.apache.commons.validator.routines.ISINValidator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class ISINValidator_ESTest(unittest.TestCase):

    def test2(self) -> None:
        iSINValidator0 = ISINValidator.getInstance(False)
        self.assertIsNotNone(iSINValidator0)

    def test1(self) -> None:

        iSINValidator0 = ISINValidator.getInstance(True)
        boolean0 = iSINValidator0.isValid("")
        self.assertFalse(boolean0)

    def test0(self) -> None:

        iSINValidator0 = ISINValidator.getInstance(True)
        object0 = iSINValidator0.validate("")
        self.assertIsNone(object0)
