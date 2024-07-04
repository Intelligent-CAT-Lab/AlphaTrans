from __future__ import annotations
import re
import unittest
import pytest
from abc import ABC
import io
from src.main.org.joda.convert.FromString import *
from src.main.org.joda.convert.ToString import *


class Test3SuperClass(ABC):

    @staticmethod
    def parse(amount: str) -> Test3SuperClass:
        amount = amount[:-1]
        return Test3Class(int(amount))

    def print(self) -> str:
        pass
