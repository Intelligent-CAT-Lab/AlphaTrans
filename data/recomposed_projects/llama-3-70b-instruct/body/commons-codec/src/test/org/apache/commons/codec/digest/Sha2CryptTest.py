from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.digest.Sha2Crypt import *


class Sha2CryptTest(unittest.TestCase):

    def testCtor(self) -> None:
        self.assertIsNotNone(Sha2Crypt())
