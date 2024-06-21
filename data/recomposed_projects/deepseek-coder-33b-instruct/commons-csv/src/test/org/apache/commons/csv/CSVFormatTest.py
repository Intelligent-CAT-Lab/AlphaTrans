from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
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

    @pytest.mark.test
    def testWithSystemRecordSeparator(self) -> None:
        formatWithRecordSeparator = CSVFormat.DEFAULT.withSystemRecordSeparator()
        self.assertEqual(os.linesep, formatWithRecordSeparator.getRecordSeparator())

    @pytest.mark.test
    def testWithRecordSeparatorLF(self) -> None:
        formatWithRecordSeparator = CSVFormat.DEFAULT.withRecordSeparator0(LF)
        self.assertEqual(str(LF), formatWithRecordSeparator.getRecordSeparator())

    @pytest.mark.test
    def testWithRecordSeparatorCRLF(self) -> None:
        formatWithRecordSeparator = CSVFormat.DEFAULT.withRecordSeparator1(CRLF)
        self.assertEqual(CRLF, formatWithRecordSeparator.getRecordSeparator())

    @pytest.mark.test
    def testWithRecordSeparatorCR(self) -> None:
        formatWithRecordSeparator = CSVFormat.DEFAULT.withRecordSeparator0(CR)
        self.assertEqual(str(CR), formatWithRecordSeparator.getRecordSeparator())

    @pytest.mark.test
    def testWithQuotePolicy(self) -> None:

        formatWithQuotePolicy = CSVFormat.DEFAULT.withQuoteMode(QuoteMode.ALL)
        self.assertEqual(QuoteMode.ALL, formatWithQuotePolicy.getQuoteMode())

    @pytest.mark.test
    def testWithQuoteLFThrowsException(self) -> None:
        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withQuote(LF)

    @pytest.mark.test
    def testWithQuoteChar(self) -> None:

        formatWithQuoteChar = CSVFormat.DEFAULT.withQuote0('"')
        self.assertEqual(
            Character.valueOf('"'), formatWithQuoteChar.getQuoteCharacter()
        )

    @pytest.mark.test
    def testWithNullString(self) -> None:
        formatWithNullString = CSVFormat.DEFAULT.withNullString("null")
        self.assertEqual("null", formatWithNullString.getNullString())

    @pytest.mark.test
    def testWithIgnoreSurround(self) -> None:

        # Test with ignore surrounding spaces set to False
        self.assertFalse(
            CSVFormat.DEFAULT.withIgnoreSurroundingSpaces1(
                False
            ).getIgnoreSurroundingSpaces()
        )

        # Test with ignore surrounding spaces set to True
        self.assertTrue(
            CSVFormat.DEFAULT.withIgnoreSurroundingSpaces0().getIgnoreSurroundingSpaces()
        )

    @pytest.mark.test
    def testWithIgnoreEmptyLines(self) -> None:

        # Test with ignoreEmptyLines set to False
        self.assertFalse(
            CSVFormat.DEFAULT.withIgnoreEmptyLines1(False).getIgnoreEmptyLines()
        )

        # Test with ignoreEmptyLines set to True
        self.assertTrue(CSVFormat.DEFAULT.withIgnoreEmptyLines0().getIgnoreEmptyLines())

    @pytest.mark.test
    def testWithHeaderComments(self) -> None:

        pass  # LLM could not translate this method

    @pytest.mark.test
    def testWithEscapeCRThrowsExceptions(self) -> None:
        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withEscape(CR)

    @pytest.mark.test
    def testWithEscape(self) -> None:

        # Create a CSVFormat object with escape character '&'
        formatWithEscape = CSVFormat.DEFAULT.withEscape0("&")

        # Assert that the escape character is '&'
        self.assertEqual(Character.valueOf("&"), formatWithEscape.getEscapeCharacter())

    @pytest.mark.test
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

    @pytest.mark.test
    def testWithDelimiterLFThrowsException(self) -> None:
        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withDelimiter(LF)

    @pytest.mark.test
    def testWithDelimiter(self) -> None:
        formatWithDelimiter = CSVFormat.DEFAULT.withDelimiter("|")
        self.assertEqual("|", formatWithDelimiter.getDelimiter())

    @pytest.mark.test
    def testWithCommentStartCRThrowsException(self) -> None:
        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withCommentMarker(CR)

    @pytest.mark.test
    def testWithCommentStart(self) -> None:

        formatWithCommentStart = CSVFormat.DEFAULT.withCommentMarker0("#")
        self.assertEqual(
            Character.valueOf("#"), formatWithCommentStart.getCommentMarker()
        )

    @pytest.mark.test
    def testTrim(self) -> None:

        formatWithTrim = (
            CSVFormat.DEFAULT.withDelimiter(",")
            .withTrim0()
            .withQuote1(None)
            .withRecordSeparator1(CRLF)
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

    @pytest.mark.test
    def testToStringAndWithCommentMarkerTakingCharacter(self) -> None:

        pass  # LLM could not translate this method

    @pytest.mark.test
    def testToString(self) -> None:

        string = CSVFormat.INFORMIX_UNLOAD.toString()

        self.assertEqual(
            'Delimiter=<|> Escape=<\\> QuoteChar=<"> RecordSeparator=<\n> EmptyLines:ignored SkipHeaderRecord:False',
            string,
        )

    @pytest.mark.test
    def testSerialization(self) -> None:

        out = io.BytesIO()

        try:
            oos = pickle.Pickler(out)
            oos.dump(CSVFormat.DEFAULT)
            oos.flush()
        finally:
            oos.clear_memo()

        in_ = pickle.Unpickler(io.BytesIO(out.getvalue()))
        format = in_.load()

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

    @pytest.mark.test
    def testRFC4180(self) -> None:

        # assertNull(RFC4180.getCommentMarker());
        self.assertIsNone(RFC4180.getCommentMarker())

        # assertEquals(',', RFC4180.getDelimiter());
        self.assertEqual(",", RFC4180.getDelimiter())

        # assertNull(RFC4180.getEscapeCharacter());
        self.assertIsNone(RFC4180.getEscapeCharacter())

        # assertFalse(RFC4180.getIgnoreEmptyLines());
        self.assertFalse(RFC4180.getIgnoreEmptyLines())

        # assertEquals(Character.valueOf('"'), RFC4180.getQuoteCharacter());
        self.assertEqual('"', RFC4180.getQuoteCharacter())

        # assertNull(RFC4180.getQuoteMode());
        self.assertIsNone(RFC4180.getQuoteMode())

        # assertEquals("\r\n", RFC4180.getRecordSeparator());
        self.assertEqual("\r\n", RFC4180.getRecordSeparator())

    @pytest.mark.test
    def testQuotePolicyNoneWithoutEscapeThrowsException_Deprecated(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.newFormat("!").withQuoteMode(QuoteMode.NONE)

    @pytest.mark.test
    def testQuotePolicyNoneWithoutEscapeThrowsException(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.newFormat("\0").builder().setQuoteMode(QuoteMode.NONE).build()

    @pytest.mark.test
    def testQuoteCharSameAsDelimiterThrowsException_Deprecated(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withQuote("0").withDelimiter("0")

    @pytest.mark.test
    def testQuoteCharSameAsDelimiterThrowsException(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.builder().setQuote0("0").setDelimiter0("0").build()

    @pytest.mark.test
    def testQuoteCharSameAsCommentStartThrowsExceptionForWrapperType_Deprecated(
        self,
    ) -> None:

        pass  # LLM could not translate this method

    @pytest.mark.test
    def testQuoteCharSameAsCommentStartThrowsExceptionForWrapperType(self) -> None:

        pass  # LLM could not translate this method

    @pytest.mark.test
    def testQuoteCharSameAsCommentStartThrowsException_Deprecated(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withQuote("0").withCommentMarker("0")

    @pytest.mark.test
    def testQuoteCharSameAsCommentStartThrowsException(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.builder().setQuote0("0").setCommentMarker0("0").build()

    @pytest.mark.test
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

    @pytest.mark.test
    def testPrintWithQuoteModeIsNONE(self) -> None:

        in_ = io.StringIO("a,b,c")
        out = io.StringIO()
        format_ = (
            CSVFormat.RFC4180.withDelimiter(",")
            .withQuote0('"')
            .withEscape0("?")
            .withQuoteMode(QuoteMode.NONE)
        )
        format_.print2(in_, out, True)
        self.assertEqual("a?,b?,c", out.getvalue())

    @pytest.mark.test
    def testPrintWithoutQuotes(self) -> None:

        in_ = io.StringIO("")
        out = io.StringIO()
        format_ = (
            CSVFormat.RFC4180.withDelimiter(",")
            .withQuote0('"')
            .withEscape0("?")
            .withQuoteMode(QuoteMode.NON_NUMERIC)
        )
        format_.print2(in_, out, True)
        self.assertEqual('""', out.getvalue())

    @pytest.mark.test
    def testPrintWithEscapesEndWithoutCRLF(self) -> None:

        in_ = io.StringIO("x,y,x")
        out = io.StringIO()
        format_ = (
            CSVFormat.RFC4180.withEscape0("?")
            .withDelimiter(",")
            .withQuote1(None)
            .withRecordSeparator1(os.linesep)
        )
        format_.print2(in_, out, True)
        self.assertEqual("x?,y?,x", out.getvalue())

    @pytest.mark.test
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

    @pytest.mark.test
    def testPrintRecordEmpty(self) -> None:

        out = io.StringIO()
        format = CSVFormat.RFC4180
        format.printRecord(out, [])
        self.assertEqual(format.getRecordSeparator(), out.getvalue())

    @pytest.mark.test
    def testPrintRecord(self) -> None:

        out = io.StringIO()
        format = CSVFormat.RFC4180
        format.printRecord(out, "a", "b", "c")
        self.assertEqual("a,b,c" + format.getRecordSeparator(), out.getvalue())

    @pytest.mark.test
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

    @pytest.mark.test
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

    @pytest.mark.test
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

    @pytest.mark.test
    def testGetAllowDuplicateHeaderNames(self) -> None:

        builder = CSVFormat.DEFAULT.builder()
        self.assertTrue(builder.build().getAllowDuplicateHeaderNames())

        builder.setDuplicateHeaderMode(DuplicateHeaderMode.ALLOW_ALL)
        self.assertTrue(builder.build().getAllowDuplicateHeaderNames())

        builder.setDuplicateHeaderMode(DuplicateHeaderMode.ALLOW_EMPTY)
        self.assertFalse(builder.build().getAllowDuplicateHeaderNames())

        builder.setDuplicateHeaderMode(DuplicateHeaderMode.DISALLOW)
        self.assertFalse(builder.build().getAllowDuplicateHeaderNames())

    @pytest.mark.test
    def testFormatThrowsNullPointerException(self) -> None:

        pass  # LLM could not translate this method

    @pytest.mark.test
    def testFormat(self) -> None:

        format = CSVFormat.DEFAULT

        self.assertEqual("", format.format([]))
        self.assertEqual("a,b,c", format.format(["a", "b", "c"]))
        self.assertEqual('"x,y",z', format.format(["x,y", "z"]))

    @pytest.mark.test
    def testEscapeSameAsCommentStartThrowsExceptionForWrapperType_Deprecated(
        self,
    ) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withEscape1(Character.valueOf("!")).withCommentMarker1(
                Character.valueOf("!")
            )

    @pytest.mark.test
    def testEscapeSameAsCommentStartThrowsExceptionForWrapperType(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.builder().setEscape1(
                Character.valueOf("!")
            ).setCommentMarker1(Character.valueOf("!")).build()

    @pytest.mark.test
    def testEscapeSameAsCommentStartThrowsException_Deprecated(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withEscape0("0").withCommentMarker0("0")

    @pytest.mark.test
    def testEscapeSameAsCommentStartThrowsException(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.builder().setEscape0("0").setCommentMarker0("0").build()

    @pytest.mark.test
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

    @pytest.mark.test
    def testEqualsSkipHeaderRecord_Deprecated(self) -> None:

        right = (
            CSVFormat.newFormat("'")
            .withRecordSeparator0("\r")
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

    @pytest.mark.test
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

    @pytest.mark.test
    def testEqualsRecordSeparator(self) -> None:

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
            .build()
        )

        left = right.builder().setRecordSeparator0(LF).build()

        self.__assertNotEquals0(right, left)

    @pytest.mark.test
    def testEqualsQuotePolicy_Deprecated(self) -> None:

        right = CSVFormat.newFormat("'").withQuote0('"').withQuoteMode(QuoteMode.ALL)
        left = right.withQuoteMode(QuoteMode.MINIMAL)

        self.__assertNotEquals0(right, left)

    @pytest.mark.test
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

    @pytest.mark.test
    def testEqualsQuoteChar_Deprecated(self) -> None:

        right = CSVFormat.newFormat("'").withQuote0('"')
        left = right.withQuote0('"')

        self.__assertNotEquals0(right, left)

    @pytest.mark.test
    def testEqualsQuoteChar(self) -> None:

        right = CSVFormat.newFormat("'").builder().setQuote0('"').build()
        left = right.builder().setQuote0('"').build()

        self.__assertNotEquals0(right, left)

    @pytest.mark.test
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

    @pytest.mark.test
    def testEqualsNullString_Deprecated(self) -> None:

        right = (
            CSVFormat.newFormat("'")
            .withRecordSeparator0("\r")
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

    @pytest.mark.test
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

    @pytest.mark.test
    def testEqualsNoQuotes_Deprecated(self) -> None:

        left = CSVFormat.newFormat(",").withQuote1(None)
        right = left.withQuote1(None)

        self.assertEqual(left, right)

    @pytest.mark.test
    def testEqualsNoQuotes(self) -> None:

        left = CSVFormat.newFormat(",").builder().setQuote1(None).build()
        right = left.builder().setQuote1(None).build()

        self.assertEqual(left, right)

    @pytest.mark.test
    def testEqualsLeftNoQuoteRightQuote_Deprecated(self) -> None:

        left = CSVFormat.newFormat(",").withQuote1(None)
        right = left.withQuote0("#")

        self.__assertNotEquals0(left, right)

    @pytest.mark.test
    def testEqualsLeftNoQuoteRightQuote(self) -> None:

        left = CSVFormat.newFormat(",").builder().setQuote1(None).build()
        right = left.builder().setQuote0("#").build()

        self.__assertNotEquals0(left, right)

    @pytest.mark.test
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

    @pytest.mark.test
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

    @pytest.mark.test
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

    @pytest.mark.test
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

    @pytest.mark.test
    def testEqualsHash(self) -> None:

        methods = CSVFormat.__dict__.values()
        for method in methods:
            if callable(method):
                name = method.__name__
                if name.startswith("with"):
                    for cls in method.__annotations__.values():
                        type = cls.__name__
                        if type == "bool":
                            defTrue = method(CSVFormat.DEFAULT, True)
                            defFalse = method(CSVFormat.DEFAULT, False)
                            self.__assertNotEquals1(name, type, defTrue, defFalse)
                        elif type == "str":
                            a = method(CSVFormat.DEFAULT, "a")
                            b = method(CSVFormat.DEFAULT, "b")
                            self.__assertNotEquals1(name, type, a, b)
                        elif type == "Character":
                            a = method(CSVFormat.DEFAULT, None)
                            b = method(CSVFormat.DEFAULT, Character("d"))
                            self.__assertNotEquals1(name, type, a, b)
                        elif type == "String":
                            a = method(CSVFormat.DEFAULT, None)
                            b = method(CSVFormat.DEFAULT, "e")
                            self.__assertNotEquals1(name, type, a, b)
                        elif type == "StringArray":
                            a = method(CSVFormat.DEFAULT, [None, None])
                            b = method(CSVFormat.DEFAULT, ["f", "g"])
                            self.__assertNotEquals1(name, type, a, b)
                        elif type == "QuoteMode":
                            a = method(CSVFormat.DEFAULT, QuoteMode.MINIMAL)
                            b = method(CSVFormat.DEFAULT, QuoteMode.ALL)
                            self.__assertNotEquals1(name, type, a, b)
                        elif type == "DuplicateHeaderMode":
                            a = method(CSVFormat.DEFAULT, DuplicateHeaderMode.ALLOW_ALL)
                            b = method(CSVFormat.DEFAULT, DuplicateHeaderMode.DISALLOW)
                            self.__assertNotEquals1(name, type, a, b)
                        elif type == "ObjectArray":
                            a = method(CSVFormat.DEFAULT, [None, None])
                            b = method(CSVFormat.DEFAULT, [Object(), Object()])
                            self.__assertNotEquals1(name, type, a, b)
                        elif name == "withHeader":  # covered above by StringArray
                            pass
                        else:
                            self.fail("Unhandled method: " + name + "(" + type + ")")

    @pytest.mark.test
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

    @pytest.mark.test
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

    @pytest.mark.test
    def testEqualsDelimiter(self) -> None:

        right = CSVFormat.newFormat("?")
        left = CSVFormat.newFormat("?")

        self.__assertNotEquals0(right, left)

    @pytest.mark.test
    def testEqualsCommentStart_Deprecated(self) -> None:

        right = (
            CSVFormat.newFormat("'")
            .withQuote0('"')
            .withCommentMarker0("#")
            .withQuoteMode(QuoteMode.ALL)
        )
        left = right.withCommentMarker0("0")

        self.__assertNotEquals0(right, left)

    @pytest.mark.test
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

    @pytest.mark.test
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

    @pytest.mark.test
    def testDelimiterSameAsRecordSeparatorThrowsException(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.newFormat(CR)

    @pytest.mark.test
    def testDelimiterSameAsEscapeThrowsException1(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.builder().setDelimiter0("0").setEscape0("0").build()

    @pytest.mark.test
    def testDelimiterSameAsEscapeThrowsException_Deprecated(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withDelimiter("0").withEscape("0")

    @pytest.mark.test
    def testDelimiterSameAsCommentStartThrowsException1(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.builder().setDelimiter0("0").setCommentMarker0(
                "0"
            ).build()

    @pytest.mark.test
    def testDelimiterSameAsCommentStartThrowsException_Deprecated(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withDelimiter("0").withCommentMarker("0")

    @pytest.mark.test
    def testDelimiterEmptyStringThrowsException1(self) -> None:

        with pytest.raises(ValueError):
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
        if hash(left) == hash(right):
            self.fail("Hash code should not be equal for " + name + "(" + type + ")")

    @staticmethod
    def __copy(format: CSVFormat) -> CSVFormat:
        return format.builder().setDelimiter0(format.getDelimiter()).build()

    @staticmethod
    def __assertNotEquals0(right: typing.Any, left: typing.Any) -> None:
        assert right != left
        assert left != right
