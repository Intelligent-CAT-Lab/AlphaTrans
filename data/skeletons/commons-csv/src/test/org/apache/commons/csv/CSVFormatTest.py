from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.csv.QuoteMode import *
from src.main.org.apache.commons.csv.DuplicateHeaderMode import *
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.CSVFormat import *
import enum
import unittest
import typing
from typing import *
import io

# Imports End


class EmptyEnum:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    # Class Methods End

    pass


class Header:

    # Class Fields Begin
    Name: Header = None
    Email: Header = None
    Phone: Header = None
    # Class Fields End

    # Class Methods Begin
    # Class Methods End


class CSVFormatTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testWithSystemRecordSeparator(self) -> None:
        pass

    def testWithRecordSeparatorLF(self) -> None:
        pass

    def testWithRecordSeparatorCRLF(self) -> None:
        pass

    def testWithRecordSeparatorCR(self) -> None:
        pass

    def testWithQuotePolicy(self) -> None:
        pass

    def testWithQuoteLFThrowsException(self) -> None:
        pass

    def testWithQuoteChar(self) -> None:
        pass

    def testWithNullString(self) -> None:
        pass

    def testWithIgnoreSurround(self) -> None:
        pass

    def testWithIgnoreEmptyLines(self) -> None:
        pass

    def testWithHeaderComments(self) -> None:
        pass

    def testWithEscapeCRThrowsExceptions(self) -> None:
        pass

    def testWithEscape(self) -> None:
        pass

    def testWithEmptyDuplicates(self) -> None:
        pass

    def testWithDelimiterLFThrowsException(self) -> None:
        pass

    def testWithDelimiter(self) -> None:
        pass

    def testWithCommentStartCRThrowsException(self) -> None:
        pass

    def testWithCommentStart(self) -> None:
        pass

    def testTrim(self) -> None:
        pass

    def testToStringAndWithCommentMarkerTakingCharacter(self) -> None:
        pass

    def testToString(self) -> None:
        pass

    def testSerialization(self) -> None:
        pass

    def testRFC4180(self) -> None:
        pass

    def testQuotePolicyNoneWithoutEscapeThrowsException_Deprecated(self) -> None:
        pass

    def testQuotePolicyNoneWithoutEscapeThrowsException(self) -> None:
        pass

    def testQuoteCharSameAsDelimiterThrowsException_Deprecated(self) -> None:
        pass

    def testQuoteCharSameAsDelimiterThrowsException(self) -> None:
        pass

    def testQuoteCharSameAsCommentStartThrowsExceptionForWrapperType_Deprecated(
        self,
    ) -> None:
        pass

    def testQuoteCharSameAsCommentStartThrowsExceptionForWrapperType(self) -> None:
        pass

    def testQuoteCharSameAsCommentStartThrowsException_Deprecated(self) -> None:
        pass

    def testQuoteCharSameAsCommentStartThrowsException(self) -> None:
        pass

    def testPrintWithQuotes(self) -> None:
        pass

    def testPrintWithQuoteModeIsNONE(self) -> None:
        pass

    def testPrintWithoutQuotes(self) -> None:
        pass

    def testPrintWithEscapesEndWithoutCRLF(self) -> None:
        pass

    def testPrintWithEscapesEndWithCRLF(self) -> None:
        pass

    def testPrintRecordEmpty(self) -> None:
        pass

    def testPrintRecord(self) -> None:
        pass

    def testNewFormat(self) -> None:
        pass

    def testHashCodeAndWithIgnoreHeaderCase(self) -> None:
        pass

    def testGetDuplicateHeaderMode(self) -> None:
        pass

    def testGetAllowDuplicateHeaderNames(self) -> None:
        pass

    def testFormatThrowsNullPointerException(self) -> None:
        pass

    def testFormat(self) -> None:
        pass

    def testEscapeSameAsCommentStartThrowsExceptionForWrapperType_Deprecated(
        self,
    ) -> None:
        pass

    def testEscapeSameAsCommentStartThrowsExceptionForWrapperType(self) -> None:
        pass

    def testEscapeSameAsCommentStartThrowsException_Deprecated(self) -> None:
        pass

    def testEscapeSameAsCommentStartThrowsException(self) -> None:
        pass

    def testEqualsWithNull(self) -> None:
        pass

    def testEqualsSkipHeaderRecord_Deprecated(self) -> None:
        pass

    def testEqualsRecordSeparator_Deprecated(self) -> None:
        pass

    def testEqualsRecordSeparator(self) -> None:
        pass

    def testEqualsQuotePolicy_Deprecated(self) -> None:
        pass

    def testEqualsQuotePolicy(self) -> None:
        pass

    def testEqualsQuoteChar_Deprecated(self) -> None:
        pass

    def testEqualsQuoteChar(self) -> None:
        pass

    def testEqualsOne(self) -> None:
        pass

    def testEqualsNullString_Deprecated(self) -> None:
        pass

    def testEqualsNullString(self) -> None:
        pass

    def testEqualsNoQuotes_Deprecated(self) -> None:
        pass

    def testEqualsNoQuotes(self) -> None:
        pass

    def testEqualsLeftNoQuoteRightQuote_Deprecated(self) -> None:
        pass

    def testEqualsLeftNoQuoteRightQuote(self) -> None:
        pass

    def testEqualsIgnoreSurroundingSpaces_Deprecated(self) -> None:
        pass

    def testEqualsIgnoreSurroundingSpaces(self) -> None:
        pass

    def testEqualsIgnoreEmptyLines_Deprecated(self) -> None:
        pass

    def testEqualsIgnoreEmptyLines(self) -> None:
        pass

    def testEqualsHash(self) -> None:
        pass

    def testEqualsEscape_Deprecated(self) -> None:
        pass

    def testEqualsEscape(self) -> None:
        pass

    def testEqualsDelimiter(self) -> None:
        pass

    def testEqualsCommentStart_Deprecated(self) -> None:
        pass

    def testEqualsCommentStart(self) -> None:
        pass

    def testEquals(self) -> None:
        pass

    def testDelimiterSameAsRecordSeparatorThrowsException(self) -> None:
        pass

    def testDelimiterSameAsEscapeThrowsException1(self) -> None:
        pass

    def testDelimiterSameAsEscapeThrowsException_Deprecated(self) -> None:
        pass

    def testDelimiterSameAsCommentStartThrowsException1(self) -> None:
        pass

    def testDelimiterSameAsCommentStartThrowsException_Deprecated(self) -> None:
        pass

    def testDelimiterEmptyStringThrowsException1(self) -> None:
        pass

    def testEqualsSkipHeaderRecord(self) -> None:
        pass

    def __assertNotEquals1(
        self, name: str, type_: str, left: typing.Any, right: typing.Any
    ) -> None:
        pass

    @staticmethod
    def __copy(format_: CSVFormat) -> CSVFormat:
        pass

    @staticmethod
    def __assertNotEquals0(right: typing.Any, left: typing.Any) -> None:
        pass

    # Class Methods End
