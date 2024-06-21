from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.apache.commons.codec.net.Utils import *


class UtilsTest(unittest.TestCase):

    def testConstructor(self) -> None:

        Utils()
