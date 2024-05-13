# Imports Begin
from src.main.org.apache.commons.csv.QuoteMode import *
from src.main.org.apache.commons.csv.DuplicateHeaderMode import *
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.CSVFormat import *
import unittest
import typing
from typing import *
import io
# Imports End

class EmptyEnum(unittest.TestCase):

    pass

class Header(unittest.TestCase):

    # Class Fields Begin
    Name: Header = None
    Email: Header = None
    Phone: Header = None
    # Class Fields End

    # Class Methods Begin
    # Class Methods End


class new Executable(...) { ... }(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def execute(self) -> None:

            self.assertTrue(CSVFormat.DEFAULT.builder().setDelimiter1("").build() == CSVFormat.DEFAULT.builder().setDelimiter1("").build(), "CSVFormat.DEFAULT.builder().setDelimiter1(\"\").build() should be equal to CSVFormat.DEFAULT.builder().setDelimiter1(\"\").build()")

    def execute(self) -> None:

            self.assertTrue(CSVFormat.DEFAULT.withDelimiter('!').withCommentMarker0('!') == CSVFormat.DEFAULT.withDelimiter('!').withCommentMarker0('!'))

    def execute(self) -> None:


        pass # LLM could not translate method body

    def execute(self) -> None:

            self.assertTrue(CSVFormat.DEFAULT.withDelimiter('!').withEscape0('!') is not None)

    def execute(self) -> None:

            self.assertTrue(CSVFormat.DEFAULT.builder().setDelimiter0('!').setEscape0('!').build() == CSVFormat.DEFAULT.builder().setDelimiter0('!').setEscape0('!').build(), "CSVFormat.DEFAULT.builder().setDelimiter0('!').setEscape0('!').build() should be equal to CSVFormat.DEFAULT.builder().setDelimiter0('!').setEscape0('!').build()")

    def execute(self) -> None:

            self.assertRaises(IllegalArgumentException, CSVFormat.newFormat, CR)

    def execute(self) -> None:

            self.assertTrue(CSVFormat.DEFAULT.builder().setEscape0('!').setCommentMarker0('!').build() == CSVFormat.DEFAULT.builder().setEscape0('!').setCommentMarker0('!').build())

    def execute(self) -> None:

            self.assertTrue(CSVFormat.DEFAULT.withEscape0('!').withCommentMarker0('!') == CSVFormat.DEFAULT.withEscape0('!').withCommentMarker0('!'))

    def execute(self) -> None:

            CSVFormat.DEFAULT.builder().setEscape1('!').setCommentMarker1('!').build()

    def execute(self) -> None:

            self.assertTrue(CSVFormat.DEFAULT.withEscape1(Character.valueOf('!')).withCommentMarker1(Character.valueOf('!')), msg="CSVFormat.DEFAULT.withEscape1(Character.valueOf('!')).withCommentMarker1(Character.valueOf('!'))")

    def execute(self) -> None:

            self.assertRaises(NullPointerException, lambda: self.csvFormat.format(None))

    def execute(self) -> None:

            self.assertTrue(CSVFormat.DEFAULT.builder().setQuote0('!').setCommentMarker0('!').build() == CSVFormat.DEFAULT.builder().setQuote0('!').setCommentMarker0('!').build())

    def execute(self) -> None:

            self.assertTrue(CSVFormat.DEFAULT.withQuote0('!').withCommentMarker0('!') == CSVFormat.DEFAULT.withQuote0('!').withCommentMarker0('!'))

    def execute(self) -> None:


        pass # LLM could not translate method body

    def execute(self) -> None:

            CSVFormat.DEFAULT.withQuote1(Character.valueOf('!')).withCommentMarker0('!')

    def execute(self) -> None:

            self.assertTrue(CSVFormat.DEFAULT.builder().setQuote0('!').setDelimiter0('!').build() == CSVFormat.DEFAULT.builder().setQuote0('!').setDelimiter0('!').build())

    def execute(self) -> None:

            self.assertTrue(CSVFormat.DEFAULT.withQuote0('!').withDelimiter('!') == CSVFormat.DEFAULT.withQuote0('!').withDelimiter('!'))

    def execute(self) -> None:

            CSVFormat.newFormat('!').builder().setQuoteMode(QuoteMode.NONE).build()

    def execute(self) -> None:

            self.assertTrue(CSVFormat.newFormat('!').withQuoteMode(QuoteMode.NONE))

    def execute(self) -> None:

            self.assertTrue(isinstance(CSVFormat.DEFAULT.withCommentMarker0(CR), CSVFormat),
                            "CSVFormat.DEFAULT.withCommentMarker0(CR) should be an instance of CSVFormat")

    def execute(self) -> None:

            self.assertRaises(IllegalArgumentException, CSVFormat.DEFAULT.withDelimiter, LF)

    def execute(self) -> None:

            self.assertRaises(IllegalArgumentException, CSVFormat.DEFAULT.withEscape0, CR)

    def execute(self) -> None:

            try:
                CSVFormat.DEFAULT.withQuote0(LF)
            except IllegalArgumentException:
                pass

    # Class Methods End


class CSVFormatTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testWithSystemRecordSeparator(self) -> None:


        pass # LLM could not translate method body

    def testWithRecordSeparatorLF(self) -> None:

            formatWithRecordSeparator = CSVFormat.DEFAULT.withRecordSeparator0(LF)
            self.assertEqual(String.valueOf(LF), formatWithRecordSeparator.getRecordSeparator())

    def testWithRecordSeparatorCRLF(self) -> None:

            formatWithRecordSeparator = CSVFormat.DEFAULT.withRecordSeparator1(CRLF)
            self.assertEqual(CRLF, formatWithRecordSeparator.getRecordSeparator())

    def testWithRecordSeparatorCR(self) -> None:

            formatWithRecordSeparator = CSVFormat.DEFAULT.withRecordSeparator0(CR)
            self.assertEqual(String.valueOf(CR), formatWithRecordSeparator.getRecordSeparator())

    def testWithQuotePolicy(self) -> None:

            formatWithQuotePolicy = CSVFormat.DEFAULT.withQuoteMode(QuoteMode.ALL)
            self.assertEqual(QuoteMode.ALL, formatWithQuotePolicy.getQuoteMode())

    def testWithQuoteLFThrowsException(self) -> None:

            self.assertRaises(IllegalArgumentException, lambda: CSVFormat.DEFAULT.withQuote0(LF))

    def testWithQuoteChar(self) -> None:

            formatWithQuoteChar = CSVFormat.DEFAULT.withQuote0('"')
            self.assertEqual(Character.valueOf('"'), formatWithQuoteChar.getQuoteCharacter())

    def testWithNullString(self) -> None:

            formatWithNullString = CSVFormat.DEFAULT.withNullString("null")
            self.assertEqual("null", formatWithNullString.getNullString())

    def testWithIgnoreSurround(self) -> None:


        pass # LLM could not translate method body

    def testWithIgnoreEmptyLines(self) -> None:


        pass # LLM could not translate method body

    def testWithHeaderComments(self) -> None:


        pass # LLM could not translate method body

    def testWithEscapeCRThrowsExceptions(self) -> None:

            self.assertRaises(IllegalArgumentException, lambda: CSVFormat.DEFAULT.withEscape0(CR))

    def testWithEscape(self) -> None:

            formatWithEscape = CSVFormat.DEFAULT.withEscape0('&')
            self.assertEqual(Character.valueOf('&'), formatWithEscape.getEscapeCharacter())

    def testWithEmptyDuplicates(self) -> None:

            formatWithEmptyDuplicates = CSVFormat.DEFAULT.builder().setDuplicateHeaderMode(DuplicateHeaderMode.ALLOW_EMPTY).build()
            self.assertEqual(DuplicateHeaderMode.ALLOW_EMPTY, formatWithEmptyDuplicates.getDuplicateHeaderMode())
            self.assertFalse(formatWithEmptyDuplicates.getAllowDuplicateHeaderNames())

    def testWithDelimiterLFThrowsException(self) -> None:

            with self.assertRaises(IllegalArgumentException):
                CSVFormat.DEFAULT.withDelimiter(LF)

    def testWithDelimiter(self) -> None:

            formatWithDelimiter = CSVFormat.DEFAULT.withDelimiter('!')
            self.assertEqual('!', formatWithDelimiter.getDelimiter())

    def testWithCommentStartCRThrowsException(self) -> None:

            self.assertRaises(IllegalArgumentException, lambda: CSVFormat.DEFAULT.withCommentMarker0(CR))

    def testWithCommentStart(self) -> None:

            formatWithCommentStart = CSVFormat.DEFAULT.withCommentMarker0('#')
            self.assertEqual(Character.valueOf('#'), formatWithCommentStart.getCommentMarker())

    def testTrim(self) -> None:

            format_with_trim = CSVFormat.DEFAULT.with_delimiter(',').with_trim0().with_quote1(None).with_record_separator1(CRLF)
            in_str = "a,b,c"
            out = StringBuilder()
            format_with_trim.print2(in_str, out, True)
            self.assertEqual("a,b,c", out.get_string())
            in_str = StringBuilder(" x,y,z")
            out.set_length(0)
            format_with_trim.print2(in_str, out, True)
            self.assertEqual("x,y,z", out.get_string())
            in_str = StringBuilder("")
            out.set_length(0)
            format_with_trim.print2(in_str, out, True)
            self.assertEqual("", out.get_string())
            in_str = StringBuilder("header\r\n")
            out.set_length(0)
            format_with_trim.print2(in_str, out, True)
            self.assertEqual("header", out.get_string())

    def testToStringAndWithCommentMarkerTakingCharacter(self) -> None:


        pass # LLM could not translate method body

    def testToString(self) -> None:

            string = CSVFormat.INFORMIX_UNLOAD.toString()
            self.assertEqual(
                "Delimiter=<|> Escape=<\\> QuoteChar=<\"> RecordSeparator=<\n"
                + "> EmptyLines:ignored SkipHeaderRecord:false",
                string)

    def testSerialization(self) -> None:


        pass # LLM could not translate method body

    def testRFC4180(self) -> None:

            self.assertIsNone(RFC4180.getCommentMarker())
            self.assertEqual(RFC4180.getDelimiter(), ',')
            self.assertIsNone(RFC4180.getEscapeCharacter())
            self.assertFalse(RFC4180.getIgnoreEmptyLines())
            self.assertEqual(RFC4180.getQuoteCharacter(), Character.valueOf('"'))
            self.assertIsNone(RFC4180.getQuoteMode())
            self.assertEqual(RFC4180.getRecordSeparator(), "\r\n")

    def testQuotePolicyNoneWithoutEscapeThrowsException_Deprecated(self) -> None:

            self.assertRaises(IllegalArgumentException, lambda: CSVFormat.newFormat('!').withQuoteMode(QuoteMode.NONE))

    def testQuotePolicyNoneWithoutEscapeThrowsException(self) -> None:

            self.assertRaises(IllegalArgumentException, lambda: CSVFormat.newFormat('!').builder().setQuoteMode(QuoteMode.NONE).build())

    def testQuoteCharSameAsDelimiterThrowsException_Deprecated(self) -> None:

            self.assertRaises(IllegalArgumentException, lambda: CSVFormat.DEFAULT.withQuote0('!').withDelimiter('!'))

    def testQuoteCharSameAsDelimiterThrowsException(self) -> None:

            self.assertRaises(IllegalArgumentException, lambda: CSVFormat.DEFAULT.builder().setQuote0('!').setDelimiter0('!').build())

    def testQuoteCharSameAsCommentStartThrowsExceptionForWrapperType_Deprecated(self) -> None:

            self.assertRaises(IllegalArgumentException, lambda: CSVFormat.DEFAULT.withQuote1(Character.valueOf('!')).withCommentMarker0('!'))

    def testQuoteCharSameAsCommentStartThrowsExceptionForWrapperType(self) -> None:

            self.assertRaises(
                IllegalArgumentException,
                lambda: CSVFormat.DEFAULT
                    .builder()
                    .setQuote1(Character.valueOf('!'))
                    .setCommentMarker0('!')
                    .build()
            )

    def testQuoteCharSameAsCommentStartThrowsException_Deprecated(self) -> None:

            self.assertRaises(IllegalArgumentException, lambda: CSVFormat.DEFAULT.withQuote0('!').withCommentMarker0('!'))

    def testQuoteCharSameAsCommentStartThrowsException(self) -> None:

            with self.assertRaises(IllegalArgumentException):
                CSVFormat.DEFAULT.builder().setQuote0('!').setCommentMarker0('!').build()

    def testPrintWithQuotes(self) -> None:

            in_ = io.StringIO("\"a,b,c\r\nx,y,z")
            out = io.StringIO()
            format = CSVFormat.RFC4180.withDelimiter(',').withQuote0('"').withEscape0('?').withQuoteMode(QuoteMode.NON_NUMERIC)
            format.print2(in_, out, True)
            self.assertEqual("\"\"\"a,b,c\r\nx,y,z\"", out.getvalue())

    def testPrintWithQuoteModeIsNONE(self) -> None:

            in_ = StringIO("a,b,c")
            out = StringBuilder()
            format = CSVFormat.RFC4180.withDelimiter(",").withQuote0('"').withEscape0("?").withQuoteMode(QuoteMode.NONE)
            format.print2(in_, out, True)
            self.assertEqual("a?,b?,c", out.getvalue())

    def testPrintWithoutQuotes(self) -> None:

            in_ = io.StringIO("")
            out = io.StringIO()
            format = CSVFormat.RFC4180.withDelimiter(",").withQuote0('"').withEscape0("?").withQuoteMode(QuoteMode.NON_NUMERIC)
            format.print2(in_, out, True)
            self.assertEqual("\"\"", out.getvalue())

    def testPrintWithEscapesEndWithoutCRLF(self) -> None:

            in_ = StringIO("x,y,x")
            out = StringBuilder()
            format = CSVFormat.RFC4180.withEscape0('?').withDelimiter(',').withQuote1(None).withRecordSeparator1(CRLF)
            format.print2(in_, out, True)
            self.assertEqual("x?,y?,x", out.getvalue())

    def testPrintWithEscapesEndWithCRLF(self) -> None:

            in_ = io.StringIO("x,y,x\r\na,?b,c\r\n")
            out = io.StringIO()
            format = CSVFormat.RFC4180.withEscape0('?').withDelimiter(',').withQuote1(None).withRecordSeparator1(CRLF)
            format.print2(in_, out, True)
            self.assertEqual("x?,y?,x?r?na?,??b?,c?r?n", out.getvalue())

    def testPrintRecordEmpty(self) -> None:

            out = StringBuilder()
            format = CSVFormat.RFC4180
            format.printRecord(out)
            self.assertEqual(format.getRecordSeparator(), out.toString())

    def testPrintRecord(self) -> None:

            out = StringBuilder()
            format = CSVFormat.RFC4180
            format.printRecord(out, ["a", "b", "c"])
            self.assertEqual("a,b,c" + format.getRecordSeparator(), out.toString())

    def testNewFormat(self) -> None:


        pass # LLM could not translate method body

    def testHashCodeAndWithIgnoreHeaderCase(self) -> None:


        pass # LLM could not translate method body

    def testGetDuplicateHeaderMode(self) -> None:


        pass # LLM could not translate method body

    def testGetAllowDuplicateHeaderNames(self) -> None:


        pass # LLM could not translate method body

    def testFormatThrowsNullPointerException(self) -> None:

            csv_format = CSVFormat.MYSQL
            with self.assertRaises(NullPointerException) as context:
                csv_format.format(None)
            self.assertEqual(Objects.__name__, context.exception.stack_trace[0].class_name)

    def testFormat(self) -> None:

            format = CSVFormat.DEFAULT
            self.assertEqual("", format.format())
            self.assertEqual("a,b,c", format.format("a", "b", "c"))
            self.assertEqual("\"x,y\",z", format.format("x,y", "z"))

    def testEscapeSameAsCommentStartThrowsExceptionForWrapperType_Deprecated(self) -> None:

            self.assertRaises(
                IllegalArgumentException,
                lambda: CSVFormat.DEFAULT.withEscape1(Character.valueOf('!')).withCommentMarker1(Character.valueOf('!'))
            )

    def testEscapeSameAsCommentStartThrowsExceptionForWrapperType(self) -> None:

            with self.assertRaises(IllegalArgumentException):
                CSVFormat.DEFAULT.builder().setEscape1(Character.valueOf('!')).setCommentMarker1(Character.valueOf('!')).build()

    def testEscapeSameAsCommentStartThrowsException_Deprecated(self) -> None:

            self.assertRaises(IllegalArgumentException, lambda: CSVFormat.DEFAULT.withEscape0('!').withCommentMarker0('!'))

    def testEscapeSameAsCommentStartThrowsException(self) -> None:

            self.assertRaises(IllegalArgumentException, lambda: CSVFormat.DEFAULT.builder().setEscape0('!').setCommentMarker0('!').build())

    def testEqualsWithNull(self) -> None:


        pass # LLM could not translate method body

    def testEqualsSkipHeaderRecord_Deprecated(self) -> None:

            right = CSVFormat.newFormat('\'') \
                .withRecordSeparator0(CR) \
                .withCommentMarker0('#') \
                .withEscape0('+') \
                .withIgnoreEmptyLines0() \
                .withIgnoreSurroundingSpaces0() \
                .withQuote0('"') \
                .withQuoteMode(QuoteMode.ALL) \
                .withNullString("null") \
                .withSkipHeaderRecord0()
            left = right.withSkipHeaderRecord1(False)
            self.assertNotEquals0(right, left)

    def testEqualsRecordSeparator_Deprecated(self) -> None:


        pass # LLM could not translate method body

    def testEqualsRecordSeparator(self) -> None:

            right = CSVFormat.newFormat('\'')\
                .builder()\
                .setRecordSeparator0(CR)\
                .setCommentMarker0('#')\
                .setEscape0('+')\
                .setIgnoreEmptyLines(True)\
                .setIgnoreSurroundingSpaces(True)\
                .setQuote0('"')\
                .setQuoteMode(QuoteMode.ALL)\
                .build()
            left = right.builder().setRecordSeparator0(LF).build()
            self.assertNotEquals0(right, left)

    def testEqualsQuotePolicy_Deprecated(self) -> None:

            right = CSVFormat.newFormat('\'').withQuote0('"').withQuoteMode(QuoteMode.ALL)
            left = right.withQuoteMode(QuoteMode.MINIMAL)
            self.assertNotEquals0(right, left)

    def testEqualsQuotePolicy(self) -> None:

            right = CSVFormat.newFormat('\'').builder().setQuote0('"').setQuoteMode(QuoteMode.ALL).build()
            left = right.builder().setQuoteMode(QuoteMode.MINIMAL).build()
            self.assertNotEquals(right, left)

    def testEqualsQuoteChar_Deprecated(self) -> None:

            right = CSVFormat.newFormat('\'').withQuote0('"')
            left = right.withQuote0('!')
            self.assertNotEquals0(right, left)

    def testEqualsQuoteChar(self) -> None:

            right = CSVFormat.newFormat('\'').builder().setQuote0('"').build()
            left = right.builder().setQuote0('!').build()
            self.assertNotEquals(right, left)

    def testEqualsOne(self) -> None:


        pass # LLM could not translate method body

    def testEqualsNullString_Deprecated(self) -> None:


        pass # LLM could not translate method body

    def testEqualsNullString(self) -> None:


        pass # LLM could not translate method body

    def testEqualsNoQuotes_Deprecated(self) -> None:

            left = CSVFormat.newFormat(',').withQuote1(None)
            right = left.withQuote1(None)
            self.assertEqual(left, right)

    def testEqualsNoQuotes(self) -> None:

            left = CSVFormat.newFormat(',').builder().setQuote1(None).build()
            right = left.builder().setQuote1(None).build()
            self.assertEqual(left, right)

    def testEqualsLeftNoQuoteRightQuote_Deprecated(self) -> None:

            left = CSVFormat.newFormat(',').withQuote1(None)
            right = left.withQuote0('#')
            self.assertNotEquals0(left, right)

    def testEqualsLeftNoQuoteRightQuote(self) -> None:

            left = CSVFormat.newFormat(',').builder().setQuote1(None).build()
            right = left.builder().setQuote0('#').build()
            self.assertNotEquals(left, right)

    def testEqualsIgnoreSurroundingSpaces_Deprecated(self) -> None:

            right = CSVFormat.newFormat('\'')\
                            .withCommentMarker0('#')\
                            .withEscape0('+')\
                            .withIgnoreSurroundingSpaces0()\
                            .withQuote0('"')\
                            .withQuoteMode(QuoteMode.ALL)
            left = right.withIgnoreSurroundingSpaces1(False)
            self.assertNotEquals0(right, left)

    def testEqualsIgnoreSurroundingSpaces(self) -> None:

            right = CSVFormat.newFormat('\'').builder().setCommentMarker0('#').setEscape0('+').setIgnoreSurroundingSpaces(True).setQuote0('"').setQuoteMode(QuoteMode.ALL).build()
            left = right.builder().setIgnoreSurroundingSpaces(False).build()
            self.assertNotEquals0(right, left)

    def testEqualsIgnoreEmptyLines_Deprecated(self) -> None:

            right = CSVFormat.newFormat('\'') \
                .withCommentMarker0('#') \
                .withEscape0('+') \
                .withIgnoreEmptyLines0() \
                .withIgnoreSurroundingSpaces0() \
                .withQuote0('"') \
                .withQuoteMode(QuoteMode.ALL)
            left = right.withIgnoreEmptyLines1(False)
            self.assertNotEquals0(right, left)

    def testEqualsIgnoreEmptyLines(self) -> None:

            right = CSVFormat.newFormat('\'').builder().setCommentMarker0('#').setEscape0('+').setIgnoreEmptyLines(True).setIgnoreSurroundingSpaces(True).setQuote0('"').setQuoteMode(QuoteMode.ALL).build()
            left = right.builder().setIgnoreEmptyLines(False).build()
            self.assertNotEquals0(right, left)

    def testEqualsHash(self) -> None:


        pass # LLM could not translate method body

    def testEqualsEscape_Deprecated(self) -> None:

            right = CSVFormat.newFormat('\'') \
                .withQuote0('"') \
                .withCommentMarker0('#') \
                .withEscape0('+') \
                .withQuoteMode(QuoteMode.ALL)
            left = right.withEscape0('!')
            self.assertNotEquals0(right, left)

    def testEqualsEscape(self) -> None:

            right = CSVFormat.newFormat('\'').builder().setQuote0('"').setCommentMarker0('#').setEscape0('+').setQuoteMode(QuoteMode.ALL).build()
            left = right.builder().setEscape0('!').build()
            self.assertNotEquals0(right, left)

    def testEqualsDelimiter(self) -> None:

            right = CSVFormat.newFormat('!')
            left = CSVFormat.newFormat('?')
            self.assertNotEquals0(right, left)

    def testEqualsCommentStart_Deprecated(self) -> None:

            right = CSVFormat.newFormat('\'')\
                            .withQuote0('"')\
                            .withCommentMarker0('#')\
                            .withQuoteMode(QuoteMode.ALL)
            left = right.withCommentMarker0('!')
            self.assertNotEquals0(right, left)

    def testEqualsCommentStart(self) -> None:

            right = CSVFormat.newFormat('\'')\
                            .builder()\
                            .setQuote0('"')\
                            .setCommentMarker0('#')\
                            .setQuoteMode(QuoteMode.ALL)\
                            .build()
            left = right.builder().setCommentMarker0('!').build()
            self.assertNotEquals(right, left)

    def testEquals(self) -> None:

            right = CSVFormat.DEFAULT
            left = self.__copy(right)
            self.assertNotEquals(None, right)
            self.assertNotEquals("A String Instance", right)
            self.assertEqual(right, right)
            self.assertEqual(right, left)
            self.assertEqual(left, right)
            self.assertEqual(right.hashCode(), right.hashCode())
            self.assertEqual(right.hashCode(), left.hashCode())

    def testDelimiterSameAsRecordSeparatorThrowsException(self) -> None:

            with self.assertRaises(IllegalArgumentException):
                CSVFormat.newFormat(CR)

    def testDelimiterSameAsEscapeThrowsException1(self) -> None:

            with self.assertRaises(IllegalArgumentException):
                CSVFormat.DEFAULT.builder().setDelimiter0('!').setEscape0('!').build()

    def testDelimiterSameAsEscapeThrowsException_Deprecated(self) -> None:

            self.assertRaises(IllegalArgumentException, lambda: CSVFormat.DEFAULT.withDelimiter('!').withEscape0('!'))

    def testDelimiterSameAsCommentStartThrowsException1(self) -> None:

            self.assertRaises(
                IllegalArgumentException,
                lambda: CSVFormat.DEFAULT
                    .builder()
                    .setDelimiter0('!')
                    .setCommentMarker0('!')
                    .build()
            )

    def testDelimiterSameAsCommentStartThrowsException_Deprecated(self) -> None:

            self.assertRaises(IllegalArgumentException, lambda: CSVFormat.DEFAULT.withDelimiter('!').withCommentMarker0('!'))

    def testDelimiterEmptyStringThrowsException1(self) -> None:

            with self.assertRaises(IllegalArgumentException):
                CSVFormat.DEFAULT.builder().setDelimiter1("").build()

    def testEqualsSkipHeaderRecord(self) -> None:

            right = CSVFormat.newFormat('\'') \
                .builder() \
                .setRecordSeparator0(CR) \
                .setCommentMarker0('#') \
                .setEscape0('+') \
                .setIgnoreEmptyLines(True) \
                .setIgnoreSurroundingSpaces(True) \
                .setQuote0('"') \
                .setQuoteMode(QuoteMode.ALL) \
                .setNullString("null") \
                .setSkipHeaderRecord(True) \
                .build()
            left = right.builder().setSkipHeaderRecord(False).build()
            self.assertNotEquals0(right, left)

    def __assertNotEquals1(self, name: str, type: str, left: typing.Any, right: typing.Any) -> None:

            if left == right or right == left:
                self.fail("Objects must not compare equal for " + name + "(" + type + ")")
            if left.__hash__() == right.__hash__():
                self.fail("Hash code should not be equal for " + name + "(" + type + ")")

    @staticmethod

    def __copy(format: CSVFormat) -> CSVFormat:


        pass # LLM could not translate method body

    @staticmethod

    def __assertNotEquals0(right: typing.Any, left: typing.Any) -> None:


        pass # LLM could not translate method body

    # Class Methods End


