from __future__ import annotations
import time
import re
import urllib
import os
import datetime
import pathlib
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
            "u value",
            urllib.parse.urlparse("https://commons.apache.org"),
            line.getOptionObject1("u"),
        )
        self.assertIsNone("v value", line.getOptionObject1("v"))

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
            "java.util.Vector",
            "-e",
            "build.xml",
            "-f",
            "java.util.Calendar",
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

        self.assertEqual("flag a", "foo", line.getOptionValue4("a"))
        self.assertEqual("string flag a", "foo", line.getOptionObject1("a"))
        self.assertEqual("object flag b", Vector(), line.getOptionObject1("b"))
        self.assertTrue("boolean true flag c", line.hasOption2("c"))
        self.assertFalse("boolean false flag d", line.hasOption2("d"))
        self.assertEqual("file flag e", Path("build.xml"), line.getOptionObject1("e"))
        self.assertEqual("class flag f", Calendar, line.getOptionObject1("f"))
        self.assertEqual("number flag n", 4.5, line.getOptionObject1("n"))
        self.assertEqual(
            "url flag t",
            urlparse("https://commons.apache.org"),
            line.getOptionObject1("t"),
        )

        self.assertEqual("flag a", "foo", line.getOptionValue0("a"))
        self.assertEqual("string flag a", "foo", line.getOptionObject0("a"))
        self.assertEqual("object flag b", Vector(), line.getOptionObject0("b"))
        self.assertTrue("boolean true flag c", line.hasOption0("c"))
        self.assertFalse("boolean false flag d", line.hasOption0("d"))
        self.assertEqual("file flag e", Path("build.xml"), line.getOptionObject0("e"))
        self.assertEqual("class flag f", Calendar, line.getOptionObject0("f"))
        self.assertEqual("number flag n", 4.5, line.getOptionObject0("n"))
        self.assertEqual(
            "url flag t",
            urlparse("https://commons.apache.org"),
            line.getOptionObject0("t"),
        )

        with self.assertRaises(NotImplementedError):
            self.assertEqual("files flag m", [], line.getOptionObject0("m"))

        with self.assertRaises(NotImplementedError):
            self.assertEqual(
                "date flag z",
                datetime.strptime(
                    "Thu Jun 06 17:48:57 EDT 2002", "%a %b %d %H:%M:%S %Z %Y"
                ),
                line.getOptionObject0("z"),
            )

    def testRequiredOption(self) -> None:

        options = PatternOptionBuilder.parsePattern("n%m%")
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

        self.assertEqual("n object class", int, type(line.getOptionObject1("n")))
        self.assertEqual("n value", 1, line.getOptionObject1("n"))

        self.assertEqual("d object class", float, type(line.getOptionObject1("d")))
        self.assertEqual("d value", 2.1, line.getOptionObject1("d"))

        self.assertIsNone("x object", line.getOptionObject1("x"))

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

        parsedReadableFileStream = line.getOptionObject1("g")

        self.assertIsNotNone(parsedReadableFileStream, "option g not parsed")
        self.assertIsInstance(
            parsedReadableFileStream, io.FileIO, "option g not FileInputStream"
        )

    def testEmptyPattern(self) -> None:

        options = PatternOptionBuilder.parsePattern("")
        self.assertTrue(len(options.getOptions()) == 0)

    def testClassPattern(self) -> None:

        options = PatternOptionBuilder.parsePattern("c+d+")
        parser = PosixParser()
        line = parser.parse0(
            options, ["-c", "java.util.Calendar", "-d", "System.DateTime"]
        )

        self.assertEqual("c value", java.util.Calendar, line.getOptionObject1("c"))
        self.assertIsNone("d value", line.getOptionObject1("d"))
