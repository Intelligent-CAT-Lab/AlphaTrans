from __future__ import annotations
import time
import re
import datetime
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.pool2.TrackedUse import *


class DefaultTrackedUse(TrackedUse):

    def getLastUsed(self) -> int:
        return 1


class TestTrackedUse(unittest.TestCase):

    def testDefaultGetLastUsedInstant(self) -> None:
        self.assertEqual(
            datetime.datetime.fromtimestamp(1), DefaultTrackedUse().getLastUsedInstant()
        )
