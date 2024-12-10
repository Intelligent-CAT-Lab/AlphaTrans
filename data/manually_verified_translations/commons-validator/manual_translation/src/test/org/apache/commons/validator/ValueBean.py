from __future__ import annotations
import re
import unittest
import pytest
import io


class ValueBean:

    _value: str = ""

    def setValue(self, value: str) -> None:
        self._value = value

    def getValue(self) -> str:
        return self._value
