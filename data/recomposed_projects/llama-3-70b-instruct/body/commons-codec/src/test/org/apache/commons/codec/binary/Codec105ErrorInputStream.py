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

        pass  # LLM could not translate this method

    def read0(self) -> int:

        pass  # LLM could not translate this method
