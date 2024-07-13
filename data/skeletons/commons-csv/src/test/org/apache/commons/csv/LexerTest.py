from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.csv.Token import *
from src.main.org.apache.commons.csv.Lexer import *
from src.main.org.apache.commons.csv.ExtendedBufferedReader import *
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.CSVFormat import *
import unittest
import io

# Imports End


class LexerTest(unittest.TestCase):

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

    def __createLexer(self, input_: str, format_: CSVFormat) -> Lexer:
        pass

    # Class Methods End
