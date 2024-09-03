import pytest

from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVPrinter import *
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.Constants import *
from src.test.org.apache.commons.csv.Utils import *
import unittest
from io import StringIO
from pathlib import Path
import locale
from urllib.parse import urlparse

class CSVParserTest(unittest.TestCase):

    __UTF_8 = 'utf-8'

    __UTF_8_NAME = 'utf-8'

    __CSV_INPUT = "a,b,c,d\n" +\
        " a , b , 1 2 \n" +\
        "\"foo baar\", b,\n" +\
        "   \"foo\n,,\n\"\",,\n\"\"\",d,e\n"

    __CSV_INPUT_1 = "a,b,c,d"

    __CSV_INPUT_2 = "a,b,1 2"

    __RESULT = [
        ["a", "b", "c", "d"],
        ["a", "b", "1 2"],
        ["foo baar", "b", ""],
        ["foo\n,,\n\",,\n\"", "d", "e"]
    ]

    __CSV_INPUT_NO_COMMENT = "A,B" + Constants.CRLF + "1,2" + Constants.CRLF

    __CSV_INPUT_HEADER_COMMENT = "# header comment" +\
        Constants.CRLF +\
        "A,B" +\
        Constants.CRLF +\
        "1,2" +\
        Constants.CRLF

    __CSV_INPUT_HEADER_TRAILER_COMMENT = "# header comment" +\
        Constants.CRLF +\
        "A,B" +\
        Constants.CRLF +\
        "1,2" +\
        Constants.CRLF +\
        "# comment"

    __CSV_INPUT_MULTILINE_HEADER_TRAILER_COMMENT = "# multi-line" +\
        Constants.CRLF +\
        "# header comment" +\
        Constants.CRLF +\
        "A,B" +\
        Constants.CRLF +\
        "1,2" +\
        Constants.CRLF +\
        "# multi-line" +\
        Constants.CRLF +\
        "# comment"

    
    def __parse(self, parser, failParseRecordNo) -> CSVRecord:
        try:
            if parser.getRecordNumber() + 1 == failParseRecordNo:
                with self.assertRaises((IOError, OSError)):
                    parser.nextRecord()
                return None
            return parser.nextRecord()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred in `__parse()`: {e}")

    
    def __parseFully(self, parser) -> None:
        parserIterator = parser.iterator()
        while True:
            try:
                record = parserIterator.next()
                self.assertIsNotNone(record)
            except StopIteration:
                break

    
    @pytest.mark.test
    def testBackslashEscaping(self) -> None:
        try:
            code = "one,two,three\n" +\
                "'',''\n" +\
                "/',/'\n" +\
                "'/'','/''\n" +\
                "'''',''''\n" +\
                "/,,/,\n" +\
                "//,//\n" +\
                "'//','//'\n" +\
                "   8   ,   \"quoted \"\" /\" // string\"   \n" +\
                "9,   /\n   \n" +\
                ""
            res = [
                ["one", "two", "three"],
                ["", ""],
                ["'", "'"],
                ["'", "'"],
                ["'", "'"],
                [",", ","],
                ["/", "/"],
                ["/", "/"],
                ["   8   ", "   \"quoted \"\" /\" / string\"   "],
                ["9", "   \n   "]
            ]

            format = CSVFormat.newFormat(',')\
                .withQuote0('\'')\
                .withRecordSeparator1(Constants.CRLF)\
                .withEscape0('/')\
                .withIgnoreEmptyLines0()

            parser = CSVParser.parse4(code, format)
            try:
                records = parser.getRecords()
                self.assertFalse(len(records) == 0)

                Utils.compare("Records do not match expected result", res, records)
            finally:
                parser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")
    

    @pytest.mark.test
    def testBackslashEscaping2(self) -> None:
        try:
            code = "" +\
                " , , \n" +\
                " \t ,  , \n" +\
                " // , /, , /,\n"
            res = [
                [" ", " ", " "],
                [" \t ", "  ", " "],
                [" / ", " , ", " ,"],
            ]

            format = CSVFormat.newFormat(',')\
                .withRecordSeparator1(Constants.CRLF)\
                .withEscape0('/')\
                .withIgnoreEmptyLines0()

            parser = CSVParser.parse4(code, format)
            try:
                records = parser.getRecords()
                self.assertFalse(len(records) == 0)

                Utils.compare("", res, records)
            finally:
                parser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @unittest.skip("Disabled")
    @pytest.mark.test
    def testBackslashEscapingOld(self) -> None:
        try:
            code = "one,two,three\n" +\
                "on\\\"e,two\n" +\
                "on\"e,two\n" +\
                "one,\"tw\\\"o\"\n" +\
                "one,\"t\\,wo\"\n" +\
                "one,two,\"th,ree\"\n" +\
                "\"a\\\\\"\n" +\
                "a\\,b\n" +\
                "\"a\\\\,b\""
            res = [
                ["one", "two", "three"],
                ["on\\\"e", "two"],
                ["on\"e", "two"],
                ["one", "tw\"o"],
                ["one", "t\\,wo"],
                ["one", "two", "th,ree"],
                ["a\\\\"],
                ["a\\", "b"],
                ["a\\\\,b"]
            ]
            parser = CSVParser.parse4(code, CSVFormat.DEFAULT)
            try:
                records = parser.getRecords()
                self.assertEqual(len(res), len(records))
                self.assertFalse(len(records) == 0)
                for i in range(len(res)):
                    self.assertEqual(res[i], records[i].values())
            finally:
                parser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testCarriageReturnEndings(self) -> None:
        try:
            code = "foo\rbaar,\rhello,world\r,kanu"
            parser = CSVParser.parse4(code, CSVFormat.DEFAULT)
            try:
                records = parser.getRecords()
                self.assertEqual(4, len(records))
            finally:
                parser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testCarriageReturnLineFeedEndings(self) -> None:
        try:
            code = "foo\r\nbaar,\r\nhello,world\r\n,kanu"
            parser = CSVParser.parse4(code, CSVFormat.DEFAULT)
            try:
                records = parser.getRecords()
                self.assertEqual(4, len(records))
            finally:
                parser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")
    

    @pytest.mark.test
    def testCSV141CSVFormat_DEFAULT(self) -> None:
        try:
            self.__testCSV141Failure(CSVFormat.DEFAULT, 3)
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testCSV141CSVFormat_INFORMIX_UNLOAD(self) -> None:
        try:
            self.__testCSV141Failure(CSVFormat.INFORMIX_UNLOAD, 1)
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")
    

    @pytest.mark.test
    def testCSV141CSVFormat_INFORMIX_UNLOAD_CSV(self) -> None:
        try:
            self.__testCSV141Failure(CSVFormat.INFORMIX_UNLOAD_CSV, 3)
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")
    
    
    @pytest.mark.test
    def testCSV141CSVFormat_ORACLE(self) -> None:
        try:
            self.__testCSV141Failure(CSVFormat.ORACLE, 2)
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testCSV141CSVFormat_POSTGRESQL_CSV(self) -> None:
        try:
            self.__testCSV141Failure(CSVFormat.POSTGRESQL_CSV, 3)
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @unittest.skip("Disabled - PR 295 does not work")
    @pytest.mark.test
    def testCSV141Excel(self) -> None:
        try:
            self.__testCSV141Ok(CSVFormat.EXCEL)
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    def __testCSV141Failure(self, format, failParseRecordNo) -> None:
        try:
            path = Path(__file__).resolve()\
                .parent.parent.parent.parent\
                .parent / 'resources' / 'org' /\
                'apache' / 'commons' / 'csv' / 'CSV-141' / 'csv-141.csv'
            parser = CSVParser.parse2(path, 'utf-8', format)
            try:
                record = self.__parse(parser, failParseRecordNo)
                if (record == None):
                    return
                self.assertEqual("1414770317901", record.get1(0))
                self.assertEqual("android.widget.EditText", record.get1(1))
                self.assertEqual("pass sem1 _84*|*", record.get1(2))
                self.assertEqual("0", record.get1(3))
                self.assertEqual("pass sem1 _8", record.get1(4))
                self.assertEqual(5, record.size())
                record = self.__parse(parser, failParseRecordNo)
                if (record == None):
                    return
                self.assertEqual("1414770318470", record.get1(0))
                self.assertEqual("android.widget.EditText", record.get1(1))
                self.assertEqual("pass sem1 _84:|", record.get1(2))
                self.assertEqual("0", record.get1(3))
                self.assertEqual("pass sem1 _84:\\", record.get1(4))
                self.assertEqual(5, record.size())
                with self.assertRaises((IOError, OSError)):
                    parser.nextRecord()
            finally:
                parser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred in `__testCSV141Failure()`: {e}")
    

    def __testCSV141Ok(self, format) -> None:
        try:
            path = Path(__file__).resolve()\
                .parent.parent.parent.parent\
                .parent / 'resources' / 'org' /\
                'apache' / 'commons' / 'csv' / 'CSV-141' / 'csv-141.csv'
            parser = CSVParser.parse2(path, 'utf-8', format)
            try:
                record = parser.nextRecord()
                self.assertEqual("1414770317901", record.get1(0))
                self.assertEqual("android.widget.EditText", record.get1(1))
                self.assertEqual("pass sem1 _84*|*", record.get1(2))
                self.assertEqual("0", record.get1(3))
                self.assertEqual("pass sem1 _8", record.get1(4))
                self.assertEqual(5, record.size())
                record = parser.nextRecord()
                self.assertEqual("1414770318470", record.get1(0))
                self.assertEqual("android.widget.EditText", record.get1(1))
                self.assertEqual("pass sem1 _84:|", record.get1(2))
                self.assertEqual("0", record.get1(3))
                self.assertEqual("pass sem1 _84:\\", record.get1(4))
                self.assertEqual(5, record.size())
                record = parser.nextRecord()
                self.assertEqual("1414770318327", record.get1(0))
                self.assertEqual("android.widget.EditText", record.get1(1))
                self.assertEqual("pass sem1", record.get1(2))
                self.assertEqual(3, record.size())
                record = parser.nextRecord()
                self.assertEqual("1414770318628", record.get1(0))
                self.assertEqual("android.widget.EditText", record.get1(1))
                self.assertEqual("pass sem1 _84*|*", record.get1(2))
                self.assertEqual("0", record.get1(3))
                self.assertEqual("pass sem1", record.get1(4))
                self.assertEqual(5, record.size())
            finally:
                parser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred in `__testCSV1410k()`: {e}")
    

    @pytest.mark.test
    def testCSV141RFC4180(self) -> None:
        try:
            self.__testCSV141Failure(CSVFormat.RFC4180, 3)
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")
    

    @pytest.mark.test
    def testCSV235(self) -> None:
        try:
            dqString = "\"aaa\",\"b\"\"bb\",\"ccc\""
            parser = CSVFormat.RFC4180.parse(StringIO(dqString))
            try:
                records = parser.iterator()
                record = next(records)
                self.assertFalse(records.hasNext())
                self.assertEqual(3, record.size())
                self.assertEqual("aaa", record.get1(0))
                self.assertEqual("b\"bb", record.get1(1))
                self.assertEqual("ccc", record.get1(2))
            finally:
                parser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")
    

    @pytest.mark.test
    def testCSV57(self) -> None:
        try:
            parser = CSVParser.parse4("", CSVFormat.DEFAULT)
            try:
                recordList = parser.getRecords()
                self.assertIsNotNone(recordList)
                self.assertEqual(0, len(recordList))
            finally:
                parser.close()
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")
    

    @pytest.mark.test
    def testDefaultFormat(self) -> None:
        try:
            code = "" +\
                "a,b#\n" +\
                "\"\n\",\" \",#\n" +\
                "#,\"\"\n" +\
                "# Final comment\n"
            res = [
                ["a", "b#"],
                ["\n", " ", "#"],
                ["#", ""],
                ["# Final comment"]
            ]

            format = CSVFormat.DEFAULT
            self.assertFalse(format.isCommentMarkerSet())
            res_comments = [
                ["a", "b#"],
                ["\n", " ", "#"]
            ]

            parser = CSVParser.parse4(code, format)
            try:
                records = parser.getRecords()
                self.assertFalse(len(records) == 0)

                Utils.compare("Failed to parse without comments", res, records)

                format = CSVFormat.DEFAULT.withCommentMarker0('#')
            finally:
                parser.close()
            

            parser = CSVParser.parse4(code, format)
            try:
                records = parser.getRecords()

                Utils.compare("Failed to parse with comments", res_comments, records)
            finally:
                parser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")
    

    @pytest.mark.test
    def testEmptyFile(self) -> None:
        try:
            path = Path(__file__).resolve()\
                .parent.parent.parent.parent\
                .parent / 'resources' / 'org' /\
                'apache' / 'commons' / 'csv' / 'empty.txt'
            parser = CSVParser.parse2(
                path,
                'utf-8',
                CSVFormat.DEFAULT
            )
            try:
                self.assertIsNone(parser.nextRecord())
            finally:
                parser.close()
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")
    

    @pytest.mark.test
    def testEmptyLineBehaviorCSV(self) -> None:
        try:
            codes = [
                "hello,\r\n\r\n\r\n",
                "hello,\n\n\n",
                "hello,\"\"\r\n\r\n\r\n",
                "hello,\"\"\n\n\n"
            ]
            res = [["hello", ""]]
            for code in codes:
                parser = CSVParser.parse4(code, CSVFormat.DEFAULT)
                try:
                    records = parser.getRecords()
                    self.assertEqual(len(res), len(records))
                    self.assertFalse(len(records) == 0)
                    for i in range(len(res)):
                        self.assertEqual(res[i], records[i].values())
                finally:
                    parser.close()
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testEmptyLineBehaviorExcel(self) -> None:
        try:
            codes = [
                "hello,\r\n\r\n\r\n",
                "hello,\n\n\n",
                "hello,\"\"\r\n\r\n\r\n",
                "hello,\"\"\n\n\n"
            ]
            res = [
                ["hello", ""],
                [""],
                [""]
            ]
            for code in codes:
                parser = CSVParser.parse4(code, CSVFormat.EXCEL)
                try:
                    records = parser.getRecords()
                    self.assertEqual(len(res), len(records))
                    self.assertFalse(len(records) == 0)
                    for i in range(len(res)):
                        self.assertEqual(res[i], records[i].values())
                finally:
                    parser.close()
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testEmptyString(self) -> None:
        try:
            parser = CSVParser.parse4("", CSVFormat.DEFAULT)
            try:
                self.assertIsNone(parser.nextRecord())
            finally:
                parser.close()
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")
    

    @pytest.mark.test
    def testEndOfFileBehaviorCSV(self) -> None:
        try:
            codes = [
                "hello,\r\n\r\nworld,\r\n",
                "hello,\r\n\r\nworld,",
                "hello,\r\n\r\nworld,\"\"\r\n",
                "hello,\r\n\r\nworld,\"\"",
                "hello,\r\n\r\nworld,\n",
                "hello,\r\n\r\nworld,",
                "hello,\r\n\r\nworld,\"\"\n",
                "hello,\r\n\r\nworld,\"\""
            ]
            res = [
                ["hello", ""],
                ["world", ""]
            ]
            for code in codes:
                parser = CSVParser.parse4(code, CSVFormat.DEFAULT)
                try:
                    records = parser.getRecords()
                    self.assertEqual(len(res), len(records))
                    self.assertFalse(len(records) == 0)
                    for i in range(len(res)):
                        self.assertEqual(res[i], records[i].values())
                finally:
                    parser.close()
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")
    

    @pytest.mark.test
    def testEndOfFileBehaviorExcel(self) -> None:
        try:
            codes = [
                "hello,\r\n\r\nworld,\r\n",
                "hello,\r\n\r\nworld,",
                "hello,\r\n\r\nworld,\"\"\r\n",
                "hello,\r\n\r\nworld,\"\"",
                "hello,\r\n\r\nworld,\n",
                "hello,\r\n\r\nworld,",
                "hello,\r\n\r\nworld,\"\"\n",
                "hello,\r\n\r\nworld,\"\""
            ]
            res = [
                ["hello", ""],
                [""],
                ["world", ""]
            ]
            for code in codes:
                parser = CSVParser.parse4(code, CSVFormat.EXCEL)
                try:
                    records = parser.getRecords()
                    self.assertEqual(len(res), len(records))
                    self.assertFalse(len(records) == 0)
                    for i in range(len(res)):
                        self.assertEqual(res[i], records[i].values())
                finally:
                    parser.close()
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")
    

    @pytest.mark.test
    def testExcelFormat1(self) -> None:
        try:
            code = "value1,value2,value3,value4\r\na,b,c,d\r\n  x,,," +\
                "\r\n\r\n\"\"\"hello\"\"\",\"  \"\"world\"\"\",\"abc\ndef\",\r\n"
            res = [
                ["value1", "value2", "value3", "value4"],
                ["a", "b", "c", "d"],
                ["  x", "", "", ""],
                [""],
                ["\"hello\"", "  \"world\"", "abc\ndef", ""]
            ]
            parser = CSVParser.parse4(code, CSVFormat.EXCEL)
            try:
                records = parser.getRecords()
                self.assertEqual(len(res), len(records))
                self.assertFalse(len(records) == 0)
                for i in range(len(res)):
                    self.assertEqual(res[i], records[i].values())
            finally:
                parser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testExcelFormat2(self) -> None:
        try:
            code = "foo,baar\r\n\r\nhello,\r\n\r\nworld,\r\n"
            res = [
                ["foo", "baar"],
                [""],
                ["hello", ""],
                [""],
                ["world", ""]
            ]
            parser = CSVParser.parse4(code, CSVFormat.EXCEL)
            try:
                records = parser.getRecords()
                self.assertEqual(len(res), len(records))
                self.assertFalse(len(records) == 0)
                for i in range(len(res)):
                    self.assertEqual(res[i], records[i].values())
            finally:
                parser.close()
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")
    

    @pytest.mark.test
    def testFirstEndOfLineCr(self) -> None:
        try:
            data = "foo\rbaar,\rhello,world\r,kanu"
            parser = CSVParser.parse4(data, CSVFormat.DEFAULT)
            try:
                records = parser.getRecords()
                self.assertEqual(4, len(records))
                self.assertEqual("\r", parser.getFirstEndOfLine())
            finally:
                parser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")
    

    @pytest.mark.test
    def testFirstEndOfLineCrLf(self) -> None:
        try:
            data = "foo\r\nbaar,\r\nhello,world\r\n,kanu"
            parser = CSVParser.parse4(data, CSVFormat.DEFAULT)
            try:
                records = parser.getRecords()
                self.assertEqual(4, len(records))
                self.assertEqual("\r\n", parser.getFirstEndOfLine())
            finally:
                parser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")
    

    @pytest.mark.test
    def testFirstEndOfLineLf(self) -> None:
        try:
            data = "foo\nbaar,\nhello,world\n,kanu"
            parser = CSVParser.parse4(data, CSVFormat.DEFAULT)
            try:
                records = parser.getRecords()
                self.assertEqual(4, len(records))
                self.assertEqual("\n", parser.getFirstEndOfLine())
            finally:
                parser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testForEach(self) -> None:
        try:
            inStream = StringIO("a,b,c\n1,2,3\nx,y,z")
            parser = CSVFormat.DEFAULT.parse(inStream)
            try:
                records = []
                parserIterator = parser.iterator()
                while True:
                    try:
                        record = next(parserIterator)
                        records.append(record)
                    except StopIteration:
                        break
                self.assertEqual(3, len(records))
                self.assertEqual(
                    ["a", "b", "c"],
                    records[0].values()
                )
                self.assertEqual(
                    ["1", "2", "3"],
                    records[1].values()
                )
                self.assertEqual(
                    ["x", "y", "z"],
                    records[2].values()
                )
            finally:
                parser.close()
                inStream.close()
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

        
    @pytest.mark.test
    def testGetLine(self) -> None:
        try:
            parser = CSVParser.parse4(
                CSVParserTest.__CSV_INPUT,
                CSVFormat.DEFAULT.withIgnoreSurroundingSpaces0()
            )
            try:
                for re in CSVParserTest.__RESULT:
                    self.assertEqual(re, parser.nextRecord().values())
                
                self.assertIsNone(parser.nextRecord())
            finally:
                parser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")
    

    @pytest.mark.test
    def testGetLineNumberWithCR(self) -> None:
        try:
            self.__validateLineNumbers(str(Constants.CR))
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")
    

    @pytest.mark.test
    def testGetLineNumberWithCRLF(self) -> None:
        try:
            self.__validateLineNumbers(Constants.CRLF)
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testGetLineNumberWithLF(self) -> None:
        try:
            self.__validateLineNumbers(str(Constants.LF))
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testGetOneLine(self) -> None:
        try:
            parser = CSVParser.parse4(
                CSVParserTest.__CSV_INPUT_1,
                CSVFormat.DEFAULT
            )
            try:
                record = parser.getRecords()[0]
                self.assertEqual(
                    CSVParserTest.__RESULT[0],
                    record.values()
                )
            finally:
                parser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testGetOneLineOneParser(self) -> None:
        format = CSVFormat.DEFAULT
        writer = StringIO()
        parser = CSVParser.CSVParser1(
            writer, format
        )
        writePos = 0
        readPos = 0
        try:
            writer.seek(writePos)
            writer.write(CSVParserTest.__CSV_INPUT_1)
            writer.write(format.getRecordSeparator())
            writePos = writer.tell()
            writer.seek(readPos)
            record1 = parser.nextRecord()
            readPos = writer.tell()
            self.assertEqual(CSVParserTest.__RESULT[0], record1.values())
            writer.seek(writePos)
            writer.write(CSVParserTest.__CSV_INPUT_2)
            writer.write(format.getRecordSeparator())
            writePos = writer.tell()
            writer.seek(readPos)
            record2 = parser.nextRecord()
            readPos = writer.tell()
            self.assertEqual(CSVParserTest.__RESULT[1], record2.values())
        finally:
            writer.close()
            parser.close()

    
    @pytest.mark.test
    def testGetRecordNumberWithCR(self) -> None:
        try:
            self.__validateRecordNumbers(str(Constants.CR))
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testGetRecordNumberWithCRLF(self) -> None:
        try:
            self.__validateRecordNumbers(Constants.CRLF)
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")
    

    @pytest.mark.test
    def testGetRecordNumberWithLF(self) -> None:
        try:
            self.__validateRecordNumbers(str(Constants.LF))
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testGetRecordPositionWithCRLF(self) -> None:
        try:
            self.__validateRecordPosition(Constants.CRLF)
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")
    

    @pytest.mark.test
    def testGetRecordPositionWithLF(self) -> None:
        try:
            self.__validateRecordPosition(str(Constants.LF))
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testGetRecords(self) -> None:
        try:
            parser = CSVParser.parse4(
                CSVParserTest.__CSV_INPUT,
                CSVFormat.DEFAULT.withIgnoreSurroundingSpaces0()
            )
            try:
                records = parser.getRecords()
                self.assertEqual(
                    len(CSVParserTest.__RESULT),
                    len(records)
                )
                self.assertFalse(len(records) == 0)
                for i in range(len(CSVParserTest.__RESULT)):
                    self.assertEqual(
                        CSVParserTest.__RESULT[i],
                        records[i].values()
                    )
            finally:
                parser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")
    

    @pytest.mark.test
    def testGetRecordWithMultiLineValues(self) -> None:
        try:
            parser = CSVParser.parse4(
                "\"a\r\n1\",\"a\r\n2\"" +\
                    Constants.CRLF +\
                    "\"b\r\n1\",\"b\r\n2\"" +\
                    Constants.CRLF +\
                    "\"c\r\n1\",\"c\r\n2\"",
                CSVFormat.DEFAULT.withRecordSeparator1(Constants.CRLF)
            )
            try:
                self.assertEqual(0, parser.getRecordNumber())
                self.assertEqual(0, parser.getCurrentLineNumber())
                record = parser.nextRecord()
                self.assertIsNotNone(record)
                self.assertEqual(3, parser.getCurrentLineNumber())
                self.assertEqual(1, record.getRecordNumber())
                self.assertEqual(1, parser.getRecordNumber())
                record = parser.nextRecord()
                self.assertIsNotNone(record)
                self.assertEqual(6, parser.getCurrentLineNumber())
                self.assertEqual(2, record.getRecordNumber())
                self.assertEqual(2, parser.getRecordNumber())
                record = parser.nextRecord()
                self.assertIsNotNone(record)
                self.assertEqual(9, parser.getCurrentLineNumber())
                self.assertEqual(3, record.getRecordNumber())
                self.assertEqual(3, parser.getRecordNumber())
                record = parser.nextRecord()
                self.assertIsNone(record)
                self.assertEqual(9, parser.getCurrentLineNumber())
                self.assertEqual(3, parser.getRecordNumber())
            finally:
                parser.close()
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")
    

    @pytest.mark.test
    def testIgnoreEmptyLines(self) -> None:
        try:
            code = "\nfoo,baar\n\r\n,\n\n,world\r\n\n"
            parser = CSVParser.parse4(code, CSVFormat.DEFAULT)
            try:
                records = parser.getRecords()
                self.assertEqual(3, len(records))
            finally:
                parser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")
    

    @pytest.mark.test
    def testInvalidFormat(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT.withDelimiter(Constants.CR)


    @pytest.mark.test
    def testIterator(self) -> None:
        try:
            inStream = StringIO("a,b,c\n1,2,3\nx,y,z")

            parser = CSVFormat.DEFAULT.parse(inStream)
            try:
                iterator = parser.iterator()

                self.assertTrue(iterator.hasNext())
                with self.assertRaises((RuntimeError, NotImplementedError, NameError)):
                    iterator.remove()
                self.assertEqual(
                    ["a", "b", "c"],
                    next(iterator).values()
                )
                self.assertEqual(
                    ["1", "2", "3"],
                    next(iterator).values()
                )
                self.assertTrue(iterator.hasNext())
                self.assertTrue(iterator.hasNext())
                self.assertTrue(iterator.hasNext())
                self.assertEqual(
                    ["x", "y", "z"],
                    next(iterator).values()
                )
                self.assertFalse(iterator.hasNext())

                with self.assertRaises(StopIteration):
                    next(iterator)
            finally:
                parser.close()
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")


    @pytest.mark.test
    def testIteratorSequenceBreaking(self) -> None:
        try:
            fiveRows = "1\n2\n3\n4\n5\n"

            parser = CSVFormat.DEFAULT.parse(StringIO(fiveRows))

            try:
                iterator = parser.iterator()
                recordNumber = 0
                while iterator.hasNext():
                    record = next(iterator)
                    recordNumber += 1
                    self.assertEqual(
                        str(recordNumber),
                        record.get1(0)
                    )
                    if (recordNumber >= 2):
                        break
                iterator.hasNext()
                while iterator.hasNext():
                    record = next(iterator)
                    recordNumber += 1
                    self.assertEqual(
                        str(recordNumber),
                        record.get1(0)
                    )
            finally:
                parser.close()
            
            parser = CSVFormat.DEFAULT.parse(StringIO(fiveRows))

            try:
                recordNumber = 0
                iterator = parser.iterator()
                while True:
                    try:
                        record = next(iterator)
                        recordNumber += 1
                        self.assertEqual(str(recordNumber), record.get1(0))
                        if (recordNumber >= 2):
                            break
                    except StopIteration:
                        break
                while True:
                    try:
                        record = next(iterator)
                        recordNumber += 1
                        self.assertEqual(str(recordNumber), record.get1(0))
                    except StopIteration:
                        break
            finally:
                parser.close()
            

            parser = CSVFormat.DEFAULT.parse(StringIO(fiveRows))

            try:
                recordNumber = 0
                iterator = parser.iterator()
                while True:
                    try:
                        record = next(iterator)
                        recordNumber += 1
                        self.assertEqual(str(recordNumber), record.get1(0))
                        if (recordNumber >= 2):
                            break
                    except StopIteration:
                        break
                parser.iterator().hasNext()
                while True:
                    try:
                        record = next(iterator)
                        recordNumber += 1
                        self.assertEqual(str(recordNumber), record.get1(0))
                    except StopIteration:
                        break
            finally:
                parser.close()

        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testLineFeedEndings(self) -> None:
        try:
            code = "foo\nbaar,\nhello,world\n,kanu"
            parser = CSVParser.parse4(code, CSVFormat.DEFAULT)
            try:
                records = parser.getRecords()
                self.assertEqual(4, len(records))
            finally:
                parser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @unittest.skip("Disabled")
    @pytest.mark.test
    def testMongoDbCsv(self) -> None:
        try:
            parser = CSVParser.parse4(
                "\"a a\",b,c" + Constants.LF + "d,e,f",
                CSVFormat.MONGODB_CSV
            )
            try:
                itr1 = parser.iterator()
                itr2 = parser.iterator()

                first = itr1.next()
                self.assertEqual("a a", first.get1(0))
                self.assertEqual("b", first.get1(1))
                self.assertEqual("c", first.get1(2))

                second = itr2.next()
                self.assertEqual("d", second.get1(0))
                self.assertEqual("e", second.get1(1))
                self.assertEqual("f", second.get1(2))
            finally:
                parser.close()
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")
    
    
    @pytest.mark.test
    def testMultipleIterators(self) -> None:
        try:
            parser = CSVParser.parse4(
                "a,b,c" + Constants.CRLF + "d,e,f",
                CSVFormat.DEFAULT
            )
            try:
                itr1 = parser.iterator()

                first = next(itr1)
                self.assertEqual("a", first.get1(0))
                self.assertEqual("b", first.get1(1))
                self.assertEqual("c", first.get1(2))

                second = next(itr1)
                self.assertEqual("d", second.get1(0))
                self.assertEqual("e", second.get1(1))
                self.assertEqual("f", second.get1(2))
            finally:
                parser.close()
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testNewCSVParserNullReaderFormat(self) -> None:
        with self.assertRaises((TypeError, AttributeError, ValueError)):
            CSVParser.CSVParser1(None, CSVFormat.DEFAULT)

    
    @pytest.mark.test
    def testNewCSVParserReaderNullFormat(self) -> None:
        with self.assertRaises((TypeError, AttributeError, ValueError)):
            CSVParser.CSVParser1(StringIO(""), None)

    
    @pytest.mark.test
    def testNoHeaderMap(self) -> None:
        try:
            parser = CSVParser.parse4("a,b,c\n1,2,3\nx,y,z", CSVFormat.DEFAULT)
            try:
                self.assertIsNone(parser.getHeaderMap())
            finally:
                parser.close()
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testNotValueCSV(self) -> None:
        try:
            source = "#"
            csvFormat = CSVFormat.DEFAULT.withCommentMarker0('#')
            csvParser = csvFormat.parse(StringIO(source))
            try:
                csvRecord = csvParser.nextRecord()
                self.assertIsNone(csvRecord)
            finally:
                csvParser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testParseFileNullFormat(self) -> None:
        with self.assertRaises((TypeError, AttributeError, ValueError)):
            path = Path(__file__).resolve()\
                .parent.parent.parent.parent\
                .parent / 'resources' / 'org' /\
                'apache' / 'commons' / 'csv' / 'CSVFileParser' /\
                'test.csv'
            CSVParser.parse0(
                path,
                locale.getpreferredencoding(),
                None
            )

    
    @pytest.mark.test
    def testParseNullFileFormat(self) -> None:
        with self.assertRaises((TypeError, AttributeError, ValueError)):
            CSVParser.parse0(
                None,
                locale.getpreferredencoding(),
                CSVFormat.DEFAULT
            )
    

    @pytest.mark.test
    def testParseNullPathFormat(self) -> None:
        with self.assertRaises((TypeError, AttributeError, ValueError)):
            CSVParser.parse2(
                None,
                locale.getpreferredencoding(),
                CSVFormat.DEFAULT
            )

    
    @pytest.mark.test
    def testParseNullStringFormat(self) -> None:
        with self.assertRaises((TypeError, AttributeError, ValueError)):
            CSVParser.parse4(None, CSVFormat.DEFAULT)

    
    @pytest.mark.test
    def testParseNullUrlCharsetFormat(self) -> None:
        with self.assertRaises((TypeError, AttributeError, ValueError)):
            CSVParser.parse5(
                None,
                locale.getpreferredencoding(),
                CSVFormat.DEFAULT
            )


    @pytest.mark.test
    def testParserUrlNullCharsetFormat(self) -> None:
        with self.assertRaises((TypeError, AttributeError, ValueError)):
            CSVParser.parse5(
                urlparse("https://commons.apache.org"),
                None,
                CSVFormat.DEFAULT
            )

    
    @pytest.mark.test
    def testParseStringNullFormat(self) -> None:
        with self.assertRaises((TypeError, AttributeError, ValueError)):
            CSVParser.parse4("csv data", None)

    
    @pytest.mark.test
    def testParseUrlCharsetNullFormat(self) -> None:
        with self.assertRaises((TypeError, AttributeError, ValueError)):
            CSVParser.parse5(
                urlparse("https://commons.apache.org"),
                locale.getpreferredencoding(),
                None
            )
    

    @pytest.mark.test
    def testParseWithDelimiterStringWithEscape(self) -> None:
        try:
            source = "a![!|!]b![|]c[|]xyz\r\nabc[abc][|]xyz"
            csvFormat = CSVFormat.DEFAULT\
                .builder()\
                .setDelimiter1("[|]")\
                .setEscape0('!')\
                .build()
            csvParser = csvFormat.parse(StringIO(source))
            try:
                csvRecord = csvParser.nextRecord()
                self.assertEqual("a[|]b![|]c", csvRecord.get1(0))
                self.assertEqual("xyz", csvRecord.get1(1))
                csvRecord = csvParser.nextRecord()
                self.assertEqual("abc[abc]", csvRecord.get1(0))
                self.assertEqual("xyz", csvRecord.get1(1))
            finally:
                csvParser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testParseWithDelimiterStringWithQuote(self) -> None:
        try:
            source = "'a[|]b[|]c'[|]xyz\r\nabc[abc][|]xyz"
            csvFormat = CSVFormat.DEFAULT\
                .builder()\
                .setDelimiter1("[|]")\
                .setQuote0('\'')\
                .build()
            csvParser = csvFormat.parse(StringIO(source))
            try:
                csvRecord = csvParser.nextRecord()
                self.assertEqual("a[|]b[|]c", csvRecord.get1(0))
                self.assertEqual("xyz", csvRecord.get1(1))
                csvRecord = csvParser.nextRecord()
                self.assertEqual("abc[abc]", csvRecord.get1(0))
                self.assertEqual("xyz", csvRecord.get1(1))
            finally:
                csvParser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testParseWithDelimiterWithEscape(self) -> None:
        try:
            source = "a!,b!,c,xyz"
            csvFormat = CSVFormat.DEFAULT.withEscape0('!')
            csvParser = csvFormat.parse(StringIO(source))
            try:
                csvRecord = csvParser.nextRecord()
                self.assertEqual("a,b,c", csvRecord.get1(0))
                self.assertEqual("xyz", csvRecord.get1(1))
            finally:
                csvParser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testParseWithDelimiterWithQuote(self) -> None:
        try:
            source = "'a,b,c',xyz"
            csvFormat = CSVFormat.DEFAULT.withQuote0('\'')
            csvParser = csvFormat.parse(StringIO(source))
            try:
                csvRecord = csvParser.nextRecord()
                self.assertEqual("a,b,c", csvRecord.get1(0))
                self.assertEqual("xyz", csvRecord.get1(1))
            finally:
                csvParser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testParseWithQuoteThrowsException(self) -> None:
        csvFormat = CSVFormat.DEFAULT.withQuote0('\'')
        with self.assertRaises((IOError, OSError)):
            csvFormat.parse(StringIO("'a,b,c','")).nextRecord()
        with self.assertRaises((IOError, OSError)):
            csvFormat.parse(StringIO("'a,b,c'abc,xyz")).nextRecord()
        with self.assertRaises((IOError, OSError)):
            csvFormat.parse(StringIO("'abc'a,b,c',xyz")).nextRecord()
    

    @pytest.mark.test
    def testParseWithQuoteWithEscape(self) -> None:
        try:
            source = "'a?,b?,c?d',xyz"
            csvFormat = CSVFormat.DEFAULT.withQuote0('\'').withEscape0('?')
            csvParser = csvFormat.parse(StringIO(source))
            try:
                csvRecord = csvParser.nextRecord()
                self.assertEqual("a,b,c?d", csvRecord.get1(0))
                self.assertEqual("xyz", csvRecord.get1(1))
            finally:
                csvParser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")


    @pytest.mark.test
    def testRoundtrip(self) -> None:
        try:
            out = StringIO()
            data = "a,b,c\r\n1,2,3\r\nx,y,z\r\n"
            printer = CSVPrinter(out, CSVFormat.DEFAULT)
            parse = CSVParser.parse4(data, CSVFormat.DEFAULT)
            try:
                iterator = parse.iterator()
                while True:
                    try:
                        record = next(iterator)
                        printer.printRecord0(record)
                    except StopIteration:
                        break
                self.assertEqual(data, out.getvalue())
            finally:
                parse.close()
                printer.close()
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")
        

    @unittest.skip("Disabled")
    @pytest.mark.test
    def testStartWithEmptyLinesThenHeaders(self) -> None:
        try:
            codes = [
                "\r\n\r\n\r\nhello,\r\n\r\n\r\n",
                "hello,\n\n\n",
                "hello,\"\"\r\n\r\n\r\n",
                "hello,\"\"\n\n\n"
            ]
            res = [
                ["hello", ""],
                [""],
                [""]
            ]
            for code in codes:
                parser = CSVParser.parse4(code, CSVFormat.EXCEL)
                try:
                    records = parser.getRecords()
                    self.assertEqual(len(res), len(records))
                    self.assertFalse(len(records) == 0)
                    for i in range(len(res)):
                        self.assertEqual(res[i], records[i].values())
                finally:
                    parser.close()
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testStream(self) -> None:
        try:
            inStream = StringIO("a,b,c\n1,2,3\nx,y,z")
            parser = CSVFormat.DEFAULT.parse(inStream)
            try:
                streamList = list(parser.stream())
                self.assertFalse(len(streamList) == 0)
                self.assertEqual(
                    ["a", "b", "c"],
                    streamList[0].values()
                )
                self.assertEqual(
                    ["1", "2", "3"],
                    streamList[1].values()
                )
                self.assertEqual(
                    ["x", "y", "z"],
                    streamList[2].values()
                )
            finally:
                parser.close()
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")
    
    
    def __validateLineNumbers(self, lineSeparator) -> None:
        try:
            parser = CSVParser.parse4(
                "a" + lineSeparator + "b" + lineSeparator + "c",
                CSVFormat.DEFAULT.withRecordSeparator1(lineSeparator)
            )
            try:
                self.assertEqual(0, parser.getCurrentLineNumber())
                self.assertIsNotNone(parser.nextRecord())
                self.assertEqual(1, parser.getCurrentLineNumber())
                self.assertIsNotNone(parser.nextRecord())
                self.assertEqual(2, parser.getCurrentLineNumber())
                self.assertIsNotNone(parser.nextRecord())
                self.assertEqual(3, parser.getCurrentLineNumber())
                self.assertIsNone(parser.nextRecord())
                self.assertEqual(3, parser.getCurrentLineNumber())
            finally:
                parser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred in `__validateLineNumbers()`: {e}")


    def __validateRecordNumbers(self, lineSeparator) -> None:
        try:
            parser = CSVParser.parse4(
                "a" + lineSeparator + "b" + lineSeparator + "c",
                CSVFormat.DEFAULT.withRecordSeparator1(lineSeparator)
            )
            try:
                self.assertEqual(0, parser.getRecordNumber())
                record = parser.nextRecord()
                self.assertIsNotNone(record)
                self.assertEqual(1, record.getRecordNumber())
                self.assertEqual(1, parser.getRecordNumber())
                record = parser.nextRecord()
                self.assertIsNotNone(record)
                self.assertEqual(2, record.getRecordNumber())
                self.assertEqual(2, parser.getRecordNumber())
                record = parser.nextRecord()
                self.assertIsNotNone(record)
                self.assertEqual(3, record.getRecordNumber())
                self.assertEqual(3, parser.getRecordNumber())
                record = parser.nextRecord()
                self.assertIsNone(record)
                self.assertEqual(3, parser.getRecordNumber())
            finally:
                parser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred in `__validateRecordNumbers()`: {e}")

        
    def __validateRecordPosition(self, lineSeparator) -> None:
        try:
            nl = lineSeparator

            code = "a,b,c" +\
                lineSeparator +\
                "1,2,3" +\
                lineSeparator +\
                "'A" +\
                nl +\
                "A','B" +\
                nl +\
                "B',CC" +\
                lineSeparator +\
                "\u00c4,\u00d6,\u00dc" +\
                lineSeparator +\
                "EOF,EOF,EOF"

            format = CSVFormat.newFormat(',')\
                .withQuote0('\'')\
                .withRecordSeparator1(lineSeparator)
            parser = CSVParser.parse4(code, format)

            self.assertEqual(0, parser.getRecordNumber())

            record = parser.nextRecord()
            self.assertIsNotNone(record)
            self.assertEqual(1, record.getRecordNumber())
            self.assertEqual(code.find('a'), record.getCharacterPosition())

            record = parser.nextRecord()
            self.assertIsNotNone(record)
            self.assertEqual(2, record.getRecordNumber())
            self.assertEqual(code.find('1'), record.getCharacterPosition())

            record = parser.nextRecord()
            self.assertIsNotNone(record)
            positionRecord3 = record.getCharacterPosition()
            self.assertEqual(3, record.getRecordNumber())
            self.assertEqual(code.find("'A"), record.getCharacterPosition())
            self.assertEqual("A" + lineSeparator + "A", record.get1(0))
            self.assertEqual("B" + lineSeparator + "B", record.get1(1))
            self.assertEqual("CC", record.get1(2))

            record = parser.nextRecord()
            self.assertIsNotNone(record)
            self.assertEqual(4, record.getRecordNumber())
            self.assertEqual(code.find('\u00c4'), record.getCharacterPosition())

            record = parser.nextRecord()
            self.assertIsNotNone(record)
            self.assertEqual(5, record.getRecordNumber())
            self.assertEqual(code.find("EOF"), record.getCharacterPosition())

            parser.close()

            parser = CSVParser(
                StringIO(code[int(positionRecord3):]),
                format,
                positionRecord3,
                3
            )

            record = parser.nextRecord()
            self.assertIsNotNone(record)
            self.assertEqual(3, record.getRecordNumber())
            self.assertEqual(code.find("'A"), record.getCharacterPosition())
            self.assertEqual("A" + lineSeparator + "A", record.get1(0))
            self.assertEqual("B" + lineSeparator + "B", record.get1(1))
            self.assertEqual("CC", record.get1(2))

            record = parser.nextRecord()
            self.assertIsNotNone(record)
            self.assertEqual(4, record.getRecordNumber())
            self.assertEqual(code.find('\u00c4'), record.getCharacterPosition())
            self.assertEqual("\u00c4", record.get1(0))

            parser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred in `__validateRecordPosition()`: {e}")
