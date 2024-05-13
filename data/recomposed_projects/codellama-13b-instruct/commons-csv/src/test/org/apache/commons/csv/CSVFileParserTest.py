# Imports Begin
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVFormat import *
import typing
import unittest
import pathlib
# Imports End

class new FilenameFilter(...) { ... }(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def accept(self, dir: pathlib.Path, name: str) -> bool:

            return name.startswith("test") and name.endswith(".txt")

    # Class Methods End


class CSVFileParserTest(unittest.TestCase):

    # Class Fields Begin
    __CSV_FILE_NAME: str = "test.csv"
    # Class Fields End

    # Class Methods Begin
    def testCSVUrl(self, testFile: pathlib.Path) -> None:

        with open(testFile, "r") as fr, BufferedReader(fr) as testData:
            line = self.__readTestData(testData)
            self.assertIsNotNone(line, "file must contain config line")
            split = line.split(" ")
            self.assertGreaterEqual(len(split), 1, f"{testFile.name} require 1 param")
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
                    self.fail(f"{testFile.name} unexpected option: {option}")
            self.assertEqual(line, format.toString(), f"{testFile.name} Expected format ")
            resource = ClassLoader.getSystemResource(f"org/apache/commons/csv/CSVFileParser/{split[0]}")
            with CSVParser.parse5(resource, StandardCharsets.UTF_8, format) as parser:
                for record in parser:
                    parsed = str(record.values())
                    comment = record.getComment()
                    if checkComments and comment is not None:
                        parsed += "#" + comment.replace("\n", "\\n")
                    count = record.size()
                    self.assertEqual(readTestData(testData), f"{count}:{parsed}", f"{testFile.name}")

    def testCSVFile(self, testFile: pathlib.Path) -> None:

        with open(testFile, "r") as fr:
            testData = BufferedReader(fr)
            line = self.__readTestData(testData)
            self.assertNotNull("file must contain config line", line)
            split = line.split(" ")
            self.assertTrue(len(split) >= 1, testFile.name + " require 1 param")
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
                    self.fail(testFile.name + " unexpected option: " + option)
            line = self.__readTestData(testData)  # get string version of format
            self.assertEqual(line, format.toString(), testFile.name + " Expected format ")
            with CSVParser.parse0(
                testFile, Charset.defaultCharset(), format
            ) as parser:
                for record in parser:
                    parsed = Arrays.toString(record.values())
                    comment = record.getComment()
                    if checkComments and comment is not None:
                        parsed += "#" + comment.replace("\n", "\\n")
                    count = record.size()
                    self.assertEqual(
                        self.__readTestData(testData),
                        count + ":" + parsed,
                        testFile.name,
                    )

    @staticmethod

    def generateData() -> typing.Iterable[pathlib.Path]:

            files = Test.BASE_DIR.glob("test*.txt")
            return files

    def __readTestData(self, reader: io.BufferedReader) -> str:

            line: str = ""
            while line != None and not line.startswith("#"):
                line = reader.readline()
            return line

    # Class Methods End


