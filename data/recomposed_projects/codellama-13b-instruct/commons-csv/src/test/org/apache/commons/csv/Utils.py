# Imports Begin
from src.main.org.apache.commons.csv.CSVRecord import *
import unittest
import typing
from typing import *

# Imports End


class Utils(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def compare(
        message: str,
        expected: typing.List[typing.List[str]],
        actual: typing.List[CSVRecord],
    ) -> None:

        expected_length = len(expected)
        assert len(actual) == expected_length, message + "  - outer array size"
        for i in range(expected_length):
            assert actual[i].values() == expected[i], (
                message + " (entry " + str(i) + ")"
            )

    def __init__(self) -> None:

        pass

    # Class Methods End
