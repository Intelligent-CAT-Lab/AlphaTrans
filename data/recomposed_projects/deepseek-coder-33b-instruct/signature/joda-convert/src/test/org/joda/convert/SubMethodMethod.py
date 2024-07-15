from __future__ import annotations
import re
import unittest
import pytest
import io
from src.test.org.joda.convert.DistanceMethodMethod import *
from src.main.org.joda.convert.FromString import *


class SubMethodMethod(DistanceMethodMethod):

    @staticmethod
    def parse(amount: str) -> SubMethodMethod:
        amount = amount[:-1]
        return SubMethodMethod(int(amount))

    def __init__(self, amount: int) -> None:
        super().__init__(amount)
