# Imports Begin
from src.main.org.apache.commons.csv.Utils import *
from src.main.org.apache.commons.csv.QuoteMode import *
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.CSVPrinter import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVFormat import *
import tempfile
import unittest
import os
import typing
from typing import *
import pathlib
# Imports End

class new Executable(...) { ... }(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def execute(self) -> None:

            self.assertRaises(IllegalArgumentException, CSVFormat.DEFAULT.withDelimiter, CR)

    def execute(self) -> None:

            self.assertRaises(ValueError, lambda: CSVPrinter(StringWriter(), None))

    def execute(self) -> None:

            self.assertRaises(ValueError, lambda: CSVPrinter(None, CSVFormat.DEFAULT))

    # Class Methods End


class CSVPrinterTest(unittest.TestCase):

    # Class Fields Begin
    __EMPTY_STRING: str = ""
    __EURO_SYMBOL: str = '\u20AC'
    __ITERATIONS_FOR_RANDOM_TEST: int = 50000
    __QUOTE_STR: str = "\""
    __longText2: str = None
    __recordSeparator: str = CSVFormat.DEFAULT.getRecordSeparator()
    # Class Fields End

    # Class Methods Begin
    def testTrimOnTwoColumns(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.DEFAULT.withTrim0())
                printer.print(" A ")
                printer.print(" B ")
                self.assertEqual("A,B", sw.toString())
            except Exception as e:
                self.fail("Error running testTrimOnTwoColumns: " + str(e))

    def testTrimOnOneColumn(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.DEFAULT.withTrim0())
                printer.print(" A ")
                self.assertEqual("A", sw.toString())
            except Exception as e:
                self.fail(f"Exception occurred: {e}")

    def testTrimOffOneColumn(self) -> None:

            sw = StringWriter()
            with CSVPrinter(sw, CSVFormat.DEFAULT.withTrim1(False)) as printer:
                printer.print(" A ")
                self.assertEqual("\" A \"", sw.toString())

    def testTrailingDelimiterOnTwoColumns(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.DEFAULT.withTrailingDelimiter0())
                printer.printRecord1("A", "B")
                self.assertEqual("A,B,\r\n", sw.toString())
            except Exception as e:
                self.fail(f"Unexpected exception: {e}")

    def testSingleQuoteQuoted(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0('\''))
                printer.print("a'b'c")
                printer.print("xyz")
                self.assertEqual("'a''b''c',xyz", sw.toString())
            except Exception as e:
                self.fail(f"Unexpected exception: {e}")

    def testSingleLineComment(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.DEFAULT.withCommentMarker0('#'))
                printer.printComment("This is a comment")
                self.assertEqual("# This is a comment" + self.__recordSeparator, sw.toString())
            except Exception as e:
                self.fail("Unexpected exception: " + str(e))

    def testRandomTdf(self) -> None:

            self.__doRandom(CSVFormat.TDF, self.__ITERATIONS_FOR_RANDOM_TEST)

    def testRandomRfc4180(self) -> None:

            self.__doRandom(CSVFormat.RFC4180, self.__ITERATIONS_FOR_RANDOM_TEST)

    def testRandomPostgreSqlText(self) -> None:

            self.__doRandom(CSVFormat.POSTGRESQL_TEXT, self.__ITERATIONS_FOR_RANDOM_TEST)

    def testRandomPostgreSqlCsv(self) -> None:

            self.__doRandom(CSVFormat.POSTGRESQL_CSV, self.__ITERATIONS_FOR_RANDOM_TEST)

    def testRandomOracle(self) -> None:

            self.__doRandom(CSVFormat.ORACLE, self.__ITERATIONS_FOR_RANDOM_TEST)

    def testRandomMySql(self) -> None:

            self.__doRandom(CSVFormat.MYSQL, self.__ITERATIONS_FOR_RANDOM_TEST)

    def testRandomMongoDbCsv(self) -> None:

            self.__doRandom(CSVFormat.MONGODB_CSV, self.__ITERATIONS_FOR_RANDOM_TEST)

    def testRandomExcel(self) -> None:

            self.__doRandom(CSVFormat.EXCEL, self.__ITERATIONS_FOR_RANDOM_TEST)

    def testRandomDefault(self) -> None:

            self.__doRandom(CSVFormat.DEFAULT, self.__ITERATIONS_FOR_RANDOM_TEST)

    def testQuoteNonNumeric(self) -> None:

            sw = StringWriter()
            with CSVPrinter(sw, CSVFormat.DEFAULT.withQuoteMode(QuoteMode.NON_NUMERIC)) as printer:
                printer.printRecord1("a", "b\nc", 1)
                self.assertEqual("\"a\",\"b\nc\",1" + self.__recordSeparator, sw.toString())

    def testQuoteCommaFirstChar(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.RFC4180)
                printer.printRecord1(",")
                self.assertEqual("\"" + self.__recordSeparator, sw.toString())
            except Exception as e:
                self.fail("Unexpected exception: " + str(e))

    def testQuoteAll(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.DEFAULT.withQuoteMode(QuoteMode.ALL))
                printer.printRecord1("a", "b\nc", "d")
                self.assertEqual("\"a\",\"b\nc\",\"d\"" + self.__recordSeparator, sw.toString())
            except Exception as e:
                self.fail("Unexpected exception: " + str(e))

    def testPrintToPathWithDefaultCharset(self) -> None:

            file = self.__createTempPath()
            with self.CSVFormat.DEFAULT.print4(file, Charset.defaultCharset()) as printer:
                printer.printRecord1("a", "b\\c")
            self.assertEqual(
                "a,b\\c" + self.__recordSeparator,
                str(Files.readAllBytes(file), Charset.defaultCharset()))

    def testPrintRecordStream(self) -> None:

            code = "a1,b1\n" + "a2,b2\n" + "a3,b3\n" + "a4,b4\n"
            res = [["a1", "b1"], ["a2", "b2"], ["a3", "b3"], ["a4", "b4"]]
            format = CSVFormat.DEFAULT
            sw = StringWriter()
            try:
                printer = format.print0(sw)
                parser = CSVParser.parse4(code, format)
                for record in parser:
                    printer.printRecord2(record.stream())
            except Exception:
                self.fail("Failed to print record stream")
            try:
                parser = CSVParser.parse4(sw.toString(), format)
                records = parser.getRecords()
                self.assertFalse(records.isEmpty())
                Utils.compare("Fail", res, records)
            except Exception:
                self.fail("Failed to compare records")

    def testPrintReaderWithoutQuoteToWriter(self) -> None:

            sw = StringWriter()
            content = "testValue"
            with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(None)) as printer:
                value = StringReader(content)
                printer.print(value)
            self.assertEqual(content, sw.toString())

    def testPrintReaderWithoutQuoteToAppendable(self) -> None:

            sb = StringBuilder()
            content = "testValue"
            try:
                printer = CSVPrinter(sb, CSVFormat.DEFAULT.withQuote1(None))
                value = StringReader(content)
                printer.print(value)
            except Exception as e:
                self.fail(f"Exception occurred: {e}")
            self.assertEqual(content, sb.toString())

    def testPrintOnePositiveInteger(self) -> None:

            sw = StringWriter()
            with CSVPrinter(sw, CSVFormat.DEFAULT.withQuoteMode(QuoteMode.MINIMAL)) as printer:
                printer.print(Integer.MAX_VALUE)
                self.assertEqual(str(Integer.MAX_VALUE), sw.toString())

    def testPrintNullValues(self) -> None:

            sw = StringWriter()
            with CSVPrinter(sw, CSVFormat.DEFAULT) as printer:
                printer.printRecord1("a", None, "b")
                self.assertEqual("a,,b" + self.__recordSeparator, sw.toString())

    def testPrinter7(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.DEFAULT)
                printer.printRecord1("a", "b\\c")
                self.assertEqual("a,b\\c" + self.__recordSeparator, sw.toString())
            except Exception as e:
                raise e

    def testPrinter6(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.DEFAULT)
                printer.printRecord1("a", "b\r\nc")
                self.assertEqual("a,\"b\r\nc\"" + self.__recordSeparator, sw.toString())
            except Exception as e:
                self.fail("Unexpected exception: " + str(e))

    def testPrinter5(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.DEFAULT)
                printer.printRecord1("a", "b\nc")
                self.assertEqual("a,\"b\nc\"" + self.__recordSeparator, sw.toString())
            except Exception as e:
                self.fail("Unexpected exception: " + str(e))

    def testPrinter4(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.DEFAULT)
                printer.printRecord1("a", "b\"c")
                self.assertEqual("a,\"b\"\"c\"" + self.__recordSeparator, sw.toString())
            except Exception as e:
                self.fail("Unexpected exception: " + str(e))

    def testPrinter3(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.DEFAULT)
                printer.printRecord1("a, b", "b ")
                self.assertEqual("\"a, b\",\"b \"" + self.__recordSeparator, sw.toString())
            except Exception as e:
                self.fail("Unexpected exception: " + str(e))

    def testPrinter2(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.DEFAULT)
                printer.printRecord1("a,b", "b")
                self.assertEqual("\"a,b\",b" + self.__recordSeparator, sw.toString())
            except Exception as e:
                print(e)

    def testPrinter1(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.DEFAULT)
                printer.printRecord1("a", "b")
                self.assertEqual("a,b" + self.__recordSeparator, sw.toString())
            except Exception as e:
                raise e

    def testPrintCustomNullValues(self) -> None:

            sw = StringWriter()
            with CSVPrinter(sw, CSVFormat.DEFAULT.withNullString("NULL")) as printer:
                printer.printRecord1("a", None, "b")
                self.assertEqual("a,NULL,b" + self.__recordSeparator, sw.toString())

    def testPrintCSVRecords(self) -> None:

            code = "a1,b1\n" + "a2,b2\n" + "a3,b3\n" + "a4,b4\n"
            res = [["a1", "b1"], ["a2", "b2"], ["a3", "b3"], ["a4", "b4"]]
            format = CSVFormat.DEFAULT
            sw = StringWriter()
            with format.print0(sw) as printer, CSVParser.parse4(code, format) as parser:
                printer.printRecords0(parser.getRecords())
            with CSVParser.parse4(sw.toString(), format) as parser:
                records = parser.getRecords()
                self.assertFalse(records.isEmpty())
                Utils.compare("Fail", res, records)

    def testPrintCSVRecord(self) -> None:

            code = "a1,b1\n" + "a2,b2\n" + "a3,b3\n" + "a4,b4\n"
            res = [["a1", "b1"], ["a2", "b2"], ["a3", "b3"], ["a4", "b4"]]
            format = CSVFormat.DEFAULT
            sw = StringWriter()
            with format.print0(sw) as printer, CSVParser.parse4(code, format) as parser:
                for record in parser:
                    printer.printRecord0(record)
            with CSVParser.parse4(sw.toString(), format) as parser:
                records = parser.getRecords()
                self.assertFalse(records.isEmpty())
                Utils.compare("Fail", res, records)

    def testPrintCSVParser(self) -> None:

            code = "a1,b1\na2,b2\na3,b3\na4,b4\n"
            res = [["a1", "b1"], ["a2", "b2"], ["a3", "b3"], ["a4", "b4"]]
            format = CSVFormat.DEFAULT
            sw = StringWriter()
            with format.print0(sw) as printer, CSVParser.parse4(code, format) as parser:
                printer.printRecords0(parser)
            with CSVParser.parse4(sw.toString(), format) as parser:
                records = parser.getRecords()
                self.assertFalse(records.isEmpty())
                Utils.compare("Fail", res, records)

    def testPrint(self) -> None:

            sw = StringWriter()
            with CSVFormat.DEFAULT.print0(sw) as printer:
                printer.printRecord1("a", "b\\c")
                self.assertEqual("a,b\\c" + self.__recordSeparator, sw.toString())

    def testPostgreSqlNullStringDefaultText(self) -> None:

            self.assertEqual("\\N", CSVFormat.POSTGRESQL_TEXT.getNullString())

    def testPostgreSqlNullStringDefaultCsv(self) -> None:

            self.assertEqual("", CSVFormat.POSTGRESQL_CSV.getNullString())

    def testPostgreSqlCsvTextOutput(self) -> None:


        pass # LLM could not translate method body

    def testPostgreSqlCsvNullOutput(self) -> None:


        pass # LLM could not translate method body

    def testPlainQuoted(self) -> None:

            sw = StringWriter()
            with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0('\'')) as printer:
                printer.print("abc")
                self.assertEqual("abc", sw.toString())

    def testPlainPlain(self) -> None:

            sw = StringWriter()
            with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(None)) as printer:
                printer.print("abc")
                printer.print("xyz")
                self.assertEqual("abc,xyz", sw.toString())

    def testPlainEscaped(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(None).withEscape0('!'))
                printer.print("abc")
                printer.print("xyz")
                self.assertEqual("abc,xyz", sw.toString())
            except Exception as e:
                self.fail(f"Unexpected exception: {e}")

    def testParseCustomNullValues(self) -> None:

            sw = StringWriter()
            format = CSVFormat.DEFAULT.withNullString("NULL")
            try:
                printer = CSVPrinter(sw, format)
                printer.printRecord1("a", None, "b")
            finally:
                printer.close()
            csv_string = sw.toString()
            self.assertEqual("a,NULL,b" + self.__recordSeparator, csv_string)
            try:
                iterable = format.parse(StringReader(csv_string))
                iterator = iterable.iterator()
                record = iterator.next()
                self.assertEqual("a", record.get1(0))
                self.assertIsNone(record.get1(1))
                self.assertEqual("b", record.get1(2))
                self.assertFalse(iterator.hasNext())
            finally:
                iterable.close()

    def testNotFlushable(self) -> None:

            out = StringBuilder()
            with CSVPrinter(out, CSVFormat.DEFAULT) as printer:
                printer.printRecord1("a", "b", "c")
                self.assertEqual("a,b,c" + self.__recordSeparator, out.toString())
                printer.flush()

    def testNewCsvPrinterNullAppendableFormat(self) -> None:

            self.assertRaises(NullPointerException, lambda: CSVPrinter(None, CSVFormat.DEFAULT))

    def testNewCsvPrinterAppendableNullFormat(self) -> None:

            self.assertRaises(NullPointerException, lambda: CSVPrinter(StringWriter(), None))

    def testMySqlNullStringDefault(self) -> None:

            self.assertEqual("\\N", CSVFormat.MYSQL.getNullString())

    def testMySqlNullOutput(self) -> None:


        pass # LLM could not translate method body

    def testMultiLineComment(self) -> None:

            sw = StringWriter()
            with CSVPrinter(sw, CSVFormat.DEFAULT.withCommentMarker0('#')) as printer:
                printer.printComment("This is a comment\non multiple lines")
                self.assertEqual(
                    "# This is a comment" + self.__recordSeparator + "# on multiple lines" + self.__recordSeparator,
                    sw.toString()
                )

    def testMongoDbTsvTabInValue(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.MONGODB_TSV)
                printer.printRecord1("a\tb", "c")
                self.assertEqual("\"a\tb\"\tc" + self.__recordSeparator, sw.toString())
            except Exception:
                raise

    def testMongoDbTsvCommaInValue(self) -> None:

            sw = StringWriter()
            with CSVPrinter(sw, CSVFormat.MONGODB_TSV) as printer:
                printer.printRecord1("a,b", "c")
                self.assertEqual("a,b\tc" + self.__recordSeparator, sw.toString())

    def testMongoDbTsvBasic(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.MONGODB_TSV)
                printer.printRecord1("a", "b")
                self.assertEqual("a\tb" + self.__recordSeparator, sw.toString())
            except Exception as e:
                self.fail("Unexpected exception: " + str(e))

    def testMongoDbCsvTabInValue(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.MONGODB_CSV)
                printer.printRecord1("a\tb", "c")
                self.assertEqual("a\tb,c" + self.__recordSeparator, sw.toString())
            except Exception as e:
                self.fail("Unexpected exception: " + str(e))

    def testMongoDbCsvDoubleQuoteInValue(self) -> None:

            sw = StringWriter()
            with CSVPrinter(sw, CSVFormat.MONGODB_CSV) as printer:
                printer.printRecord1("a \"c\" b", "d")
                self.assertEqual("\"a \"\"c\"\" b\"" + self.__recordSeparator, sw.toString())

    def testMongoDbCsvCommaInValue(self) -> None:

            sw = StringWriter()
            with CSVPrinter(sw, CSVFormat.MONGODB_CSV) as printer:
                printer.printRecord1("a,b", "c")
                self.assertEqual("\"a,b\",c" + self.__recordSeparator, sw.toString())

    def testMongoDbCsvBasic(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.MONGODB_CSV)
                printer.printRecord1("a", "b")
                self.assertEqual("a,b" + self.__recordSeparator, sw.toString())
            except Exception:
                raise
            finally:
                sw.close()

    def testJira135All(self) -> None:

            format = CSVFormat.DEFAULT.withRecordSeparator0('\n').withQuote0(DQUOTE_CHAR).withEscape0(BACKSLASH)
            sw = StringWriter()
            list = LinkedList()
            try:
                printer = CSVPrinter(sw, format)
                list.add("\"")
                list.add("\n")
                list.add("\\")
                printer.printRecord0(list)
            finally:
                printer.close()
            expected = "\"\\\"\",\"\\n\",\"\\\"" + format.getRecordSeparator()
            self.assertEqual(expected, sw.toString())
            record0 = self.__toFirstRecordValues(expected, format)
            self.assertArrayEquals(self.__expectNulls(list.toArray(), format), record0)

    def testJira135_part3(self) -> None:

            format = CSVFormat.DEFAULT.withRecordSeparator0('\n').withQuote0(DQUOTE_CHAR).withEscape0(BACKSLASH)
            sw = StringWriter()
            list = LinkedList()
            try:
                printer = CSVPrinter(sw, format)
                list.add("\\")
                printer.printRecord0(list)
            finally:
                printer.close()
            expected = "\"\\\\\"" + format.getRecordSeparator()
            self.assertEqual(expected, sw.toString())
            record0 = self.__toFirstRecordValues(expected, format)
            self.assertArrayEquals(self.__expectNulls(list.toArray(), format), record0)

    def testJira135_part2(self) -> None:

            format = CSVFormat.DEFAULT.withRecordSeparator0('\n').withQuote0(DQUOTE_CHAR).withEscape0(BACKSLASH)
            sw = StringWriter()
            list = LinkedList()
            try:
                list.add("\n")
                printer = CSVPrinter(sw, format)
                printer.printRecord0(list)
            finally:
                printer.close()
            expected = "\"\\n\"" + format.getRecordSeparator()
            self.assertEqual(expected, sw.toString())
            record0 = self.__toFirstRecordValues(expected, format)
            self.assertArrayEquals(self.__expectNulls(list.toArray(), format), record0)

    def testJira135_part1(self) -> None:

            format = CSVFormat.DEFAULT.withRecordSeparator0('\n').withQuote0(DQUOTE_CHAR).withEscape0(BACKSLASH)
            sw = StringWriter()
            list = LinkedList()
            try:
                printer = CSVPrinter(sw, format)
                list.add("\"")
                printer.printRecord0(list)
            finally:
                printer.close()
            expected = "\"\\\"\"" + format.getRecordSeparator()
            self.assertEqual(expected, sw.toString())
            record0 = self.__toFirstRecordValues(expected, format)
            self.assertArrayEquals(self.__expectNulls(list.toArray(), format), record0)

    def testInvalidFormat(self) -> None:

            with self.assertRaises(IllegalArgumentException):
                CSVFormat.DEFAULT.withDelimiter(CR)

    def testHeaderNotSet(self) -> None:

            sw = StringWriter()
            with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(None)) as printer:
                printer.printRecord1("a", "b", "c")
                printer.printRecord1("x", "y", "z")
                self.assertEqual("a,b,c\r\nx,y,z\r\n", sw.toString())

    def testExcelPrinter2(self) -> None:

            sw = StringWriter()
            with CSVPrinter(sw, CSVFormat.EXCEL) as printer:
                printer.printRecord1("a,b", "b")
                self.assertEqual("\"a,b\",b" + self.__recordSeparator, sw.toString())

    def testExcelPrinter1(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.EXCEL)
                printer.printRecord1("a", "b")
                self.assertEqual("a,b" + self.__recordSeparator, sw.toString())
            except Exception:
                raise

    def testExcelPrintAllIterableOfLists(self) -> None:

            sw = StringWriter()
            with CSVPrinter(sw, CSVFormat.EXCEL) as printer:
                printer.printRecords0(
                    [
                        ["r1c1", "r1c2"],
                        ["r2c1", "r2c2"]
                    ]
                )
                self.assertEqual(
                    "r1c1,r1c2" + self.__recordSeparator + "r2c1,r2c2" + self.__recordSeparator,
                    sw.toString()
                )

    def testExcelPrintAllIterableOfArrays(self) -> None:

            sw = StringWriter()
            with CSVPrinter(sw, CSVFormat.EXCEL) as printer:
                printer.printRecords0(
                    [["r1c1", "r1c2"], ["r2c1", "r2c2"]])
                self.assertEqual(
                    "r1c1,r1c2" + self.__recordSeparator + "r2c1,r2c2" + self.__recordSeparator, sw.toString())

    def testExcelPrintAllArrayOfLists(self) -> None:


        pass # LLM could not translate method body

    def testExcelPrintAllArrayOfArrays(self) -> None:


        pass # LLM could not translate method body

    def testEscapeNull5(self) -> None:

            sw = StringWriter()
            with CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(None)) as printer:
                printer.print("\\\\")
            self.assertEqual("\\\\", sw.toString())

    def testEscapeNull4(self) -> None:

            sw = StringWriter()
            with CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(None)) as printer:
                printer.print("\\\\")
            self.assertEqual("\\\\", sw.toString())

    def testEscapeNull3(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(None))
                printer.print("X\\\r")
            finally:
                printer.close()
            self.assertEqual("\"X\\\r\"", sw.toString())

    def testEscapeNull2(self) -> None:

            sw = StringWriter()
            with CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(None)) as printer:
                printer.print("\\\r")
            self.assertEqual("\"\\\r\"", sw.toString())

    def testEscapeNull1(self) -> None:

            sw = StringWriter()
            with CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(None)) as printer:
                printer.print("\\")
            self.assertEqual("\\", sw.toString())

    def testEscapeBackslash5(self) -> None:

            sw = StringWriter()
            with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(self.__QUOTE_CH)) as printer:
                printer.print("\\\\")
            self.assertEqual("\\\\", sw.toString())

    def testEscapeBackslash4(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(QUOTE_CH))
                printer.print("\\\\")
            except Exception as e:
                self.fail(f"Unexpected exception: {e}")
            self.assertEqual("\\\\", sw.toString())

    def testEscapeBackslash3(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(QUOTE_CH))
                printer.print("X\\\r")
            finally:
                printer.close()
            self.assertEqual("'X\\\r'", sw.toString())

    def testEscapeBackslash2(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(QUOTE_CH))
                printer.print("\\\r")
            finally:
                printer.close()
            self.assertEqual("'\\\r'", sw.toString())

    def testEscapeBackslash1(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(QUOTE_CH))
                printer.print("\\")
            finally:
                printer.close()
            self.assertEqual("\\", sw.toString())

    def testEolQuoted(self) -> None:

            sw = StringWriter()
            with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0('\'')) as printer:
                printer.print("a\rb\nc")
                printer.print("x\by\fz")
                self.assertEqual("'a\rb\nc',x\by\fz", sw.toString())

    def testEolPlain(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(None))
                printer.print("a\rb\nc")
                printer.print("x\fy\bz")
                self.assertEqual("a\rb\nc,x\fy\bz", sw.toString())
            finally:
                printer.close()

    def testEolEscaped(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(None).withEscape0('!'))
                printer.print("a\rb\nc")
                printer.print("x\fy\bz")
                self.assertEqual("a!rb!nc,x\fy\bz", sw.toString())
            except Exception as e:
                self.fail(f"Unexpected exception: {e}")

    def testDontQuoteEuroFirstChar(self) -> None:

            sw = StringWriter()
            with CSVPrinter(sw, CSVFormat.RFC4180) as printer:
                printer.printRecord1(EURO_CH, "Deux")
                self.assertEqual(EURO_CH + ",Deux" + recordSeparator, sw.toString())

    def testDisabledComment(self) -> None:

            sw = StringWriter()
            with CSVPrinter(sw, CSVFormat.DEFAULT) as printer:
                printer.printComment("This is a comment")
                self.assertEqual("", sw.toString())

    def testDelimiterStringEscaped(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.DEFAULT.builder().setDelimiter1("|||").setEscape0('!').setQuote1(None).build())
                printer.print("a|||b|||c")
                printer.print("xyz")
                self.assertEqual("a!|!|!|b!|!|!|c|||xyz", sw.toString())
            except Exception as e:
                self.fail("testDelimiterStringEscaped() failed with Exception: " + str(e))
            finally:
                sw.close()

    def testDelimiterPlain(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(None))
                printer.print("a,b,c")
                printer.print("xyz")
                self.assertEqual("a,b,c,xyz", sw.toString())
            except Exception as e:
                self.fail(f"Exception occurred: {e}")

    def testDelimiterEscaped(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.DEFAULT.withEscape0('!').withQuote1(None))
                printer.print("a,b,c")
                printer.print("xyz")
                self.assertEqual("a!,b!,c,xyz", sw.toString())
            except Exception as e:
                self.fail(f"Unexpected exception: {e}")

    def testDelimeterStringQuoteNone(self) -> None:

            sw = StringWriter()
            format = CSVFormat.DEFAULT.builder().setDelimiter1("[|]").setEscape0('!').setQuoteMode(QuoteMode.NONE).build()
            printer = CSVPrinter(sw, format)
            printer.print("a[|]b[|]c")
            printer.print("xyz")
            printer.print("a[xy]bc[]")
            self.assertEqual("a![!|!]b![!|!]c[|]xyz[|]a[xy]bc[]", sw.toString())
            printer.close()

    def testDelimeterStringQuoted(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.DEFAULT.builder().setDelimiter1("[|]").setQuote0('\'').build())
                printer.print("a[|]b[|]c")
                printer.print("xyz")
                self.assertEqual("'a[|]b[|]c'[|]xyz", sw.toString())
            except Exception as e:
                self.fail(f"Exception occurred: {e}")

    def testDelimeterQuoteNone(self) -> None:

            sw = StringWriter()
            format = CSVFormat.DEFAULT.withEscape0('!').withQuoteMode(QuoteMode.NONE)
            try:
                printer = CSVPrinter(sw, format)
                printer.print("a,b,c")
                printer.print("xyz")
                self.assertEqual("a!,b!,c,xyz", sw.toString())
            except Exception as e:
                self.fail(f"Unexpected error: {e}")

    def testDelimeterQuoted(self) -> None:

            sw = StringWriter()
            try:
                printer = CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0('\''))
                printer.print("a,b,c")
                printer.print("xyz")
                self.assertEqual("'a,b,c',xyz", sw.toString())
            except Exception as e:
                self.fail(f"Unexpected exception: {e}")

    def testCSV259(self) -> None:

            sw = StringWriter()
            with FileReader("src/test/resources/org/apache/commons/csv/CSV-259/sample.txt") as reader, CSVPrinter(sw, CSVFormat.DEFAULT.withEscape0('!').withQuote1(None)) as printer:
                printer.print(reader)
                self.assertEqual("x!,y!,z", sw.toString())

    def testCSV135(self) -> None:

            list = ["\"\"", "\\\\", "\\\"\\"]
            self.__tryFormat(list, None, None, "\"\",\\\\,\\\"\\")
            self.__tryFormat(list, '"', None, "\"\"\"\"\"\",\\\\,\"\\\"\"\\\"")
            self.__tryFormat(list, None, '\\', "\"\",\\\\\\\\,\\\\\"\\\\")
            self.__tryFormat(list, '"', '\\', "\"\\\"\\\"\",\"\\\\\\\\\",\"\\\\\\\"\\\\\"")
            self.__tryFormat(list, '"', '"', "\"\"\"\"\"\",\\\\,\"\\\"\"\\\"")

    def testCRComment(self) -> None:

            sw = StringWriter()
            value = "abc"
            try:
                printer = CSVPrinter(sw, CSVFormat.DEFAULT.withCommentMarker0('#'))
                printer.print(value)
                printer.printComment("This is a comment\r\non multiple lines\rthis is next comment\r")
                self.assertEqual(
                    "abc"
                    + self.__recordSeparator
                    + "# This is a comment"
                    + self.__recordSeparator
                    + "# on multiple lines"
                    + self.__recordSeparator
                    + "# this is next comment"
                    + self.__recordSeparator
                    + "# "
                    + self.__recordSeparator,
                    sw.toString()
                )
            finally:
                printer.close()

    def __tryFormat(self, list: typing.List[str], quote: str, escape: str, expected: str) -> None:

        format = CSVFormat.DEFAULT.withQuote1(quote).withEscape1(escape).withRecordSeparator1(None)
        out = StringBuilder()
        with CSVPrinter(out, format) as printer:
            printer.printRecord0(list)
        self.assertEqual(expected, out.toString())

    def __toFirstRecordValues(self, expected: str, format: CSVFormat) -> typing.List[str]:

            try:
                with CSVParser.parse4(expected, format) as parser:
                    return parser.getRecords()[0].values()
            except Exception as e:
                raise e

    def __randStr(self) -> str:

            r = random.Random()
            sz = r.randint(0, 20)
            buf = [None] * sz
            for i in range(sz):
                what = r.randint(0, 20)
                if what == 0:
                    ch = '\r'
                elif what == 1:
                    ch = '\n'
                elif what == 2:
                    ch = '\t'
                elif what == 3:
                    ch = '\f'
                elif what == 4:
                    ch = ' '
                elif what == 5:
                    ch = ','
                elif what == 6:
                    ch = self.__DQUOTE_CHAR
                elif what == 7:
                    ch = '\''
                elif what == 8:
                    ch = __BACKSLASH
                else:
                    ch = chr(r.randint(0, 300))
                buf[i] = ch
            return ''.join(buf)

    def __generateLines(self, nLines: int, nCol: int) -> typing.List[typing.List[str]]:

            lines = [[self.__randStr() for _ in range(nCol)] for _ in range(nLines)]
            return lines

    def __expectNulls(self, original: typing.List[typing.Any], csvFormat: CSVFormat) -> typing.List[typing.Any]:

            fixed = original.copy()
            for i in range(len(fixed)):
                if fixed[i] == csvFormat.getNullString():
                    fixed[i] = None
            return fixed

    def __doRandom(self, format: CSVFormat, iter: int) -> None:

            for i in range(iter):
                self.__doOneRandom(format)

    def __doOneRandom(self, format: CSVFormat) -> None:

        r = Random()
        nLines = r.nextInt(4) + 1
        nCol = r.nextInt(3) + 1
        lines = self.__generateLines(nLines, nCol)
        sw = StringWriter()
        with CSVPrinter(sw, format) as printer:
            for i in range(nLines):
                printer.printRecord1(lines[i])
            printer.flush()
        result = sw.toString()
        with CSVParser.parse4(result, format) as parser:
            parseResult = parser.getRecords()
            expected = lines.clone()
            for i in range(len(expected)):
                expected[i] = self.__expectNulls(expected[i], format)
            Utils.compare(f"Printer output :{self.__printable(result)}", expected, parseResult)

    def __createTempPath(self) -> Path:

            return Path(tempfile.mkstemp(suffix=".csv", prefix=self.__class__.__name__))

    def __createTempFile(self) -> pathlib.Path:

            return self.__createTempPath().to_file()

    @staticmethod

    def __printable(s: str) -> str:


        pass # LLM could not translate method body

    # Class Methods End


