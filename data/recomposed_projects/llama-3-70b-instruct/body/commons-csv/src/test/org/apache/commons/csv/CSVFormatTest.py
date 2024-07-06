from __future__ import annotations
import copy
import re
import os
from io import BytesIO
from io import StringIO
from io import IOBase
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

    @staticmethod
    def initialize_fields() -> None:
        Header.Phone: Header = None
        Header.Email: Header = None
        Header.Name: Header = None


class CSVFormatTest(unittest.TestCase):

    def testWithSystemRecordSeparator(self) -> None:
        formatWithRecordSeparator = CSVFormat.DEFAULT.withSystemRecordSeparator()
        self.assertEqual(os.linesep, formatWithRecordSeparator.getRecordSeparator())

    def testWithRecordSeparatorLF(self) -> None:
        formatWithRecordSeparator = CSVFormat.DEFAULT.withRecordSeparator0(LF)
        self.assertEqual(
            String.valueOf(LF), formatWithRecordSeparator.getRecordSeparator()
        )

    def testWithRecordSeparatorCRLF(self) -> None:
        formatWithRecordSeparator = CSVFormat.DEFAULT.withRecordSeparator1(CRLF)
        self.assertEqual(CRLF, formatWithRecordSeparator.getRecordSeparator())

    def testWithRecordSeparatorCR(self) -> None:
        formatWithRecordSeparator = CSVFormat.DEFAULT.withRecordSeparator0(CR)
        self.assertEqual(
            String.valueOf(CR), formatWithRecordSeparator.getRecordSeparator()
        )

    def testWithQuotePolicy(self) -> None:
        formatWithQuotePolicy: CSVFormat = CSVFormat.DEFAULT.withQuoteMode(
            QuoteMode.ALL
        )
        self.assertEqual(QuoteMode.ALL, formatWithQuotePolicy.getQuoteMode())

    def testWithQuoteLFThrowsException(self) -> None:
        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withQuote0(LF)

    def testWithQuoteChar(self) -> None:
        formatWithQuoteChar: CSVFormat = CSVFormat.DEFAULT.withQuote0('"')
        self.assertEqual(
            Character.valueOf('"'), formatWithQuoteChar.getQuoteCharacter()
        )

    def testWithNullString(self) -> None:
        formatWithNullString: CSVFormat = CSVFormat.DEFAULT.withNullString("null")
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
        self.assertNotSame(csvFormat, csvFormatTwo)
        self.assertNotSame(csvFormatTwo, csvFormat)
        self.assertNotEqual(csvFormatTwo, csvFormat)  # CSV-244 - should not be equal
        string = csvFormatTwo.format(objectArray)
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
        self.assertNotSame(csvFormat, csvFormatTwo)
        self.assertNotSame(csvFormatTwo, csvFormat)
        self.assertNotEqual(csvFormat, csvFormatTwo)  # CSV-244 - should not be equal
        self.assertNotEqual(csvFormatTwo, csvFormat)  # CSV-244 - should not be equal
        self.assertNotNull(string)
        self.assertEqual(",,,,,,,", string)

    def testWithEscapeCRThrowsExceptions(self) -> None:
        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withEscape0(CR)

    def testWithEscape(self) -> None:
        formatWithEscape: CSVFormat = CSVFormat.DEFAULT.withEscape0("&")
        self.assertEqual(Character.valueOf("&"), formatWithEscape.getEscapeCharacter())

    def testWithEmptyDuplicates(self) -> None:
        formatWithEmptyDuplicates: CSVFormat = (
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
        formatWithDelimiter: CSVFormat = CSVFormat.DEFAULT.withDelimiter("!")
        self.assertEqual("!", formatWithDelimiter.getDelimiter())

    def testWithCommentStartCRThrowsException(self) -> None:
        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withCommentMarker0(CR)

    def testWithCommentStart(self) -> None:
        formatWithCommentStart: CSVFormat = CSVFormat.DEFAULT.withCommentMarker0("#")
        self.assertEqual(
            Character.valueOf("#"), formatWithCommentStart.getCommentMarker()
        )

    def testTrim(self) -> None:

        pass  # LLM could not translate this method

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
        with open(out, "wb") as oos:
            oos.write(CSVFormat.DEFAULT)
            oos.flush()
        with open(out, "rb") as in_:
            format = in_.read()
        self.assertIsNotNone(format)
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
            CSVFormat.DEFAULT.withQuote0("!").withDelimiter("!")

    def testQuoteCharSameAsDelimiterThrowsException(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT.builder().setQuote0("!").setDelimiter0("!").build()

    def testQuoteCharSameAsCommentStartThrowsExceptionForWrapperType_Deprecated(
        self,
    ) -> None:
        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withQuote1(Character.valueOf("!")).withCommentMarker0("!")

    def testQuoteCharSameAsCommentStartThrowsExceptionForWrapperType(self) -> None:
        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.builder().setQuote1(
                Character.valueOf("!")
            ).setCommentMarker0("!").build()

    def testQuoteCharSameAsCommentStartThrowsException_Deprecated(self) -> None:
        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withQuote0("!").withCommentMarker0("!")

    def testQuoteCharSameAsCommentStartThrowsException(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT.builder().setQuote0("!").setCommentMarker0("!").build()

    def testPrintWithQuotes(self) -> None:
        in0: Reader = StringReader('"a,b,c\r\nx,y,z')
        out: Appendable = StringBuilder()
        format: CSVFormat = (
            CSVFormat.RFC4180.withDelimiter(",")
            .withQuote0('"')
            .withEscape0("?")
            .withQuoteMode(QuoteMode.NON_NUMERIC)
        )
        format.print2(in0, out, True)
        self.assertEqual('"""a,b,c\r\nx,y,z"', out.toString())

    def testPrintWithQuoteModeIsNONE(self) -> None:
        in0: Reader = StringReader("a,b,c")
        out: Appendable = StringBuilder()
        format: CSVFormat = (
            CSVFormat.RFC4180.withDelimiter(",")
            .withQuote0('"')
            .withEscape0("?")
            .withQuoteMode(QuoteMode.NONE)
        )
        format.print2(in0, out, True)
        self.assertEqual("a?,b?,c", out.toString())

    def testPrintWithoutQuotes(self) -> None:
        in0: typing.Union[typing.List, io.TextIOBase] = io.StringIO("")
        out: typing.Union[typing.List, io.TextIOBase] = io.StringIO()
        format: CSVFormat = (
            CSVFormat.RFC4180.withDelimiter(",")
            .withQuote0('"')
            .withEscape0("?")
            .withQuoteMode(QuoteMode.NON_NUMERIC)
        )
        format.print2(in0, out, True)
        self.assertEqual('""', out.getvalue())

    def testPrintWithEscapesEndWithoutCRLF(self) -> None:
        in0: io.TextIOWrapper = io.StringIO("x,y,x")
        out: io.StringIO = io.StringIO()
        format: CSVFormat = (
            CSVFormat.RFC4180.withEscape0("?")
            .withDelimiter(",")
            .withQuote1(None)
            .withRecordSeparator1(CRLF)
        )
        format.print2(in0, out, True)
        self.assertEqual("x?,y?,x", out.getvalue())

    def testPrintWithEscapesEndWithCRLF(self) -> None:
        in0: io.TextIOWrapper = io.StringIO("x,y,x\r\na,?b,c\r\n")
        out: io.StringIO = io.StringIO()
        format: CSVFormat = (
            CSVFormat.RFC4180.withEscape0("?")
            .withDelimiter(",")
            .withQuote1(None)
            .withRecordSeparator1(CRLF)
        )
        format.print2(in0, out, True)
        self.assertEqual("x?,y?,x?r?na?,??b?,c?r?n", out.getvalue())

    def testPrintRecordEmpty(self) -> None:
        out = io.StringIO()
        format = CSVFormat.RFC4180
        format.printRecord(out)
        self.assertEqual(format.getRecordSeparator(), out.getvalue())

    def testPrintRecord(self) -> None:
        out = io.StringIO()
        format = CSVFormat.RFC4180
        format.printRecord(out, "a", "b", "c")
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
        csvFormat = CSVFormat.INFORMIX_UNLOAD_CSV
        csvFormatTwo = csvFormat.withIgnoreHeaderCase0()
        csvFormatTwo.hashCode()

        self.assertFalse(csvFormat.getIgnoreHeaderCase())
        self.assertTrue(csvFormatTwo.getIgnoreHeaderCase())  # now different
        self.assertFalse(csvFormatTwo.getTrailingDelimiter())

        self.assertNotEqual(csvFormatTwo, csvFormat)  # CSV-244 - should not be equal
        self.assertFalse(csvFormatTwo.getAllowMissingColumnNames())

        self.assertFalse(csvFormatTwo.getTrim())

    def testGetDuplicateHeaderMode(self) -> None:
        builder: Builder = CSVFormat.DEFAULT.builder()

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
        csvFormat = CSVFormat.MYSQL
        with pytest.raises(RuntimeError):
            csvFormat.format(None)

    def testFormat(self) -> None:
        format = CSVFormat.DEFAULT

        self.assertEqual("", format.format())
        self.assertEqual("a,b,c", format.format("a", "b", "c"))
        self.assertEqual('"x,y",z', format.format("x,y", "z"))

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
        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withEscape0("!").withCommentMarker0("!")

    def testEscapeSameAsCommentStartThrowsException(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT.builder().setEscape0("!").setCommentMarker0("!").build()

    def testEqualsWithNull(self) -> None:
        csvFormat: CSVFormat = CSVFormat.POSTGRESQL_TEXT

        self.assertEqual("\\", chr(csvFormat.getEscapeCharacter()))
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

        self.assertEqual("\\", chr(csvFormat.getEscapeCharacter()))
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

        self.assertNotEqual(None, csvFormat)

    def testEqualsSkipHeaderRecord_Deprecated(self) -> None:
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
            .withSkipHeaderRecord0()
        )
        left = right.withSkipHeaderRecord1(False)

        self.__assertNotEquals0(right, left)

    def testEqualsRecordSeparator_Deprecated(self) -> None:
        right: CSVFormat = (
            CSVFormat.newFormat("'")
            .withRecordSeparator0(CR)
            .withCommentMarker0("#")
            .withEscape0("+")
            .withIgnoreEmptyLines0()
            .withIgnoreSurroundingSpaces0()
            .withQuote0('"')
            .withQuoteMode(QuoteMode.ALL)
        )
        left: CSVFormat = right.withRecordSeparator0(LF)
        self.__assertNotEquals0(right, left)

    def testEqualsRecordSeparator(self) -> None:
        right: CSVFormat = (
            CSVFormat.newFormat("'")
            .builder()
            .setRecordSeparator0(CR)
            .setCommentMarker0("#")
            .setEscape0("+")
            .setIgnoreEmptyLines(True)
            .setIgnoreSurroundingSpaces(True)
            .setQuote0('"')
            .setQuoteMode(QuoteMode.ALL)
            .build()
        )
        left: CSVFormat = right.builder().setRecordSeparator0(LF).build()
        self.__assertNotEquals0(right, left)

    def testEqualsQuotePolicy_Deprecated(self) -> None:
        right: CSVFormat = (
            CSVFormat.newFormat("'").withQuote0('"').withQuoteMode(QuoteMode.ALL)
        )
        left: CSVFormat = right.withQuoteMode(QuoteMode.MINIMAL)

        self.__assertNotEquals0(right, left)

    def testEqualsQuotePolicy(self) -> None:
        right: CSVFormat = (
            CSVFormat.newFormat("'")
            .builder()
            .setQuote0('"')
            .setQuoteMode(QuoteMode.ALL)
            .build()
        )
        left: CSVFormat = right.builder().setQuoteMode(QuoteMode.MINIMAL).build()
        self.__assertNotEquals0(right, left)

    def testEqualsQuoteChar_Deprecated(self) -> None:
        right: CSVFormat = CSVFormat.newFormat("'").withQuote0('"')
        left: CSVFormat = right.withQuote0("!")
        self.__assertNotEquals0(right, left)

    def testEqualsQuoteChar(self) -> None:
        right: CSVFormat = CSVFormat.newFormat("'").builder().setQuote0('"').build()
        left: CSVFormat = right.builder().setQuote0("!").build()

        self.__assertNotEquals0(right, left)

    def testEqualsOne(self) -> None:
        csvFormatOne: CSVFormat = CSVFormat.INFORMIX_UNLOAD
        csvFormatTwo: CSVFormat = CSVFormat.MYSQL
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
        self.assertNotEqual(csvFormatTwo, csvFormatOne)
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
        self.assertNotEqual(csvFormatOne, csvFormatTwo)
        self.assertNotEqual(csvFormatTwo, csvFormatOne)
        self.assertNotEqual(csvFormatOne, csvFormatTwo)
        self.assertNotEqual(csvFormatTwo, csvFormatOne)
        self.assertNotEqual(csvFormatTwo, csvFormatOne)

    def testEqualsNullString_Deprecated(self) -> None:
        right: CSVFormat = (
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
        left: CSVFormat = right.withNullString("---")
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
        left = CSVFormat.newFormat(",").builder().setQuote1(None).build()
        right = left.builder().setQuote1(None).build()
        self.assertEqual(left, right)

    def testEqualsLeftNoQuoteRightQuote_Deprecated(self) -> None:
        left: CSVFormat = CSVFormat.newFormat(",").withQuote1(None)
        right: CSVFormat = left.withQuote0("#")

        self.__assertNotEquals0(left, right)

    def testEqualsLeftNoQuoteRightQuote(self) -> None:
        left: CSVFormat = CSVFormat.newFormat(",").builder().setQuote1(None).build()
        right: CSVFormat = left.builder().setQuote0("#").build()

        CSVFormatTest.__assertNotEquals0(left, right)

    def testEqualsIgnoreSurroundingSpaces_Deprecated(self) -> None:
        right: CSVFormat = (
            CSVFormat.newFormat("'")
            .withCommentMarker0("#")
            .withEscape0("+")
            .withIgnoreSurroundingSpaces0()
            .withQuote0('"')
            .withQuoteMode(QuoteMode.ALL)
        )
        left: CSVFormat = right.withIgnoreSurroundingSpaces1(False)

        self.__assertNotEquals0(right, left)

    def testEqualsIgnoreSurroundingSpaces(self) -> None:
        right: CSVFormat = (
            CSVFormat.newFormat("'")
            .builder()
            .setCommentMarker0("#")
            .setEscape0("+")
            .setIgnoreSurroundingSpaces(True)
            .setQuote0('"')
            .setQuoteMode(QuoteMode.ALL)
            .build()
        )
        left: CSVFormat = right.builder().setIgnoreSurroundingSpaces(False).build()
        self.__assertNotEquals0(right, left)

    def testEqualsIgnoreEmptyLines_Deprecated(self) -> None:
        right: CSVFormat = (
            CSVFormat.newFormat("'")
            .withCommentMarker0("#")
            .withEscape0("+")
            .withIgnoreEmptyLines0()
            .withIgnoreSurroundingSpaces0()
            .withQuote0('"')
            .withQuoteMode(QuoteMode.ALL)
        )
        left: CSVFormat = right.withIgnoreEmptyLines1(False)

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
        methods = CSVFormat.__dict__["__dict__"]["_declared_fields"]
        for method in methods:
            if method.__dict__["__dict__"]["_field_info"].__dict__["_is_public"]:
                name = method.__dict__["__dict__"]["_field_info"].__dict__["_name"]
                if name.startswith("with"):
                    for cls in method.__dict__["__dict__"]["_field_info"].__dict__[
                        "_type"
                    ]:
                        type = cls.__dict__["__dict__"]["_name"]
                        if "boolean" == type:
                            defTrue = method(CSVFormat.DEFAULT, True)
                            defFalse = method(CSVFormat.DEFAULT, False)
                            self.__assertNotEquals1(name, type, defTrue, defFalse)
                        elif "char" == type:
                            a = method(CSVFormat.DEFAULT, "a")
                            b = method(CSVFormat.DEFAULT, "b")
                            self.__assertNotEquals1(name, type, a, b)
                        elif "java.lang.Character" == type:
                            a = method(CSVFormat.DEFAULT, None)
                            b = method(CSVFormat.DEFAULT, "d")
                            self.__assertNotEquals1(name, type, a, b)
                        elif "java.lang.String" == type:
                            a = method(CSVFormat.DEFAULT, None)
                            b = method(CSVFormat.DEFAULT, "e")
                            self.__assertNotEquals1(name, type, a, b)
                        elif "java.lang.String[]" == type:
                            a = method(CSVFormat.DEFAULT, [None, None])
                            b = method(CSVFormat.DEFAULT, ["f", "g"])
                            self.__assertNotEquals1(name, type, a, b)
                        elif "org.apache.commons.csv.QuoteMode" == type:
                            a = method(CSVFormat.DEFAULT, QuoteMode.MINIMAL)
                            b = method(CSVFormat.DEFAULT, QuoteMode.ALL)
                            self.__assertNotEquals1(name, type, a, b)
                        elif "org.apache.commons.csv.DuplicateHeaderMode" == type:
                            a = method(CSVFormat.DEFAULT, DuplicateHeaderMode.ALLOW_ALL)
                            b = method(CSVFormat.DEFAULT, DuplicateHeaderMode.DISALLOW)
                            self.__assertNotEquals1(name, type, a, b)
                        elif "java.lang.Object[]" == type:
                            a = method(CSVFormat.DEFAULT, [None, None])
                            b = method(CSVFormat.DEFAULT, [None, None])
                            self.__assertNotEquals1(name, type, a, b)
                        elif "withHeader" == name:  # covered above by String[]
                            pass
                        else:
                            self.fail("Unhandled method: " + name + "(" + type + ")")

    def testEqualsEscape_Deprecated(self) -> None:
        right: CSVFormat = (
            CSVFormat.newFormat("'")
            .withQuote0('"')
            .withCommentMarker0("#")
            .withEscape0("+")
            .withQuoteMode(QuoteMode.ALL)
        )
        left: CSVFormat = right.withEscape0("!")
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
        left = right.builder().setEscape0("!").build()
        self.__assertNotEquals0(right, left)

    def testEqualsDelimiter(self) -> None:
        right: CSVFormat = CSVFormat.newFormat("!")
        left: CSVFormat = CSVFormat.newFormat("?")
        self.__assertNotEquals0(right, left)

    def testEqualsCommentStart_Deprecated(self) -> None:
        right: CSVFormat = (
            CSVFormat.newFormat("'")
            .withQuote0('"')
            .withCommentMarker0("#")
            .withQuoteMode(QuoteMode.ALL)
        )
        left: CSVFormat = right.withCommentMarker0("!")
        self.__assertNotEquals0(right, left)

    def testEqualsCommentStart(self) -> None:
        right: CSVFormat = (
            CSVFormat.newFormat("'")
            .builder()
            .setQuote0('"')
            .setCommentMarker0("#")
            .setQuoteMode(QuoteMode.ALL)
            .build()
        )
        left: CSVFormat = right.builder().setCommentMarker0("!").build()
        self.__assertNotEquals0(right, left)

    def testEquals(self) -> None:
        right: CSVFormat = CSVFormat.DEFAULT
        left: CSVFormat = self.__copy(right)

        self.assertNotEqual(None, right)
        self.assertNotEqual("A String Instance", right)

        self.assertEqual(right, right)
        self.assertEqual(right, left)
        self.assertEqual(left, right)

        self.assertEqual(right.hashCode(), right.hashCode())
        self.assertEqual(right.hashCode(), left.hashCode())

    def testDelimiterSameAsRecordSeparatorThrowsException(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.newFormat(CR)

    def testDelimiterSameAsEscapeThrowsException1(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT.builder().setDelimiter0("!").setEscape0("!").build()

    def testDelimiterSameAsEscapeThrowsException_Deprecated(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT.withDelimiter("!").withEscape0("!")

    def testDelimiterSameAsCommentStartThrowsException1(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT.builder().setDelimiter0("!").setCommentMarker0(
                "!"
            ).build()

    def testDelimiterSameAsCommentStartThrowsException_Deprecated(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT.withDelimiter("!").withCommentMarker0("!")

    def testDelimiterEmptyStringThrowsException1(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT.builder().setDelimiter1("").build()

    def testEqualsSkipHeaderRecord(self) -> None:
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
        if left.__hash__() == right.__hash__():
            self.fail("Hash code should not be equal for " + name + "(" + type + ")")

    @staticmethod
    def __copy(format: CSVFormat) -> CSVFormat:
        return format.builder().setDelimiter0(format.getDelimiter())

    @staticmethod
    def __assertNotEquals0(right: typing.Any, left: typing.Any) -> None:
        assert right != left
        assert left != right


Header.initialize_fields()
