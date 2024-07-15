from __future__ import annotations
import time
import locale
import re
import mock
import urllib
import os
import typing
from typing import *
import numbers
from io import BytesIO
from io import StringIO
import pathlib
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVParser import *

# from src.test.org.apache.commons.csv.CSVParser_ESTest_scaffolding import *
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.DuplicateHeaderMode import *
from src.main.org.apache.commons.csv.QuoteMode import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *


class CSVParser_ESTest(unittest.TestCase):

    def test45(self) -> None:

        csv_format = CSVFormat.DEFAULT
        csv_parser = CSVParser.parse4("vwt<sh@~`,g:5", csv_format)
        csv_parser.getRecords()
        self.assertEqual(1, csv_parser.getRecordNumber())

    def test44(self) -> None:

        cSVFormat0 = CSVFormat.TDF
        cSVParser0 = CSVParser.parse4("E<OF", cSVFormat0)
        cSVParser_CSVRecordIterator0 = cSVParser0.new_CSVRecordIterator()

        with pytest.raises(NotImplementedError):
            cSVParser_CSVRecordIterator0.remove()

    def test43(self) -> None:

        csv_format = CSVFormat.EXCEL
        csv_parser = CSVParser.parse4(
            ") invalid char between encapsulated token and delimiter", csv_format
        )
        csv_parser.getHeaderMapRaw()
        self.assertEqual(0, csv_parser.getRecordNumber())

    def test42(self) -> None:

        csv_format = CSVFormat.RFC4180
        csv_parser = CSVParser.parse4("]N", csv_format)
        csv_parser.getFirstEndOfLine()
        self.assertEqual(0, csv_parser.getRecordNumber())

    def test41(self) -> None:

        csv_format = CSVFormat.RFC4180
        csv_parser = CSVParser.parse4("]N", csv_format)
        csv_parser.getCurrentLineNumber()
        self.assertEqual(0, csv_parser.getRecordNumber())

    def test40(self) -> None:

        cSVFormat0 = CSVFormat.newFormat("F")
        cSVParser0 = CSVParser.parse4("", cSVFormat0)
        cSVParser0.getHeaderNames()
        self.assertEqual(0, cSVParser0.getRecordNumber())

    def test39(self) -> None:

        csv_format = CSVFormat.DEFAULT
        mock_file = MockFile("")
        path = mock_file.toPath()
        charset = Charset.defaultCharset()
        csv_parser = CSVParser.parse2(path, charset, csv_format)
        self.assertEqual(0, csv_parser.getRecordNumber())

    def test38(self) -> None:

        csv_format = CSVFormat.POSTGRESQL_TEXT
        charset = "utf-8"

        with self.assertRaises(ValueError) as context:
            CSVParser.parse0(None, charset, csv_format)

        self.assertTrue("file cannot be None" in str(context.exception))

    def test37(self) -> None:

        csv_format = CSVFormat.POSTGRESQL_TEXT
        csv_parser = CSVParser.parse4("aJ", csv_format)
        csv_parser.getHeaderComment()
        self.assertEqual(0, csv_parser.getRecordNumber())

    def test36(self) -> None:

        csv_format = CSVFormat.EXCEL
        charset = "utf-8"

        with pytest.raises(ValueError) as e:
            CSVParser.parse5(None, charset, csv_format)

        assert str(e.value) == "None values are not allowed"

    def test35(self) -> None:

        csv_format = CSVFormat.DEFAULT
        piped_reader = io.PipedReader()
        csv_parser = CSVParser.CSVParser1(piped_reader, csv_format)
        csv_parser.getTrailerComment()
        self.assertEqual(0, csv_parser.getRecordNumber())

    def test34(self) -> None:

        csv_format = CSVFormat.POSTGRESQL_TEXT
        csv_parser = CSVParser.parse4("]N", csv_format)
        record_number = csv_parser.getRecordNumber()
        self.assertEqual(0, record_number)

    def test33(self) -> None:

        csv_format = CSVFormat.POSTGRESQL_TEXT
        csv_parser = CSVParser.parse4("]N", csv_format)
        csv_parser.close()
        csv_parser.getRecords()
        self.assertEqual(0, csv_parser.getRecordNumber())

    def test32(self) -> None:

        csv_format = CSVFormat.MYSQL
        csv_parser = CSVParser.parse4("L}F", csv_format)
        csv_record_iterator = csv_parser.new_csv_record_iterator()
        csv_record_iterator.has_next()
        boolean_value = csv_record_iterator.has_next()
        self.assertEqual(1, csv_parser.get_record_number())
        self.assertTrue(boolean_value)

    def test31(self) -> None:

        csv_format = CSVFormat.POSTGRESQL_TEXT
        csv_parser = CSVParser.parse4(')"MF;N=', csv_format)
        csv_parser.close()
        csv_parser_csv_record_iterator = csv_parser.CSVRecordIterator()

        try:
            csv_parser_csv_record_iterator.next()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException(
                "org.apache.commons.csv.CSVParser$CSVRecordIterator", e
            )

    def test30(self) -> None:

        csv_format = CSVFormat.POSTGRESQL_TEXT
        csv_parser = CSVParser.parse4("#C2rpb%", csv_format)
        csv_record_iterator = csv_parser.new_csv_record_iterator()
        csv_record = csv_record_iterator.next()
        self.assertEqual(1, csv_parser.get_record_number())
        self.assertEqual(0, csv_record.get_character_position())

    def test29(self) -> None:

        csv_format = CSVFormat.POSTGRESQL_TEXT
        csv_parser = CSVParser.parse4("#C2rpb%", csv_format)
        csv_parser.getRecords()
        csv_parser_csv_record_iterator = csv_parser.CSVRecordIterator()

        try:
            csv_parser_csv_record_iterator.next()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException(
                "org.apache.commons.csv.CSVParser$CSVRecordIterator", e
            )

    def test28(self) -> None:

        cSVFormat0 = CSVFormat.TDF
        cSVParser0 = CSVParser.parse4(" ", cSVFormat0)
        cSVParser0.getRecords()
        self.assertEqual(1, cSVParser0.getRecordNumber())

    def test27(self) -> None:

        csv_format = CSVFormat.MYSQL
        csv_parser = CSVParser.parse4("L}F", csv_format)
        csv_parser.getHeaderMap()
        self.assertEqual(0, csv_parser.getRecordNumber())

    def test26(self) -> None:

        character0 = "("
        cSVFormat_Builder0 = Builder.create0()
        cSVFormat_Builder1 = cSVFormat_Builder0.setNullString("]N")
        quoteMode0 = QuoteMode.NONE
        duplicateHeaderMode0 = DuplicateHeaderMode.ALLOW_EMPTY
        stringArray0 = [""] * 6
        cSVFormat0 = CSVFormat(
            -711,
            True,
            True,
            "]N",
            "A header name is missing in ",
            character0,
            True,
            True,
            cSVFormat_Builder1,
            character0,
            True,
            character0,
            quoteMode0,
            True,
            duplicateHeaderMode0,
            stringArray0,
            True,
            True,
            stringArray0,
            "A header name is missing in ",
        )
        cSVParser0 = CSVParser.parse4("]N", cSVFormat0)
        cSVParser0.getRecords()
        self.assertEqual(1, cSVParser0.getRecordNumber())

    def test25(self) -> None:

        csv_format = CSVFormat.POSTGRESQL_TEXT
        csv_parser = CSVParser.parse4(')"MF;N=', csv_format)
        boolean = csv_parser.hasHeaderComment()
        self.assertEqual(0, csv_parser.getRecordNumber())
        self.assertFalse(boolean)

    def test24(self) -> None:

        csv_format = CSVFormat.MYSQL
        csv_parser = CSVParser.parse4("L}F", csv_format)
        boolean_result = csv_parser.hasTrailerComment()
        self.assertFalse(boolean_result)
        self.assertEqual(0, csv_parser.getRecordNumber())

    def test23(self) -> None:

        reader0 = io.StringIO("")
        cSVFormat0 = CSVFormat.INFORMIX_UNLOAD_CSV
        cSVParser0 = CSVParser(reader0, cSVFormat0, 0, 0)
        long0 = cSVParser0.getRecordNumber()
        self.assertEqual((-1), long0)

    def test22(self) -> None:

        cSVFormat0 = CSVFormat.TDF
        cSVParser0 = CSVParser.parse4("E<OF", cSVFormat0)
        cSVParser0.stream()
        self.assertEqual(0, cSVParser0.getRecordNumber())

    def test21(self) -> None:

        reader0 = io.StringIO("")
        csv_format0 = CSVFormat.DEFAULT
        csv_parser0 = CSVParser(reader0, csv_format0, 4086, 4086)
        consumer0 = mock(Consumer)
        csv_parser0.forEach(consumer0)
        self.assertEqual(4085, csv_parser0.getRecordNumber())

    def test20(self) -> None:

        csv_format = CSVFormat.POSTGRESQL_TEXT
        csv_parser = CSVParser.parse4("N", csv_format)
        self.assertTrue(csv_parser.isClosed())
        self.assertEqual(0, csv_parser.getRecordNumber())

    def test19(self) -> None:

        pipedOutputStream0 = io.BytesIO()
        pipedInputStream0 = io.BytesIO(pipedOutputStream0.getvalue())
        charset0 = "utf-8"
        cSVFormat0 = CSVFormat.POSTGRESQL_TEXT
        cSVParser0 = CSVParser.parse1(pipedInputStream0, charset0, cSVFormat0)
        self.assertEqual(0, cSVParser0.getRecordNumber())

    def test18(self) -> None:

        csv_format = CSVFormat.POSTGRESQL_TEXT
        reader = io.StringIO("")
        csv_parser = CSVParser.parse3(reader, csv_format)
        self.assertEqual(0, csv_parser.getRecordNumber())

    def test17(self) -> None:

        csv_format = CSVFormat.ORACLE
        csv_parser = None
        try:
            csv_parser = CSVParser(None, csv_format, 0, -554)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # reader
            # verifyException("java.util.Objects", e)
            pass

    def test16(self) -> None:

        csv_format = CSVFormat.DEFAULT

        try:
            CSVParser.CSVParser1(None, csv_format)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(type(e)), "<class 'java.util.Objects'>")

    def test15(self) -> None:

        pipedReader0 = io.PipeReader()
        cSVFormat0 = CSVFormat()
        cSVParser0 = cSVFormat0.parse(pipedReader0)

        try:
            cSVParser0.getRecords()
            self.fail("Expecting exception: UncheckedIOException")

        except UncheckedIOException as e:
            self.verifyException(
                "org.apache.commons.csv.CSVParser$CSVRecordIterator", e
            )

    def test14(self) -> None:

        cSVFormat0 = CSVFormat.POSTGRESQL_TEXT
        pipedReader0 = io.PipedReader()
        cSVParser0 = CSVParser.CSVParser1(pipedReader0, cSVFormat0)
        try:
            cSVParser0.nextRecord()
            self.fail("Expecting exception: IOException")

        except IOError as e:
            # Pipe not connected
            self.verifyException("java.io.PipedReader", e)

    def test13(self) -> None:

        mockFile0 = MockFile("\fe_")
        charset0 = "utf-8"
        cSVFormat0 = CSVFormat.TDF

        try:
            CSVParser.parse0(mockFile0, charset0, cSVFormat0)
            self.fail("Expecting exception: NoSuchFileException")

        except NoSuchFileException:
            pass

    def test12(self) -> None:

        csv_format = CSVFormat.POSTGRESQL_TEXT
        charset = "utf-8"

        try:
            CSVParser.parse1(None, charset, csv_format)
            self.fail("Expecting exception: RuntimeError")

        except ValueError as e:
            self.assertEqual(str(e), "inputStream and format cannot be None")

    def test11(self) -> None:

        charset0 = locale.getpreferredencoding()
        cSVFormat0 = CSVFormat.POSTGRESQL_CSV

        with self.assertRaises(RuntimeError):
            CSVParser.parse2(None, charset0, cSVFormat0)

    def test10(self) -> None:

        csv_format = CSVFormat.POSTGRESQL_TEXT
        mock_file = MockFile("&{?cjN08V<.")
        path = mock_file.toPath()
        charset = Charset.defaultCharset()

        try:
            CSVParser.parse2(path, charset, csv_format)
            self.fail("Expecting exception: NoSuchFileException")
        except NoSuchFileException:
            pass

    def test09(self) -> None:

        pipedReader0 = io.PipeReader()
        try:
            CSVParser.parse3(pipedReader0, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(type(e)), "<class 'java.lang.RuntimeError'>")

    def test08(self) -> None:

        csv_format = CSVFormat.TDF

        try:
            CSVParser.parse4(None, csv_format)
            self.fail("Expecting exception: RuntimeError")

        except ValueError as e:
            self.assertEqual(str(e), "string and format cannot be None")

    def test07(self) -> None:

        csv_format = CSVFormat.TDF
        url = MockURL.getHttpExample()
        charset = "utf-8"

        try:
            CSVParser.parse5(url, charset, csv_format)
            self.fail("Expecting exception: IOException")

        except urllib.error.URLError as e:
            # Could not find: www.someFakeButWellFormedURL.org
            self.assertTrue("www.someFakeButWellFormedURL.org" in str(e))

    def test06(self) -> None:

        pass  # LLM could not translate this method

    def test05(self) -> None:

        pass  # LLM could not translate this method

    def test04(self) -> None:

        csv_format = CSVFormat.POSTGRESQL_TEXT
        csv_parser = CSVParser.parse4("N", csv_format)
        csv_parser.close()
        boolean = csv_parser.isClosed()
        self.assertTrue(boolean)
        self.assertEqual(0, csv_parser.getRecordNumber())

    def test03(self) -> None:

        csv_format0 = CSVFormat.DEFAULT
        piped_reader0 = io.PipedReader()
        csv_parser0 = CSVParser.CSVParser1(piped_reader0, csv_format0)
        csv_parser0.iterator()
        self.assertEqual(0, csv_parser0.getRecordNumber())

    def test02(self) -> None:

        cSVFormat0 = CSVFormat.POSTGRESQL_TEXT
        cSVParser0 = CSVParser.parse4("N", cSVFormat0)
        cSVParser0.nextRecord()
        self.assertEqual(1, cSVParser0.getRecordNumber())

    def test01(self) -> None:

        pass  # LLM could not translate this method

    def test00(self) -> None:

        mockFile0 = MockFile("")
        charset0 = str(Charset.defaultCharset())
        cSVFormat0 = CSVFormat.TDF
        cSVParser0 = CSVParser.parse0(mockFile0, charset0, cSVFormat0)
        self.assertEqual(0, cSVParser0.getRecordNumber())
