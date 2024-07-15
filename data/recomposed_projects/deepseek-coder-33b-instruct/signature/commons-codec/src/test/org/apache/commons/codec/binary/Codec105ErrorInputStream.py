from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import os


class Codec105ErrorInputStream:

    __EOF: int = -1
    countdown: int = 3

    def read(self) -> int:
        return self.read0()

    def read1(self, b: typing.List[int], pos: int, len: int) -> int:

        if self.countdown > 0:
            self.countdown -= 1
            b[pos] = ord("\n")
            return 1
        else:
            return self.__EOF

    def read0(self) -> int:
        if self.countdown > 0:
            self.countdown -= 1
            return "\n"
        else:
            return self.__EOF
