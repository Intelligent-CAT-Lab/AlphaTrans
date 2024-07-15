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

        # Instantiate DefaultTrackedUse
        default_tracked_use = DefaultTrackedUse()

        # Assert that the getLastUsedInstant method returns the expected value
        self.assertEqual(
            datetime.datetime.fromtimestamp(1 / 1000.0, tz=datetime.timezone.utc),
            default_tracked_use.getLastUsedInstant(),
        )
