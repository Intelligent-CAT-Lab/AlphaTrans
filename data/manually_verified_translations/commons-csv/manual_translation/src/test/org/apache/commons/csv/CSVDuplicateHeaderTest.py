from __future__ import annotations
import copy
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.apache.commons.csv.DuplicateHeaderMode import *


class CSVDuplicateHeaderTest:

    @staticmethod
    def duplicateHeaderData() -> typing.Iterable[typing.List]:

        return [
            (
                DuplicateHeaderMode.DISALLOW,
                False,
                False,
                ["A", "B"],
                True
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                False,
                False,
                ["A", "B"],
                True
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                False,
                False,
                ["A", "B"],
                True
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                True,
                False,
                ["A", "B"],
                True
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                True,
                False,
                ["A", "B"],
                True
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                True,
                False,
                ["A", "B"],
                True
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                False,
                False,
                ["A", ""],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                False,
                False,
                ["A", ""],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                False,
                False,
                ["A", ""],
                False
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                True,
                False,
                ["A", ""],
                True
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                True,
                False,
                ["A", ""],
                True
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                True,
                False,
                ["A", ""],
                True
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                False,
                False,
                ["A", " "],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                False,
                False,
                ["A", " "],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                False,
                False,
                ["A", " "],
                False
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                True,
                False,
                ["A", " "],
                True
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                True,
                False,
                ["A", " "],
                True
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                True,
                False,
                ["A", " "],
                True
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                False,
                False,
                ["A", None],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                False,
                False,
                ["A", None],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                False,
                False,
                ["A", None],
                False
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                True,
                False,
                ["A", None],
                True
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                True,
                False,
                ["A", None],
                True
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                True,
                False,
                ["A", None],
                True
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                False,
                False,
                ["A", "A"],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                False,
                False,
                ["A", "A"],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                False,
                False,
                ["A", "A"],
                True
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                True,
                False,
                ["A", "A"],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                True,
                False,
                ["A", "A"],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                True,
                False,
                ["A", "A"],
                True
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                False,
                False,
                ["", ""],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                False,
                False,
                ["", ""],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                False,
                False,
                ["", ""],
                False
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                True,
                False,
                ["", ""],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                True,
                False,
                ["", ""],
                True
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                True,
                False,
                ["", ""],
                True
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                False,
                False,
                [" ", " "],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                False,
                False,
                [" ", " "],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                False,
                False,
                [" ", " "],
                False
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                True,
                False,
                [" ", " "],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                True,
                False,
                [" ", " "],
                True
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                True,
                False,
                [" ", " "],
                True
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                False,
                False,
                ["   ", "   "],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                False,
                False,
                ["   ", "   "],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                False,
                False,
                ["   ", "   "],
                False
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                True,
                False,
                ["   ", "   "],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                True,
                False,
                ["   ", "   "],
                True
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                True,
                False,
                ["   ", "   "],
                True
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                False,
                False,
                [None, None],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                False,
                False,
                [None, None],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                False,
                False,
                [None, None],
                False
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                True,
                False,
                [None, None],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                True,
                False,
                [None, None],
                True
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                True,
                False,
                [None, None],
                True
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                False,
                False,
                [" ", "   "],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                False,
                False,
                [" ", "   "],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                False,
                False,
                [" ", "   "],
                False
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                True,
                False,
                [" ", "   "],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                True,
                False,
                [" ", "   "],
                True
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                True,
                False,
                [" ", "   "],
                True
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                False,
                False,
                [" ", None],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                False,
                False,
                [" ", None],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                False,
                False,
                [" ", None],
                False
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                True,
                False,
                [" ", None],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                True,
                False,
                [" ", None],
                True
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                True,
                False,
                [" ", None],
                True
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                False,
                False,
                ["A", "A", "", ""],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                False,
                False,
                ["A", "A", "", ""],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                False,
                False,
                ["A", "A", "", ""],
                False
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                True,
                False,
                ["A", "A", "", ""],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                True,
                False,
                ["A", "A", "", ""],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                True,
                False,
                ["A", "A", "", ""],
                True
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                False,
                False,
                ["A", "B", "", ""],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                False,
                False,
                ["A", "B", "", ""],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                False,
                False,
                ["A", "B", "", ""],
                False
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                True,
                False,
                ["A", "B", "", ""],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                True,
                False,
                ["A", "B", "", ""],
                True
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                True,
                False,
                ["A", "B", "", ""],
                True
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                False,
                False,
                ["A", "A", " ", " "],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                False,
                False,
                ["A", "A", " ", " "],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                False,
                False,
                ["A", "A", " ", " "],
                False
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                True,
                False,
                ["A", "A", " ", " "],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                True,
                False,
                ["A", "A", " ", " "],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                True,
                False,
                ["A", "A", " ", " "],
                True
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                False,
                False,
                ["A", "A", None, None],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                False,
                False,
                ["A", "A", None, None],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                False,
                False,
                ["A", "A", None, None],
                False
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                True,
                False,
                ["A", "A", None, None],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                True,
                False,
                ["A", "A", None, None],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                True,
                False,
                ["A", "A", None, None],
                True
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                False,
                False,
                ["A", "", ""],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                False,
                False,
                ["A", "", ""],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                False,
                False,
                ["A", "", ""],
                False
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                True,
                False,
                ["A", "", ""],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                True,
                False,
                ["A", "", ""],
                True
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                True,
                False,
                ["A", "", ""],
                True
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                False,
                False,
                ["A", None, None],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                False,
                False,
                ["A", None, None],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                False,
                False,
                ["A", None, None],
                False
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                True,
                False,
                ["A", None, None],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                True,
                False,
                ["A", None, None],
                True
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                True,
                False,
                ["A", None, None],
                True
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                False,
                False,
                ["A", " ", "   "],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                False,
                False,
                ["A", " ", "   "],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                False,
                False,
                ["A", " ", "   "],
                False
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                True,
                False,
                ["A", " ", "   "],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                True,
                False,
                ["A", " ", "   "],
                True
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                True,
                False,
                ["A", " ", "   "],
                True
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                False,
                True,
                ["A", "a"],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                False,
                True,
                ["A", "a"],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                False,
                True,
                ["A", "a"],
                True
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                True,
                True,
                ["A", "a"],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                True,
                True,
                ["A", "a"],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                True,
                True,
                ["A", "a"],
                True
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                False,
                True,
                ["A", "a", "", ""],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                False,
                True,
                ["A", "a", "", ""],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                False,
                True,
                ["A", "a", "", ""],
                False
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                True,
                True,
                ["A", "a", "", ""],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                True,
                True,
                ["A", "a", "", ""],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                True,
                True,
                ["A", "a", "", ""],
                True
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                False,
                True,
                ["A", "a", " ", " "],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                False,
                True,
                ["A", "a", " ", " "],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                False,
                True,
                ["A", "a", " ", " "],
                False
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                True,
                True,
                ["A", "a", " ", " "],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                True,
                True,
                ["A", "a", " ", " "],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                True,
                True,
                ["A", "a", " ", " "],
                True
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                False,
                True,
                ["A", "a", None, None],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                False,
                True,
                ["A", "a", None, None],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                False,
                True,
                ["A", "a", None, None],
                False
            ),
            (
                DuplicateHeaderMode.DISALLOW,
                True,
                True,
                ["A", "a", None, None],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_EMPTY,
                True,
                True,
                ["A", "a", None, None],
                False
            ),
            (
                DuplicateHeaderMode.ALLOW_ALL,
                True,
                True,
                ["A", "a", None, None],
                True
            )
        ]

    @staticmethod
    def duplicateHeaderAllowsMissingColumnsNamesData() -> typing.Iterable[typing.List]:

        data = []
        for arg in CSVDuplicateHeaderTest.duplicateHeaderData():
            if arg[1] == True and arg[2] == False:
                for a in [True, False]:
                    for b in [True, False]:
                        newArg = list(arg)
                        newArg[1] = a
                        newArg[2] = b
                        data.append(tuple(newArg))
        return data
