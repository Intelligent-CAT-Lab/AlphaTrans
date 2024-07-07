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

        # Create a CSVFormat object with LF as the record separator
        formatWithRecordSeparator = CSVFormat.DEFAULT.withRecordSeparator0(LF)

        # Assert that the record separator is equal to LF
        self.assertEqual(str(LF), formatWithRecordSeparator.getRecordSeparator())

    def testWithRecordSeparatorCRLF(self) -> None:

        formatWithRecordSeparator = CSVFormat.DEFAULT.withRecordSeparator1(CRLF)
        self.assertEqual(CRLF, formatWithRecordSeparator.getRecordSeparator())

    def testWithRecordSeparatorCR(self) -> None:

        # Create a CSVFormat object with record separator as CR
        formatWithRecordSeparator = CSVFormat.DEFAULT.withRecordSeparator0(CR)

        # Assert that the record separator is equal to the string representation of CR
        self.assertEqual(str(CR), formatWithRecordSeparator.getRecordSeparator())

    def testWithQuotePolicy(self) -> None:

        formatWithQuotePolicy = CSVFormat.DEFAULT.withQuoteMode(QuoteMode.ALL)
        self.assertEqual(QuoteMode.ALL, formatWithQuotePolicy.getQuoteMode())

    def testWithQuoteLFThrowsException(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withQuote(LF)

    def testWithQuoteChar(self) -> None:

        formatWithQuoteChar = CSVFormat.DEFAULT.withQuote0('"')
        self.assertEqual('"', formatWithQuoteChar.getQuoteCharacter())

    def testWithNullString(self) -> None:

        formatWithNullString = CSVFormat.DEFAULT.withNullString("null")
        self.assertEqual("null", formatWithNullString.getNullString())

    def testWithIgnoreSurround(self) -> None:

        assertFalse(
            CSVFormat.DEFAULT.withIgnoreSurroundingSpaces1(
                False
            ).getIgnoreSurroundingSpaces()
        )
        assertTrue(
            CSVFormat.DEFAULT.withIgnoreSurroundingSpaces0().getIgnoreSurroundingSpaces()
        )

    def testWithIgnoreEmptyLines(self) -> None:

        assert not CSVFormat.DEFAULT.withIgnoreEmptyLines1(False).getIgnoreEmptyLines()
        assert CSVFormat.DEFAULT.withIgnoreEmptyLines0().getIgnoreEmptyLines()

    def testWithHeaderComments(self) -> None:

        pass  # LLM could not translate this method

    def testWithEscapeCRThrowsExceptions(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withEscape(CR)

    def testWithEscape(self) -> None:

        formatWithEscape = CSVFormat.DEFAULT.withEscape0("&")
        self.assertEqual(Character.valueOf("&"), formatWithEscape.getEscapeCharacter())

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

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withDelimiter(LF)

    def testWithDelimiter(self) -> None:

        formatWithDelimiter = CSVFormat.DEFAULT.withDelimiter("|")
        self.assertEqual("|", formatWithDelimiter.getDelimiter())

    def testWithCommentStartCRThrowsException(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withCommentMarker(CR)

    def testWithCommentStart(self) -> None:

        formatWithCommentStart = CSVFormat.DEFAULT.withCommentMarker0("#")
        self.assertEqual("#", formatWithCommentStart.getCommentMarker())

    def testTrim(self) -> None:

        formatWithTrim = (
            CSVFormat.DEFAULT.withDelimiter(",")
            .withTrim0()
            .withQuote1(None)
            .withRecordSeparator1(CRLF)
        )

        in_ = "a,b,c"
        out = io.StringIO()
        formatWithTrim.print2(in_, out, True)
        self.assertEqual("a,b,c", out.getvalue())

        in_ = io.StringIO(" x,y,z")
        out = io.StringIO()
        formatWithTrim.print2(in_, out, True)
        self.assertEqual("x,y,z", out.getvalue())

        in_ = io.StringIO("")
        out = io.StringIO()
        formatWithTrim.print2(in_, out, True)
        self.assertEqual("", out.getvalue())

        in_ = io.StringIO("header\r\n")
        out = io.StringIO()
        formatWithTrim.print2(in_, out, True)
        self.assertEqual("header", out.getvalue())

    def testToStringAndWithCommentMarkerTakingCharacter(self) -> None:

        csvFormat_Predefined = Predefined.Default
        csvFormat = csvFormat_Predefined.getFormat()

        assert csvFormat.getEscapeCharacter() is None
        assert csvFormat.isQuoteCharacterSet()

        assert not csvFormat.getTrim()
        assert not csvFormat.getIgnoreSurroundingSpaces()

        assert not csvFormat.getTrailingDelimiter()
        assert csvFormat.getDelimiter() == ","

        assert not csvFormat.getIgnoreHeaderCase()
        assert csvFormat.getRecordSeparator() == "\r\n"

        assert not csvFormat.isCommentMarkerSet()
        assert csvFormat.getCommentMarker() is None

        assert not csvFormat.isNullStringSet()
        assert not csvFormat.getAllowMissingColumnNames()

        assert not csvFormat.isEscapeCharacterSet()
        assert not csvFormat.getSkipHeaderRecord()

        assert csvFormat.getNullString() is None
        assert csvFormat.getQuoteMode() is None

        assert csvFormat.getIgnoreEmptyLines()
        assert csvFormat.getQuoteCharacter() == '"'

        character = "n"

        csvFormatTwo = csvFormat.withCommentMarker1(character)

        assert csvFormat.getEscapeCharacter() is None
        assert csvFormat.isQuoteCharacterSet()

        assert not csvFormat.getTrim()
        assert not csvFormat.getIgnoreSurroundingSpaces()

        assert not csvFormat.getTrailingDelimiter()
        assert csvFormat.getDelimiter() == ","

        assert not csvFormat.getIgnoreHeaderCase()
        assert csvFormat.getRecordSeparator() == "\r\n"

        assert not csvFormat.isCommentMarkerSet()
        assert csvFormat.getCommentMarker() is None

        assert not csvFormat.isNullStringSet()
        assert not csvFormat.getAllowMissingColumnNames()

        assert not csvFormat.isEscapeCharacterSet()
        assert not csvFormat.getSkipHeaderRecord()

        assert csvFormat.getNullString() is None
        assert csvFormat.getQuoteMode() is None

        assert csvFormat.getIgnoreEmptyLines()
        assert csvFormat.getQuoteCharacter() == '"'

        assert not csvFormatTwo.isNullStringSet()
        assert not csvFormatTwo.getAllowMissingColumnNames()

        assert csvFormatTwo.getQuoteCharacter() == '"'
        assert csvFormatTwo.getNullString() is None

        assert csvFormatTwo.getDelimiter() == ","
        assert not csvFormatTwo.getTrailingDelimiter()

        assert csvFormatTwo.isCommentMarkerSet()
        assert not csvFormatTwo.getIgnoreHeaderCase()

        assert not csvFormatTwo.getTrim()
        assert csvFormatTwo.getEscapeCharacter() is None

        assert csvFormatTwo.isQuoteCharacterSet()
        assert not csvFormatTwo.getIgnoreSurroundingSpaces()

        assert csvFormatTwo.getRecordSeparator() == "\r\n"
        assert csvFormatTwo.getQuoteMode() is None

        assert csvFormatTwo.getCommentMarker() == "n"
        assert not csvFormatTwo.getSkipHeaderRecord()

        assert not csvFormatTwo.isEscapeCharacterSet()
        assert csvFormatTwo.getIgnoreEmptyLines()

        assert csvFormat != csvFormatTwo
        assert csvFormatTwo != csvFormat

        assert csvFormat.getEscapeCharacter() is None
        assert csvFormat.isQuoteCharacterSet()

        assert not csvFormat.getTrim()
        assert not csvFormat.getIgnoreSurroundingSpaces()

        assert not csvFormat.getTrailingDelimiter()
        assert csvFormat.getDelimiter() == ","

        assert not csvFormat.getIgnoreHeaderCase()
        assert csvFormat.getRecordSeparator() == "\r\n"

        assert not csvFormat.isCommentMarkerSet()
        assert csvFormat.getCommentMarker() is None

        assert not csvFormat.isNullStringSet()
        assert not csvFormat.getAllowMissingColumnNames()

        assert not csvFormat.isEscapeCharacterSet()
        assert not csvFormat.getSkipHeaderRecord()

        assert csvFormat.getNullString() is None
        assert csvFormat.getQuoteMode() is None

        assert csvFormat.getIgnoreEmptyLines()
        assert csvFormat.getQuoteCharacter() == '"'

        assert not csvFormatTwo.isNullStringSet()
        assert not csvFormatTwo.getAllowMissingColumnNames()

        assert csvFormatTwo.getQuoteCharacter() == '"'
        assert csvFormatTwo.getNullString() is None

        assert csvFormatTwo.getDelimiter() == ","
        assert not csvFormatTwo.getTrailingDelimiter()

        assert csvFormatTwo.isCommentMarkerSet()
        assert not csvFormatTwo.getIgnoreHeaderCase()

        assert not csvFormatTwo.getTrim()
        assert csvFormatTwo.getEscapeCharacter() is None

        assert csvFormatTwo.isQuoteCharacterSet()
        assert not csvFormatTwo.getIgnoreSurroundingSpaces()

        assert csvFormatTwo.getRecordSeparator() == "\r\n"
        assert csvFormatTwo.getQuoteMode() is None

        assert csvFormatTwo.getCommentMarker() == "n"
        assert not csvFormatTwo.getSkipHeaderRecord()

        assert not csvFormatTwo.isEscapeCharacterSet()
        assert csvFormatTwo.getIgnoreEmptyLines()

        assert csvFormat != csvFormatTwo
        assert csvFormatTwo != csvFormat

        assert (
            csvFormatTwo.toString()
            == 'Delimiter=<,> QuoteChar=<"> CommentStart=<n> RecordSeparator=<\r\n> EmptyLines:ignored SkipHeaderRecord:false'
        )

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
        self.assertEqual(
            CSVFormat.DEFAULT.getDelimiter(), format.getDelimiter(), "delimiter"
        )
        self.assertEqual(
            CSVFormat.DEFAULT.getQuoteCharacter(),
            format.getQuoteCharacter(),
            "encapsulator",
        )
        self.assertEqual(
            CSVFormat.DEFAULT.getCommentMarker(),
            format.getCommentMarker(),
            "comment start",
        )
        self.assertEqual(
            CSVFormat.DEFAULT.getRecordSeparator(),
            format.getRecordSeparator(),
            "record separator",
        )
        self.assertEqual(
            CSVFormat.DEFAULT.getEscapeCharacter(),
            format.getEscapeCharacter(),
            "escape",
        )
        self.assertEqual(
            CSVFormat.DEFAULT.getIgnoreSurroundingSpaces(),
            format.getIgnoreSurroundingSpaces(),
            "trim",
        )
        self.assertEqual(
            CSVFormat.DEFAULT.getIgnoreEmptyLines(),
            format.getIgnoreEmptyLines(),
            "empty lines",
        )

    def testRFC4180(self) -> None:

        self.assertIsNone(RFC4180.getCommentMarker())
        self.assertEqual(",", RFC4180.getDelimiter())
        self.assertIsNone(RFC4180.getEscapeCharacter())
        self.assertFalse(RFC4180.getIgnoreEmptyLines())
        self.assertEqual('"', RFC4180.getQuoteCharacter())
        self.assertIsNone(RFC4180.getQuoteMode())
        self.assertEqual("\r\n", RFC4180.getRecordSeparator())

    def testQuotePolicyNoneWithoutEscapeThrowsException_Deprecated(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.newFormat("!").withQuoteMode(QuoteMode.NONE)

    def testQuotePolicyNoneWithoutEscapeThrowsException(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.newFormat("!").builder().setQuoteMode(QuoteMode.NONE).build()

    def testQuoteCharSameAsDelimiterThrowsException_Deprecated(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withQuote("0").withDelimiter("0")

    def testQuoteCharSameAsDelimiterThrowsException(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.builder().setQuote0("0").setDelimiter0("0").build()

    def testQuoteCharSameAsCommentStartThrowsExceptionForWrapperType_Deprecated(
        self,
    ) -> None:

        pass  # LLM could not translate this method

    def testQuoteCharSameAsCommentStartThrowsExceptionForWrapperType(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.builder().setQuote1(
                Character.valueOf("!")
            ).setCommentMarker0("0").build()

    def testQuoteCharSameAsCommentStartThrowsException_Deprecated(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withQuote("0").withCommentMarker("0")

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

        in_ = io.StringIO("a,b,c")
        out = io.StringIO()
        format = (
            CSVFormat.RFC4180.withDelimiter(",")
            .withQuote0('"')
            .withEscape0("?")
            .withQuoteMode(QuoteMode.NONE)
        )
        format.print2(in_, out, True)
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
            .withRecordSeparator1("\n")
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
            .withRecordSeparator1("\r\n")
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
        format.printRecord(out, "a", "b", "c")
        self.assertEqual("a,b,c" + format.getRecordSeparator(), out.getvalue())

    def testNewFormat(self) -> None:

        csv_format = CSVFormat.newFormat("X")

        self.assertFalse(csv_format.getSkipHeaderRecord())
        self.assertFalse(csv_format.isEscapeCharacterSet())

        self.assertIsNone(csv_format.getRecordSeparator())
        self.assertIsNone(csv_format.getQuoteMode())

        self.assertIsNone(csv_format.getCommentMarker())
        self.assertFalse(csv_format.getIgnoreHeaderCase())

        self.assertFalse(csv_format.getAllowMissingColumnNames())
        self.assertFalse(csv_format.getTrim())

        self.assertFalse(csv_format.isNullStringSet())
        self.assertIsNone(csv_format.getEscapeCharacter())

        self.assertFalse(csv_format.getIgnoreSurroundingSpaces())
        self.assertFalse(csv_format.getTrailingDelimiter())

        self.assertEqual("X", csv_format.getDelimiter())
        self.assertIsNone(csv_format.getNullString())

        self.assertFalse(csv_format.isQuoteCharacterSet())
        self.assertFalse(csv_format.isCommentMarkerSet())

        self.assertIsNone(csv_format.getQuoteCharacter())
        self.assertFalse(csv_format.getIgnoreEmptyLines())

        self.assertFalse(csv_format.getSkipHeaderRecord())
        self.assertFalse(csv_format.isEscapeCharacterSet())

        self.assertIsNone(csv_format.getRecordSeparator())
        self.assertIsNone(csv_format.getQuoteMode())

        self.assertIsNone(csv_format.getCommentMarker())
        self.assertFalse(csv_format.getIgnoreHeaderCase())

        self.assertFalse(csv_format.getAllowMissingColumnNames())
        self.assertFalse(csv_format.getTrim())

        self.assertFalse(csv_format.isNullStringSet())
        self.assertIsNone(csv_format.getEscapeCharacter())

        self.assertFalse(csv_format.getIgnoreSurroundingSpaces())
        self.assertFalse(csv_format.getTrailingDelimiter())

        self.assertEqual("X", csv_format.getDelimiter())
        self.assertIsNone(csv_format.getNullString())

        self.assertFalse(csv_format.isQuoteCharacterSet())
        self.assertFalse(csv_format.isCommentMarkerSet())

        self.assertIsNone(csv_format.getQuoteCharacter())
        self.assertFalse(csv_format.getIgnoreEmptyLines())

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

        with pytest.raises(RuntimeError) as e:
            csv_format.format(None)

        assert e.type == RuntimeError
        assert e.value.getStackTrace()[0].getClassName() == Objects.__class__.__name__

    def testFormat(self) -> None:

        format = CSVFormat.DEFAULT

        self.assertEqual("", format.format([]))
        self.assertEqual("a,b,c", format.format(["a", "b", "c"]))
        self.assertEqual('"x,y",z', format.format(["x,y", "z"]))

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
            .withRecordSeparator0("\r")
            .withCommentMarker0("#")
            .withEscape0("+")
            .withIgnoreEmptyLines0()
            .withIgnoreSurroundingSpaces0()
            .withQuote0('"')
            .withQuoteMode(QuoteMode.ALL)
        )
        left = right.withRecordSeparator0("\n")

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

        right = CSVFormat.newFormat("'").builder().setQuote0('"')
        left = right.setQuote0('"').build()

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
            .withRecordSeparator0(CR)
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
            .setRecordSeparator0(CR)
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

        left = CSVFormat.newFormat(",").builder().setQuote1(None)
        right = left.builder().setQuote1(None)

        self.assertEqual(left, right)

    def testEqualsLeftNoQuoteRightQuote_Deprecated(self) -> None:

        left = CSVFormat.newFormat(",").withQuote1(None)
        right = left.withQuote0("#")

        self.__assertNotEquals0(left, right)

    def testEqualsLeftNoQuoteRightQuote(self) -> None:

        left = CSVFormat.newFormat(",").builder().setQuote1(None)
        right = left.setQuote0("#").build()

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

        methods = CSVFormat.class_.getDeclaredMethods()
        for method in methods:
            if Modifier.isPublic(method.getModifiers()):
                name = method.getName()
                if name.startswith("with"):
                    for cls in method.getParameterTypes():
                        type = cls.getCanonicalName()
                        if "boolean" == type:
                            defTrue = method.invoke(CSVFormat.DEFAULT, True)
                            defFalse = method.invoke(CSVFormat.DEFAULT, False)
                            self.__assertNotEquals1(name, type, defTrue, defFalse)
                        elif "char" == type:
                            a = method.invoke(CSVFormat.DEFAULT, "a")
                            b = method.invoke(CSVFormat.DEFAULT, "b")
                            self.__assertNotEquals1(name, type, a, b)
                        elif "java.lang.Character" == type:
                            a = method.invoke(CSVFormat.DEFAULT, [None])
                            b = method.invoke(CSVFormat.DEFAULT, Character.valueOf("d"))
                            self.__assertNotEquals1(name, type, a, b)
                        elif "java.lang.String" == type:
                            a = method.invoke(CSVFormat.DEFAULT, [None])
                            b = method.invoke(CSVFormat.DEFAULT, "e")
                            self.__assertNotEquals1(name, type, a, b)
                        elif "java.lang.String[]" == type:
                            a = method.invoke(CSVFormat.DEFAULT, [["null", "null"]])
                            b = method.invoke(CSVFormat.DEFAULT, [["f", "g"]])
                            self.__assertNotEquals1(name, type, a, b)
                        elif "org.apache.commons.csv.QuoteMode" == type:
                            a = method.invoke(CSVFormat.DEFAULT, QuoteMode.MINIMAL)
                            b = method.invoke(CSVFormat.DEFAULT, QuoteMode.ALL)
                            self.__assertNotEquals1(name, type, a, b)
                        elif "org.apache.commons.csv.DuplicateHeaderMode" == type:
                            a = method.invoke(
                                CSVFormat.DEFAULT, DuplicateHeaderMode.ALLOW_ALL
                            )
                            b = method.invoke(
                                CSVFormat.DEFAULT, DuplicateHeaderMode.DISALLOW
                            )
                            self.__assertNotEquals1(name, type, a, b)
                        elif "java.lang.Object[]" == type:
                            a = method.invoke(CSVFormat.DEFAULT, [[None, None]])
                            b = method.invoke(CSVFormat.DEFAULT, [[object(), object()]])
                            self.__assertNotEquals1(name, type, a, b)
                        elif "withHeader" == name:
                            pass
                        else:
                            self.fail("Unhandled method: " + name + "(" + type + ")")

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
        left = right.builder().setEscape0("'").build()

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
        left = right.withCommentMarker0("\x21")

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
            CSVFormat.newFormat(CR)

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
            .setRecordSeparator0("\r")
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
        self, name: str, type: str, left: typing.Any, right: typing.Any
    ) -> None:

        if left == right or right == left:
            self.fail("Objects must not compare equal for " + name + "(" + type + ")")
        if hash(left) == hash(right):
            self.fail("Hash code should not be equal for " + name + "(" + type + ")")

    @staticmethod
    def __copy(format: CSVFormat) -> CSVFormat:
        return format.builder().setDelimiter0(format.getDelimiter()).build()

    @staticmethod
    def __assertNotEquals0(right: typing.Any, left: typing.Any) -> None:
        assert right != left, f"{right} should not equal {left}"
        assert left != right, f"{left} should not equal {right}"
