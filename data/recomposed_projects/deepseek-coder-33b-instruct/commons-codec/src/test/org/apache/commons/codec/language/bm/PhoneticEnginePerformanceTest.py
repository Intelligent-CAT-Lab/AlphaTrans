from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.apache.commons.codec.language.bm.NameType import *
from src.main.org.apache.commons.codec.language.bm.PhoneticEngine import *
from src.main.org.apache.commons.codec.language.bm.RuleType import *


class PhoneticEnginePerformanceTest(unittest.TestCase):

    __LOOP: int = 80000

    def test(self) -> None:

        engine = PhoneticEngine.PhoneticEngine0(NameType.GENERIC, RuleType.APPROX, True)
        input = "Angelo"
        startMillis = int(round(time.time() * 1000))
        for i in range(self.__LOOP):
            engine.encode0(input)
        totalMillis = int(round(time.time() * 1000)) - startMillis
        print(
            "Time for encoding {:,} times the input '{}': {:,} millis.".format(
                self.__LOOP, input, totalMillis
            )
        )
