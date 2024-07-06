from __future__ import annotations
import time
import re
import typing
from typing import *
import unittest
import pytest
import io
import unittest
from src.main.org.joda.convert.StringConvert import *


class TestJavaTime(unittest.TestCase):

    def test_basics(self) -> None:
        test: StringConvert = StringConvert.INSTANCE

        zoneIdClass: typing.Type[typing.Any] = type("java.time.ZoneId")
        self.assertEqual(
            "Europe/Paris",
            test.convertFromString(zoneIdClass, "Europe/Paris").toString(),
        )

        zoneRegionClass: typing.Type[typing.Any] = type("java.time.ZoneRegion")
        self.assertEqual(
            "Europe/Paris",
            test.convertFromString(zoneRegionClass, "Europe/Paris").toString(),
        )
