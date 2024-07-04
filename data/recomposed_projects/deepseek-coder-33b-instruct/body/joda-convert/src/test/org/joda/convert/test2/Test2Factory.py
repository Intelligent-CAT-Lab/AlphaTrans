from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.joda.convert.FromString import *
from src.test.org.joda.convert.test2.Test2Class import *


class Test2Factory:

    @staticmethod
    def parse(amount: str) -> Test2Class:
        return Test2Class(int(amount[:-1]))
