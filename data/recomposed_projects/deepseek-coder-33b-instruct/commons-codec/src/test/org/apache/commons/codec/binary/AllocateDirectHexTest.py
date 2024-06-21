from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.test.org.apache.commons.codec.binary.HexTest import *


class AllocateDirectHexTest(HexTest, unittest.TestCase):

    def _allocate(self, capacity: int) -> typing.Union[bytearray, memoryview]:

        # Bytearray is a mutable sequence of integers.
        # Memoryview is a flexible way of accessing the same block of memory.
        # In this case, we are using bytearray as it is mutable.
        return bytearray(capacity)
