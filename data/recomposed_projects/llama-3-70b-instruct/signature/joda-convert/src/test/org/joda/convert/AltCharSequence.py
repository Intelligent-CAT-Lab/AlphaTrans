from __future__ import annotations
import re
import unittest
import pytest
import io


class AltCharSequence(str):

    def subSequence(self, start: int, end: int) -> str:
        return self[start:end]

    def charAt(self, index: int) -> str:
        return "A"

    def length(self) -> int:
        return 1
