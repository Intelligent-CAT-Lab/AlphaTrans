from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.joda.convert.FromStringFactory import *
from src.main.org.joda.convert.ToString import *


class DistanceWithFactory:

    amount: int = 0

    def toString(self) -> str:
        return str(self.amount) + "m"

    def __init__(self, amount: int) -> None:
        self.amount = amount
