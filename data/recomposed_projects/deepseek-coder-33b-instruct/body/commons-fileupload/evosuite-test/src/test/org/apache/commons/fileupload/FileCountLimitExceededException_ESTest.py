from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.fileupload.FileCountLimitExceededException import *

# from src.test.org.apache.commons.fileupload.FileCountLimitExceededException_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class FileCountLimitExceededException_ESTest(unittest.TestCase):

    def test2(self) -> None:

        fileCountLimitExceededException0 = FileCountLimitExceededException(
            ";e%Q.", -1598
        )
        long0 = fileCountLimitExceededException0.getLimit()
        self.assertEqual(-1598, long0)

    def test1(self) -> None:
        fileCountLimitExceededException0 = FileCountLimitExceededException("", 1214)
        long0 = fileCountLimitExceededException0.getLimit()
        self.assertEqual(1214, long0)

    def test0(self) -> None:
        fileCountLimitExceededException0 = FileCountLimitExceededException("", 0)
        long0 = fileCountLimitExceededException0.getLimit()
        self.assertEqual(0, long0)
