from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.ValidatorException import *

# from src.test.org.apache.commons.validator.ValidatorException_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class ValidatorException_ESTest(unittest.TestCase):

    def test1(self) -> None:
        validatorException0 = ValidatorException.ValidatorException1()
        assert validatorException0 is not None

    def test0(self) -> None:
        validatorException0 = ValidatorException("")
