# Imports Begin
from src.main.org.apache.commons.csv.Token import *
from src.main.org.apache.commons.csv.Lexer import *
from src.main.org.apache.commons.csv.ExtendedBufferedReader import *
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.CSVFormat import *

# Imports End


class LexerTest:

    # Class Fields Begin
    __formatWithEscaping: CSVFormat = None
    # Class Fields End

    # Class Methods Begin
    def testReadEscapeFF(self) -> None:
        pass

    def testReadEscapeBackspace(self) -> None:
        pass

    def testIsMetaCharCommentStart(self) -> None:
        pass

    def testEscapingAtEOF(self) -> None:
        pass

    def setUp(self) -> None:
        pass

    def __createLexer(self, input: str, format: CSVFormat) -> Lexer:
        pass

    # Class Methods End


class Executable:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def execute(self) -> None:
        pass

    # Class Methods End
