from __future__ import annotations
import time
import re
import unittest
import pytest
import io
import unittest
from src.main.org.joda.convert.StringConvert import *


class TestJavaTime(unittest.TestCase):

    def test_basics(self) -> None:

        test = StringConvert.INSTANCE

        zoneIdClass = type("java.time.ZoneId", (object,), {})
        self.assertEqual(
            "Europe/Paris",
            test.convertFromString(zoneIdClass, "Europe/Paris").toString(),
        )

        zoneRegionClass = type("java.time.ZoneRegion", (object,), {})
        self.assertEqual(
            "Europe/Paris",
            test.convertFromString(zoneRegionClass, "Europe/Paris").toString(),
        )
