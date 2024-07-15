from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.test.org.apache.commons.codec.binary.HexTest import *


class AllocateDirectHexTest(HexTest):

    def _allocate(self, capacity: int) -> typing.Union[bytearray, memoryview]:

        # Python does not have a direct equivalent to Java's ByteBuffer.allocateDirect()
        # However, we can use bytearray or memoryview to achieve similar functionality
        # Here, we use bytearray as an example

        return bytearray(capacity)
