from __future__ import annotations
import unittest
import pytest
import io
import numbers
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

        assert line.hasOption0("a")
        assert line.getOptionObject0("a") is None
        assert line.hasOption0("b")
        assert line.getOptionObject0("b") is None
        assert line.hasOption0("c")
        assert line.getOptionObject0("c") is None

    def testSimplePattern(self) -> None:

        pass  # LLM could not translate this method

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

        assert line.getOptionObject1("o") == "", "o value"
        assert line.getOptionObject1("i") is None, "i value"
        assert line.getOptionObject1("n") is None, "n value"

    def testNumberPattern(self) -> None:

        options = PatternOptionBuilder.parsePattern("n%d%x%")
        parser = PosixParser()
        line = parser.parse0(options, ["-n", "1", "-d", "2.1", "-x", "3,5"])

        self.assertEqual(
            "n object class", numbers.Integral, type(line.getOptionObject1("n"))
        )
        self.assertEqual("n value", 1, line.getOptionObject1("n"))

        self.assertEqual("d object class", float, type(line.getOptionObject1("d")))
        self.assertEqual("d value", 2.1, line.getOptionObject1("d"))

        self.assertIsNone("x object", line.getOptionObject1("x"))

    def testExistingFilePatternFileNotExist(self) -> None:

        options = PatternOptionBuilder.parsePattern("f<")
        parser = PosixParser()
        line = parser.parse0(options, ["-f", "non-existing.file"])

        assert line.getOptionObject1("f") is None, "option f parsed"

    def testExistingFilePattern(self) -> None:

        options = PatternOptionBuilder.parsePattern("g<")
        parser = PosixParser()
        line = parser.parse0(
            options,
            ["-g", "src/test/resources/org/apache/commons/cli/existing-readable.file"],
        )

        parsedReadableFileStream = line.getOptionObject1("g")

        assert parsedReadableFileStream is not None, "option g not parsed"
        assert isinstance(
            parsedReadableFileStream, io.FileIO
        ), "option g not FileInputStream"

    def testEmptyPattern(self) -> None:

        options = PatternOptionBuilder.parsePattern("")
        assert len(options.getOptions()) == 0

    def testClassPattern(self) -> None:

        options = PatternOptionBuilder.parsePattern("c+d+")
        parser = PosixParser()
        line = parser.parse0(
            options, ["-c", "java.util.Calendar", "-d", "System.DateTime"]
        )

        assert "c value" == line.getOptionObject1("c")
        assert "d value" == line.getOptionObject1("d")
