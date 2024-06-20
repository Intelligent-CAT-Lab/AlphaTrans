from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.TrackedUse import *
import unittest
import io

# Imports End


class DefaultTrackedUse(TrackedUse):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def getLastUsed(self) -> int:
        pass

    # Class Methods End


class TestTrackedUse(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testDefaultGetLastUsedInstant(self) -> None:
        pass

    # Class Methods End
