from __future__ import annotations
import re
import urllib
import unittest
import pytest
import pathlib
import io
import typing
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVRecord import *


class CSVFileParserTest:

    __BASE_DIR: pathlib.Path = pathlib.Path(
        "src/test/resources/org/apache/commons/csv/CSVFileParser"
    )

    @pytest.mark.skip(reason="Ignore")
    def testCSVUrl(self, testFile: pathlib.Path) -> None:

        with open(testFile, "r") as fr:
            testData = io.BufferedReader(fr)
            line = self.__readTestData(testData)
            assert line is not None, "file must contain config line"
            split = line.split(" ")
            assert len(split) >= 1, f"{testFile.name} require 1 param"
            format_ = CSVFormat.newFormat(",").withQuote0('"')
            checkComments = False
            for i in range(1, len(split)):
                option = split[i]
                option_parts = option.split("=", 1)
                if "IgnoreEmpty".lower() == option_parts[0].lower():
                    format_ = format_.withIgnoreEmptyLines1(bool(option_parts[1]))
                elif "IgnoreSpaces".lower() == option_parts[0].lower():
                    format_ = format_.withIgnoreSurroundingSpaces1(
                        bool(option_parts[1])
                    )
                elif "CommentStart".lower() == option_parts[0].lower():
                    format_ = format_.withCommentMarker0(option_parts[1][0])
                elif "CheckComments".lower() == option_parts[0].lower():
                    checkComments = True
                else:
                    pytest.fail(f"{testFile.name} unexpected option: {option}")

            line = self.__readTestData(testData)  # get string version of format
            assert line == format_.toString(), f"{testFile.name} Expected format"

            resource = urllib.parse.urljoin(
                "org/apache/commons/csv/CSVFileParser/", split[0]
            )
            with CSVParser.parse5(resource, "utf-8", format_) as parser:
                for record in parser:
                    parsed = str(record.values())
                    comment = record.getComment()
                    if checkComments and comment is not None:
                        parsed += "#" + comment.replace("\n", "\\n")
                    count = record.size()
                    assert (
                        self.__readTestData(testData) == f"{count}:{parsed}"
                    ), testFile.name

    @pytest.mark.skip(reason="Ignore")
    def testCSVFile(self, testFile: pathlib.Path) -> None:

        with open(testFile, "r") as fr:
            testData = io.BufferedReader(fr)
            line = self.__readTestData(testData)
            assert line is not None, "file must contain config line"
            split = line.split(" ")
            assert len(split) >= 1, testFile.name + " require 1 param"
            format_ = CSVFormat.newFormat(",").withQuote0('"')
            checkComments = False
            for i in range(1, len(split)):
                option = split[i]
                option_parts = option.split("=", 1)
                if "IgnoreEmpty".lower() == option_parts[0].lower():
                    format_ = format_.withIgnoreEmptyLines1(bool(option_parts[1]))
                elif "IgnoreSpaces".lower() == option_parts[0].lower():
                    format_ = format_.withIgnoreSurroundingSpaces1(
                        bool(option_parts[1])
                    )
                elif "CommentStart".lower() == option_parts[0].lower():
                    format_ = format_.withCommentMarker0(option_parts[1][0])
                elif "CheckComments".lower() == option_parts[0].lower():
                    checkComments = True
                else:
                    pytest.fail(testFile.name + " unexpected option: " + option)

            line = self.__readTestData(testData)  # get string version of format
            assert line == format_.toString(), testFile.name + " Expected format "

            parser = CSVFormat.parse0(
                pathlib.Path(self.__BASE_DIR, split[0]), "utf-8", format_
            )
            for record in parser:
                parsed = str(record.values())
                comment = record.getComment()
                if checkComments and comment is not None:
                    parsed += "#" + comment.replace("\n", "\\n")
                count = record.size()
                assert (
                    self.__readTestData(testData) == str(count) + ":" + parsed
                ), testFile.name

    @staticmethod
    def generateData() -> typing.Iterable[pathlib.Path]:

        files = CSVFileParserTest.__BASE_DIR.glob("test*.txt")
        return files

    def __readTestData(self, reader: io.BufferedReader) -> str:

        line = reader.readline()
        while line and line.startswith("#"):
            line = reader.readline()
        return line
