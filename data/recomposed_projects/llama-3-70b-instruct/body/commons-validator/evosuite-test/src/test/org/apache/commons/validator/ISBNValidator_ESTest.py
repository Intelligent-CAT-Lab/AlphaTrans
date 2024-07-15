from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.ISBNValidator import *

# from src.test.org.apache.commons.validator.ISBNValidator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
from src.main.org.apache.commons.validator.routines.ISBNValidator import *

# from src.test.org.apache.commons.validator.routines.ISBNValidator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *


class ISBNValidator_ESTest(unittest.TestCase):

    def test0(self) -> None:

        iSBNValidator0 = ISBNValidator()
        boolean0 = iSBNValidator0.isValid("Regular expressions are missing")
        self.assertFalse(boolean0)
