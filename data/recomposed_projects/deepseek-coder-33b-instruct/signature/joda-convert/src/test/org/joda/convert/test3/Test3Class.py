from __future__ import annotations
import re
import unittest
import pytest
import io
from src.test.org.joda.convert.test3.Test3Interface import *
from src.test.org.joda.convert.test3.Test3SuperClass import *


class Test3Class(Test3Interface, Test3SuperClass):

    amount: int = 0

    def toString(self) -> str:
        return "Weight[" + str(self.amount) + "g]"

    def print(self) -> str:
        return str(self.amount) + "g"

    def __init__(self, amount: int) -> None:
        self.amount = amount
