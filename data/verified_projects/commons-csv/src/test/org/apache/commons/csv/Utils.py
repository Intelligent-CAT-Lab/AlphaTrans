import pytest

from src.main.org.apache.commons.csv.CSVRecord import *
import unittest


class Utils(unittest.TestCase):

    def __init__(self) -> None:
        pass

    
    @staticmethod
    def compare(message, expected, actual) -> None:
        expectedLength = len(expected)
        unittest.TestCase().assertEqual(
            len(actual),
            expectedLength,
            message + "  - outer array size"
        )
        for i in range(expectedLength):
            unittest.TestCase().assertEqual(
                expected[i],
                actual[i].values(),
                message + " (entry " + str(i) + ")"
            )
