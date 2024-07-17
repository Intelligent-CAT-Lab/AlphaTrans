import pytest

import os
import io
import gzip
import time
from pathlib import Path
from typing import Callable
from src.main.org.apache.commons.csv.IOUtils import *
from src.main.org.apache.commons.csv.Token import *
from src.main.org.apache.commons.csv.Lexer import *
from src.main.org.apache.commons.csv.ExtendedBufferedReader import *
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVFormat import *


class PerformanceTest:

    class __CSVParserFactory:
        def createParser(self) -> CSVParser:
            raise NotImplementedError

    
    class __CSVParserFactoryForTestParseCommonsCSV(__CSVParserFactory):
        def createParser(self) -> CSVParser:
            return CSVParser.CSVParser1(PerformanceTest._createReader(), format)

    
    class __CSVParserFactoryForTestParsePath(__CSVParserFactory):
        def createParser(self) -> CSVParser:
            return CSVParser.parse1(
                PerformanceTest.__BIG_FILE.open('rb'),
                'ISO-8859-1',
                PerformanceTest.__format
            )

    
    class __CSVParserFactoryForTestParsePathDoubleBuffering(__CSVParserFactory):
        def createParser(self) -> CSVParser:
            return CSVParser.parse3(
                PerformanceTest.__BIG_FILE.open('r', encoding='ISO-8859-1'),
                PerformanceTest.__format
            )
    

    class __CSVParserFactoryForTestParseURL(__CSVParserFactory):
        def createParser(self) -> CSVParser:
            return CSVParser.parse5(
                PerformanceTest.__BIG_FILE.as_uri(),
                'ISO-8859-1',
                PerformanceTest.__format
            )

    
    class __Stats:
        def __init__(self, c, f) -> None:
            self.count = c
            self.fields = f

    
    __PROPERTY_NAMES = [
        "java.version",  # Java Runtime Environment version
        "java.vendor",  # Java Runtime Environment vendor
        "java.vm.version",  # Java Virtual Machine implementation version
        "java.vm.name",  # Java Virtual Machine implementation name
        "os.name",  # Operating system name
        "os.arch",  # Operating system architecture
        "os.version"  # Operating system version
    ]
    __max = 11  # skip first test

    __num = 0  # number of elapsed times recorded

    __ELAPSED_TIMES = [0] * __max
    __format = CSVFormat.EXCEL

    __TEST_RESRC = Path(__file__).resolve()\
        .parent.parent.parent.parent.parent \
        / 'resources' / 'org' / 'apache' / 'commons' / 'csv' / 'perf' / 'worldcitiespop.txt.gz'

    __BIG_FILE = Path(os.getenv('TMPDIR', '/tmp')) / "worldcitiespop.txt"

    
    @staticmethod
    def _createReader() -> io.TextIOWrapper:
        return io.open(PerformanceTest.__BIG_FILE, mode='r', encoding='ISO-8859-1')

    
    @staticmethod
    def __createTestCSVLexer(test, input) -> Lexer:
        if test.startswith("CSVLexer"):
            return PerformanceTest.__getLexerCtor(test)(PerformanceTest.__format, input)
        else:
            return Lexer(PerformanceTest.__format, input)

    
    @staticmethod
    def __getLexerCtor(clazz) -> Callable:
        lexerClass = globals()[clazz]
        return lexerClass.__init__

    
    @staticmethod
    def __iterate(iterable) -> "PerformanceTest.__Stats":
        count = 0
        fields = 0
        for record in iterable:
            count += 1
            fields += record.size()
        return PerformanceTest.__Stats(count, fields)

    
    @staticmethod
    def main(args) -> None:
        if PerformanceTest.__BIG_FILE.exists():
            print("Found test fixture " + str(PerformanceTest.__BIG_FILE) +\
                ": " + str(PerformanceTest.__BIG_FILE.stat().st_size) + " bytes.")
        else:
            print(f"Decompressing test fixture to: {PerformanceTest.__BIG_FILE}...")
            with gzip.open(PerformanceTest.__TEST_RESRC, 'rb') as gz_file,\
                io.TextIOWrapper(gz_file, encoding='utf-8') as input,\
                open(PerformanceTest.__BIG_FILE, 'wb') as output:
                
                IOUtils.copy0(input, output)
            print("Decompressed test fixture " + str(PerformanceTest.__BIG_FILE) +\
                ": " + str(PerformanceTest.__BIG_FILE.stat().st_size) + " bytes.")

        argc = len(args)
        if argc > 0:
            PerformanceTest.__max = int(args[0])

        if argc > 1:
            tests = args[1:]
        else:
            tests = [
                "file",
                "split",
                "extb",
                "exts",
                "csv",
                "csv-path",
                "csv-path-db",
                "csv-url",
                "lexreset",
                "lexnew"
            ]

        for p in PerformanceTest.__PROPERTY_NAMES:
            print(f"{p}={os.getenv(p)}")
        print(f"Max count: {PerformanceTest.__max}\n")

        for test in tests:
            if test == "file":
                PerformanceTest.__testReadBigFile(False)
            elif test == "split":
                PerformanceTest.__testReadBigFile(True)
            elif test == "csv":
                PerformanceTest.__testParseCommonsCSV()
            elif test == "csv-path":
                PerformanceTest.__testParsePath()
            elif test == "csv-path-db":
                PerformanceTest.__testParsePathDoubleBuffering()
            elif test == "csv-url":
                PerformanceTest.__testParseURL()
            elif test == "lexreset":
                PerformanceTest.__testCSVLexer(False, test)
            elif test == "lexnew":
                PerformanceTest.__testCSVLexer(True, test)
            elif test.startswith("CSVLexer"):
                PerformanceTest.__testCSVLexer(False, test)
            elif test == "extb":
                PerformanceTest.__testExtendedBuffer(False)
            elif test == "exts":
                PerformanceTest.__testExtendedBuffer(True)
            else:
                print(f"Invalid test name: {test}")

    
    @staticmethod
    def __readAll(infile, split) -> "PerformanceTest.__Stats":
        count = 0
        fields = 0
        for record in infile:
            count += 1
            fields += len(record.split(',')) if split else 1
        return PerformanceTest.__Stats(count, fields)

    
    @staticmethod
    def __show0() -> None:
        if PerformanceTest.__num > 1:
            total = sum(PerformanceTest.__ELAPSED_TIMES[1:PerformanceTest.__num])
            print(
                f"{'Average(not first)':<20}: {total // (PerformanceTest.__num - 1):5d}ms\n"
            )
        PerformanceTest.__num = 0  # ready for next set

    
    @staticmethod
    def __show1(msg, stats, start) -> None:
        elapsed = int((time.time() * 1000) - start)
        print(f"{msg:<20}: {elapsed:5d}ms {stats.count} lines {stats.fields} fields")
        PerformanceTest.__ELAPSED_TIMES[PerformanceTest.__num] = elapsed
        PerformanceTest.__num += 1

    
    @staticmethod
    def __testCSVLexer(newToken, test) -> None:
        token = Token()
        dynamic = ""
        for i in range(PerformanceTest.__max):
            simpleName = ""
            startMillis = 0
            input = ExtendedBufferedReader(PerformanceTest._createReader())
            lexer = PerformanceTest.__createTestCSVLexer(test, input)
            try:
                if test.startswith("CSVLexer"):
                    dynamic = "!"
                simpleName = lexer.__class__.__name__
                count = 0
                fields = 0
                startMillis = int(time.time() * 1000)
                while True:
                    if newToken:
                        token = Token()
                    else:
                        token.reset()
                    lexer.nextToken(token)
                    if token.type == Token.Type.EOF:
                        break
                    elif token.type == Token.Type.EORECORD:
                        fields += 1
                        count += 1
                    elif token.type == Token.INVALID:
                        raise IOError(f"invalid parse sequence <{token.content}>")
                    elif token.type == Token.TOKEN:
                        fields += 1
                    elif token.type == Token.COMMENT:
                        pass
                    else:
                        raise RuntimeError(f"Unexpected Token type: {token.type}")
                stats = PerformanceTest.__Stats(count, fields)
            finally:
                input.close()
                lexer.close()
            PerformanceTest.__show1(
                f"{simpleName}{dynamic} {'new' if newToken else 'reset'}", stats, startMillis
            )
        PerformanceTest.__show0()

    
    @staticmethod
    def __testExtendedBuffer(makeString) -> None:
        for i in range(PerformanceTest.__max):
            fields = 0
            lines = 0
            startMillis = 0
            infile = ExtendedBufferedReader(PerformanceTest._createReader())
            try:
                startMillis = int(time.time() * 1000)
                if makeString:
                    sb = []
                    read = infile.read0()
                    while read != -1:
                        sb.append(chr(read))
                        if read == ord(','):
                            ''.join(sb)
                            sb = []
                            fields += 1
                        elif read == ord('\n'):
                            ''.join(sb)
                            sb = []
                            lines += 1
                        read = infile.read0()
                else:
                    read = infile.read0()
                    while read != -1:
                        if read == ord(','):
                            fields += 1
                        elif read == ord('\n'):
                            lines += 1
                        read = infile.read0()
                fields += lines  # EOL is a delimiter too
            finally:
                infile.close()
            PerformanceTest.__show1(
                f"Extended{' toString' if makeString else ''}",
                PerformanceTest.__Stats(lines, fields),
                startMillis
            )
        PerformanceTest.__show0()

    
    @staticmethod
    def __testParseCommonsCSV() -> None:
        PerformanceTest.__testParser(
            "CSV", 
            PerformanceTest.__CSVParserFactoryForTestParseCommonsCSV()
        )

    
    @staticmethod
    def __testParsePath() -> None:
        PerformanceTest.__testParser(
            "CSV-PATH",
            PerformanceTest.__CSVParserFactoryForTestParsePath()
        )

    
    @staticmethod
    def __testParsePathDoubleBuffering() -> None:
        PerformanceTest.__testParser(
            "CSV-PATH-DB",
            PerformanceTest.__CSVParserFactoryForTestParsePathDoubleBuffering()
        )

    
    @staticmethod
    def __testParser(msg, fac) -> None:
        for i in range(PerformanceTest.__max):
            startMillis = 0
            parser = fac.createParser()
            try:
                startMillis = int(time.time() * 1000)
                stats = PerformanceTest.__iterate(parser)
            finally:
                parser.close()
            PerformanceTest.__show1(msg, stats, startMillis)
        PerformanceTest.__show0()

    
    @staticmethod
    def __testParseURL() -> None:
        PerformanceTest.__testParser(
            "CSV-URL",
            PerformanceTest.__CSVParserFactoryForTestParseURL()
        )

    
    @staticmethod
    def __testReadBigFile(split):
        startMillis = 0
        stats = None
        for i in range(PerformanceTest.__max):
            infile = io.BufferedReader(PerformanceTest._createReader().buffer)
            try:
                startMillis = int(time.time() * 1000)
                stats = PerformanceTest.__readAll(infile, split)
            finally:
                infile.close()
            PerformanceTest.__show1("file+split" if split else "file", stats, startMillis)
        PerformanceTest.__show0()


if __name__ == "__main__":
    import sys
    PerformanceTest.main(sys.argv)
