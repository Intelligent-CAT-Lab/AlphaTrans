import pytest

from enum import Enum
import io
import unittest
import pickle
import traceback
import os
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.DuplicateHeaderMode import *
from src.main.org.apache.commons.csv.QuoteMode import *

class CSVFormatTest(unittest.TestCase):

    
    class EmptyEnum(Enum):
        pass

    
    class Header(Enum):
        Name = 1
        Email = 2
        Phone = 3

    @staticmethod
    def __assertNotEquals0(right, left) -> None:
        unittest.TestCase().assertNotEqual(right, left)
        unittest.TestCase().assertNotEqual(left, right)

    
    @staticmethod
    def __copy(format) -> CSVFormat:
        return format.builder().setDelimiter0(format.getDelimiter()).build()

    
    def __assertNotEquals1(self, name, type, left, right) -> None:
        if left == right or right == left:
            self.fail(f"Objects must not compare equal for {name}({type})")
        try:
            if hash(left) == hash(right):
                self.fail(f"Hash code should not be equal for {name}({type})")
        except TypeError as te: # UnHashable by default - check if `hashCode()` presents
            try:
                if left.hashCode() == right.hashCode():
                    self.fail(f"Hash code should not be equal for {name}({type})")
            except AttributeError as ae:
                self.fail(f"Object not hashable: {left} or {right} - {str(ae)}")

    
    @pytest.mark.test
    def testDelimiterEmptyStringThrowsException1(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT.builder().setDelimiter1("").build()

    
    @pytest.mark.test
    def testDelimiterSameAsCommentStartThrowsException_Deprecated(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT.withDelimiter('!').withCommentMarker0('!')

    
    @pytest.mark.test
    def testDelimiterSameAsCommentStartThrowsException1(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT\
                .builder()\
                .setDelimiter0('!')\
                .setCommentMarker0('!')\
                .build()
    

    @pytest.mark.test
    def testDelimiterSameAsEscapeThrowsException_Deprecated(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT.withDelimiter('!').withEscape0('!')

    
    @pytest.mark.test
    def testDelimiterSameAsEscapeThrowsException1(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT.builder().setDelimiter0('!').setEscape0('!').build()

    
    @pytest.mark.test
    def testDelimiterSameAsRecordSeparatorThrowsException(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.newFormat(Constants.CR)

    
    @pytest.mark.test
    def testEquals(self) -> None:
        right = CSVFormat.DEFAULT
        left = CSVFormatTest.__copy(right)

        self.assertNotEqual(None, right)
        self.assertNotEqual("A String Instance", right)

        self.assertEqual(right, right)
        self.assertEqual(right, left)
        self.assertEqual(left, right)

        self.assertEqual(right.hashCode(), right.hashCode())
        self.assertEqual(right.hashCode(), left.hashCode())


    @pytest.mark.test
    def testEqualsCommentStart(self) -> None:
        right = CSVFormat.newFormat('\'')\
            .builder()\
            .setQuote0('"')\
            .setCommentMarker0('#')\
            .setQuoteMode(QuoteMode.ALL)\
            .build()
        left = right.builder().setCommentMarker0('!').build()

        CSVFormatTest.__assertNotEquals0(right, left)


    @pytest.mark.test
    def testEqualsCommentStart_Deprecated(self) -> None:
        right = CSVFormat.newFormat('\'')\
            .withQuote0('"')\
            .withCommentMarker0('#')\
            .withQuoteMode(QuoteMode.ALL)
        left = right.withCommentMarker0('!')

        CSVFormatTest.__assertNotEquals0(right, left)

    
    @pytest.mark.test
    def testEqualsDelimiter(self) -> None:
        right = CSVFormat.newFormat('!')
        left = CSVFormat.newFormat('?')

        CSVFormatTest.__assertNotEquals0(right, left)


    @pytest.mark.test
    def testEqualsEscape(self) -> None:
        right = CSVFormat.newFormat('\'')\
            .builder()\
            .setQuote0('"')\
            .setCommentMarker0('#')\
            .setEscape0('+')\
            .setQuoteMode(QuoteMode.ALL)\
            .build()
        left = right.builder().setEscape0('!').build()

        CSVFormatTest.__assertNotEquals0(right, left)


    @pytest.mark.test
    def testEqualsEscape_Deprecated(self) -> None:
        right = CSVFormat.newFormat('\'')\
            .withQuote0('"')\
            .withCommentMarker0('#')\
            .withEscape0('+')\
            .withQuoteMode(QuoteMode.ALL)
        left = right.withEscape0('!')

        CSVFormatTest.__assertNotEquals0(right, left)

    
    @pytest.mark.test
    def testEqualsHash(self) -> None:
        methods = [
            method for method in dir(CSVFormat)\
                if callable(getattr(CSVFormat, method))\
                and not method.startswith("_")
        ]
        for name in methods:
            method = getattr(CSVFormat, name)
            if name.startswith("with"):
                parameterTypes = []
                try:
                    for params in method.__annotations__:
                        if params != 'return':
                            parameterTypes.append(
                                eval(method.__annotations__.get(params))
                            )
                except Exception as e:
                    continue
                for cls in parameterTypes:
                    parameterTypeName = cls.__name__
                    if parameterTypeName == 'bool':
                        defTrue = method(CSVFormat.DEFAULT, True)
                        defFalse = method(CSVFormat.DEFAULT, False)
                        self.__assertNotEquals1(name, parameterTypeName, defTrue, defFalse)
                    elif parameterTypeName == 'str':
                        a = method(CSVFormat.DEFAULT, 'a')
                        b = method(CSVFormat.DEFAULT, 'b')
                        self.__assertNotEquals1(name, type, a, b)
                        try:
                            a = method(CSVFormat.DEFAULT, None)
                            b = method(CSVFormat.DEFAULT, 'd')
                            self.__assertNotEquals1(name, type, a, b)
                            a = method(CSVFormat.DEFAULT, None)
                            b = method(CSVFormat.DEFAULT, 'e')
                            self.__assertNotEquals1(name, type, a, b)
                        except ValueError as e:
                            self.assertEqual(str(e), "The delimiter cannot be empty")
                    elif parameterTypeName == 'List':
                        try:
                            a = method(CSVFormat.DEFAULT, [None, None])
                            b = method(CSVFormat.DEFAULT, ['f', 'g'])
                        except Exception as e:
                            a = method(CSVFormat.DEFAULT, [None, None])
                            b = method(CSVFormat.DEFAULT, [object(), object()])
                        self.__assertNotEquals1(name, type, a, b)
                        try:
                            a = method(CSVFormat.DEFAULT, [None, None])
                            b = method(CSVFormat.DEFAULT, [object(), object()])
                        except Exception as e:
                            a = method(CSVFormat.DEFAULT, [None, None])
                            b = method(CSVFormat.DEFAULT, ['f', 'g'])
                        self.__assertNotEquals1(name, type, a, b)
                    elif parameterTypeName == 'QuoteMode':
                        a = method(CSVFormat.DEFAULT, QuoteMode.MINIMAL)
                        b = method(CSVFormat.DEFAULT, QuoteMode.ALL)
                        self.__assertNotEquals1(name, type, a, b)
                    elif parameterTypeName == 'DuplicateHeaderMode':
                        a = method(CSVFormat.DEFAULT, DuplicateHeaderMode.ALLOW_ALL)
                        b = method(CSVFormat.DEFAULT, DuplicateHeaderMode.DISALLOW)
                        self.__assertNotEquals1(name, type, a, b)
                    elif name == 'withHeader':
                        continue  # covered above by List[str]
                    else:
                        self.fail(f"Unhandled method: {name}({type})")
        
    
    @pytest.mark.test
    def testEqualsIgnoreEmptyLines(self) -> None:
        right = CSVFormat.newFormat('\'')\
            .builder()\
            .setCommentMarker0('#')\
            .setEscape0('+')\
            .setIgnoreEmptyLines(True)\
            .setIgnoreSurroundingSpaces(True)\
            .setQuote0('"')\
            .setQuoteMode(QuoteMode.ALL)\
            .build()
        left = right.builder().setIgnoreEmptyLines(False).build()

        CSVFormatTest.__assertNotEquals0(right, left)

    
    @pytest.mark.test
    def testEqualsIgnoreEmptyLines_Deprecated(self) -> None:
        right = CSVFormat.newFormat('\'')\
            .withCommentMarker0('#')\
            .withEscape0('+')\
            .withIgnoreEmptyLines0()\
            .withIgnoreSurroundingSpaces0()\
            .withQuote0('"')\
            .withQuoteMode(QuoteMode.ALL)
        left = right.withIgnoreEmptyLines1(False)

        CSVFormatTest.__assertNotEquals0(right, left)

    
    @pytest.mark.test
    def testEqualsIgnoreSurroundingSpaces(self) -> None:
        right = CSVFormat.newFormat('\'')\
            .builder()\
            .setCommentMarker0('#')\
            .setEscape0('+')\
            .setIgnoreSurroundingSpaces(True)\
            .setQuote0('"')\
            .setQuoteMode(QuoteMode.ALL)\
            .build()
        left = right.builder().setIgnoreSurroundingSpaces(False).build()

        CSVFormatTest.__assertNotEquals0(right, left)

    
    @pytest.mark.test
    def testEqualsIgnoreSurroundingSpaces_Deprecated(self) -> None:
        right = CSVFormat.newFormat('\'')\
            .withCommentMarker0('#')\
            .withEscape0('+')\
            .withIgnoreSurroundingSpaces0()\
            .withQuote0('"')\
            .withQuoteMode(QuoteMode.ALL)
        left = right.withIgnoreSurroundingSpaces1(False)

        CSVFormatTest.__assertNotEquals0(right, left)
    

    @pytest.mark.test
    def testEqualsLeftNoQuoteRightQuote(self) -> None:
        left = CSVFormat.newFormat(',')\
            .builder()\
            .setQuote1(None)\
            .build()
        right = left.builder()\
            .setQuote0('#')\
            .build()

        CSVFormatTest.__assertNotEquals0(left, right)

    
    @pytest.mark.test
    def testEqualsLeftNoQuoteRightQuote_Deprecated(self) -> None:
        left = CSVFormat.newFormat(',')\
            .withQuote1(None)
        right = left.withQuote0('#')

        CSVFormatTest.__assertNotEquals0(left, right)

    
    @pytest.mark.test
    def testEqualsNoQuotes(self) -> None:
        left = CSVFormat.newFormat(',')\
            .builder()\
            .setQuote1(None)\
            .build()
        right = left.builder()\
            .setQuote1(None)\
            .build()

        self.assertEqual(left, right)

    
    @pytest.mark.test
    def testEqualsNoQuotes_Deprecated(self) -> None:
        left = CSVFormat.newFormat(',')\
            .withQuote1(None)
        right = left.withQuote1(None)

        self.assertEqual(left, right)


    @pytest.mark.test
    def testEqualsNullString(self) -> None:
        right = CSVFormat.newFormat('\'')\
            .builder()\
            .setRecordSeparator0(Constants.CR)\
            .setCommentMarker0('#')\
            .setEscape0('+')\
            .setIgnoreEmptyLines(True)\
            .setIgnoreSurroundingSpaces(True)\
            .setQuote0('"')\
            .setQuoteMode(QuoteMode.ALL)\
            .setNullString("null")\
            .build()
        left = right.builder()\
            .setNullString("---")\
            .build()

        CSVFormatTest.__assertNotEquals0(right, left)

    
    @pytest.mark.test
    def testEqualsNullString_Deprecated(self) -> None:
        right = CSVFormat.newFormat('\'')\
            .withRecordSeparator0(Constants.CR)\
            .withCommentMarker0('#')\
            .withEscape0('+')\
            .withIgnoreEmptyLines0()\
            .withIgnoreSurroundingSpaces0()\
            .withQuote0('"')\
            .withQuoteMode(QuoteMode.ALL)\
            .withNullString("null")
        left = right.withNullString("---")

        CSVFormatTest.__assertNotEquals0(right, left)


    @pytest.mark.test
    def testEqualsOne(self) -> None:
        csvFormatOne = CSVFormat.INFORMIX_UNLOAD
        csvFormatTwo = CSVFormat.MYSQL

        self.assertEqual('\\', csvFormatOne.getEscapeCharacter())
        self.assertIsNone(csvFormatOne.getQuoteMode())

        self.assertTrue(csvFormatOne.getIgnoreEmptyLines())
        self.assertFalse(csvFormatOne.getSkipHeaderRecord())

        self.assertFalse(csvFormatOne.getIgnoreHeaderCase())
        self.assertIsNone(csvFormatOne.getCommentMarker())

        self.assertFalse(csvFormatOne.isCommentMarkerSet())
        self.assertTrue(csvFormatOne.isQuoteCharacterSet())

        self.assertEqual('|', csvFormatOne.getDelimiter())
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

        self.assertEqual('\t', csvFormatTwo.getDelimiter())
        self.assertEqual("\n", csvFormatTwo.getRecordSeparator())

        self.assertFalse(csvFormatTwo.isQuoteCharacterSet())
        self.assertTrue(csvFormatTwo.isNullStringSet())

        self.assertEqual('\\', csvFormatTwo.getEscapeCharacter())
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

        self.assertEqual('\\', csvFormatOne.getEscapeCharacter())
        self.assertIsNone(csvFormatOne.getQuoteMode())

        self.assertTrue(csvFormatOne.getIgnoreEmptyLines())
        self.assertFalse(csvFormatOne.getSkipHeaderRecord())

        self.assertFalse(csvFormatOne.getIgnoreHeaderCase())
        self.assertIsNone(csvFormatOne.getCommentMarker())

        self.assertFalse(csvFormatOne.isCommentMarkerSet())
        self.assertTrue(csvFormatOne.isQuoteCharacterSet())

        self.assertEqual('|', csvFormatOne.getDelimiter())
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

        self.assertEqual('\t', csvFormatTwo.getDelimiter())
        self.assertEqual("\n", csvFormatTwo.getRecordSeparator())

        self.assertFalse(csvFormatTwo.isQuoteCharacterSet())
        self.assertTrue(csvFormatTwo.isNullStringSet())

        self.assertEqual('\\', csvFormatTwo.getEscapeCharacter())
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
    def testEqualsQuoteChar(self) -> None:
        right = CSVFormat.newFormat('\'')\
            .builder()\
            .setQuote0('"')\
            .build()
        left = right.builder().setQuote0('!').build()

        CSVFormatTest.__assertNotEquals0(right, left)

    
    @pytest.mark.test
    def testEqualsQuoteChar_Deprecated(self) -> None:
        right = CSVFormat.newFormat('\'')\
            .withQuote0('"')
        left = right.withQuote0('!')

        CSVFormatTest.__assertNotEquals0(right, left)

    
    @pytest.mark.test
    def testEqualsQuotePolicy(self) -> None:
        right = CSVFormat.newFormat('\'')\
            .builder()\
            .setQuote0('"')\
            .setQuoteMode(QuoteMode.ALL)\
            .build()
        left = right.builder().setQuoteMode(QuoteMode.MINIMAL).build()

        CSVFormatTest.__assertNotEquals0(right, left)

    
    @pytest.mark.test
    def testEqualsQuotePolicy_Deprecated(self) -> None:
        right = CSVFormat.newFormat('\'')\
            .withQuote0('"')\
            .withQuoteMode(QuoteMode.ALL)
        left = right.withQuoteMode(QuoteMode.MINIMAL)

        CSVFormatTest.__assertNotEquals0(right, left)


    @pytest.mark.test
    def testEqualsRecordSeparator(self) -> None:
        right = CSVFormat.newFormat('\'')\
            .builder()\
            .setRecordSeparator0(Constants.CR)\
            .setCommentMarker0('#')\
            .setEscape0('+')\
            .setIgnoreEmptyLines(True)\
            .setIgnoreSurroundingSpaces(True)\
            .setQuote0('"')\
            .setQuoteMode(QuoteMode.ALL)\
            .build()
        left = right.builder().setRecordSeparator0(Constants.LF).build()

        CSVFormatTest.__assertNotEquals0(right, left)

    
    @pytest.mark.test
    def testEqualsRecordSeparator_Deprecated(self) -> None:
        right = CSVFormat.newFormat('\'')\
            .withRecordSeparator0(Constants.CR)\
            .withCommentMarker0('#')\
            .withEscape0('+')\
            .withIgnoreEmptyLines0()\
            .withIgnoreSurroundingSpaces0()\
            .withQuote0('"')\
            .withQuoteMode(QuoteMode.ALL)
        left = right.withRecordSeparator0(Constants.LF)

        CSVFormatTest.__assertNotEquals0(right, left)

    
    @pytest.mark.test
    def testEqualsSkipHeaderRecord(self) -> None:
        right = CSVFormat.newFormat('\'')\
            .builder()\
            .setRecordSeparator0(Constants.CR)\
            .setCommentMarker0('#')\
            .setEscape0('+')\
            .setIgnoreEmptyLines(True)\
            .setIgnoreSurroundingSpaces(True)\
            .setQuote0('"')\
            .setQuoteMode(QuoteMode.ALL)\
            .setNullString("null")\
            .setSkipHeaderRecord(True)\
            .build()
        left = right.builder().setSkipHeaderRecord(False).build()

        CSVFormatTest.__assertNotEquals0(right, left)

    
    @pytest.mark.test
    def _testEqualsSkipHeaderRecord_Deprecated(self) -> None:
        right = CSVFormat.newFormat('\'')\
            .withRecordSeparator0(Constants.CR)\
            .withCommentMarker0('#')\
            .withEscape0('+')\
            .withIgnoreEmptyLines0()\
            .withIgnoreSurroundingSpaces0()\
            .withQuote0('"')\
            .withQuoteMode(QuoteMode.ALL)\
            .withNullString("null")\
            .withSkipHeaderRecord0()
        left = right.withSkipHeaderRecord1(False)

        CSVFormatTest.__assertNotEquals0(right, left)


    @pytest.mark.test
    def testEqualsWithNull(self) -> None:
        csvFormat = CSVFormat.POSTGRESQL_TEXT

        self.assertEqual('\\', csvFormat.getEscapeCharacter())
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

        self.assertEqual('\t', csvFormat.getDelimiter())
        self.assertFalse(csvFormat.getSkipHeaderRecord())

        self.assertEqual("\n", csvFormat.getRecordSeparator())
        self.assertFalse(csvFormat.getIgnoreEmptyLines())

        self.assertIsNone(csvFormat.getQuoteCharacter())
        self.assertTrue(csvFormat.isNullStringSet())

        self.assertEqual('\\', csvFormat.getEscapeCharacter())
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

        self.assertEqual('\t', csvFormat.getDelimiter())
        self.assertFalse(csvFormat.getSkipHeaderRecord())

        self.assertEqual("\n", csvFormat.getRecordSeparator())
        self.assertFalse(csvFormat.getIgnoreEmptyLines())

        self.assertIsNone(csvFormat.getQuoteCharacter())
        self.assertTrue(csvFormat.isNullStringSet())

        self.assertNotEqual(None, csvFormat)


    @pytest.mark.test
    def testEscapeSameAsCommentStartThrowsException(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT\
                .builder()\
                .setEscape0('!')\
                .setCommentMarker0('!')\
                .build()

    
    @pytest.mark.test
    def testEscapeSameAsCommentStartThrowsException_Deprecated(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT.withEscape0('!').withCommentMarker0('!')

    
    @pytest.mark.test
    def testEscapeSameAsCommentStartThrowsExceptionForWrapperType(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT\
                .builder()\
                .setEscape1('!')\
                .setCommentMarker1('!')\
                .build()
    

    @pytest.mark.test
    def testEscapeSameAsCommentStartThrowsExceptionForWrapperType_Deprecated(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT\
                .withEscape1('!')\
                .withCommentMarker1('!')

    
    @pytest.mark.test
    def testFormat(self) -> None:
        format = CSVFormat.DEFAULT

        if hasattr(format, 'format'):
            try:
                self.assertEqual("", format.format())
                self.assertEqual("a,b,c", format.format("a", "b", "c"))
                self.assertEqual("\"x,y\",z", format.format("x,y", "z"))
            except TypeError:
                self.assertEqual("", format.format([]))
                self.assertEqual("a,b,c", format.format(["a", "b", "c"]))
                self.assertEqual("\"x,y\",z", format.format(["x,y", "z"]))
        else:
            try:
                self.assertEqual("", format.format_())
                self.assertEqual("a,b,c", format.format_("a", "b", "c"))
                self.assertEqual("\"x,y\",z", format.format_("x,y", "z"))
            except TypeError:
                self.assertEqual("", format.format_([]))
                self.assertEqual("a,b,c", format.format_(["a", "b", "c"]))
                self.assertEqual("\"x,y\",z", format.format_(["x,y", "z"]))


    
    @pytest.mark.test
    def testFormatThrowsNullPointerException(self) -> None:
        csvFormat = CSVFormat.MYSQL

        try:
            csvFormat.format(None)
            self.fail("Expected TypeError or AttributeError to be thrown")
        except (TypeError, AttributeError) as e:
            self.assertIn("CSVFormat", traceback.format_exc())


    @pytest.mark.test
    def testGetAllowDuplicateHeaderNames(self) -> None:
        builder = CSVFormat.DEFAULT.builder()
        self.assertTrue(
            builder.build().getAllowDuplicateHeaderNames()
        )
        self.assertTrue(
            builder\
                .setDuplicateHeaderMode(DuplicateHeaderMode.ALLOW_ALL)\
                .build()\
                .getAllowDuplicateHeaderNames()
        )
        self.assertFalse(
            builder\
                .setDuplicateHeaderMode(DuplicateHeaderMode.ALLOW_EMPTY)\
                .build()\
                .getAllowDuplicateHeaderNames()
        )
        self.assertFalse(
            builder\
                .setDuplicateHeaderMode(DuplicateHeaderMode.DISALLOW)\
                .build()\
                .getAllowDuplicateHeaderNames()
        )


    @pytest.mark.test
    def testGetDuplicateHeaderMode(self) -> None:
        builder = CSVFormat.DEFAULT.builder()

        self.assertEqual(
            DuplicateHeaderMode.ALLOW_ALL,
            builder.build().getDuplicateHeaderMode()
        )
        self.assertEqual(
            DuplicateHeaderMode.ALLOW_ALL,
            builder.setDuplicateHeaderMode(DuplicateHeaderMode.ALLOW_ALL)\
                .build().getDuplicateHeaderMode()
        )
        self.assertEqual(
            DuplicateHeaderMode.ALLOW_EMPTY,
            builder.setDuplicateHeaderMode(DuplicateHeaderMode.ALLOW_EMPTY)\
                .build().getDuplicateHeaderMode()
        )
        self.assertEqual(
            DuplicateHeaderMode.DISALLOW,
            builder.setDuplicateHeaderMode(DuplicateHeaderMode.DISALLOW)\
                .build().getDuplicateHeaderMode()
        )


    @pytest.mark.test
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

    
    @pytest.mark.test
    def testNewFormat(self) -> None:
        csvFormat = CSVFormat.newFormat('X')

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

        self.assertEqual('X', csvFormat.getDelimiter())
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

        self.assertEqual('X', csvFormat.getDelimiter())
        self.assertIsNone(csvFormat.getNullString())

        self.assertFalse(csvFormat.isQuoteCharacterSet())
        self.assertFalse(csvFormat.isCommentMarkerSet())

        self.assertIsNone(csvFormat.getQuoteCharacter())
        self.assertFalse(csvFormat.getIgnoreEmptyLines())


    @pytest.mark.test
    def testPrintRecord(self) -> None:
        try:
            out = []
            format = CSVFormat.RFC4180
            try:
                format.printRecord(out, "a", "b", "c")
            except TypeError:
                format.printRecord(out, ["a", "b", "c"])
            self.assertEqual("a,b,c" + format.getRecordSeparator(), ''.join(out))
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")


    @pytest.mark.test
    def testPrintRecordEmpty(self) -> None:
        try:
            out = []
            format = CSVFormat.RFC4180
            try:
                format.printRecord(out)
            except TypeError:
                format.printRecord(out, [])
            self.assertEqual(format.getRecordSeparator(), ''.join(out))
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testPrintWithEscapesEndWithCRLF(self) -> None:
        try:
            data = "x,y,x\r\na,?b,c\r\n"
            inStream = io.StringIO(data)
            out = []
            format = CSVFormat.RFC4180\
                .withEscape0('?')\
                .withDelimiter(',')\
                .withQuote1(None)\
                .withRecordSeparator1(Constants.CRLF)
            format.print2(inStream, out, True)
            self.assertEqual("x?,y?,x?r?na?,??b?,c?r?n", ''.join(out))
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testPrintWithEscapesEndWithoutCRLF(self) -> None:
        try:
            data = "x,y,x"
            inStream = io.StringIO(data)
            out = []
            format = CSVFormat.RFC4180\
                .withEscape0('?')\
                .withDelimiter(',')\
                .withQuote1(None)\
                .withRecordSeparator1(Constants.CRLF)
            format.print2(inStream, out, True)
            self.assertEqual("x?,y?,x", ''.join(out))
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")
 

    @pytest.mark.test
    def testPrintWithoutQuotes(self) -> None:
        try:
            data = ""
            inStream = io.StringIO(data)
            out = []
            format = CSVFormat.RFC4180\
                .withDelimiter(',')\
                .withQuote0('"')\
                .withEscape0('?')\
                .withQuoteMode(QuoteMode.NON_NUMERIC)
            format.print2(inStream, out, True)
            self.assertEqual("\"\"", ''.join(out))
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")


    @pytest.mark.test
    def testPrintWithQuoteModeIsNONE(self) -> None:
        try:
            data = "a,b,c"
            inStream = io.StringIO(data)
            out = []
            format = CSVFormat.RFC4180\
                .withDelimiter(',')\
                .withQuote0('"')\
                .withEscape0('?')\
                .withQuoteMode(QuoteMode.NONE)
            format.print2(inStream, out, True)
            self.assertEqual("a?,b?,c", ''.join(out))
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")


    @pytest.mark.test
    def testPrintWithQuotes(self) -> None:
        try:
            data = "\"a,b,c\r\nx,y,z"
            inStream = io.StringIO(data)
            out = []
            format = CSVFormat.RFC4180\
                .withDelimiter(',')\
                .withQuote0('"')\
                .withEscape0('?')\
                .withQuoteMode(QuoteMode.NON_NUMERIC)
            format.print2(inStream, out, True)
            self.assertEqual("\"\"\"a,b,c\r\nx,y,z\"", ''.join(out))
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")


    @pytest.mark.test
    def testQuoteCharSameAsCommentStartThrowsException(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT\
                .builder()\
                .setQuote0('!')\
                .setCommentMarker0('!')\
                .build()


    @pytest.mark.test
    def testQuoteCharSameAsCommentStartThrowsException_Deprecated(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT\
                .withQuote0('!')\
                .withCommentMarker0('!')


    @pytest.mark.test
    def testQuoteCharSameAsCommentStartThrowsExceptionForWrapperType(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT\
                .builder()\
                .setQuote1('!')\
                .setCommentMarker0('!')\
                .build()


    @pytest.mark.test
    def testQuoteCharSameAsCommentStartThrowsExceptionForWrapperType_Deprecated(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT\
                .withQuote1('!')\
                .withCommentMarker0('!')


    @pytest.mark.test
    def testQuoteCharSameAsDelimiterThrowsException(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT\
                .builder()\
                .setQuote0('!')\
                .setDelimiter0('!')\
                .build()


    @pytest.mark.test
    def testQuoteCharSameAsDelimiterThrowsException_Deprecated(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT\
                .withQuote0('!')\
                .withDelimiter('!')


    @pytest.mark.test
    def testQuotePolicyNoneWithoutEscapeThrowsException(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.newFormat('!')\
                .builder()\
                .setQuoteMode(QuoteMode.NONE)\
                .build()


    @pytest.mark.test
    def testQuotePolicyNoneWithoutEscapeThrowsException_Deprecated(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.newFormat('!')\
                .withQuoteMode(QuoteMode.NONE)

    
    @pytest.mark.test
    def testRFC4180(self) -> None:
        self.assertIsNone(CSVFormat.RFC4180.getCommentMarker())
        self.assertEqual(',', CSVFormat.RFC4180.getDelimiter())
        self.assertIsNone(CSVFormat.RFC4180.getEscapeCharacter())
        self.assertFalse(CSVFormat.RFC4180.getIgnoreEmptyLines())
        self.assertEqual('"', CSVFormat.RFC4180.getQuoteCharacter())
        self.assertIsNone(CSVFormat.RFC4180.getQuoteMode())
        self.assertEqual("\r\n", CSVFormat.RFC4180.getRecordSeparator())


    @pytest.mark.test
    def testSerialization(self) -> None:
        try:
            out = io.BytesIO()
        
            pickle.dump(CSVFormat.DEFAULT, out)
            out.seek(0)
        
            inStream = io.BytesIO(out.read())
            format = pickle.load(inStream)

            self.assertIsNotNone(format)
            self.assertEqual(
                CSVFormat.DEFAULT.getDelimiter(),
                format.getDelimiter(),
                "delimiter"
            )
            self.assertEqual(
                CSVFormat.DEFAULT.getQuoteCharacter(),
                format.getQuoteCharacter(),
                "encapsulator"
            )
            self.assertEqual(
                CSVFormat.DEFAULT.getCommentMarker(),
                format.getCommentMarker(),
                "comment start"
            )
            self.assertEqual(
                CSVFormat.DEFAULT.getRecordSeparator(),
                format.getRecordSeparator(),
                "record separator"
            )
            self.assertEqual(
                CSVFormat.DEFAULT.getEscapeCharacter(),
                format.getEscapeCharacter(),
                "escape"
            )
            self.assertEqual(
                CSVFormat.DEFAULT.getIgnoreSurroundingSpaces(),
                format.getIgnoreSurroundingSpaces(),
                "trim"
            )
            self.assertEqual(
                CSVFormat.DEFAULT.getIgnoreEmptyLines(),
                format.getIgnoreEmptyLines(),
                "empty lines"
            )
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testToString(self) -> None:
        string = CSVFormat.INFORMIX_UNLOAD.toString()

        self.assertEqual(
            "Delimiter=<|> Escape=<\\> QuoteChar=<\"> RecordSeparator=<\n" +\
                "> EmptyLines:ignored SkipHeaderRecord:false",
            string
        )


    @pytest.mark.test
    def testToStringAndWithCommentMarkerTakingCharacter(self) -> None:
        try:
            csvFormat_Predefined = CSVFormat.Predefined.Default
        except AttributeError:
            csvFormat_Predefined = Predefined.Default
        csvFormat = csvFormat_Predefined.getFormat()

        self.assertIsNone(csvFormat.getEscapeCharacter())
        self.assertTrue(csvFormat.isQuoteCharacterSet())

        self.assertFalse(csvFormat.getTrim())
        self.assertFalse(csvFormat.getIgnoreSurroundingSpaces())

        self.assertFalse(csvFormat.getTrailingDelimiter())
        self.assertEqual(',', csvFormat.getDelimiter())

        self.assertFalse(csvFormat.getIgnoreHeaderCase())
        self.assertEqual("\r\n", csvFormat.getRecordSeparator())

        self.assertFalse(csvFormat.isCommentMarkerSet())
        self.assertIsNone(csvFormat.getCommentMarker())

        self.assertFalse(csvFormat.isNullStringSet())
        self.assertFalse(csvFormat.getAllowMissingColumnNames())

        self.assertFalse(csvFormat.isEscapeCharacterSet())
        self.assertFalse(csvFormat.getSkipHeaderRecord())

        self.assertIsNone(csvFormat.getNullString())
        self.assertIsNone(csvFormat.getQuoteMode())

        self.assertTrue(csvFormat.getIgnoreEmptyLines())
        self.assertEqual('\"', csvFormat.getQuoteCharacter())

        character = 'n'

        csvFormatTwo = csvFormat.withCommentMarker1(character)

        self.assertIsNone(csvFormat.getEscapeCharacter())
        self.assertTrue(csvFormat.isQuoteCharacterSet())

        self.assertFalse(csvFormat.getTrim())
        self.assertFalse(csvFormat.getIgnoreSurroundingSpaces())

        self.assertFalse(csvFormat.getTrailingDelimiter())
        self.assertEqual(',', csvFormat.getDelimiter())

        self.assertFalse(csvFormat.getIgnoreHeaderCase())
        self.assertEqual("\r\n", csvFormat.getRecordSeparator())

        self.assertFalse(csvFormat.isCommentMarkerSet())
        self.assertIsNone(csvFormat.getCommentMarker())

        self.assertFalse(csvFormat.isNullStringSet())
        self.assertFalse(csvFormat.getAllowMissingColumnNames())

        self.assertFalse(csvFormat.isEscapeCharacterSet())
        self.assertFalse(csvFormat.getSkipHeaderRecord())

        self.assertIsNone(csvFormat.getNullString())
        self.assertIsNone(csvFormat.getQuoteMode())

        self.assertTrue(csvFormat.getIgnoreEmptyLines())
        self.assertEqual('\"', csvFormat.getQuoteCharacter())

        self.assertFalse(csvFormatTwo.isNullStringSet())
        self.assertFalse(csvFormatTwo.getAllowMissingColumnNames())

        self.assertEqual('\"', csvFormatTwo.getQuoteCharacter())
        self.assertIsNone(csvFormatTwo.getNullString())

        self.assertEqual(',', csvFormatTwo.getDelimiter())
        self.assertFalse(csvFormatTwo.getTrailingDelimiter())

        self.assertTrue(csvFormatTwo.isCommentMarkerSet())
        self.assertFalse(csvFormatTwo.getIgnoreHeaderCase())

        self.assertFalse(csvFormatTwo.getTrim())
        self.assertIsNone(csvFormatTwo.getEscapeCharacter())

        self.assertTrue(csvFormatTwo.isQuoteCharacterSet())
        self.assertFalse(csvFormatTwo.getIgnoreSurroundingSpaces())

        self.assertEqual("\r\n", csvFormatTwo.getRecordSeparator())
        self.assertIsNone(csvFormatTwo.getQuoteMode())

        self.assertEqual('n', csvFormatTwo.getCommentMarker())
        self.assertFalse(csvFormatTwo.getSkipHeaderRecord())

        self.assertFalse(csvFormatTwo.isEscapeCharacterSet())
        self.assertTrue(csvFormatTwo.getIgnoreEmptyLines())

        self.assertIsNot(csvFormat, csvFormatTwo)
        self.assertIsNot(csvFormatTwo, csvFormat)

        self.assertNotEqual(csvFormatTwo, csvFormat)

        self.assertIsNone(csvFormat.getEscapeCharacter())
        self.assertTrue(csvFormat.isQuoteCharacterSet())

        self.assertFalse(csvFormat.getTrim())
        self.assertFalse(csvFormat.getIgnoreSurroundingSpaces())

        self.assertFalse(csvFormat.getTrailingDelimiter())
        self.assertEqual(',', csvFormat.getDelimiter())

        self.assertFalse(csvFormat.getIgnoreHeaderCase())
        self.assertEqual("\r\n", csvFormat.getRecordSeparator())

        self.assertFalse(csvFormat.isCommentMarkerSet())
        self.assertIsNone(csvFormat.getCommentMarker())

        self.assertFalse(csvFormat.isNullStringSet())
        self.assertFalse(csvFormat.getAllowMissingColumnNames())

        self.assertFalse(csvFormat.isEscapeCharacterSet())
        self.assertFalse(csvFormat.getSkipHeaderRecord())

        self.assertIsNone(csvFormat.getNullString())
        self.assertIsNone(csvFormat.getQuoteMode())

        self.assertTrue(csvFormat.getIgnoreEmptyLines())
        self.assertEqual('\"', csvFormat.getQuoteCharacter())

        self.assertFalse(csvFormatTwo.isNullStringSet())
        self.assertFalse(csvFormatTwo.getAllowMissingColumnNames())

        self.assertEqual('\"', csvFormatTwo.getQuoteCharacter())
        self.assertIsNone(csvFormatTwo.getNullString())

        self.assertEqual(',', csvFormatTwo.getDelimiter())
        self.assertFalse(csvFormatTwo.getTrailingDelimiter())

        self.assertTrue(csvFormatTwo.isCommentMarkerSet())
        self.assertFalse(csvFormatTwo.getIgnoreHeaderCase())

        self.assertFalse(csvFormatTwo.getTrim())
        self.assertIsNone(csvFormatTwo.getEscapeCharacter())

        self.assertTrue(csvFormatTwo.isQuoteCharacterSet())
        self.assertFalse(csvFormatTwo.getIgnoreSurroundingSpaces())

        self.assertEqual("\r\n", csvFormatTwo.getRecordSeparator())
        self.assertIsNone(csvFormatTwo.getQuoteMode())

        self.assertEqual('n', csvFormatTwo.getCommentMarker())
        self.assertFalse(csvFormatTwo.getSkipHeaderRecord())

        self.assertFalse(csvFormatTwo.isEscapeCharacterSet())
        self.assertTrue(csvFormatTwo.getIgnoreEmptyLines())

        self.assertIsNot(csvFormat, csvFormatTwo)
        self.assertIsNot(csvFormatTwo, csvFormat)

        self.assertNotEqual(csvFormat, csvFormatTwo)

        self.assertNotEqual(csvFormatTwo, csvFormat)
        self.assertEqual(
            "Delimiter=<,> QuoteChar=<\"> CommentStart=<n> " +\
                "RecordSeparator=<\r\n> EmptyLines:ignored SkipHeaderRecord:false",
            csvFormatTwo.toString()
        )


    @pytest.mark.test
    def testTrim(self) -> None:
        try:
            formatWithTrim = CSVFormat.DEFAULT\
                .withDelimiter(',')\
                .withTrim0()\
                .withQuote1(None)\
                .withRecordSeparator1(Constants.CRLF)
            inStream = "a,b,c"
            out = []
            formatWithTrim.print2(inStream, out, True)
            self.assertEqual("a,b,c", ''.join(out))

            inStream = " x,y,z"
            out.clear()
            formatWithTrim.print2(inStream, out, True)
            self.assertEqual("x,y,z", ''.join(out))

            inStream = ""
            out.clear()
            formatWithTrim.print2(inStream, out, True)
            self.assertEqual("", ''.join(out))

            inStream = "header\r\n"
            out.clear()
            formatWithTrim.print2(inStream, out, True)
            self.assertEqual("header", ''.join(out))
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")


    @pytest.mark.test
    def testWithCommentStart(self) -> None:
        formatWithCommentStart = CSVFormat.DEFAULT.withCommentMarker0('#')
        self.assertEqual('#', formatWithCommentStart.getCommentMarker())


    @pytest.mark.test
    def testWithCommentStartCRThrowsException(self) -> None:
        with self.assertRaises(ValueError):
             CSVFormat.DEFAULT\
                 .withCommentMarker0(Constants.CR)


    @pytest.mark.test
    def testWithDelimiter(self) -> None:
        formatWithDelimiter = CSVFormat.DEFAULT.withDelimiter('!')
        self.assertEqual('!', formatWithDelimiter.getDelimiter())


    @pytest.mark.test
    def testWithDelimiterLFThrowsException(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT\
                .withDelimiter(Constants.LF)


    @pytest.mark.test
    def testWithEmptyDuplicates(self) -> None:
        formatWithEmptyDuplicates = CSVFormat.DEFAULT\
            .builder()\
            .setDuplicateHeaderMode(DuplicateHeaderMode.ALLOW_EMPTY)\
            .build()

        self.assertEqual(
            DuplicateHeaderMode.ALLOW_EMPTY,
            formatWithEmptyDuplicates.getDuplicateHeaderMode()
        )
        self.assertFalse(
            formatWithEmptyDuplicates.getAllowDuplicateHeaderNames()
        )


    @pytest.mark.test
    def testWithEscape(self) -> None:
        formatWithEscape = CSVFormat.DEFAULT.withEscape0('&')
        self.assertEqual(
             '&',
             formatWithEscape.getEscapeCharacter()
        )


    @pytest.mark.test
    def testWithEscapeCRThrowsExceptions(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT\
                .withEscape0(Constants.CR)


    @pytest.mark.test
    def testWithHeaderComments(self) -> None:
        csvFormat = CSVFormat.DEFAULT

        self.assertEqual('\"', csvFormat.getQuoteCharacter())
        self.assertFalse(csvFormat.isCommentMarkerSet())

        self.assertFalse(csvFormat.isEscapeCharacterSet())
        self.assertTrue(csvFormat.isQuoteCharacterSet())

        self.assertFalse(csvFormat.getSkipHeaderRecord())
        self.assertIsNone(csvFormat.getQuoteMode())

        self.assertEqual(',', csvFormat.getDelimiter())
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

        self.assertEqual('\"', csvFormat.getQuoteCharacter())
        self.assertFalse(csvFormat.isCommentMarkerSet())

        self.assertFalse(csvFormat.isEscapeCharacterSet())
        self.assertTrue(csvFormat.isQuoteCharacterSet())

        self.assertFalse(csvFormat.getSkipHeaderRecord())
        self.assertIsNone(csvFormat.getQuoteMode())

        self.assertEqual(',', csvFormat.getDelimiter())
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
        self.assertEqual('\"', csvFormatTwo.getQuoteCharacter())

        self.assertFalse(csvFormatTwo.getAllowMissingColumnNames())
        self.assertIsNone(csvFormatTwo.getNullString())

        self.assertFalse(csvFormatTwo.isNullStringSet())
        self.assertFalse(csvFormatTwo.getTrailingDelimiter())

        self.assertEqual("\r\n", csvFormatTwo.getRecordSeparator())
        self.assertEqual(',', csvFormatTwo.getDelimiter())

        self.assertIsNone(csvFormatTwo.getCommentMarker())
        self.assertFalse(csvFormatTwo.isCommentMarkerSet())

        self.assertIsNot(csvFormat, csvFormatTwo)
        self.assertIsNot(csvFormatTwo, csvFormat)

        self.assertNotEqual(csvFormatTwo, csvFormat)

        if hasattr(csvFormatTwo, "format"):
            string = csvFormatTwo.format(objectArray)
        else:
            string = csvFormatTwo.format_(objectArray)

        self.assertEqual('\"', csvFormat.getQuoteCharacter())
        self.assertFalse(csvFormat.isCommentMarkerSet())

        self.assertFalse(csvFormat.isEscapeCharacterSet())
        self.assertTrue(csvFormat.isQuoteCharacterSet())

        self.assertFalse(csvFormat.getSkipHeaderRecord())
        self.assertIsNone(csvFormat.getQuoteMode())

        self.assertEqual(',', csvFormat.getDelimiter())
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
        self.assertEqual('\"', csvFormatTwo.getQuoteCharacter())

        self.assertFalse(csvFormatTwo.getAllowMissingColumnNames())
        self.assertIsNone(csvFormatTwo.getNullString())

        self.assertFalse(csvFormatTwo.isNullStringSet())
        self.assertFalse(csvFormatTwo.getTrailingDelimiter())

        self.assertEqual("\r\n", csvFormatTwo.getRecordSeparator())
        self.assertEqual(',', csvFormatTwo.getDelimiter())

        self.assertIsNone(csvFormatTwo.getCommentMarker())
        self.assertFalse(csvFormatTwo.isCommentMarkerSet())

        self.assertIsNot(csvFormat, csvFormatTwo)
        self.assertIsNot(csvFormatTwo, csvFormat)

        self.assertIsNotNone(string)
        self.assertNotEqual(csvFormat, csvFormatTwo)

        self.assertNotEqual(csvFormatTwo, csvFormat)
        self.assertEqual(",,,,,,,", string)


    @pytest.mark.test
    def testWithIgnoreEmptyLines(self) -> None:
        self.assertFalse(
            CSVFormat.DEFAULT\
                .withIgnoreEmptyLines1(False)\
                .getIgnoreEmptyLines()
        )
        self.assertTrue(
            CSVFormat.DEFAULT\
                .withIgnoreEmptyLines0()\
                .getIgnoreEmptyLines()
        )


    @pytest.mark.test
    def testWithIgnoreSurround(self) -> None:
        self.assertFalse(
            CSVFormat.DEFAULT\
                .withIgnoreSurroundingSpaces1(False)\
                .getIgnoreSurroundingSpaces()
        )
        self.assertTrue(
            CSVFormat.DEFAULT\
                .withIgnoreSurroundingSpaces0()\
                .getIgnoreSurroundingSpaces()
        )


    @pytest.mark.test
    def testWithNullString(self) -> None:
        formatWithNullString = CSVFormat.DEFAULT.withNullString("null")
        self.assertEqual("null", formatWithNullString.getNullString())


    @pytest.mark.test
    def testWithQuoteChar(self) -> None:
        formatWithQuoteChar = CSVFormat.DEFAULT.withQuote0('"')
        self.assertEqual('"', formatWithQuoteChar.getQuoteCharacter())


    @pytest.mark.test
    def testWithQuoteLFThrowsException(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT\
                .withQuote0(Constants.LF)


    @pytest.mark.test
    def testWithQuotePolicy(self) -> None:
        formatWithQuotePolicy = CSVFormat.DEFAULT.withQuoteMode(QuoteMode.ALL)
        self.assertEqual(QuoteMode.ALL, formatWithQuotePolicy.getQuoteMode())


    @pytest.mark.test
    def testWithRecordSeparatorCR(self) -> None:
        formatWithRecordSeparator = CSVFormat.DEFAULT\
            .withRecordSeparator0(Constants.CR)
        self.assertEqual(
            str(Constants.CR),
            formatWithRecordSeparator.getRecordSeparator()
        )


    @pytest.mark.test
    def testWithRecordSeparatorCRLF(self) -> None:
        formatWithRecordSeparator = CSVFormat.DEFAULT\
            .withRecordSeparator1(Constants.CRLF)
        self.assertEqual(
            str(Constants.CRLF),
            formatWithRecordSeparator.getRecordSeparator()
        )


    @pytest.mark.test
    def testWithRecordSeparatorLF(self) -> None:
        formatWithRecordSeparator = CSVFormat.DEFAULT\
            .withRecordSeparator0(Constants.LF)
        self.assertEqual(
            str(Constants.LF),
            formatWithRecordSeparator.getRecordSeparator()
        )


    @pytest.mark.test
    def testWithSystemRecordSeparator(self) -> None:
        formatWithRecordSeparator = CSVFormat.DEFAULT\
            .withSystemRecordSeparator()
        self.assertEquals(
            os.linesep,
            formatWithRecordSeparator.getRecordSeparator()
        )
