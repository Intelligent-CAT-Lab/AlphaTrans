from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.joda.convert.FromString import *
from src.test.org.joda.convert.test4.Test4Class import *
from src.test.org.joda.convert.test4.Test4Interface import *


class Test4Factory:

    @staticmethod
    def parseClass(amount: str) -> Test4Class:
        return Test4Class(int(amount[:-1]))

    @staticmethod
    def parseInterface(amount: str) -> Test4Interface:
        amount = amount[:-1]
        return Test4Class(int(amount))
