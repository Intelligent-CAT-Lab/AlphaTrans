from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.Validator import *
from src.main.org.apache.commons.validator.ValidatorResources import *

# from src.test.org.apache.commons.validator.Validator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Validator_ESTest(unittest.TestCase):

    def test2(self) -> None:
        try:
            Validator.Validator2(None)
            self.fail("Expecting exception: ValueError")
        except ValueError as e:
            verifyException("org.apache.commons.validator.Validator", e)

    def test1(self) -> None:

        validator0 = None
        try:
            validator0 = Validator(0, None, "j//EJ", "j//EJ")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Resources cannot be null.
            self.assertEqual(str(e), "Resources cannot be null.")

    def test0(self) -> None:

        validator0 = None
        try:
            validator0 = Validator(-438, None, "),v,&x3rV[Vrdw", "),v,&x3rV[Vrdw")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Resources cannot be null.
            self.assertEqual(str(e), "Resources cannot be null.")
