from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.apache.commons.csv.CSVRecord import *


class Utils:

    @staticmethod
    def compare(
        message: str,
        expected: typing.List[typing.List[str]],
        actual: typing.List[CSVRecord],
    ) -> None:

        expected_length = len(expected)
        assert expected_length == len(actual), message + "  - outer array size"
        for i in range(expected_length):
            assert expected[i] == actual[i].values(), (
                message + " (entry " + str(i) + ")"
            )

    def __init__(self) -> None:
        pass
