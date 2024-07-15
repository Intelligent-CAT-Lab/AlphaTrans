from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.joda.convert.FromString import *
from src.test.org.joda.convert.test3.Test3Interface import *


class Test3Factory:

    @staticmethod
    def parse(amount: str) -> Test3Interface:
        return Test3(amount)
