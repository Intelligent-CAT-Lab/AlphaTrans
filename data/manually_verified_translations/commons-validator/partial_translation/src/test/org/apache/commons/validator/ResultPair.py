from __future__ import annotations
import re
import unittest
import pytest
import io


class ResultPair:

    valid: bool = False

    item: str = ""

    def __init__(self, item: str, valid: bool) -> None:
        self.item = item
        self.valid = valid
