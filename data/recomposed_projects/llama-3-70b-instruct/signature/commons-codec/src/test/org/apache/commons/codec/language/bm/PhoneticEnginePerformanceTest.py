from __future__ import annotations
import time
import re
import typing
from typing import *
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.language.bm.NameType import *
from src.main.org.apache.commons.codec.language.bm.PhoneticEngine import *
from src.main.org.apache.commons.codec.language.bm.RuleType import *


class PhoneticEnginePerformanceTest(unittest.TestCase):

    __LOOP: int = 80000

    def test(self) -> None:
        engine: PhoneticEngine = PhoneticEngine.PhoneticEngine0(
            NameType.GENERIC, RuleType.APPROX, True
        )
        input: str = "Angelo"
        startMillis: int = int(round(time.time() * 1000))
        for i in range(0, self.__LOOP):
            engine.encode0(input)
        totalMillis: int = int(round(time.time() * 1000)) - startMillis
        print(
            "Time for encoding %d times the input '%s': %d millis."
            % (self.__LOOP, input, totalMillis)
        )
