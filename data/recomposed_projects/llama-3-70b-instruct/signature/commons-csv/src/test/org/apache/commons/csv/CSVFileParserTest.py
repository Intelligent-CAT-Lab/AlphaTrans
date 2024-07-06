from __future__ import annotations
import re
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
            assert len(split) >= 1, testFile.name + " require 1 param"
            format = CSVFormat.newFormat(",").withQuote0('"')
            checkComments = False
            for i in range(1, len(split)):
                option = split[i]
                option_parts = option.split("=", 2)
                if "IgnoreEmpty".equalsIgnoreCase(option_parts[0]):
                    format = format.withIgnoreEmptyLines1(bool(option_parts[1]))
                elif "IgnoreSpaces".equalsIgnoreCase(option_parts[0]):
                    format = format.withIgnoreSurroundingSpaces1(bool(option_parts[1]))
                elif "CommentStart".equalsIgnoreCase(option_parts[0]):
                    format = format.withCommentMarker0(option_parts[1][0])
                elif "CheckComments".equalsIgnoreCase(option_parts[0]):
                    checkComments = True
                else:
                    assert False, testFile.name + " unexpected option: " + option
            line = self.__readTestData(testData)  # get string version of format
            assert line == format.toString(), testFile.name + " Expected format "
            resource = ClassLoader.getSystemResource(
                "org/apache/commons/csv/CSVFileParser/" + split[0]
            )
            with CSVParser.parse5(resource, StandardCharsets.UTF_8, format) as parser:
                for record in parser:
                    parsed = str(record.values())
                    comment = record.getComment()
                    if checkComments and comment is not None:
                        parsed += "#" + comment.replace("\n", "\\n")
                    count = record.size()
                    assert (
                        self.__readTestData(testData) == str(count) + ":" + parsed
                    ), testFile.name

    @pytest.mark.skip(reason="Ignore")
    def testCSVFile(self, testFile: pathlib.Path) -> None:
        with io.BufferedReader(io.FileReader(testFile)) as testData:
            line = self.__readTestData(testData)
            assert line is not None, "file must contain config line"
            split = line.split(" ")
            assert len(split) >= 1, testFile.name + " require 1 param"
            format = CSVFormat.newFormat(",").withQuote0('"')
            checkComments = False
            for i in range(1, len(split)):
                option = split[i]
                option_parts = option.split("=", 2)
                if "IgnoreEmpty".equalsIgnoreCase(option_parts[0]):
                    format = format.withIgnoreEmptyLines1(
                        Boolean.parseBoolean(option_parts[1])
                    )
                elif "IgnoreSpaces".equalsIgnoreCase(option_parts[0]):
                    format = format.withIgnoreSurroundingSpaces1(
                        Boolean.parseBoolean(option_parts[1])
                    )
                elif "CommentStart".equalsIgnoreCase(option_parts[0]):
                    format = format.withCommentMarker0(option_parts[1].charAt(0))
                elif "CheckComments".equalsIgnoreCase(option_parts[0]):
                    checkComments = True
                else:
                    assert False, testFile.name + " unexpected option: " + option
            line = self.__readTestData(testData)  # get string version of format
            assert line == format.toString(), testFile.name + " Expected format "

            with CSVParser.parse0(
                pathlib.Path(self.__BASE_DIR, split[0]),
                Charset.defaultCharset(),
                format,
            ) as parser:
                for record in parser:
                    parsed = Arrays.toString(record.values())
                    comment = record.getComment()
                    if checkComments and comment is not None:
                        parsed += "#" + comment.replace("\n", "\\n")
                    count = record.size()
                    assert (
                        self.__readTestData(testData) == count + ":" + parsed
                    ), testFile.name

    @staticmethod
    def generateData() -> typing.Iterable[pathlib.Path]:
        return filter(
            lambda p: p.name.startswith("test") and p.name.endswith(".txt"),
            CSVFileParserTest.__BASE_DIR.iterdir(),
        )

    def __readTestData(self, reader: io.BufferedReader) -> str:
        line: str
        while True:
            line = reader.readline()
            if line is None or not line.startswith("#"):
                break
        return line
