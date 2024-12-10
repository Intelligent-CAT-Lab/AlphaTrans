from __future__ import annotations
import pytest
import unittest
import os
from pathlib import Path
import locale
from urllib.parse import urlparse
from typing import Generator
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVRecord import *

BASE_DIR = Path(__file__).resolve()\
    .parent.parent.parent.parent\
    .parent / 'resources' / 'org' / 'apache' / 'commons' / 'csv' / 'CSVFileParser' 


def generateData() -> Generator:
    for filename in os.listdir(BASE_DIR):
        if filename.startswith('test') and filename.endswith('.txt'):
            yield os.path.join(BASE_DIR, filename)


class CSVFileParserTest(unittest.TestCase):

    def readTestData(self, reader: io.BufferedReader) -> str:
        try:
            while True:
                line = reader.readline()
                if not line:
                    return None
                if not line.startswith('#'):
                    return line.strip()
        except (IOError, OSError) as e:
            self.fail("An error occurred when reading data: " + str(e))

    
    def _testCSVFile(self, testFile: pathlib.Path) -> None:
        with open(testFile, 'r', encoding='utf-8') as fr:
            line = self.readTestData(fr)
            self.assertIsNotNone(line, "file must contain config line")
            split = line.split(" ")
            self.assertTrue(len(split) >= 1, f"{os.path.basename(testFile)} require 1 param")
            format = CSVFormat.newFormat(',').withQuote0('"')
            checkComments = False
            for option in split[1:]:
                optionParts = option.split("=", 2)
                if optionParts[0].lower() == "ignoreempty":
                    format = format.withIgnoreEmptyLines1(optionParts[1].lower() == 'true')
                elif optionParts[0].lower() == "ignorespaces":
                    format = format.withIgnoreSurroundingSpaces1(
                        optionParts[1].lower() == 'true'
                    )
                elif optionParts[0].lower() == "commentstart":
                    format = format.withCommentMarker0(optionParts[1][0])
                elif optionParts[0].lower() == "checkcomments":
                    checkComments = True
                else:
                    self.fail(f"{os.path.basename(testFile)} unexpected option: {option}")
            line = self.readTestData(fr)
            self.assertEqual(
                line,
                format.toString(),
                f"{os.path.basename(testFile)} Expected format "
            )

            parser = CSVParser.parse0(
                    Path.joinpath(BASE_DIR, split[0]), 
                    locale.getpreferredencoding(), 
                    format
                )
            try:
                for record in parser:
                    parsed = "[" + ", ".join(str(e) for e in record.values()) + "]"
                    comment = record.getComment()
                    if (checkComments and comment != None):
                        parsed += ("#" + comment.replace("\n", "\\n"))
                    count = record.size()
                    self.assertEqual(
                        self.readTestData(fr),
                        str(count) + ":" + parsed,
                        os.path.basename(testFile)
                    )
            finally:
                parser.close()

    
    def _testCSVUrl(self, testFile: pathlib.Path) -> None:
        with open(testFile, 'r', encoding='utf-8') as fr:
            line = self.readTestData(fr)
            self.assertIsNotNone(line, "file must contain config line")
            split = line.split(" ")
            self.assertTrue(len(split) >= 1, f"{os.path.basename(testFile)} require 1 param")
            format = CSVFormat.newFormat(',').withQuote0('"')
            checkComments = False
            for option in split[1:]:
                optionParts = option.split("=", 2)
                if optionParts[0].lower() == "ignoreempty":
                    format = format.withIgnoreEmptyLines1(optionParts[1].lower() == 'true')
                elif optionParts[0].lower() == "ignorespaces":
                    format = format.withIgnoreSurroundingSpaces1(
                        optionParts[1].lower() == 'true'
                    )
                elif optionParts[0].lower() == "commentstart":
                    format = format.withCommentMarker0(optionParts[1][0])
                elif optionParts[0].lower() == "checkcomments":
                    checkComments = True
                else:
                    self.fail(f"{os.path.basename(testFile)} unexpected option: {option}")
            line = self.readTestData(fr)
            self.assertEqual(
                line,
                format.toString(),
                f"{os.path.basename(testFile)} Expected format "
            )

            resource = urlparse(Path.joinpath(BASE_DIR, split[0]).as_uri())
            parser = CSVParser.parse5(resource, 'utf-8', format)
            try:
                for record in parser:
                    parsed = "[" + ", ".join(str(e) for e in record.values()) + "]"
                    comment = record.getComment()
                    if (checkComments and comment != None):
                        parsed += ("#" + comment.replace("\n", "\\n"))
                    count = record.size()
                    self.assertEqual(
                        self.readTestData(fr),
                        str(count) + ":" + parsed,
                        os.path.basename(testFile)
                    )
            finally:
                parser.close()


@pytest.mark.parametrize("testFile", generateData())
def testCSVFile(testFile) -> None:
    test = CSVFileParserTest()
    test._testCSVFile(testFile)


@pytest.mark.parametrize("testFile", generateData())
def testCSVUrl(testFile) -> None:
    test = CSVFileParserTest()
    test._testCSVUrl(testFile)
