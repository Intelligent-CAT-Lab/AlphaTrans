from __future__ import annotations
import time
import re
import urllib
import os
from datetime import datetime
import pathlib
import unittest
import urllib.parse
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
            urllib.parse.urlparse("https://commons.apache.org"),
            line.getOptionObject1("u"),
            "u value"
        )
        self.assertIsNone(line.getOptionObject1("v"), "v value")

    def testUntypedPattern(self) -> None:

        options = PatternOptionBuilder.parsePattern("abc")
        parser = PosixParser()
        line = parser.parse0(options, ["-abc"])

        self.assertTrue(line.hasOption0("a"))
        self.assertIsNone(line.getOptionObject0("a"))
        self.assertTrue(line.hasOption0("b"))
        self.assertIsNone(line.getOptionObject0("b"))
        self.assertTrue(line.hasOption0("c"))
        self.assertIsNone(line.getOptionObject0("c"))

    def testSimplePattern(self) -> None:

        options = PatternOptionBuilder.parsePattern("a:b@cde>f+n%t/m*z#")
        args = [
            "-c",
            "-a",
            "foo",
            "-b",
            "list",
            "-e",
            "build.xml",
            "-f",
            "datetime",
            "-n",
            "4.5",
            "-t",
            "https://commons.apache.org",
            "-z",
            "Thu Jun 06 17:48:57 EDT 2002",
            "-m",
            "test*",
        ]

        parser = PosixParser()
        line = parser.parse0(options, args)

        self.assertEqual("foo", line.getOptionValue0("a"), "flag a")
        self.assertEqual("foo", line.getOptionObject0("a"), "string flag a")
        self.assertEqual(list(), line.getOptionObject0("b"), "object flag b")
        self.assertTrue(line.hasOption0("c"), "boolean true flag c")
        self.assertFalse(line.hasOption0("d"), "boolean false flag d")
        self.assertEqual(pathlib.Path("build.xml"), line.getOptionObject0("e"), "file flag e")
        self.assertEqual(datetime, line.getOptionObject0("f"), "class flag f")
        self.assertEqual(4.5, line.getOptionObject0("n"), "number flag n")
        self.assertEqual(
            urllib.parse.urlparse("https://commons.apache.org"),
            line.getOptionObject0("t"),
            "url flag t"
        )

        try:
            self.assertEqual(
                [pathlib.Path("test*")], line.getOptionObject0("m"), "files flag m"
            )
            self.fail("Multiple files are not supported yet, should have failed")
        except NotImplementedError as uoe:
            pass

        try:
            self.assertEqual(
                datetime.fromtimestamp(1023400137276 / 1000),
                line.getOptionObject0("z"),
                "date flag z"
            )
            self.fail("Date is not supported yet, should have failed")
        except NotImplementedError as uoe:
            pass

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
                "str",
                "-i",
                "datetime",
                "-n",
                "System.DateTime",
            ],
        )

        self.assertEqual("", line.getOptionObject1("o"), "o value")
        self.assertIsNone(line.getOptionObject1("i"), "i value")
        self.assertIsNone(line.getOptionObject1("n"), "n value")

    def testNumberPattern(self) -> None:

        options = PatternOptionBuilder.parsePattern("n%d%x%")
        parser = PosixParser()
        line = parser.parse0(options, ["-n", "1", "-d", "2.1", "-x", "3,5"])

        self.assertEqual(int, type(line.getOptionObject1("n")), "n object class")
        self.assertEqual(1, line.getOptionObject1("n"), "n value")

        self.assertEqual(float, type(line.getOptionObject1("d")), "d object class")
        self.assertEqual(2.1, line.getOptionObject1("d"), "d value")

        self.assertIsNone(line.getOptionObject1("x"))

    def testExistingFilePatternFileNotExist(self) -> None:

        options = PatternOptionBuilder.parsePattern("f<")
        parser = PosixParser()
        line = parser.parse0(options, ["-f", "non-existing.file"])

        self.assertIsNone(line.getOptionObject1("f"))

    def testExistingFilePattern(self) -> None:

        options = PatternOptionBuilder.parsePattern("g<")
        parser = PosixParser()
        line = parser.parse0(
            options,
            ["-g", "src/test/resources/org/apache/commons/cli/existing-readable.file"],
        )

        parsed_readable_file_stream = line.getOptionObject1("g")

        self.assertIsNotNone(parsed_readable_file_stream, "option g not parsed")
        self.assertIsInstance(
            parsed_readable_file_stream, io.TextIOWrapper, "option g not FileInputStream"
        )

    def testEmptyPattern(self) -> None:

        options = PatternOptionBuilder.parsePattern("")
        self.assertTrue(len(list(options.getOptions())) == 0)

    def testClassPattern(self) -> None:

        options = PatternOptionBuilder.parsePattern("c+d+")
        parser = PosixParser()
        line = parser.parse0(
            options, ["-c", "datetime", "-d", "System.DateTime"]
        )

        self.assertEqual(datetime, line.getOptionObject1("c"), "c value")
        self.assertIsNone(line.getOptionObject1("d"), "d value")
