from __future__ import annotations
import re
import unittest
import pytest
from abc import ABC
import io
import unittest
from src.main.org.apache.commons.codec.BinaryEncoder import *
from src.main.org.apache.commons.codec.EncoderException import *


class BinaryEncoderAbstractTest(ABC, unittest.TestCase):

    def testEncodeNull(self) -> None:

        pass  # LLM could not translate this method

    def testEncodeEmpty(self) -> None:

        pass  # LLM could not translate this method

    def _makeEncoder(self) -> BinaryEncoder:
        return self.makeEncoder()
