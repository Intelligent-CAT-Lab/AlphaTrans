from __future__ import annotations
import re
import typing
from typing import *
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVRecord import *


class JiraCsv290Test(unittest.TestCase):

    def testPostgresqlText(self) -> None:

        self.__testHelper("psql.tsv", CSVFormat.POSTGRESQL_TEXT)

    def testPostgresqlCsv(self) -> None:

        self.__testHelper("psql.csv", CSVFormat.POSTGRESQL_CSV)

    def __testHelper(self, filename: str, format: CSVFormat) -> None:

        content = []
        with CSVParser.parse3(
            io.TextIOWrapper(
                io.BufferedReader(
                    open(
                        os.path.join(
                            os.path.dirname(__file__),
                            "org",
                            "apache",
                            "commons",
                            "csv",
                            "CSV-290",
                            filename,
                        ),
                        "r",
                    )
                )
            ),
            format,
        ) as csvParser:
            content = [record.toList() for record in csvParser.stream()]

        assert len(content) == 3

        assert content[0][0] == "1"
        assert content[0][1] == "abc"
        assert content[0][2] == "test line 1\ntest line 2"  # new line
        assert content[0][3] == None  # null
        assert content[0][4] == ""

        assert content[1][0] == "2"
        assert content[1][2] == "\\b:\b \\t:\t \\n:\n \\r:\r"  # \b, \t, \n, \r

        assert content[2][0] == "3"
        assert content[2][2] == "b,c,d"  # value has comma
        assert content[2][3] == '"quoted"'  # quoted
