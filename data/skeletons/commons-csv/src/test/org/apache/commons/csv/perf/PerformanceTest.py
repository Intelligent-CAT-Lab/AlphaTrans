# Imports Begin
from src.main.org.apache.commons.io.IOUtils import *
from src.main.org.apache.commons.csv.Token import *
from src.main.org.apache.commons.csv.Lexer import *
from src.main.org.apache.commons.csv.ExtendedBufferedReader import *
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVFormat import *
import pathlib

# Imports End


class PerformanceTest:

    # Class Fields Begin
    __TEST_RESRC: str = None
    __BIG_FILE: pathlib.Path = None
    __max: int = None
    # Class Fields End

    # Class Methods Begin
    def testReadBigFile(self) -> None:
        pass

    def testParseBigFileRepeat(self) -> None:
        pass

    def testParseBigFile(self, traverseColumns: bool) -> int:
        pass

    def __readAll(self, in_: io.BufferedReader) -> int:
        pass

    def __println(self, s: str) -> None:
        pass

    def __parse(
        self,
        reader: typing.Union[io.TextIOWrapper, io.BufferedReader],
        traverseColumns: bool,
    ) -> int:
        pass

    def __createBufferedReader(self) -> io.BufferedReader:
        pass

    # Class Methods End
