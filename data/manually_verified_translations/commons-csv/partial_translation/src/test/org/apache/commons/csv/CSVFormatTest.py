from __future__ import annotations
import copy
import re
import pickle
import os
from io import BytesIO
from io import StringIO
import unittest
import pytest
import io
import typing
from typing import *
import unittest
import enum
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.DuplicateHeaderMode import *
from src.main.org.apache.commons.csv.QuoteMode import *


class EmptyEnum:

    pass


class Header:

    Phone: Header = None

    Email: Header = None

    Name: Header = None


class CSVFormatTest(unittest.TestCase):

    def testWithSystemRecordSeparator(self) -> None:

        formatWithRecordSeparator = CSVFormat.DEFAULT.withSystemRecordSeparator()
        self.assertEqual(os.linesep, formatWithRecordSeparator.getRecordSeparator())

    def testWithRecordSeparatorLF(self) -> None:

        formatWithRecordSeparator = CSVFormat.DEFAULT.withRecordSeparator0(Constants.LF)
        self.assertEqual(
            str(Constants.LF), formatWithRecordSeparator.getRecordSeparator()
        )

    def testWithRecordSeparatorCRLF(self) -> None:

        formatWithRecordSeparator = CSVFormat.DEFAULT.withRecordSeparator1(
            Constants.CRLF
        )
        self.assertEqual(Constants.CRLF, formatWithRecordSeparator.getRecordSeparator())

    def testWithRecordSeparatorCR(self) -> None:

        formatWithRecordSeparator = CSVFormat.DEFAULT.withRecordSeparator0(Constants.CR)
        self.assertEqual(
            str(Constants.CR), formatWithRecordSeparator.getRecordSeparator()
        )

    def testWithQuotePolicy(self) -> None:

        formatWithQuotePolicy = CSVFormat.DEFAULT.withQuoteMode(QuoteMode.ALL)
        self.assertEqual(QuoteMode.ALL, formatWithQuotePolicy.getQuoteMode())

    def testWithQuoteLFThrowsException(self) -> None:

        with self.assertRaises(Exception):
            CSVFormat.DEFAULT.withQuote(Constants.LF)

    def testWithQuoteChar(self) -> None:

        formatWithQuoteChar = CSVFormat.DEFAULT.withQuote0('"')
        self.assertEqual('"', formatWithQuoteChar.getQuoteCharacter())

    def testWithNullString(self) -> None:
        formatWithNullString = CSVFormat.DEFAULT.withNullString("null")
        self.assertEqual("null", formatWithNullString.getNullString())

    def testWithIgnoreSurround(self) -> None:

        self.assertFalse(
            CSVFormat.DEFAULT.withIgnoreSurroundingSpaces1(
                False
            ).getIgnoreSurroundingSpaces()
        )
        self.assertTrue(
            CSVFormat.DEFAULT.withIgnoreSurroundingSpaces0().getIgnoreSurroundingSpaces()
        )

    def testWithIgnoreEmptyLines(self) -> None:

        self.assertFalse(
            CSVFormat.DEFAULT.withIgnoreEmptyLines1(False).getIgnoreEmptyLines()
        )
        self.assertTrue(CSVFormat.DEFAULT.withIgnoreEmptyLines0().getIgnoreEmptyLines())

    def testWithHeaderComments(self) -> None:

        csvFormat = CSVFormat.DEFAULT

        self.assertEqual('"', csvFormat.getQuoteCharacter())
        self.assertFalse(csvFormat.isCommentMarkerSet())

        self.assertFalse(csvFormat.isEscapeCharacterSet())
        self.assertTrue(csvFormat.isQuoteCharacterSet())

        self.assertFalse(csvFormat.getSkipHeaderRecord())
        self.assertIsNone(csvFormat.getQuoteMode())

        self.assertEqual(",", csvFormat.getDelimiter())
        self.assertTrue(csvFormat.getIgnoreEmptyLines())

        self.assertFalse(csvFormat.getIgnoreHeaderCase())
        self.assertIsNone(csvFormat.getCommentMarker())

        self.assertEqual("\r\n", csvFormat.getRecordSeparator())
        self.assertFalse(csvFormat.getTrailingDelimiter())

        self.assertFalse(csvFormat.getAllowMissingColumnNames())
        self.assertFalse(csvFormat.getTrim())

        self.assertFalse(csvFormat.isNullStringSet())
        self.assertIsNone(csvFormat.getNullString())

        self.assertFalse(csvFormat.getIgnoreSurroundingSpaces())
        self.assertIsNone(csvFormat.getEscapeCharacter())

        objectArray = [None] * 8
        csvFormatTwo = csvFormat.withHeaderComments(objectArray)

        self.assertEqual('"', csvFormat.getQuoteCharacter())
        self.assertFalse(csvFormat.isCommentMarkerSet())

        self.assertFalse(csvFormat.isEscapeCharacterSet())
        self.assertTrue(csvFormat.isQuoteCharacterSet())

        self.assertFalse(csvFormat.getSkipHeaderRecord())
        self.assertIsNone(csvFormat.getQuoteMode())

        self.assertEqual(",", csvFormat.getDelimiter())
        self.assertTrue(csvFormat.getIgnoreEmptyLines())

        self.assertFalse(csvFormat.getIgnoreHeaderCase())
        self.assertIsNone(csvFormat.getCommentMarker())

        self.assertEqual("\r\n", csvFormat.getRecordSeparator())
        self.assertFalse(csvFormat.getTrailingDelimiter())

        self.assertFalse(csvFormat.getAllowMissingColumnNames())
        self.assertFalse(csvFormat.getTrim())

        self.assertFalse(csvFormat.isNullStringSet())
        self.assertIsNone(csvFormat.getNullString())

        self.assertFalse(csvFormat.getIgnoreSurroundingSpaces())
        self.assertIsNone(csvFormat.getEscapeCharacter())

        self.assertFalse(csvFormatTwo.getIgnoreHeaderCase())
        self.assertIsNone(csvFormatTwo.getQuoteMode())

        self.assertTrue(csvFormatTwo.getIgnoreEmptyLines())
        self.assertFalse(csvFormatTwo.getIgnoreSurroundingSpaces())

        self.assertIsNone(csvFormatTwo.getEscapeCharacter())
        self.assertFalse(csvFormatTwo.getTrim())

        self.assertFalse(csvFormatTwo.isEscapeCharacterSet())
        self.assertTrue(csvFormatTwo.isQuoteCharacterSet())

        self.assertFalse(csvFormatTwo.getSkipHeaderRecord())
        self.assertEqual('"', csvFormatTwo.getQuoteCharacter())

        self.assertFalse(csvFormatTwo.getAllowMissingColumnNames())
        self.assertIsNone(csvFormatTwo.getNullString())

        self.assertFalse(csvFormatTwo.isNullStringSet())
        self.assertFalse(csvFormatTwo.getTrailingDelimiter())

        self.assertEqual("\r\n", csvFormatTwo.getRecordSeparator())
        self.assertEqual(",", csvFormatTwo.getDelimiter())

        self.assertIsNone(csvFormatTwo.getCommentMarker())
        self.assertFalse(csvFormatTwo.isCommentMarkerSet())

        self.assertIsNot(csvFormat, csvFormatTwo)
        self.assertIsNot(csvFormatTwo, csvFormat)

        self.assertNotEqual(csvFormatTwo, csvFormat)

        string = csvFormatTwo.format_(objectArray)

        self.assertEqual('"', csvFormat.getQuoteCharacter())
        self.assertFalse(csvFormat.isCommentMarkerSet())

        self.assertFalse(csvFormat.isEscapeCharacterSet())
        self.assertTrue(csvFormat.isQuoteCharacterSet())

        self.assertFalse(csvFormat.getSkipHeaderRecord())
        self.assertIsNone(csvFormat.getQuoteMode())

        self.assertEqual(",", csvFormat.getDelimiter())
        self.assertTrue(csvFormat.getIgnoreEmptyLines())

        self.assertFalse(csvFormat.getIgnoreHeaderCase())
        self.assertIsNone(csvFormat.getCommentMarker())

        self.assertEqual("\r\n", csvFormat.getRecordSeparator())
        self.assertFalse(csvFormat.getTrailingDelimiter())

        self.assertFalse(csvFormat.getAllowMissingColumnNames())
        self.assertFalse(csvFormat.getTrim())

        self.assertFalse(csvFormat.isNullStringSet())
        self.assertIsNone(csvFormat.getNullString())

        self.assertFalse(csvFormat.getIgnoreSurroundingSpaces())
        self.assertIsNone(csvFormat.getEscapeCharacter())

        self.assertFalse(csvFormatTwo.getIgnoreHeaderCase())
        self.assertIsNone(csvFormatTwo.getQuoteMode())

        self.assertTrue(csvFormatTwo.getIgnoreEmptyLines())
        self.assertFalse(csvFormatTwo.getIgnoreSurroundingSpaces())

        self.assertIsNone(csvFormatTwo.getEscapeCharacter())
        self.assertFalse(csvFormatTwo.getTrim())

        self.assertFalse(csvFormatTwo.isEscapeCharacterSet())
        self.assertTrue(csvFormatTwo.isQuoteCharacterSet())

        self.assertFalse(csvFormatTwo.getSkipHeaderRecord())
        self.assertEqual('"', csvFormatTwo.getQuoteCharacter())

        self.assertFalse(csvFormatTwo.getAllowMissingColumnNames())
        self.assertIsNone(csvFormatTwo.getNullString())

        self.assertFalse(csvFormatTwo.isNullStringSet())
        self.assertFalse(csvFormatTwo.getTrailingDelimiter())

        self.assertEqual("\r\n", csvFormatTwo.getRecordSeparator())
        self.assertEqual(",", csvFormatTwo.getDelimiter())

        self.assertIsNone(csvFormatTwo.getCommentMarker())
        self.assertFalse(csvFormatTwo.isCommentMarkerSet())

        self.assertIsNot(csvFormat, csvFormatTwo)
        self.assertIsNot(csvFormatTwo, csvFormat)

        self.assertIsNotNone(string)
        self.assertNotEqual(csvFormat, csvFormatTwo)

        self.assertEqual(",,,,,,,", string)

    def testWithEscapeCRThrowsExceptions(self) -> None:

        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT.withEscape(Constants.CR)

    def testWithEscape(self) -> None:

        formatWithEscape = CSVFormat.DEFAULT.withEscape0("&")
        self.assertEqual("&", formatWithEscape.getEscapeCharacter())

    def testWithEmptyDuplicates(self) -> None:

        formatWithEmptyDuplicates = (
            CSVFormat.DEFAULT.builder()
            .setDuplicateHeaderMode(DuplicateHeaderMode.ALLOW_EMPTY)
            .build()
        )

        self.assertEqual(
            DuplicateHeaderMode.ALLOW_EMPTY,
            formatWithEmptyDuplicates.getDuplicateHeaderMode(),
        )
        self.assertFalse(formatWithEmptyDuplicates.getAllowDuplicateHeaderNames())

    def testWithDelimiterLFThrowsException(self) -> None:

        with pytest.raises(Exception):
            CSVFormat.DEFAULT.withDelimiter(Constants.LF)

    def testWithDelimiter(self) -> None:

        formatWithDelimiter = CSVFormat.DEFAULT.withDelimiter("|")
        self.assertEqual("|", formatWithDelimiter.getDelimiter())

    def testWithCommentStartCRThrowsException(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withCommentMarker(Constants.CR)

    def testWithCommentStart(self) -> None:

        formatWithCommentStart = CSVFormat.DEFAULT.withCommentMarker0("#")
        self.assertEqual("#", formatWithCommentStart.getCommentMarker())

    def testTrim(self) -> None:

        formatWithTrim = (
            CSVFormat.DEFAULT.withDelimiter(",")
            .withTrim0()
            .withQuote1(None)
            .withRecordSeparator1(Constants.CRLF)
        )

        in_str = "a,b,c"
        out = io.StringIO()
        formatWithTrim.print2(in_str, out, True)
        self.assertEqual("a,b,c", out.getvalue())

        in_str = " x,y,z"
        out = io.StringIO()
        formatWithTrim.print2(in_str, out, True)
        self.assertEqual("x,y,z", out.getvalue())

        in_str = ""
        out = io.StringIO()
        formatWithTrim.print2(in_str, out, True)
        self.assertEqual("", out.getvalue())

        in_str = "header\r\n"
        out = io.StringIO()
        formatWithTrim.print2(in_str, out, True)
        self.assertEqual("header", out.getvalue())

    def testToStringAndWithCommentMarkerTakingCharacter(self) -> None:

        pass  # LLM could not translate this method

    def testToString(self) -> None:

        string = CSVFormat.INFORMIX_UNLOAD.toString()

        self.assertEqual(
            'Delimiter=<|> Escape=<\\> QuoteChar=<"> RecordSeparator=<\n'
            + "> EmptyLines:ignored SkipHeaderRecord:false",
            string,
        )

    def testSerialization(self) -> None:

        out = io.BytesIO()

        try:
            oos = pickle.Pickler(out)
            oos.dump(CSVFormat.DEFAULT)
            oos.flush()
        finally:
            oos.clear_memo()

        in_ = io.BytesIO(out.getvalue())
        format = pickle.Unpickler(in_).load()

        assert format is not None
        assert CSVFormat.DEFAULT.getDelimiter() == format.getDelimiter(), "delimiter"
        assert (
            CSVFormat.DEFAULT.getQuoteCharacter() == format.getQuoteCharacter()
        ), "encapsulator"
        assert (
            CSVFormat.DEFAULT.getCommentMarker() == format.getCommentMarker()
        ), "comment start"
        assert (
            CSVFormat.DEFAULT.getRecordSeparator() == format.getRecordSeparator()
        ), "record separator"
        assert (
            CSVFormat.DEFAULT.getEscapeCharacter() == format.getEscapeCharacter()
        ), "escape"
        assert (
            CSVFormat.DEFAULT.getIgnoreSurroundingSpaces()
            == format.getIgnoreSurroundingSpaces()
        ), "trim"
        assert (
            CSVFormat.DEFAULT.getIgnoreEmptyLines() == format.getIgnoreEmptyLines()
        ), "empty lines"

    def testRFC4180(self) -> None:

        self.assertIsNone(CSVFormat.RFC4180.getCommentMarker())
        self.assertEqual(",", CSVFormat.RFC4180.getDelimiter())
        self.assertIsNone(CSVFormat.RFC4180.getEscapeCharacter())
        self.assertFalse(CSVFormat.RFC4180.getIgnoreEmptyLines())
        self.assertEqual('"', CSVFormat.RFC4180.getQuoteCharacter())
        self.assertIsNone(CSVFormat.RFC4180.getQuoteMode())
        self.assertEqual("\r\n", CSVFormat.RFC4180.getRecordSeparator())

    def testQuotePolicyNoneWithoutEscapeThrowsException_Deprecated(self) -> None:

        with self.assertRaises(ValueError):
            CSVFormat.newFormat("!").withQuoteMode(QuoteMode.NONE)

    def testQuotePolicyNoneWithoutEscapeThrowsException(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.newFormat("\0").builder().setQuoteMode(QuoteMode.NONE).build()

    def testQuoteCharSameAsDelimiterThrowsException_Deprecated(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withQuote("0").withDelimiter("0")

    def testQuoteCharSameAsDelimiterThrowsException(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.builder().setQuote0("0").setDelimiter0("0").build()

    def testQuoteCharSameAsCommentStartThrowsExceptionForWrapperType_Deprecated(
        self,
    ) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withQuote1(Character.valueOf("!"))

    def testQuoteCharSameAsCommentStartThrowsExceptionForWrapperType(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.builder().setQuote1(
                Character.valueOf("!")
            ).setCommentMarker0("0").build()

    def testQuoteCharSameAsCommentStartThrowsException_Deprecated(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withQuote0("0").withCommentMarker0("0")

    def testQuoteCharSameAsCommentStartThrowsException(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.builder().setQuote0("0").setCommentMarker0("0").build()

    def testPrintWithQuotes(self) -> None:

        in_ = io.StringIO('"a,b,c\r\nx,y,z')
        out = io.StringIO()
        format = (
            CSVFormat.RFC4180.withDelimiter(",")
            .withQuote0('"')
            .withEscape0("?")
            .withQuoteMode(QuoteMode.NON_NUMERIC)
        )
        format.print2(in_, out, True)
        self.assertEqual('"""a,b,c\r\nx,y,z"', out.getvalue())

    def testPrintWithQuoteModeIsNONE(self) -> None:

        in_str = "a,b,c"
        out = io.StringIO()
        format = (
            CSVFormat.RFC4180.withDelimiter(",")
            .withQuote0('"')
            .withEscape0("?")
            .withQuoteMode(QuoteMode.NONE)
        )
        format.print2(in_str, out, True)
        self.assertEqual("a?,b?,c", out.getvalue())

    def testPrintWithoutQuotes(self) -> None:

        in_ = io.StringIO("")
        out = io.StringIO()
        format = (
            CSVFormat.RFC4180.withDelimiter(",")
            .withQuote0('"')
            .withEscape0("?")
            .withQuoteMode(QuoteMode.NON_NUMERIC)
        )
        format.print2(in_, out, True)
        self.assertEqual('""', out.getvalue())

    def testPrintWithEscapesEndWithoutCRLF(self) -> None:

        in_str = "x,y,x"
        in_reader = io.StringIO(in_str)
        out_builder = io.StringIO()
        format = (
            CSVFormat.RFC4180.withEscape0("?")
            .withDelimiter(",")
            .withQuote1(None)
            .withRecordSeparator1(Constants.CRLF)
        )
        format.print2(in_reader, out_builder, True)
        self.assertEqual("x?,y?,x", out_builder.getvalue())

    def testPrintWithEscapesEndWithCRLF(self) -> None:

        in_str = "x,y,x\r\na,?b,c\r\n"
        in_reader = io.StringIO(in_str)
        out_builder = io.StringIO()
        format = (
            CSVFormat.RFC4180.withEscape0("?")
            .withDelimiter(",")
            .withQuote1(None)
            .withRecordSeparator1(Constants.CRLF)
        )
        format.print2(in_reader, out_builder, True)
        self.assertEqual("x?,y?,x?r?na?,??b?,c?r?n", out_builder.getvalue())

    def testPrintRecordEmpty(self) -> None:

        out = io.StringIO()
        format = CSVFormat.RFC4180
        format.printRecord(out, [])
        self.assertEqual(format.getRecordSeparator(), out.getvalue())

    def testPrintRecord(self) -> None:

        out = io.StringIO()
        format = CSVFormat.RFC4180
        format.printRecord(out, ["a", "b", "c"])
        self.assertEqual("a,b,c" + format.getRecordSeparator(), out.getvalue())

    def testNewFormat(self) -> None:

        csvFormat = CSVFormat.newFormat("X")

        self.assertFalse(csvFormat.getSkipHeaderRecord())
        self.assertFalse(csvFormat.isEscapeCharacterSet())

        self.assertIsNone(csvFormat.getRecordSeparator())
        self.assertIsNone(csvFormat.getQuoteMode())

        self.assertIsNone(csvFormat.getCommentMarker())
        self.assertFalse(csvFormat.getIgnoreHeaderCase())

        self.assertFalse(csvFormat.getAllowMissingColumnNames())
        self.assertFalse(csvFormat.getTrim())

        self.assertFalse(csvFormat.isNullStringSet())
        self.assertIsNone(csvFormat.getEscapeCharacter())

        self.assertFalse(csvFormat.getIgnoreSurroundingSpaces())
        self.assertFalse(csvFormat.getTrailingDelimiter())

        self.assertEqual("X", csvFormat.getDelimiter())
        self.assertIsNone(csvFormat.getNullString())

        self.assertFalse(csvFormat.isQuoteCharacterSet())
        self.assertFalse(csvFormat.isCommentMarkerSet())

        self.assertIsNone(csvFormat.getQuoteCharacter())
        self.assertFalse(csvFormat.getIgnoreEmptyLines())

        self.assertFalse(csvFormat.getSkipHeaderRecord())
        self.assertFalse(csvFormat.isEscapeCharacterSet())

        self.assertIsNone(csvFormat.getRecordSeparator())
        self.assertIsNone(csvFormat.getQuoteMode())

        self.assertIsNone(csvFormat.getCommentMarker())
        self.assertFalse(csvFormat.getIgnoreHeaderCase())

        self.assertFalse(csvFormat.getAllowMissingColumnNames())
        self.assertFalse(csvFormat.getTrim())

        self.assertFalse(csvFormat.isNullStringSet())
        self.assertIsNone(csvFormat.getEscapeCharacter())

        self.assertFalse(csvFormat.getIgnoreSurroundingSpaces())
        self.assertFalse(csvFormat.getTrailingDelimiter())

        self.assertEqual("X", csvFormat.getDelimiter())
        self.assertIsNone(csvFormat.getNullString())

        self.assertFalse(csvFormat.isQuoteCharacterSet())
        self.assertFalse(csvFormat.isCommentMarkerSet())

        self.assertIsNone(csvFormat.getQuoteCharacter())
        self.assertFalse(csvFormat.getIgnoreEmptyLines())

    def testHashCodeAndWithIgnoreHeaderCase(self) -> None:

        csv_format = CSVFormat.INFORMIX_UNLOAD_CSV
        csv_format_two = csv_format.withIgnoreHeaderCase0()
        csv_format_two.hashCode()

        self.assertFalse(csv_format.getIgnoreHeaderCase())
        self.assertTrue(csv_format_two.getIgnoreHeaderCase())  # now different
        self.assertFalse(csv_format_two.getTrailingDelimiter())

        self.assertNotEqual(csv_format_two, csv_format)  # CSV-244 - should not be equal
        self.assertFalse(csv_format_two.getAllowMissingColumnNames())

        self.assertFalse(csv_format_two.getTrim())

    def testGetDuplicateHeaderMode(self) -> None:

        builder = CSVFormat.DEFAULT.builder()

        self.assertEqual(
            DuplicateHeaderMode.ALLOW_ALL, builder.build().getDuplicateHeaderMode()
        )
        self.assertEqual(
            DuplicateHeaderMode.ALLOW_ALL,
            builder.setDuplicateHeaderMode(DuplicateHeaderMode.ALLOW_ALL)
            .build()
            .getDuplicateHeaderMode(),
        )
        self.assertEqual(
            DuplicateHeaderMode.ALLOW_EMPTY,
            builder.setDuplicateHeaderMode(DuplicateHeaderMode.ALLOW_EMPTY)
            .build()
            .getDuplicateHeaderMode(),
        )
        self.assertEqual(
            DuplicateHeaderMode.DISALLOW,
            builder.setDuplicateHeaderMode(DuplicateHeaderMode.DISALLOW)
            .build()
            .getDuplicateHeaderMode(),
        )

    def testGetAllowDuplicateHeaderNames(self) -> None:

        builder = CSVFormat.DEFAULT.builder()
        self.assertTrue(builder.build().getAllowDuplicateHeaderNames())

        self.assertTrue(
            builder.setDuplicateHeaderMode(DuplicateHeaderMode.ALLOW_ALL)
            .build()
            .getAllowDuplicateHeaderNames()
        )

        self.assertFalse(
            builder.setDuplicateHeaderMode(DuplicateHeaderMode.ALLOW_EMPTY)
            .build()
            .getAllowDuplicateHeaderNames()
        )

        self.assertFalse(
            builder.setDuplicateHeaderMode(DuplicateHeaderMode.DISALLOW)
            .build()
            .getAllowDuplicateHeaderNames()
        )

    def testFormatThrowsRuntimeError(self) -> None:

        csv_format = CSVFormat.MYSQL

        with pytest.raises(TypeError) as e:
            csv_format.format(None)
        assert str(e.value) == "Object of type Object is not JSON serializable"

    def testFormat(self) -> None:

        format_ = CSVFormat.DEFAULT

        self.assertEqual("", format_.format_())
        self.assertEqual("a,b,c", format_.format_("a", "b", "c"))
        self.assertEqual('"x,y",z', format_.format_("x,y", "z"))

    def testEscapeSameAsCommentStartThrowsExceptionForWrapperType_Deprecated(
        self,
    ) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withEscape1(Character.valueOf("!")).withCommentMarker1(
                Character.valueOf("!")
            )

    def testEscapeSameAsCommentStartThrowsExceptionForWrapperType(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.builder().setEscape1(
                Character.valueOf("!")
            ).setCommentMarker1(Character.valueOf("!")).build()

    def testEscapeSameAsCommentStartThrowsException_Deprecated(self) -> None:

        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT.withEscape0("0").withCommentMarker0("0")

    def testEscapeSameAsCommentStartThrowsException(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.builder().setEscape0("0").setCommentMarker0("0").build()

    def testEqualsWithNull(self) -> None:

        csvFormat = CSVFormat.POSTGRESQL_TEXT

        self.assertEqual("\\", csvFormat.getEscapeCharacter())
        self.assertFalse(csvFormat.getIgnoreSurroundingSpaces())

        self.assertFalse(csvFormat.getTrailingDelimiter())
        self.assertFalse(csvFormat.getTrim())

        self.assertFalse(csvFormat.isQuoteCharacterSet())
        self.assertEqual("\\N", csvFormat.getNullString())

        self.assertFalse(csvFormat.getIgnoreHeaderCase())
        self.assertTrue(csvFormat.isEscapeCharacterSet())

        self.assertFalse(csvFormat.isCommentMarkerSet())
        self.assertIsNone(csvFormat.getCommentMarker())

        self.assertFalse(csvFormat.getAllowMissingColumnNames())
        self.assertEqual(QuoteMode.ALL_NON_NULL, csvFormat.getQuoteMode())

        self.assertEqual("\t", csvFormat.getDelimiter())
        self.assertFalse(csvFormat.getSkipHeaderRecord())

        self.assertEqual("\n", csvFormat.getRecordSeparator())
        self.assertFalse(csvFormat.getIgnoreEmptyLines())

        self.assertIsNone(csvFormat.getQuoteCharacter())
        self.assertTrue(csvFormat.isNullStringSet())

        self.assertEqual("\\", csvFormat.getEscapeCharacter())
        self.assertFalse(csvFormat.getIgnoreSurroundingSpaces())

        self.assertFalse(csvFormat.getTrailingDelimiter())
        self.assertFalse(csvFormat.getTrim())

        self.assertFalse(csvFormat.isQuoteCharacterSet())
        self.assertEqual("\\N", csvFormat.getNullString())

        self.assertFalse(csvFormat.getIgnoreHeaderCase())
        self.assertTrue(csvFormat.isEscapeCharacterSet())

        self.assertFalse(csvFormat.isCommentMarkerSet())
        self.assertIsNone(csvFormat.getCommentMarker())

        self.assertFalse(csvFormat.getAllowMissingColumnNames())
        self.assertEqual(QuoteMode.ALL_NON_NULL, csvFormat.getQuoteMode())

        self.assertEqual("\t", csvFormat.getDelimiter())
        self.assertFalse(csvFormat.getSkipHeaderRecord())

        self.assertEqual("\n", csvFormat.getRecordSeparator())
        self.assertFalse(csvFormat.getIgnoreEmptyLines())

        self.assertIsNone(csvFormat.getQuoteCharacter())
        self.assertTrue(csvFormat.isNullStringSet())

        self.assertIsNotNone(csvFormat)

    def testEqualsSkipHeaderRecord_Deprecated(self) -> None:

        right = (
            CSVFormat.newFormat("'")
            .withRecordSeparator0(Constants.CR)
            .withCommentMarker0("#")
            .withEscape0("+")
            .withIgnoreEmptyLines0()
            .withIgnoreSurroundingSpaces0()
            .withQuote0('"')
            .withQuoteMode(QuoteMode.ALL)
            .withNullString("null")
            .withSkipHeaderRecord0()
        )
        left = right.withSkipHeaderRecord1(False)

        self.__assertNotEquals0(right, left)

    def testEqualsRecordSeparator_Deprecated(self) -> None:

        right = (
            CSVFormat.newFormat("'")
            .withRecordSeparator0(Constants.CR)
            .withCommentMarker0("#")
            .withEscape0("+")
            .withIgnoreEmptyLines0()
            .withIgnoreSurroundingSpaces0()
            .withQuote0('"')
            .withQuoteMode(QuoteMode.ALL)
        )
        left = right.withRecordSeparator0(Constants.LF)

        self.__assertNotEquals0(right, left)

    def testEqualsRecordSeparator(self) -> None:

        right = (
            CSVFormat.newFormat("'")
            .builder()
            .setRecordSeparator0(Constants.CR)
            .setCommentMarker0("#")
            .setEscape0("+")
            .setIgnoreEmptyLines(True)
            .setIgnoreSurroundingSpaces(True)
            .setQuote0('"')
            .setQuoteMode(QuoteMode.ALL)
            .build()
        )

        left = right.builder().setRecordSeparator0(Constants.LF).build()

        self.__assertNotEquals0(right, left)

    def testEqualsQuotePolicy_Deprecated(self) -> None:

        right = CSVFormat.newFormat("'").withQuote0('"').withQuoteMode(QuoteMode.ALL)
        left = right.withQuoteMode(QuoteMode.MINIMAL)

        self.__assertNotEquals0(right, left)

    def testEqualsQuotePolicy(self) -> None:

        right = (
            CSVFormat.newFormat("'")
            .builder()
            .setQuote0('"')
            .setQuoteMode(QuoteMode.ALL)
            .build()
        )
        left = right.builder().setQuoteMode(QuoteMode.MINIMAL).build()

        self.__assertNotEquals0(right, left)

    def testEqualsQuoteChar_Deprecated(self) -> None:

        right = CSVFormat.newFormat("'").withQuote0('"')
        left = right.withQuote0('"')

        self.__assertNotEquals0(right, left)

    def testEqualsQuoteChar(self) -> None:

        right = CSVFormat.newFormat("'").builder().setQuote0('"').build()
        left = right.builder().setQuote0("'").build()

        self.__assertNotEquals0(right, left)

    def testEqualsOne(self) -> None:

        csvFormatOne = CSVFormat.INFORMIX_UNLOAD
        csvFormatTwo = CSVFormat.MYSQL

        self.assertEqual("\\", csvFormatOne.getEscapeCharacter())
        self.assertIsNone(csvFormatOne.getQuoteMode())

        self.assertTrue(csvFormatOne.getIgnoreEmptyLines())
        self.assertFalse(csvFormatOne.getSkipHeaderRecord())

        self.assertFalse(csvFormatOne.getIgnoreHeaderCase())
        self.assertIsNone(csvFormatOne.getCommentMarker())

        self.assertFalse(csvFormatOne.isCommentMarkerSet())
        self.assertTrue(csvFormatOne.isQuoteCharacterSet())

        self.assertEqual("|", csvFormatOne.getDelimiter())
        self.assertFalse(csvFormatOne.getAllowMissingColumnNames())

        self.assertTrue(csvFormatOne.isEscapeCharacterSet())
        self.assertEqual("\n", csvFormatOne.getRecordSeparator())

        self.assertEqual('"', csvFormatOne.getQuoteCharacter())
        self.assertFalse(csvFormatOne.getTrailingDelimiter())

        self.assertFalse(csvFormatOne.getTrim())
        self.assertFalse(csvFormatOne.isNullStringSet())

        self.assertIsNone(csvFormatOne.getNullString())
        self.assertFalse(csvFormatOne.getIgnoreSurroundingSpaces())

        self.assertTrue(csvFormatTwo.isEscapeCharacterSet())
        self.assertIsNone(csvFormatTwo.getQuoteCharacter())

        self.assertFalse(csvFormatTwo.getAllowMissingColumnNames())
        self.assertEqual(QuoteMode.ALL_NON_NULL, csvFormatTwo.getQuoteMode())

        self.assertEqual("\t", csvFormatTwo.getDelimiter())
        self.assertEqual("\n", csvFormatTwo.getRecordSeparator())

        self.assertFalse(csvFormatTwo.isQuoteCharacterSet())
        self.assertTrue(csvFormatTwo.isNullStringSet())

        self.assertEqual("\\", csvFormatTwo.getEscapeCharacter())
        self.assertFalse(csvFormatTwo.getIgnoreHeaderCase())

        self.assertFalse(csvFormatTwo.getTrim())
        self.assertFalse(csvFormatTwo.getIgnoreEmptyLines())

        self.assertEqual("\\N", csvFormatTwo.getNullString())
        self.assertFalse(csvFormatTwo.getIgnoreSurroundingSpaces())

        self.assertFalse(csvFormatTwo.getTrailingDelimiter())
        self.assertFalse(csvFormatTwo.getSkipHeaderRecord())

        self.assertIsNone(csvFormatTwo.getCommentMarker())
        self.assertFalse(csvFormatTwo.isCommentMarkerSet())

        self.assertIsNot(csvFormatTwo, csvFormatOne)
        self.assertNotEqual(csvFormatTwo, csvFormatOne)

        self.assertEqual("\\", csvFormatOne.getEscapeCharacter())
        self.assertIsNone(csvFormatOne.getQuoteMode())

        self.assertTrue(csvFormatOne.getIgnoreEmptyLines())
        self.assertFalse(csvFormatOne.getSkipHeaderRecord())

        self.assertFalse(csvFormatOne.getIgnoreHeaderCase())
        self.assertIsNone(csvFormatOne.getCommentMarker())

        self.assertFalse(csvFormatOne.isCommentMarkerSet())
        self.assertTrue(csvFormatOne.isQuoteCharacterSet())

        self.assertEqual("|", csvFormatOne.getDelimiter())
        self.assertFalse(csvFormatOne.getAllowMissingColumnNames())

        self.assertTrue(csvFormatOne.isEscapeCharacterSet())
        self.assertEqual("\n", csvFormatOne.getRecordSeparator())

        self.assertEqual('"', csvFormatOne.getQuoteCharacter())
        self.assertFalse(csvFormatOne.getTrailingDelimiter())

        self.assertFalse(csvFormatOne.getTrim())
        self.assertFalse(csvFormatOne.isNullStringSet())

        self.assertIsNone(csvFormatOne.getNullString())
        self.assertFalse(csvFormatOne.getIgnoreSurroundingSpaces())

        self.assertTrue(csvFormatTwo.isEscapeCharacterSet())
        self.assertIsNone(csvFormatTwo.getQuoteCharacter())

        self.assertFalse(csvFormatTwo.getAllowMissingColumnNames())
        self.assertEqual(QuoteMode.ALL_NON_NULL, csvFormatTwo.getQuoteMode())

        self.assertEqual("\t", csvFormatTwo.getDelimiter())
        self.assertEqual("\n", csvFormatTwo.getRecordSeparator())

        self.assertFalse(csvFormatTwo.isQuoteCharacterSet())
        self.assertTrue(csvFormatTwo.isNullStringSet())

        self.assertEqual("\\", csvFormatTwo.getEscapeCharacter())
        self.assertFalse(csvFormatTwo.getIgnoreHeaderCase())

        self.assertFalse(csvFormatTwo.getTrim())
        self.assertFalse(csvFormatTwo.getIgnoreEmptyLines())

        self.assertEqual("\\N", csvFormatTwo.getNullString())
        self.assertFalse(csvFormatTwo.getIgnoreSurroundingSpaces())

        self.assertFalse(csvFormatTwo.getTrailingDelimiter())
        self.assertFalse(csvFormatTwo.getSkipHeaderRecord())

        self.assertIsNone(csvFormatTwo.getCommentMarker())
        self.assertFalse(csvFormatTwo.isCommentMarkerSet())

        self.assertIsNot(csvFormatOne, csvFormatTwo)
        self.assertIsNot(csvFormatTwo, csvFormatOne)

        self.assertNotEqual(csvFormatOne, csvFormatTwo)
        self.assertNotEqual(csvFormatTwo, csvFormatOne)

        self.assertNotEqual(csvFormatTwo, csvFormatOne)

    def testEqualsNullString_Deprecated(self) -> None:

        right = (
            CSVFormat.newFormat("'")
            .withRecordSeparator0(Constants.CR)
            .withCommentMarker0("#")
            .withEscape0("+")
            .withIgnoreEmptyLines0()
            .withIgnoreSurroundingSpaces0()
            .withQuote0('"')
            .withQuoteMode(QuoteMode.ALL)
            .withNullString("null")
        )
        left = right.withNullString("---")

        self.__assertNotEquals0(right, left)

    def testEqualsNullString(self) -> None:

        right = (
            CSVFormat.newFormat("'")
            .builder()
            .setRecordSeparator0(Constants.CR)
            .setCommentMarker0("#")
            .setEscape0("+")
            .setIgnoreEmptyLines(True)
            .setIgnoreSurroundingSpaces(True)
            .setQuote0('"')
            .setQuoteMode(QuoteMode.ALL)
            .setNullString("null")
            .build()
        )

        left = right.builder().setNullString("---").build()

        self.__assertNotEquals0(right, left)

    def testEqualsNoQuotes_Deprecated(self) -> None:

        left = CSVFormat.newFormat(",").withQuote1(None)
        right = left.withQuote1(None)

        self.assertEqual(left, right)

    def testEqualsNoQuotes(self) -> None:

        left = CSVFormat.newFormat(",").builder().setQuote1(None).build()
        right = left.builder().setQuote1(None).build()

        self.assertEqual(left, right)

    def testEqualsLeftNoQuoteRightQuote_Deprecated(self) -> None:

        left = CSVFormat.newFormat(",").withQuote1(None)
        right = left.withQuote0("#")

        self.__assertNotEquals0(left, right)

    def testEqualsLeftNoQuoteRightQuote(self) -> None:

        left = CSVFormat.newFormat(",").builder().setQuote1(None).build()
        right = left.builder().setQuote0("#").build()

        self.__assertNotEquals0(left, right)

    def testEqualsIgnoreSurroundingSpaces_Deprecated(self) -> None:

        right = (
            CSVFormat.newFormat("'")
            .withCommentMarker0("#")
            .withEscape0("+")
            .withIgnoreSurroundingSpaces0()
            .withQuote0('"')
            .withQuoteMode(QuoteMode.ALL)
        )

        left = right.withIgnoreSurroundingSpaces1(False)

        self.__assertNotEquals0(right, left)

    def testEqualsIgnoreSurroundingSpaces(self) -> None:

        right = (
            CSVFormat.newFormat("'")
            .builder()
            .setCommentMarker0("#")
            .setEscape0("+")
            .setIgnoreSurroundingSpaces(True)
            .setQuote0('"')
            .setQuoteMode(QuoteMode.ALL)
            .build()
        )

        left = right.builder().setIgnoreSurroundingSpaces(False).build()

        self.__assertNotEquals0(right, left)

    def testEqualsIgnoreEmptyLines_Deprecated(self) -> None:

        right = (
            CSVFormat.newFormat("'")
            .withCommentMarker0("#")
            .withEscape0("+")
            .withIgnoreEmptyLines0()
            .withIgnoreSurroundingSpaces0()
            .withQuote0('"')
            .withQuoteMode(QuoteMode.ALL)
        )

        left = right.withIgnoreEmptyLines1(False)

        self.__assertNotEquals0(right, left)

    def testEqualsIgnoreEmptyLines(self) -> None:

        right = (
            CSVFormat.newFormat("'")
            .builder()
            .setCommentMarker0("#")
            .setEscape0("+")
            .setIgnoreEmptyLines(True)
            .setIgnoreSurroundingSpaces(True)
            .setQuote0('"')
            .setQuoteMode(QuoteMode.ALL)
            .build()
        )

        left = right.builder().setIgnoreEmptyLines(False).build()

        self.__assertNotEquals0(right, left)

    def testEqualsHash(self) -> None:

        methods = CSVFormat.__dict__.values()
        for method in methods:
            if callable(method):
                name = method.__name__
                if name.startswith("with"):
                    for cls in method.__annotations__.values():
                        type_ = cls.__name__
                        if type_ == "bool":
                            defTrue = method(CSVFormat.DEFAULT, True)
                            defFalse = method(CSVFormat.DEFAULT, False)
                            self.__assertNotEquals1(name, type_, defTrue, defFalse)
                        elif type_ == "str":
                            a = method(CSVFormat.DEFAULT, "a")
                            b = method(CSVFormat.DEFAULT, "b")
                            self.__assertNotEquals1(name, type_, a, b)
                        elif type_ == "Character":
                            a = method(CSVFormat.DEFAULT, None)
                            b = method(CSVFormat.DEFAULT, Character("d"))
                            self.__assertNotEquals1(name, type_, a, b)
                        elif type_ == "String":
                            a = method(CSVFormat.DEFAULT, None)
                            b = method(CSVFormat.DEFAULT, "e")
                            self.__assertNotEquals1(name, type_, a, b)
                        elif type_ == "StringArray":
                            a = method(CSVFormat.DEFAULT, [None, None])
                            b = method(CSVFormat.DEFAULT, ["f", "g"])
                            self.__assertNotEquals1(name, type_, a, b)
                        elif type_ == "QuoteMode":
                            a = method(CSVFormat.DEFAULT, QuoteMode.MINIMAL)
                            b = method(CSVFormat.DEFAULT, QuoteMode.ALL)
                            self.__assertNotEquals1(name, type_, a, b)
                        elif type_ == "DuplicateHeaderMode":
                            a = method(CSVFormat.DEFAULT, DuplicateHeaderMode.ALLOW_ALL)
                            b = method(CSVFormat.DEFAULT, DuplicateHeaderMode.DISALLOW)
                            self.__assertNotEquals1(name, type_, a, b)
                        elif type_ == "ObjectArray":
                            a = method(CSVFormat.DEFAULT, [None, None])
                            b = method(CSVFormat.DEFAULT, [Object(), Object()])
                            self.__assertNotEquals1(name, type_, a, b)
                        elif name == "withHeader":  # covered above by StringArray
                            pass
                        else:
                            self.fail("Unhandled method: " + name + "(" + type_ + ")")

    def testEqualsEscape_Deprecated(self) -> None:

        right = (
            CSVFormat.newFormat("'")
            .withQuote0('"')
            .withCommentMarker0("#")
            .withEscape0("+")
            .withQuoteMode(QuoteMode.ALL)
        )
        left = right.withEscape0("+")

        self.__assertNotEquals0(right, left)

    def testEqualsEscape(self) -> None:

        right = (
            CSVFormat.newFormat("'")
            .builder()
            .setQuote0('"')
            .setCommentMarker0("#")
            .setEscape0("+")
            .setQuoteMode(QuoteMode.ALL)
            .build()
        )

        left = right.builder().setEscape0("0").build()

        self.__assertNotEquals0(right, left)

    def testEqualsDelimiter(self) -> None:

        right = CSVFormat.newFormat("?")
        left = CSVFormat.newFormat("?")

        self.__assertNotEquals0(right, left)

    def testEqualsCommentStart_Deprecated(self) -> None:

        right = (
            CSVFormat.newFormat("'")
            .withQuote0('"')
            .withCommentMarker0("#")
            .withQuoteMode(QuoteMode.ALL)
        )
        left = right.withCommentMarker0("0")

        self.__assertNotEquals0(right, left)

    def testEqualsCommentStart(self) -> None:

        right = (
            CSVFormat.newFormat("'")
            .builder()
            .setQuote0('"')
            .setCommentMarker0("#")
            .setQuoteMode(QuoteMode.ALL)
            .build()
        )

        left = right.builder().setCommentMarker0("'").build()

        self.__assertNotEquals0(right, left)

    def testEquals(self) -> None:

        right = CSVFormat.DEFAULT
        left = self.__copy(right)

        self.assertIsNotNone(right)
        self.assertNotEqual("A String Instance", right)

        self.assertEqual(right, right)
        self.assertEqual(right, left)
        self.assertEqual(left, right)

        self.assertEqual(right.hashCode(), right.hashCode())
        self.assertEqual(right.hashCode(), left.hashCode())

    def testDelimiterSameAsRecordSeparatorThrowsException(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.newFormat(Constants.CR)

    def testDelimiterSameAsEscapeThrowsException1(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.builder().setDelimiter0("0").setEscape0("0").build()

    def testDelimiterSameAsEscapeThrowsException_Deprecated(self) -> None:

        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT.withDelimiter("0").withEscape("0")

    def testDelimiterSameAsCommentStartThrowsException1(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.builder().setDelimiter0("0").setCommentMarker0(
                "0"
            ).build()

    def testDelimiterSameAsCommentStartThrowsException_Deprecated(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withDelimiter("0").withCommentMarker("0")

    def testDelimiterEmptyStringThrowsException1(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.builder().setDelimiter1("").build()

    def testEqualsSkipHeaderRecord(self) -> None:

        right = (
            CSVFormat.newFormat("'")
            .builder()
            .setRecordSeparator0(Constants.CR)
            .setCommentMarker0("#")
            .setEscape0("+")
            .setIgnoreEmptyLines(True)
            .setIgnoreSurroundingSpaces(True)
            .setQuote0('"')
            .setQuoteMode(QuoteMode.ALL)
            .setNullString("null")
            .setSkipHeaderRecord(True)
            .build()
        )

        left = right.builder().setSkipHeaderRecord(False).build()

        self.__assertNotEquals0(right, left)

    def __assertNotEquals1(
        self, name: str, type_: str, left: typing.Any, right: typing.Any
    ) -> None:

        if left == right or right == left:
            self.fail("Objects must not compare equal for " + name + "(" + type_ + ")")
        if hash(left) == hash(right):
            self.fail("Hash code should not be equal for " + name + "(" + type_ + ")")

    @staticmethod
    def __copy(format_: CSVFormat) -> CSVFormat:
        return format_.builder().setDelimiter0(format_.getDelimiter()).build()

    @staticmethod
    def __assertNotEquals0(right: typing.Any, left: typing.Any) -> None:
        assert right != left, f"{right} should not equal {left}"
        assert left != right, f"{left} should not equal {right}"
