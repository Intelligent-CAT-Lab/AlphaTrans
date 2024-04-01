# Imports Begin
from src.main.org.apache.commons.cli.PosixParser import *
from src.main.org.apache.commons.cli.PatternOptionBuilder import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.MissingOptionException import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.CommandLine import *
import unittest
import os
import numbers

# Imports End


class PatternOptionBuilderTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testURLPattern(self) -> None:

        options = PatternOptionBuilder.parsePattern("u/v/")
        parser = PosixParser()
        line = parser.parse0(
            options,
            ["-u", "https://commons.apache.org", "-v", "foo://commons.apache.org"],
        )
        self.assertEqual(line.getOptionObject1("u"), URL("https://commons.apache.org"))
        self.assertIsNone(line.getOptionObject1("v"))

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

        pass  # LLM could not translate method body

    def testRequiredOption(self) -> None:

        options = self.parsePattern("!n%m%")
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
        self.assertEqual(line.getOptionObject1("n").__class__, int)
        self.assertEqual(line.getOptionObject1("n"), 1)
        self.assertEqual(line.getOptionObject1("d").__class__, float)
        self.assertEqual(line.getOptionObject1("d"), 2.1)
        self.assertIsNone(line.getOptionObject1("x"))

    def testExistingFilePatternFileNotExist(self) -> None:

        options = self.parsePattern("f<")
        parser = PosixParser()
        line = parser.parse0(options, ["-f", "non-existing.file"])
        self.assertIsNone(line.getOptionObject1("f"))

    def testExistingFilePattern(self) -> None:

        options = self.parsePattern("g<")
        parser = PosixParser()
        line = parser.parse0(
            options,
            ["-g", "src/test/resources/org/apache/commons/cli/existing-readable.file"],
        )
        parsed_readable_file_stream = line.getOptionObject1("g")
        self.assertIsNotNone(parsed_readable_file_stream)
        self.assertTrue(isinstance(parsed_readable_file_stream, FileInputStream))

    def testEmptyPattern(self) -> None:

        options = PatternOptionBuilder.parsePattern("")
        assert options.getOptions().isEmpty()

    def testClassPattern(self) -> None:

        options = PatternOptionBuilder.parsePattern("c+d+")
        parser = PosixParser()
        line = parser.parse0(
            options, ["-c", "java.util.Calendar", "-d", "System.DateTime"]
        )
        self.assertEqual("c value", Calendar, line.getOptionObject1("c"))
        self.assertIsNone("d value", line.getOptionObject1("d"))

    # Class Methods End
