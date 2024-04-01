# Imports Begin
from src.main.org.apache.commons.pool2.TrackedUse import *
import unittest

# Imports End


class DefaultTrackedUse(unittest.TestCase, TrackedUse):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def getLastUsed(self) -> int:

        return 1

    # Class Methods End


class TestTrackedUse(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testDefaultGetLastUsedInstant(self) -> None:

        pass  # LLM could not translate method body

    # Class Methods End
