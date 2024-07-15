from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.digest.HmacAlgorithms import *

# from src.test.org.apache.commons.codec.digest.HmacAlgorithms_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class HmacAlgorithms_ESTest(unittest.TestCase):

    def test3(self) -> None:
        hmacAlgorithms0 = HmacAlgorithms.HMAC_SHA_1
        string0 = hmacAlgorithms0.getName()
        self.assertEqual(string0, "HmacSHA1")

    def test2(self) -> None:
        hmacAlgorithms0 = HmacAlgorithms.HMAC_SHA_224
        string0 = hmacAlgorithms0.toString()
        self.assertEqual("HmacSHA224", string0)

    def test1(self) -> None:

        hmacAlgorithms0 = HmacAlgorithms.valueOf("HMAC_SHA_512")
        self.assertEqual("HmacSHA512", hmacAlgorithms0.toString())

    def test0(self) -> None:

        hmacAlgorithmsArray0 = HmacAlgorithms.values()
        self.assertEqual(6, len(hmacAlgorithmsArray0))
