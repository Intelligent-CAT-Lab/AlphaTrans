from __future__ import annotations
import re
import unittest
import pytest
import io


class AltCharSequence(str):

    def subSequence(self, start: int, end: int) -> str:

        if start < 0 or end > len(self) or start > end:
            raise IndexError("Index out of bounds")

        return self[start:end]

    def charAt(self, index: int) -> str:
        return self[index]

    def length(self) -> int:
        return len(self)
