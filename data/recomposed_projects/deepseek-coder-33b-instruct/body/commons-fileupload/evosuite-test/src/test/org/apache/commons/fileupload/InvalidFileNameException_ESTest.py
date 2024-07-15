from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.fileupload.InvalidFileNameException import *

# from src.test.org.apache.commons.fileupload.InvalidFileNameException_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class InvalidFileNameException_ESTest(unittest.TestCase):

    def test2(self) -> None:

        invalidFileNameException0 = InvalidFileNameException(
            'WoB?dJj"Tk)', 'WoB?dJj"Tk)'
        )
        string0 = invalidFileNameException0.getName()
        self.assertEqual(string0, 'WoB?dJj"Tk)')

    def test1(self) -> None:

        invalidFileNameException0 = InvalidFileNameException("", "")
        string0 = invalidFileNameException0.getName()
        self.assertEqual("", string0)

    def test0(self) -> None:

        invalidFileNameException0 = InvalidFileNameException(None, None)
        string0 = invalidFileNameException0.getName()
        self.assertIsNone(string0)
