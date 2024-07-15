from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.digest.Sha2Crypt import *


class Sha2CryptTest(unittest.TestCase):

    def testCtor(self) -> None:

        # The 'assert' keyword is used to test if a condition returns True.
        # The 'is not None' condition checks if the object is not None.
        assert Sha2Crypt() is not None
