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
        return bytearray(capacity)
