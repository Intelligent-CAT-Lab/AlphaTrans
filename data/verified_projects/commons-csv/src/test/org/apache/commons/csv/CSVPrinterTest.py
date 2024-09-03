import pytest

from src.test.org.apache.commons.csv.Utils import *
from src.main.org.apache.commons.csv.QuoteMode import *
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.CSVPrinter import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVFormat import *
import random
from pathlib import Path
import io
from typing import List, TypeVar, Union
import tempfile
import unittest
import copy
import sys
import locale

T = TypeVar('T')

class CSVPrinterTest(unittest.TestCase):

    __DQUOTE_CHAR = '"'
    __EURO_CH = '\u20AC'
    __ITERATIONS_FOR_RANDOM_TEST = 50000
    __QUOTE_CH = '\''

    __longText2 = None
    __recordSeparator = CSVFormat.DEFAULT.getRecordSeparator()

    
    @staticmethod
    def __printable(s) -> str:
        sb = []
        for ch in s:
            if ord(ch) <= 32 or ord(ch) >= 128:
                sb.append("(")
                sb.append(str(ord(ch)))
                sb.append(")")
            else:
                sb.append(ch)
        return ''.join(sb)

    
    def __createTempFile(self) -> Path:
        try:
            return self.__createTempPath()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred in `__createTempFile()`: {e}")

    
    def __createTempPath(self) -> Path:
        try:
            return Path(
                tempfile.mkstemp(
                    prefix = self.__class__.__name__,
                    suffix = ".csv"
                )[1]
            )
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred in `__createTempPath()`: {e}")

    
    def __doOneRandom(self, format) -> None:
        try:
            r = random.Random()

            nLines = r.randint(0, 3) + 1
            nCol = r.randint(0, 2) + 1
            lines = self.__generateLines(nLines, nCol)

            sw = io.StringIO()
            printer = CSVPrinter(sw, format)

            try:
                for i in range(nLines):
                    printer.printRecord1(lines[i])
                
                result = sw.getvalue()

                parser = CSVParser.parse4(result, format)

                try:
                    parseResult = parser.getRecords()

                    expected = copy.deepcopy(lines)
                    for i in range(len(expected)):
                        expected[i] = self.__expectNulls(expected[i], format)
                    Utils.compare(
                        "Printer output :" + CSVPrinterTest.__printable(result),
                        expected,
                        parseResult
                    )
                finally:
                    parser.close()
                
                printer.flush()
            finally:
                printer.close()
        except Exception as e:
            self.fail(f"An unexpected exception occurred in `__doOneRandom()`: {e}")

    
    def __doRandom(self, format, iter) -> None:
        try:
            for i in range(iter):
                self.__doOneRandom(format)
        except Exception as e:
            self.fail(f"An unexpected exception occurred in `__doRandom()`: {e}")

    
    def __expectNulls(self, original, csvFormat) -> List[Union[T, None]]:
        fixed = copy.deepcopy(original)
        for i in range(len(fixed)):
            if fixed[i] == csvFormat.getNullString():
                fixed[i] = None
        return fixed

    
    def __generateLines(self, nLines, nCol) -> List[List[str]]:
        lines = [None] * nLines
        for i in range(nLines):
            line = [None] * nCol
            lines[i] = line
            for j in range(nCol):
                line[j] = self.__randStr()
        return lines

    def __randStr(self) -> str:
        r = random.Random()

        sz = r.randint(0, 19)
        buf = ['\u0000'] * sz
        for i in range(sz):
            what = r.randint(0, 19)
            ch = {
                0: '\r',
                1: '\n',
                2: '\t',
                3: '\f',
                4: ' ',
                5: ',',
                6: CSVPrinterTest.__DQUOTE_CHAR,
                7: '\'',
                8: Constants.BACKSLASH
            }.get(what, chr(r.randint(0, 299)))
            if ch == '\xa0':
                ch = " "
            elif ch == '\x85':
                ch = "\n"
            buf[i] = ch
        return ''.join(buf)

    
    @pytest.mark.test
    def testCRComment(self) -> None:
        try:
            sw = io.StringIO()
            value = "abc"
            printer = CSVPrinter(sw, CSVFormat.DEFAULT.withCommentMarker0('#'))
            try:
                try:
                    printer.print(value)
                except AttributeError:
                    printer.print_(value)
                printer.printComment(
                    "This is a comment\r\non multiple lines\rthis is next comment\r"
                )
                self.assertEqual(
                    "abc" +\
                        self.__recordSeparator +\
                        "# This is a comment" +\
                        self.__recordSeparator +\
                        "# on multiple lines" +\
                        self.__recordSeparator +\
                        "# this is next comment" +\
                        self.__recordSeparator +\
                        "# " +\
                        self.__recordSeparator,
                    sw.getvalue()
                )
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")
    

    @pytest.mark.test
    def testCSV135(self) -> None:
        try:
            list_ = []
            list_.append("\"\"")
            list_.append("\\\\")
            list_.append("\\\"\\")
            self.__tryFormat(list_, None, None, "\"\",\\\\,\\\"\\")
            self.__tryFormat(list_, '"', None, "\"\"\"\"\"\",\\\\,\"\\\"\"\\\"")
            self.__tryFormat(list_, None, '\\', "\"\",\\\\\\\\,\\\\\"\\\\")
            self.__tryFormat(list_, '"', '\\', "\"\\\"\\\"\",\"\\\\\\\\\",\"\\\\\\\"\\\\\"")
            self.__tryFormat(list_, '"', '"', "\"\"\"\"\"\",\\\\,\"\\\"\"\\\"")
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testCSV259(self) -> None:
        try:
            sw = io.StringIO()
            path = Path(__file__).resolve()\
                .parent.parent.parent.parent\
                .parent / 'resources' / 'org' / 'apache' / 'commons' / 'csv' /\
                'CSV-259' / 'sample.txt'
            reader = open(path, "r")
            printer = CSVPrinter(
                sw,
                CSVFormat.DEFAULT.withEscape0('!').withQuote1(None)
            )
            try:
                try:
                    printer.print(reader)
                except AttributeError:
                    printer.print_(reader)
                self.assertEqual("x!,y!,z", sw.getvalue())
            finally:
                printer.close()
                reader.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testDelimeterQuoted(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0('\''))
            try:
                try:
                    printer.print("a,b,c")
                    printer.print("xyz")
                except AttributeError:
                    printer.print_("a,b,c")
                    printer.print_("xyz")
                self.assertEqual("'a,b,c',xyz", sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testDelimeterQuoteNone(self) -> None:
        try:
            sw = io.StringIO()
            format = CSVFormat.DEFAULT.withEscape0('!').withQuoteMode(QuoteMode.NONE)
            printer = CSVPrinter(sw, format)
            try:
                try:
                    printer.print("a,b,c")
                    printer.print("xyz")
                except AttributeError:
                    printer.print_("a,b,c")
                    printer.print_("xyz")
                self.assertEqual("a!,b!,c,xyz", sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testDelimeterStringQuoted(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(
                sw,
                CSVFormat.DEFAULT\
                    .builder()\
                    .setDelimiter1("[|]")\
                    .setQuote0('\'')\
                    .build()
            )
            try:
                try:
                    printer.print("a[|]b[|]c")
                    printer.print("xyz")
                except AttributeError:
                    printer.print_("a[|]b[|]c")
                    printer.print_("xyz")
                self.assertEqual("'a[|]b[|]c'[|]xyz", sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testDelimeterStringQuoteNone(self) -> None:
        try:
            sw = io.StringIO()
            format = CSVFormat.DEFAULT\
                .builder()\
                .setDelimiter1("[|]")\
                .setEscape0('!')\
                .setQuoteMode(QuoteMode.NONE)\
                .build()
            printer = CSVPrinter(sw, format)
            try:
                try:
                    printer.print("a[|]b[|]c")
                    printer.print("xyz")
                    printer.print("a[xy]bc[]")
                except AttributeError:
                    printer.print_("a[|]b[|]c")
                    printer.print_("xyz")
                    printer.print_("a[xy]bc[]")
                self.assertEqual(
                    "a![!|!]b![!|!]c[|]xyz[|]a[xy]bc[]",
                    sw.getvalue()
                )
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testDelimiterEscaped(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(
                sw,
                CSVFormat.DEFAULT.withEscape0('!').withQuote1(None)
            )
            try:
                try:
                    printer.print("a,b,c")
                    printer.print("xyz")
                except AttributeError:
                    printer.print_("a,b,c")
                    printer.print_("xyz")
                self.assertEqual("a!,b!,c,xyz", sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testDelimiterPlain(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(None))
            try:
                try:
                    printer.print("a,b,c")
                    printer.print("xyz")
                except AttributeError:
                    printer.print_("a,b,c")
                    printer.print_("xyz")
                self.assertEqual("a,b,c,xyz", sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testDelimiterStringEscaped(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(
                sw,
                CSVFormat.DEFAULT\
                    .builder()\
                    .setDelimiter1("|||")\
                    .setEscape0('!')\
                    .setQuote1(None)\
                    .build()
            )
            try:
                try:
                    printer.print("a|||b|||c")
                    printer.print("xyz")
                except AttributeError:
                    printer.print_("a|||b|||c")
                    printer.print_("xyz")
                self.assertEqual("a!|!|!|b!|!|!|c|||xyz", sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testDisabledComment(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.DEFAULT)
            try:
                printer.printComment("This is a comment")
                self.assertEqual("", sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testDontQuoteEuroFirstChar(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.RFC4180)
            try:
                try:
                    printer.printRecord1(CSVPrinterTest.__EURO_CH, "Deux")
                except TypeError:
                    printer.printRecord1([CSVPrinterTest.__EURO_CH, "Deux"])
                self.assertEqual(
                    CSVPrinterTest.__EURO_CH + ",Deux" + self.__recordSeparator,
                    sw.getvalue()
                )
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testEolEscaped(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(
                sw,
                CSVFormat.DEFAULT.withQuote1(None).withEscape0('!')
            )
            try:
                try:
                    printer.print("a\rb\nc")
                    printer.print("x\fy\bz")
                except AttributeError:
                    printer.print_("a\rb\nc")
                    printer.print_("x\fy\bz")
                self.assertEqual("a!rb!nc,x\fy\bz", sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testEolPlain(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(None))
            try:
                try:
                    printer.print("a\rb\nc")
                    printer.print("x\fy\bz")
                except AttributeError:
                    printer.print_("a\rb\nc")
                    printer.print_("x\fy\bz")
                self.assertEqual("a\rb\nc,x\fy\bz", sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testEolQuoted(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0('\''))
            try:
                try:
                    printer.print("a\rb\nc")
                    printer.print("x\by\fz")
                except AttributeError:
                    printer.print_("a\rb\nc")
                    printer.print_("x\by\fz")
                self.assertEqual("'a\rb\nc',x\by\fz", sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testEscapeBackslash1(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(
                sw,
                CSVFormat.DEFAULT.withQuote0(CSVPrinterTest.__QUOTE_CH)
            )
            try:
                try:
                    printer.print("\\")
                except AttributeError:
                    printer.print_("\\")
                self.assertEqual("\\", sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")


    @pytest.mark.test
    def testEscapeBackslash2(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(
                sw,
                CSVFormat.DEFAULT.withQuote0(CSVPrinterTest.__QUOTE_CH)
            )
            try:
                try:
                    printer.print("\\\r")
                except AttributeError:
                    printer.print_("\\\r")
                self.assertEqual("'\\\r'", sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testEscapeBackslash3(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(
                sw,
                CSVFormat.DEFAULT.withQuote0(CSVPrinterTest.__QUOTE_CH)
            )
            try:
                try:
                    printer.print("X\\\r")
                except AttributeError:
                    printer.print_("X\\\r")
                self.assertEqual("'X\\\r'", sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testEscapeBackslash4(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(
                sw,
                CSVFormat.DEFAULT.withQuote0(CSVPrinterTest.__QUOTE_CH)
            )
            try:
                try:
                    printer.print("\\\\")
                except AttributeError:
                    printer.print_("\\\\")
                self.assertEqual("\\\\", sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testEscapeBackslash5(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(
                sw,
                CSVFormat.DEFAULT.withQuote0(CSVPrinterTest.__QUOTE_CH)
            )
            try:
                try:
                    printer.print("\\\\")
                except AttributeError:
                    printer.print_("\\\\")
                self.assertEqual("\\\\", sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testEscapeNull1(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(None))
            try:
                try:
                    printer.print("\\")
                except AttributeError:
                    printer.print_("\\")
                self.assertEqual("\\", sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testEscapeNull2(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(None))
            try:
                try:
                    printer.print("\\\r")
                except AttributeError:
                    printer.print_("\\\r")
                self.assertEqual("\"\\\r\"", sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testEscapeNull3(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(None))
            try:
                try:
                    printer.print("X\\\r")
                except AttributeError:
                    printer.print_("X\\\r")
                self.assertEqual("\"X\\\r\"", sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testEscapeNull4(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(None))
            try:
                try:
                    printer.print("\\\\")
                except AttributeError:
                    printer.print_("\\\\")
                self.assertEqual("\\\\", sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testEscapeNull5(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(None))
            try:
                try:
                    printer.print("\\\\")
                except AttributeError:
                    printer.print_("\\\\")
                self.assertEqual("\\\\", sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testExcelPrintAllArrayOfArrays(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.EXCEL)
            try:
                printer.printRecords1(
                    [["r1c1", "r1c2"], ["r2c1", "r2c2"]]
                )
                self.assertEqual(
                    "r1c1,r1c2" +\
                        self.__recordSeparator +\
                        "r2c1,r2c2" +\
                        self.__recordSeparator,
                    sw.getvalue()
                )
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testExcelPrintAllArrayOfLists(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.EXCEL)
            try:
                printer.printRecords1(
                    [["r1c1", "r1c2"], ["r2c1", "r2c2"]]
                )
                self.assertEqual(
                    "r1c1,r1c2" +\
                        self.__recordSeparator +\
                        "r2c1,r2c2" +\
                        self.__recordSeparator,
                    sw.getvalue()
                )
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testExcelPrintAllIterableOfArrays(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.EXCEL)
            try:
                printer.printRecords0(
                    [["r1c1", "r1c2"], ["r2c1", "r2c2"]]
                )
                self.assertEqual(
                    "r1c1,r1c2" +\
                        self.__recordSeparator +\
                        "r2c1,r2c2" +\
                        self.__recordSeparator,
                    sw.getvalue()
                )
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testExcelPrintAllIterableOfLists(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.EXCEL)
            try:
                printer.printRecords0(
                    [["r1c1", "r1c2"], ["r2c1", "r2c2"]]
                )
                self.assertEqual(
                    "r1c1,r1c2" +\
                        self.__recordSeparator +\
                        "r2c1,r2c2" +\
                        self.__recordSeparator,
                    sw.getvalue()
                )
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testExcelPrinter1(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.EXCEL)
            try:
                try:
                    printer.printRecord1("a", "b")
                except TypeError:
                    printer.printRecord1(["a", "b"])
                self.assertEqual(
                    "a,b" + self.__recordSeparator,
                    sw.getvalue()
                )
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testExcelPrinter2(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.EXCEL)
            try:
                try:
                    printer.printRecord1("a,b", "b")
                except TypeError:
                    printer.printRecord1(["a,b", "b"])
                self.assertEqual(
                    "\"a,b\",b" + self.__recordSeparator,
                    sw.getvalue()
                )
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testHeaderNotSet(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(None))
            try:
                try:
                    printer.printRecord1("a", "b", "c")
                    printer.printRecord1("x", "y", "z")
                except TypeError:
                    printer.printRecord1(["a", "b", "c"])
                    printer.printRecord1(["x", "y", "z"])
                self.assertEqual("a,b,c\r\nx,y,z\r\n", sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testInvalidFormat(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT.withDelimiter(Constants.CR)

    
    @pytest.mark.test
    def testJira135_part1(self) -> None:
        try:
            format = CSVFormat.DEFAULT\
                .withRecordSeparator0('\n')\
                .withQuote0(CSVPrinterTest.__DQUOTE_CHAR)\
                .withEscape0(Constants.BACKSLASH)
            sw = io.StringIO()
            list_ = []
            printer = CSVPrinter(sw, format)
            try:
                list_.append("\"")
                printer.printRecord0(list_)
                expected = "\"\\\"\"" + format.getRecordSeparator()
                self.assertEqual(expected, sw.getvalue())
                record0 = self.__toFirstRecordValues(expected, format)
                self.assertEqual(self.__expectNulls(list_, format), record0)
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @unittest.skip("Disabled")
    @pytest.mark.test
    def testJira135_part2(self) -> None:
        try:
            format = CSVFormat.DEFAULT\
                .withRecordSeparator0('\n')\
                .withQuote0(CSVPrinterTest.__DQUOTE_CHAR)\
                .withEscape0(Constants.BACKSLASH)
            sw = io.StringIO()
            list_ = []
            printer = CSVPrinter(sw, format)
            try:
                list_.append("\n")
                printer.printRecord0(list_)
                expected = "\"\\n\"" + format.getRecordSeparator()
                self.assertEqual(expected, sw.getvalue())
                record0 = self.__toFirstRecordValues(expected, format)
                self.assertEqual(self.__expectNulls(list_, format), record0)
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testJira135_part3(self) -> None:
        try:
            format = CSVFormat.DEFAULT\
                .withRecordSeparator0('\n')\
                .withQuote0(CSVPrinterTest.__DQUOTE_CHAR)\
                .withEscape0(Constants.BACKSLASH)
            sw = io.StringIO()
            list_ = []
            printer = CSVPrinter(sw, format)
            try:
                list_.append("\\")
                printer.printRecord0(list_)
                expected = "\"\\\\\"" + format.getRecordSeparator()
                self.assertEqual(expected, sw.getvalue())
                record0 = self.__toFirstRecordValues(expected, format)
                self.assertEqual(self.__expectNulls(list_, format), record0)
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @unittest.skip("Disabled test")
    @pytest.mark.test
    def testJira135All(self) -> None:
        try:
            format = CSVFormat.DEFAULT\
                .withRecordSeparator0('\n')\
                .withQuote0(CSVPrinterTest.__DQUOTE_CHAR)\
                .withEscape0(Constants.BACKSLASH)
            sw = io.StringIO()
            list_ = []
            printer = CSVPrinter(sw, format)
            try:
                list_.append("\"")
                list_.append("\n")
                list_.append("\\")
                printer.printRecord0(list_)
            finally:
                printer.close()
            expected = "\"\\\"\",\"\\n\",\"\\\"" + format.getRecordSeparator()
            self.assertEqual(expected, sw.getvalue())
            record0 = self.__toFirstRecordValues(expected, format)
            self.assertEqual(self.__expectNulls(list_, format), record0)
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testMongoDbCsvBasic(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.MONGODB_CSV)
            try:
                try:
                    printer.printRecord1("a", "b")
                except TypeError:
                    printer.printRecord1(["a", "b"])
                self.assertEqual("a,b" + self.__recordSeparator, sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")


    @pytest.mark.test
    def testMongoDbCsvCommaInValue(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.MONGODB_CSV)
            try:
                try:
                    printer.printRecord1("a,b", "c")
                except TypeError:
                    printer.printRecord1(["a,b", "c"])
                self.assertEqual("\"a,b\",c" + self.__recordSeparator, sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testMongoDbCsvDoubleQuoteInValue(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.MONGODB_CSV)
            try:
                try:
                    printer.printRecord1("a \"c\" b", "d")
                except TypeError:
                    printer.printRecord1(["a \"c\" b", "d"])
                self.assertEqual(
                    "\"a \"\"c\"\" b\",d" + self.__recordSeparator,
                    sw.getvalue()
                )
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testMongoDbCsvTabInValue(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.MONGODB_CSV)
            try:
                try:
                    printer.printRecord1("a\tb", "c")
                except TypeError:
                    printer.printRecord1(["a\tb", "c"])
                self.assertEqual("a\tb,c" + self.__recordSeparator, sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testMongoDbTsvBasic(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.MONGODB_TSV)
            try:
                try:
                    printer.printRecord1("a", "b")
                except TypeError:
                    printer.printRecord1(["a", "b"])
                self.assertEqual("a\tb" + self.__recordSeparator, sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testMongoDbTsvCommaInValue(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.MONGODB_TSV)
            try:
                try:
                    printer.printRecord1("a,b", "c")
                except TypeError:
                    printer.printRecord1(["a,b", "c"])
                self.assertEqual("a,b\tc" + self.__recordSeparator, sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testMongoDbTsvTabInValue(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.MONGODB_TSV)
            try:
                try:
                    printer.printRecord1("a\tb", "c")
                except TypeError:
                    printer.printRecord1(["a\tb", "c"])
                self.assertEqual(
                    "\"a\tb\"\tc" + self.__recordSeparator,
                    sw.getvalue()
                )
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

   
    @pytest.mark.test
    def testMultiLineComment(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.DEFAULT.withCommentMarker0('#'))
            try:
                printer.printComment("This is a comment\non multiple lines")
                self.assertEqual(
                    "# This is a comment" +\
                        self.__recordSeparator +\
                        "# on multiple lines" +\
                        self.__recordSeparator,
                    sw.getvalue()
                )
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")
    
    
    @pytest.mark.test
    def testMySqlNullOutput(self) -> None:
        try:
            s = ["NULL", None]
            format = CSVFormat.MYSQL\
                .withQuote0(CSVPrinterTest.__DQUOTE_CHAR)\
                .withNullString("NULL")\
                .withQuoteMode(QuoteMode.NON_NUMERIC)
            writer = io.StringIO()
            printer = CSVPrinter(writer, format)
            try:
                printer.printRecord1(s)
                expected = "\"NULL\"\tNULL\n"
                self.assertEqual(expected, writer.getvalue())
                record0 = self.__toFirstRecordValues(expected, format)
                self.assertEqual(s, record0)
            finally:
                printer.close()
            
            s = ["\\N", None]
            format = CSVFormat.MYSQL.withNullString("\\N")
            writer = io.StringIO()
            printer = CSVPrinter(writer, format)
            try:
                printer.printRecord1(s)
                expected = "\\\\N\t\\N\n"
                self.assertEqual(expected, writer.getvalue())
                record0 = self.__toFirstRecordValues(expected, format)
                self.assertEqual(
                    self.__expectNulls(s, format),
                    record0
                )
            finally:
                printer.close()
            
            s = ["\\N", "A"]
            format = CSVFormat.MYSQL.withNullString("\\N")
            writer = io.StringIO()
            printer = CSVPrinter(writer, format)
            try:
                printer.printRecord1(s)
                expected = "\\\\N\tA\n"
                self.assertEqual(expected, writer.getvalue())
                record0 = self.__toFirstRecordValues(expected, format)
                self.assertEqual(
                    self.__expectNulls(s, format),
                    record0
                )
            finally:
                printer.close()
            
            s = ["\n", "A"]
            format = CSVFormat.MYSQL.withNullString("\\N")
            writer = io.StringIO()
            printer = CSVPrinter(writer, format)
            try:
                printer.printRecord1(s)
                expected = "\\n\tA\n"
                self.assertEqual(expected, writer.getvalue())
                record0 = self.__toFirstRecordValues(expected, format)
                self.assertEqual(
                    self.__expectNulls(s, format),
                    record0
                )
            finally:
                printer.close()
            
            s = ["", None]
            format = CSVFormat.MYSQL.withNullString("NULL")
            writer = io.StringIO()
            printer = CSVPrinter(writer, format)
            try:
                printer.printRecord1(s)
                expected = "\tNULL\n"
                self.assertEqual(expected, writer.getvalue())
                record0 = self.__toFirstRecordValues(expected, format)
                self.assertEqual(
                    self.__expectNulls(s, format),
                    record0
                )
            finally:
                printer.close()
            
            s = ["", None]
            format = CSVFormat.MYSQL
            writer = io.StringIO()
            printer = CSVPrinter(writer, format)
            try:
                printer.printRecord1(s)
                expected = "\t\\N\n"
                self.assertEqual(expected, writer.getvalue())
                record0 = self.__toFirstRecordValues(expected, format)
                self.assertEqual(
                    self.__expectNulls(s, format),
                    record0
                )
            finally:
                printer.close()
            
            s = ["\\N", "", "\u000e,\\\r"]
            format = CSVFormat.MYSQL
            writer = io.StringIO()
            printer = CSVPrinter(writer, format)
            try:
                printer.printRecord1(s)
                expected = "\\\\N\t\t\u000e,\\\\\\r\n"
                self.assertEqual(expected, writer.getvalue())
                record0 = self.__toFirstRecordValues(expected, format)
                self.assertEqual(
                    self.__expectNulls(s, format),
                    record0
                )
            finally:
                printer.close()
            
            s = ["NULL", "\\\r"]
            format = CSVFormat.MYSQL
            writer = io.StringIO()
            printer = CSVPrinter(writer, format)
            try:
                printer.printRecord1(s)
                expected = "NULL\t\\\\\\r\n"
                self.assertEqual(expected, writer.getvalue())
                record0 = self.__toFirstRecordValues(expected, format)
                self.assertEqual(
                    self.__expectNulls(s, format),
                    record0
                )
            finally:
                printer.close()
            
            s = ["\\\r"]
            format = CSVFormat.MYSQL
            writer = io.StringIO()
            printer = CSVPrinter(writer, format)
            try:
                printer.printRecord1(s)
                expected = "\\\\\\r\n"
                self.assertEqual(expected, writer.getvalue())
                record0 = self.__toFirstRecordValues(expected, format)
                self.assertEqual(
                    self.__expectNulls(s, format),
                    record0
                )
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testMySqlNullStringDefault(self) -> None:
        self.assertEqual("\\N", CSVFormat.MYSQL.getNullString())

    
    @pytest.mark.test
    def testNewCsvPrinterAppendableNullFormat(self) -> None:
        with self.assertRaises((TypeError, ValueError, AttributeError)):
            CSVPrinter(io.StringIO(), None)

    
    @pytest.mark.test
    def testNewCsvPrinterNullAppendableFormat(self) -> None:
        with self.assertRaises((TypeError, ValueError, AttributeError)):
            CSVPrinter(None, CSVFormat.DEFAULT)

    
    @pytest.mark.test
    def testNotFlushable(self) -> None:
        try:
            out = []
            printer = CSVPrinter(out, CSVFormat.DEFAULT)
            try:
                try:
                    printer.printRecord1("a", "b", "c")
                except TypeError:
                    printer.printRecord1(["a", "b", "c"])
                self.assertEqual(
                    "a,b,c" + self.__recordSeparator, "".join(out)
                )
                printer.flush()
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testParseCustomNullValues(self) -> None:
        try:
            sw = io.StringIO()
            format = CSVFormat.DEFAULT.withNullString("NULL")
            printer = CSVPrinter(sw, format)
            try:
                try:
                    printer.printRecord1("a", None, "b")
                except TypeError:
                    printer.printRecord1(["a", None, "b"])
                csvString = sw.getvalue()
                self.assertEqual(
                    "a,NULL,b" + self.__recordSeparator,
                    csvString
                )
            finally:
                printer.close()
            iterable = format.parse(io.StringIO(csvString))
            try:
                iterator = iterable.iterator()
                record = next(iterator)
                self.assertEqual("a", record.get1(0))
                self.assertIsNone(record.get1(1))
                self.assertEqual("b", record.get1(2))
                self.assertFalse(iterator.hasNext())
            finally:
                iterable.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testPlainEscaped(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(
                sw,
                CSVFormat.DEFAULT.withQuote1(None).withEscape0('!')
            )
            try:
                try:
                    printer.print("abc")
                    printer.print("xyz")
                except AttributeError:
                    printer.print_("abc")
                    printer.print_("xyz")
                self.assertEqual("abc,xyz", sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testPlainPlain(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(None))
            try:
                try:
                    printer.print("abc")
                    printer.print("xyz")
                except AttributeError:
                    printer.print_("abc")
                    printer.print_("xyz")
                self.assertEqual("abc,xyz", sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testPlainQuoted(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0('\''))
            try:
                try:
                    printer.print("abc")
                except AttributeError:
                    printer.print_("abc")
                self.assertEqual("abc", sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @unittest.skip("Disabled")
    @pytest.mark.test
    def testPostgreSqlCsvNullOutput(self) -> None:
        try:
            s = ["NULL", None]
            format = (CSVFormat.POSTGRESQL_CSV\
                .withQuote0(CSVPrinterTest.DQUOTE_CHAR)\
                .withNullString("NULL")\
                .withQuoteMode(QuoteMode.ALL_NON_NULL))
            writer = io.StringIO()
            printer = CSVPrinter(writer, format)
            try:
                printer.printRecord1(s)
            finally:
                printer.close()
            expected = "\"NULL\",NULL\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format)
            self.assertEqual([None, None], record0)

            s = ["\\N", None]
            format = CSVFormat.POSTGRESQL_CSV\
                .withNullString("\\N")
            writer = io.StringIO()
            printer = CSVPrinter(writer, format)
            try:
                printer.printRecord1(s)
            finally:
                printer.close()
            expected = "\\\\N\t\\N\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format)
            self.assertEqual(
                self.__expectNulls(s, format),
                record0
            )

            s = ["\\N", "A"]
            format = CSVFormat.POSTGRESQL_CSV\
                .withNullString("\\N")
            writer = io.StringIO()
            printer = CSVPrinter(writer, format)
            try:
                printer.printRecord1(s)
            finally:
                printer.close()
            expected = "\\\\N\tA\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format)
            self.assertEqual(
                self.__expectNulls(s, format),
                record0
            )

            s = ["\n", "A"]
            format = CSVFormat.POSTGRESQL_CSV\
                .withNullString("\\N")
            writer = io.StringIO()
            printer = CSVPrinter(writer, format)
            try:
                printer.printRecord1(s)
            finally:
                printer.close()
            expected = "\\n\tA\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format)
            self.assertEqual(
                self.__expectNulls(s, format),
                record0
            )

            s = ["", None]
            format = CSVFormat.POSTGRESQL_CSV.withNullString("NULL")
            writer = io.StringIO()
            printer = CSVPrinter(writer, format)
            try:
                printer.printRecord1(s)
            finally:
                printer.close()
            expected = "\tNULL\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format)
            self.assertEqual(
                self.__expectNulls(s, format),
                record0
            )

            s = ["", None]
            format = CSVFormat.POSTGRESQL_CSV
            writer = io.StringIO()
            printer = CSVPrinter(writer, format)
            try:
                printer.printRecord1(s)
            finally:
                printer.close()
            expected = "\t\\N\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format)
            self.assertEqual(
                self.__expectNulls(s, format),
                record0
            )

            s = ["\\N", "", "\u000e,\\\r"]
            format = CSVFormat.POSTGRESQL_CSV
            writer = io.StringIO()
            printer = CSVPrinter(writer, format)
            try:
                printer.printRecord1(s)
            finally:
                printer.close()
            expected = "\\\\N\t\t\u000e,\\\\\\r\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format)
            self.assertEqual(
                self.__expectNulls(s, format),
                record0
            )

            s = ["NULL", "\\\r"]
            format = CSVFormat.POSTGRESQL_CSV
            writer = io.StringIO()
            printer = CSVPrinter(writer, format)
            try:
                printer.printRecord1(s)
            finally:
                printer.close()
            expected = "NULL\t\\\\\\r\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format)
            self.assertEqual(
                self.__expectNulls(s, format),
                record0
            )

            s = ["\\\r"]
            format = CSVFormat.POSTGRESQL_CSV
            writer = io.StringIO()
            printer = CSVPrinter(writer, format)
            try:
                printer.printRecord1(s)
            finally:
                printer.close()
            expected = "\\\\\\r\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format)
            self.assertEqual(
                self.__expectNulls(s, format),record0
            )
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @unittest.skip("Disabled")
    @pytest.mark.test
    def testPostgreSqlCsvTextOutput(self) -> None:
        try:
            s = ["NULL", None]
            format = (CSVFormat.POSTGRESQL_TEXT\
                .withQuote0(CSVPrinterTest.__DQUOTE_CHAR)\
                .withNullString("NULL")
                .withQuoteMode(QuoteMode.ALL_NON_NULL))
            writer = io.StringIO()
            printer = CSVPrinter(writer, format)
            try:
                printer.printRecord1(s)
            finally:
                printer.close()
            expected = "\"NULL\"\tNULL\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format)
            self.assertEqual([None, None], record0)

            s = ["\\N", None]
            format = CSVFormat.POSTGRESQL_TEXT.withNullString("\\N")
            writer = io.StringIO()
            printer = CSVPrinter(writer, format)
            try:
                printer.printRecord1(s)
            finally:
                printer.close()
            expected = "\\\\N\t\\N\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format)
            self.assertEqual(
                self.__expectNulls(s, format),
                record0
            )

            s = ["\\N", "A"]
            format = CSVFormat.POSTGRESQL_TEXT.withNullString("\\N")
            writer = io.StringIO()
            printer = CSVPrinter(writer, format)
            try:
                printer.printRecord1(s)
            finally:
                printer.close()
            expected = "\\\\N\tA\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format)
            self.assertEqual(
                self.__expectNulls(s, format),
                record0
            )

            s = ["\n", "A"]
            format = CSVFormat.POSTGRESQL_TEXT.withNullString("\\N")
            writer = io.StringIO()
            printer = CSVPrinter(writer, format)
            try:
                printer.printRecord1(s)
            finally:
                printer.close()
            expected = "\\n\tA\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format)
            self.assertEqual(
                self.__expectNulls(s, format),
                record0
            )

            s = ["", None]
            format = CSVFormat.POSTGRESQL_TEXT.withNullString("NULL")
            writer = io.StringIO()
            printer = CSVPrinter(writer, format)
            try:
                printer.printRecord1(s)
            finally:
                printer.close()
            expected = "\tNULL\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format)
            self.assertEqual(
                self.__expectNulls(s, format),
                record0
            )

            s = ["", None]
            format = CSVFormat.POSTGRESQL_TEXT
            writer = io.StringIO()
            printer = CSVPrinter(writer, format)
            try:
                printer.printRecord1(s)
            finally:
                printer.close()
            expected = "\t\\N\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format)
            self.assertEqual(
                self.__expectNulls(s, format),
                record0
            )

            s = ["\\N", "", "\u000e,\\\r"]
            format = CSVFormat.POSTGRESQL_TEXT
            writer = io.StringIO()
            printer = CSVPrinter(writer, format)
            try:
                printer.printRecord1(s)
            finally:
                printer.close()
            expected = "\\\\N\t\t\u000e,\\\\\\r\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format)
            self.assertEqual(
                self.__expectNulls(s, format),
                record0
            )

            s = ["NULL", "\\\r"]
            format = CSVFormat.POSTGRESQL_TEXT
            writer = io.StringIO()
            printer = CSVPrinter(writer, format)
            try:
                printer.printRecord1(s)
            finally:
                printer.close()
            expected = "NULL\t\\\\\\r\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format)
            self.assertEqual(
                self.__expectNulls(s, format),
                record0
            )

            s = ["\\\r"]
            format = CSVFormat.POSTGRESQL_TEXT
            writer = io.StringIO()
            printer = CSVPrinter(writer, format)
            try:
                printer.printRecord1(s)
            finally:
                printer.close()
            expected = "\\\\\\r\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format)
            self.assertEqual(
                self.__expectNulls(s, format),
                record0
            )
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testPostgreSqlNullStringDefaultCsv(self) -> None:
        self.assertEqual(
            "",
            CSVFormat.POSTGRESQL_CSV.getNullString()
        )

   
    @pytest.mark.test
    def testPostgreSqlNullStringDefaultText(self) -> None:
        self.assertEqual(
            "\\N",
            CSVFormat.POSTGRESQL_TEXT.getNullString()
        )
    

    @pytest.mark.test
    def testPrint(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVFormat.DEFAULT.print0(sw)
            try:
                try:
                    printer.printRecord1("a", "b\\c")
                except TypeError:
                    printer.printRecord1(["a", "b\\c"])
                self.assertEqual(
                    "a,b\\c" + self.__recordSeparator,
                    sw.getvalue()
                )
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testPrintCSVParser(self) -> None:
        try:
            code = "a1,b1\n" +\
                "a2,b2\n" +\
                "a3,b3\n" +\
                "a4,b4\n"
            res = [["a1", "b1"], ["a2", "b2"], ["a3", "b3"], ["a4", "b4"]]
            format = CSVFormat.DEFAULT
            sw = io.StringIO()
            printer = format.print0(sw)
            parser = CSVParser.parse4(code, format)
            try:
                printer.printRecords0(parser)
                parser2 = CSVParser.parse4(sw.getvalue(), format)
                try:
                    records = parser2.getRecords()
                    self.assertFalse(len(records) == 0)
                    Utils.compare("Fail", res, records)
                finally:
                    parser2.close()
            finally:
                printer.close()
                parser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testPrintCSVRecord(self) -> None:
        try:
            code = "a1,b1\n" +\
                "a2,b2\n" +\
                "a3,b3\n" +\
                "a4,b4\n"
            res = [["a1", "b1"], ["a2", "b2"], ["a3", "b3"], ["a4", "b4"]]
            format = CSVFormat.DEFAULT
            sw = io.StringIO()
            printer = format.print0(sw)
            parser = CSVParser.parse4(code, format)
            try:
                parserIterator = parser.iterator()
                while True:
                    try:
                        record = next(parserIterator)
                        printer.printRecord0(record)
                    except StopIteration:
                        break
                parser2 = CSVParser.parse4(sw.getvalue(), format)
                try:
                    records = parser2.getRecords()
                    self.assertFalse(len(records) == 0)
                    Utils.compare("Fail", res, records)
                finally:
                    parser2.close()
            finally:
                printer.close()
                parser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testPrintCSVRecords(self) -> None:
        try:
            code = "a1,b1\n" +\
                "a2,b2\n" +\
                "a3,b3\n" +\
                "a4,b4\n"
            res = [["a1", "b1"], ["a2", "b2"], ["a3", "b3"], ["a4", "b4"]]
            format = CSVFormat.DEFAULT
            sw = io.StringIO()
            printer = format.print0(sw)
            parser = CSVParser.parse4(code, format)
            try:
                printer.printRecords0(parser.getRecords())
                parser2 = CSVParser.parse4(sw.getvalue(), format)
                try:
                    records = parser2.getRecords()
                    self.assertFalse(len(records) == 0)
                    Utils.compare("Fail", res, records)
                finally:
                    parser2.close()
            finally:
                printer.close()
                parser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testPrintCustomNullValues(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.DEFAULT.withNullString("NULL"))
            try:
                try:
                    printer.printRecord1("a", None, "b")
                except TypeError:
                    printer.printRecord1(["a", None, "b"])
                self.assertEqual(
                    "a,NULL,b" + self.__recordSeparator,
                    sw.getvalue()
                )
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testPrinter1(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.DEFAULT)
            try:
                try:
                    printer.printRecord1("a", "b")
                except TypeError:
                    printer.printRecord1(["a", "b"])
                self.assertEqual(
                    "a,b" + self.__recordSeparator,
                    sw.getvalue()
                )
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testPrinter2(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.DEFAULT)
            try:
                try:
                    printer.printRecord1("a,b", "b")
                except TypeError:
                    printer.printRecord1(["a,b", "b"])
                self.assertEqual(
                    "\"a,b\",b" + self.__recordSeparator,
                    sw.getvalue()
                )
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testPrinter3(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.DEFAULT)
            try:
                try:
                    printer.printRecord1("a, b", "b ")
                except TypeError:
                    printer.printRecord1(["a, b", "b "])
                self.assertEqual(
                    "\"a, b\",\"b \"" + self.__recordSeparator,
                    sw.getvalue()
                )
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testPrinter4(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.DEFAULT)
            try:
                try:
                    printer.printRecord1("a", "b\"c")
                except TypeError:
                    printer.printRecord1(["a", "b\"c"])
                self.assertEqual(
                    "a,\"b\"\"c\"" + self.__recordSeparator,
                    sw.getvalue()
                )
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testPrinter5(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.DEFAULT)
            try:
                try:
                    printer.printRecord1("a", "b\nc")
                except TypeError:
                    printer.printRecord1(["a", "b\nc"])
                self.assertEqual(
                    "a,\"b\nc\"" + self.__recordSeparator,
                    sw.getvalue()
                )
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testPrinter6(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.DEFAULT)
            try:
                try:
                    printer.printRecord1("a", "b\r\nc")
                except TypeError:
                    printer.printRecord1(["a", "b\r\nc"])
                self.assertEqual(
                    "a,\"b\r\nc\"" + self.__recordSeparator,
                    sw.getvalue()
                )
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testPrinter7(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.DEFAULT)
            try:
                try:
                    printer.printRecord1("a", "b\\c")
                except TypeError:
                    printer.printRecord1(["a", "b\\c"])
                self.assertEqual(
                    "a,b\\c" + self.__recordSeparator,
                    sw.getvalue()
                )
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testPrintNullValues(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.DEFAULT)
            try:
                try:
                    printer.printRecord1("a", None, "b")
                except TypeError:
                    printer.printRecord1(["a", None, "b"])
                self.assertEqual(
                    "a,,b" + self.__recordSeparator,
                    sw.getvalue()
                )
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testPrintOnePositiveInteger(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(
                sw,
                CSVFormat.DEFAULT.withQuoteMode(QuoteMode.MINIMAL)
            )
            try:
                try:
                    printer.print(sys.maxsize)
                except AttributeError:
                    printer.print_(sys.maxsize)
                self.assertEqual(str(sys.maxsize), sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testPrintReaderWithoutQuoteToAppendable(self) -> None:
        try:
            sb = []
            content = "testValue"
            printer = CSVPrinter(sb, CSVFormat.DEFAULT.withQuote1(None))
            try:
                value = io.StringIO(content)
                try:
                    printer.print(value)
                except AttributeError:
                    printer.print_(value)
            finally:
                printer.close()
            self.assertEqual(content, ''.join(sb))
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")
    

    @pytest.mark.test
    def testPrintReaderWithoutQuoteToWriter(self) -> None:
        try:
            sw = io.StringIO()
            content = "testValue"
            printer = CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(None))
            try:
                value = io.StringIO(content)
                try:
                    printer.print(value)
                except AttributeError:
                    printer.print_(value)
                self.assertEqual(content, sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")
        

    @pytest.mark.test
    def testPrintRecordStream(self) -> None:
        try:
            code = "a1,b1\n" +\
                "a2,b2\n" +\
                "a3,b3\n" +\
                "a4,b4\n"
            res = [["a1", "b1"], ["a2", "b2"], ["a3", "b3"], ["a4", "b4"]]
            format = CSVFormat.DEFAULT
            sw = io.StringIO()
            printer = format.print0(sw)
            parser = CSVParser.parse4(code, format)
            try:
                parserIterator = parser.iterator()
                while True:
                    try:
                        record = next(parserIterator)
                        printer.printRecord2(record.stream())
                    except StopIteration:
                        break
                parser2 = CSVParser.parse4(sw.getvalue(), format)
                try:
                    records = parser2.getRecords()
                    self.assertFalse(len(records) == 0)
                    Utils.compare("Fail", res, records)
                finally:
                    parser2.close()
            finally:
                printer.close()
                parser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testPrintToPathWithDefaultCharset(self) -> None:
        try:
            file = self.__createTempPath()
            printer = CSVFormat.DEFAULT.print4(file, locale.getpreferredencoding())
            try:
                try:
                    printer.printRecord1("a", "b\\c")
                except TypeError:
                    printer.printRecord1(["a", "b\\c"])
            finally:
                printer.close()
            with open(file, 'r', encoding=locale.getpreferredencoding(), newline='') as f:
                self.assertEqual(
                    "a,b\\c" + self.__recordSeparator,
                    f.read()
                )
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testQuoteAll(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(
                sw,
                CSVFormat.DEFAULT.withQuoteMode(QuoteMode.ALL)
            )
            try:
                try:
                    printer.printRecord1("a", "b\nc", "d")
                except TypeError:
                    printer.printRecord1(["a", "b\nc", "d"])
                self.assertEqual(
                    "\"a\",\"b\nc\",\"d\"" + self.__recordSeparator,
                    sw.getvalue()
                )
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")
        

    @pytest.mark.test
    def testQuoteCommaFirstChar(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.RFC4180)
            try:
                try:
                    printer.printRecord1(",")
                except TypeError:
                    printer.printRecord1([","])
                self.assertEqual(
                    "\",\"" + self.__recordSeparator,
                    sw.getvalue()
                )
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testQuoteNonNumeric(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(
                sw,
                CSVFormat.DEFAULT.withQuoteMode(QuoteMode.NON_NUMERIC)
            )
            try:
                try:
                    printer.printRecord1("a", "b\nc", 1)
                except TypeError:
                    printer.printRecord1(["a", "b\nc", 1])
                self.assertEqual(
                    "\"a\",\"b\nc\",1" + self.__recordSeparator,
                    sw.getvalue()
                )
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testRandomDefault(self) -> None:
        try:
            self.__doRandom(
                CSVFormat.DEFAULT,
                CSVPrinterTest.__ITERATIONS_FOR_RANDOM_TEST
            )
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testRandomExcel(self) -> None:
        try:
            self.__doRandom(
                CSVFormat.EXCEL,
                CSVPrinterTest.__ITERATIONS_FOR_RANDOM_TEST
            )
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @unittest.skip("Disabled")
    @pytest.mark.test
    def testRandomMongoDbCsv(self) -> None:
        try:
            self.__doRandom(
                CSVFormat.MONGODB_CSV,
                CSVPrinterTest.__ITERATIONS_FOR_RANDOM_TEST
            )
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testRandomMySql(self) -> None:
        try:
            self.__doRandom(
                CSVFormat.MYSQL,
                CSVPrinterTest.__ITERATIONS_FOR_RANDOM_TEST
            )
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @unittest.skip("Disabled")
    @pytest.mark.test
    def testRandomOracle(self) -> None:
        try:
            self.__doRandom(
                CSVFormat.ORACLE,
                CSVPrinterTest.__ITERATIONS_FOR_RANDOM_TEST
            )
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @unittest.skip("Disabled")
    @pytest.mark.test
    def testRandomPostgreSqlCsv(self) -> None:
        try:
            self.__doRandom(
                CSVFormat.POSTGRESQL_CSV,
                CSVPrinterTest.__ITERATIONS_FOR_RANDOM_TEST
            )
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testRandomPostgreSqlText(self) -> None:
        try:
            self.__doRandom(
                CSVFormat.POSTGRESQL_TEXT,
                CSVPrinterTest.__ITERATIONS_FOR_RANDOM_TEST
            )
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testRandomRfc4180(self) -> None:
        try:
            self.__doRandom(
                CSVFormat.RFC4180,
                CSVPrinterTest.__ITERATIONS_FOR_RANDOM_TEST
            )
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")


    @pytest.mark.test
    def testRandomTdf(self) -> None:
        try:
            self.__doRandom(
                CSVFormat.TDF,
                CSVPrinterTest.__ITERATIONS_FOR_RANDOM_TEST
            )
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testSingleLineComment(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(
                sw,
                CSVFormat.DEFAULT.withCommentMarker0('#')
            )
            try:
                printer.printComment("This is a comment")
                self.assertEqual(
                    "# This is a comment" + self.__recordSeparator,
                    sw.getvalue()
                )
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testSingleQuoteQuoted(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(
                sw,
                CSVFormat.DEFAULT.withQuote0('\'')
            )
            try:
                try:
                    printer.print("a'b'c")
                    printer.print("xyz")
                except AttributeError:
                    printer.print_("a'b'c")
                    printer.print_("xyz")
                self.assertEqual("'a''b''c',xyz", sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")
        

    @pytest.mark.test
    def testTrailingDelimiterOnTwoColumns(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(
                sw,
                CSVFormat.DEFAULT.withTrailingDelimiter0()
            )
            try:
                try:
                    printer.printRecord1("A", "B")
                except TypeError:
                    printer.printRecord1(["A", "B"])
                self.assertEqual("A,B,\r\n", sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testTrimOffOneColumn(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(
                sw,
                CSVFormat.DEFAULT.withTrim1(False)
            )
            try:
                try:
                    printer.print(" A ")
                except AttributeError:
                    printer.print_(" A ")
                self.assertEqual("\" A \"", sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")
        

    @pytest.mark.test
    def testTrimOnOneColumn(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(
                sw,
                CSVFormat.DEFAULT.withTrim0()
            )
            try:
                try:
                    printer.print(" A ")
                except AttributeError:
                    printer.print_(" A ")
                self.assertEqual("A", sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")
        

    @pytest.mark.test
    def testTrimOnTwoColumns(self) -> None:
        try:
            sw = io.StringIO()
            printer = CSVPrinter(sw, CSVFormat.DEFAULT.withTrim0())
            try:
                try:
                    printer.print(" A ")
                    printer.print(" B ")
                except AttributeError:
                    printer.print_(" A ")
                    printer.print_(" B ")
                self.assertEqual("A,B", sw.getvalue())
            finally:
                printer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    def __toFirstRecordValues(self, expected: str, format) -> List[str]:
        try:
            parser = CSVParser.parse4(expected, format)
            try:
                return parser.getRecords()[0].values()
            finally:
                parser.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred in `__toFirstRecordValues()`: {e}")

    
    def __tryFormat(self, list_, quote, escape, expected) -> None:
        try:
            format = CSVFormat.DEFAULT\
                .withQuote1(quote)\
                .withEscape1(escape)\
                .withRecordSeparator1(None)
            out = []
            printer = CSVPrinter(out, format)
            try:
                printer.printRecord0(list_)
            finally:
                printer.close()
            self.assertEqual(expected, ''.join(out))
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred in `__tryFormat()`: {e}")
