from __future__ import annotations
import time
import re
import os
from io import BytesIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.Resources import *

# from src.test.org.apache.commons.codec.Resources_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Resources_ESTest(unittest.TestCase):

    def test3(self) -> None:
        resources0 = Resources()

    def test2(self) -> None:

        # Create a BytesIO object with some data
        data = b"Test data here"
        inputStream0 = io.BytesIO(data)

        # Check if the available data is equal to the length of the data
        self.assertEqual(len(data), inputStream0.getbuffer().nbytes)

    def test1(self) -> None:

        # Undeclared exception
        try:
            Resources.getInputStream(",uUBDV)1z`=v")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Unable to resolve required resource: ,uUBDV)1z`=v
            self.verifyException("org.apache.commons.codec.Resources", e)

    def test0(self) -> None:

        with pytest.raises(RuntimeError):
            Resources.getInputStream(None)
