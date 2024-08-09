import pytest

from src.main.org.apache.commons.cli.PosixParser import *
from src.main.org.apache.commons.cli.PatternOptionBuilder import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.MissingOptionException import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.CommandLine import *
import unittest
import io
from pathlib import Path
from urllib.parse import urlparse
from datetime import datetime, date, time, timedelta, timezone


class PatternOptionBuilderTest(unittest.TestCase):

    @pytest.mark.test
    def testClassPattern(self) -> None:
        try:
            options = PatternOptionBuilder.parsePattern("c+d+")
            parser = PosixParser()
            line = parser.parse0(
                options, ["-c", "datetime", "-d", "System.DateTime"]
            )
            self.assertIn(
                line.getOptionObject1("c"),
                [datetime, date, time, timedelta, timezone],
                "c value"
            )
            self.assertIsNone(line.getOptionObject1("d"), "d value")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testEmptyPattern(self) -> None:
        options = PatternOptionBuilder.parsePattern("")
        self.assertEquals(len(options.getOptions()), 0)


    @pytest.mark.test
    def testExistingFilePattern(self) -> None:
        try:
            options = PatternOptionBuilder.parsePattern("g<")
            parser = PosixParser()
            line = parser.parse0(
                options,
                ["-g", "src/test/resources/org/apache/commons/cli/existing-readable.file"]
            )

            parsedReadableFileStream = line.getOptionObject1("g")

            self.assertIsNotNone(parsedReadableFileStream, "option g not parsed")
            self.assertTrue(
                isinstance(parsedReadableFileStream, io.FileIO)\
                    or isinstance(parsedReadableFileStream, io.BufferedReader)\
                    or isinstance(parsedReadableFileStream, io.TextIOWrapper),
                "option g not FileInputStream"
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
     
    @pytest.mark.test
    def testExistingFilePatternFileNotExist(self) -> None:
        try:
            options = PatternOptionBuilder.parsePattern("f<")
            parser = PosixParser()
            line = parser.parse0(options, ["-f", "non-existing.file"])

            self.assertIsNone(line.getOptionObject1("f"), "option f parsed")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")


    @pytest.mark.test
    def testNumberPattern(self) -> None:
        try:
            options = PatternOptionBuilder.parsePattern("n%d%x%")
            parser = PosixParser()
            line = parser.parse0(options, ["-n", "1", "-d", "2.1", "-x", "3,5"])

            self.assertEqual(type(line.getOptionObject1("n")), int, "n object class")
            self.assertEqual(line.getOptionObject1("n"), 1, "n value")

            self.assertEqual(type(line.getOptionObject1("d")), float, "d object class")
            self.assertEqual(line.getOptionObject1("d"), 2.1, "d value")

            self.assertIsNone(line.getOptionObject1("x"), "x object")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testObjectPattern(self) -> None:
        try:
            options = PatternOptionBuilder.parsePattern("o@i@n@")
            parser = PosixParser()
            line = parser.parse0(
                options,
                [
                    "-o",
                    "str",
                    "-i",
                    "datetime.datetime",
                    "-n",
                    "System.DateTime",
                ]
            )

            self.assertEqual("", line.getOptionObject1("o"), "o value")
            self.assertIsNone(line.getOptionObject1("i"), "i value")
            self.assertIsNone(line.getOptionObject1("n"), "n value")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testRequiredOption(self) -> None:
        try:
            options = PatternOptionBuilder.parsePattern("!n%m%")
            parser = PosixParser()
            try:
                parser.parse0(options, [""])
                self.fail("MissingOptionException wasn't thrown")
            except MissingOptionException as e:
                self.assertEqual(1, len(e.getMissingOptions()))
                self.assertTrue("n" in e.getMissingOptions())
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testSimplePattern(self) -> None:
        try:
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
                "test*"
            ]

            parser = PosixParser()
            line = parser.parse0(options, args)

            self.assertEqual("foo", line.getOptionValue4("a"), "flag a")
            self.assertEqual("foo", line.getOptionObject1("a"), "string flag a")
            self.assertEqual([], line.getOptionObject1("b"), "object flag b")
            self.assertTrue(line.hasOption2("c"), "boolean true flag c")
            self.assertFalse(line.hasOption2("d"), "boolean false flag d")
            self.assertEqual(Path("build.xml"), line.getOptionObject1("e"), "file flag e")
            self.assertIn(
                line.getOptionObject1("f"),
                [datetime, date, time, timedelta, timezone],
                "class flag f"
            )
            self.assertEqual(float(4.5), line.getOptionObject1("n"), "number flag n")
            self.assertIn(
                line.getOptionObject1("t"),
                ["https://commons.apache.org", urlparse("https://commons.apache.org")],
                "url flag t"
            )

            self.assertEqual("foo", line.getOptionValue0('a'), "flag a")
            self.assertEqual("foo", line.getOptionObject0('a'), "string flag a")
            self.assertEqual([], line.getOptionObject0('b'), "object flag b")
            self.assertTrue(line.hasOption0('c'), "boolean true flag c")
            self.assertFalse(line.hasOption0('d'), "boolean false flag d")
            self.assertEqual(Path("build.xml"), line.getOptionObject0('e'), "file flag e")
            self.assertIn(
                line.getOptionObject0('f'),
                [datetime, date, time, timedelta, timezone],
                "class flag f"
            )
            self.assertEqual(float(4.5), line.getOptionObject0('n'), "number flag n")
            self.assertIn(
                line.getOptionObject0('t'),
                ["https://commons.apache.org", urlparse("https://commons.apache.org")],
                "url flag t"
            )

            try:
                self.assertEqual([], line.getOptionObject0('m'), "files flag m")
                self.fail("Multiple files are not supported yet, should have failed")
            except (RuntimeError, NotImplementedError) as uoe:
                pass

            try:
                self.assertIn(
                    line.getOptionObject0('z'),
                    [datetime.datetime.fromtimestamp(1023400137.276),
                        datetime.datetime.fromtimestamp(1023400137.276).date()],
                    "date flag z"
                )
                self.fail("Date is not supported yet, should have failed")
            except (RuntimeError, NotImplementedError) as uoe:
                pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testUntypedPattern(self) -> None:
        try:
            options = PatternOptionBuilder.parsePattern("abc")
            parser = PosixParser()
            line = parser.parse0(options, ["-abc"])

            self.assertTrue(line.hasOption0('a'))
            self.assertIsNone(line.getOptionObject0('a'), "value a")
            self.assertTrue(line.hasOption0('b'))
            self.assertIsNone(line.getOptionObject0('b'), "value b")
            self.assertTrue(line.hasOption0('c'))
            self.assertIsNone(line.getOptionObject0('c'), "value c")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testURLPattern(self) -> None:
        try:
            options = PatternOptionBuilder.parsePattern("u/v/")
            parser = PosixParser()
            line = parser.parse0(
                options,
                ["-u", "https://commons.apache.org", "-v", "foo://commons.apache.org"],
            )
            
            self.assertIn(
                line.getOptionObject1("u"),
                ["https://commons.apache.org", urlparse("https://commons.apache.org")],
                "u value"
            )
            self.assertIsNone(line.getOptionObject1("v"), "v value")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
