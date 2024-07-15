from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.digest.MessageDigestAlgorithms import *

# from src.test.org.apache.commons.codec.digest.MessageDigestAlgorithms_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class MessageDigestAlgorithms_ESTest(unittest.TestCase):

    def test0(self) -> None:
        stringArray0 = MessageDigestAlgorithms.values()
        self.assertEqual(len(stringArray0), 13)
