from __future__ import annotations
import re
import os
import unittest
import pytest
import io
import numbers
import unittest
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.MissingOptionException import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.PatternOptionBuilder import *
from src.main.org.apache.commons.cli.PosixParser import *


class PatternOptionBuilderTest(unittest.TestCase):

    def testURLPattern(self) -> None:
        options = PatternOptionBuilder.parsePattern("u/v/")
        parser = PosixParser()
        line = parser.parse0(
            options,
            ["-u", "https://commons.apache.org", "-v", "foo://commons.apache.org"],
        )
        self.assertEqual(
            "u value", URL("https://commons.apache.org"), line.getOptionObject1("u")
        )
        self.assertIsNone("v value", line.getOptionObject1("v"))

    def testUntypedPattern(self) -> None:
        options = PatternOptionBuilder.parsePattern("abc")
        parser = PosixParser()
        line = parser.parse0(options, ["-abc"])

        self.assertTrue(line.hasOption0("a"))
        self.assertIsNone("value a", line.getOptionObject0("a"))
        self.assertTrue(line.hasOption0("b"))
        self.assertIsNone("value b", line.getOptionObject0("b"))
        self.assertTrue(line.hasOption0("c"))
        self.assertIsNone("value c", line.getOptionObject0("c"))

    def testSimplePattern(self) -> None:

        pass  # LLM could not translate this method

    def testRequiredOption(self) -> None:
        options = PatternOptionBuilder.parsePattern("!n%m%")
        parser = PosixParser()

        try:
            parser.parse0(options, [""])
            self.fail("MissingOptionException wasn't thrown")
        except MissingOptionException as e:
            self.assertEqual(1, len(e.getMissingOptions()))
            self.assertTrue("n" in e.getMissingOptions())

    def testObjectPattern(self) -> None:
        options = PatternOptionBuilder.parsePattern("o@i@n@")
        parser = PosixParser()
        line = parser.parse0(
            options,
            [
                "-o",
                "java.lang.String",
                "-i",
                "java.util.Calendar",
                "-n",
                "System.DateTime",
            ],
        )

        self.assertEqual("o value", "", line.getOptionObject1("o"))
        self.assertIsNone("i value", line.getOptionObject1("i"))
        self.assertIsNone("n value", line.getOptionObject1("n"))

    def testNumberPattern(self) -> None:
        options = PatternOptionBuilder.parsePattern("n%d%x%")
        parser = PosixParser()
        line = parser.parse0(options, ["-n", "1", "-d", "2.1", "-x", "3,5"])

        self.assertEqual("n object class", Long, line.getOptionObject1("n").__class__)
        self.assertEqual("n value", Long(1), line.getOptionObject1("n"))

        self.assertEqual("d object class", Double, line.getOptionObject1("d").__class__)
        self.assertEqual("d value", Double(2.1), line.getOptionObject1("d"))

        self.assertIsNone("x object", line.getOptionObject1("x"))

    def testExistingFilePatternFileNotExist(self) -> None:
        options = PatternOptionBuilder.parsePattern("f<")
        parser = PosixParser()
        line = parser.parse0(options, ["-f", "non-existing.file"])
        self.assertIsNone("option f parsed", line.getOptionObject1("f"))

    def testExistingFilePattern(self) -> None:
        options = PatternOptionBuilder.parsePattern("g<")
        parser = PosixParser()
        line = parser.parse0(
            options,
            ["-g", "src/test/resources/org/apache/commons/cli/existing-readable.file"],
        )
        parsedReadableFileStream = line.getOptionObject1("g")
        self.assertIsNotNone(parsedReadableFileStream, "option g not parsed")
        self.assertIsInstance(
            parsedReadableFileStream, io.FileIO, "option g not FileInputStream"
        )

    def testEmptyPattern(self) -> None:
        options = PatternOptionBuilder.parsePattern("")
        self.assertTrue(options.getOptions().isEmpty())

    def testClassPattern(self) -> None:
        options = PatternOptionBuilder.parsePattern("c+d+")
        parser = PosixParser()
        line = parser.parse0(
            options, ["-c", "java.util.Calendar", "-d", "System.DateTime"]
        )
        self.assertEqual("c value", Calendar, line.getOptionObject1("c"))
        self.assertIsNone("d value", line.getOptionObject1("d"))
