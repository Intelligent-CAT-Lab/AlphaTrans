from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.apache.commons.codec.digest.Sha2Crypt import *


class Sha2CryptTest(unittest.TestCase):

    def testCtor(self) -> None:

        assert self.new_Sha2Crypt() is not None
