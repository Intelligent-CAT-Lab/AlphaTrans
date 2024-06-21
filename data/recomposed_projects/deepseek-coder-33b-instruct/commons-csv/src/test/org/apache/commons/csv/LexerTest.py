from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.ExtendedBufferedReader import *
from src.main.org.apache.commons.csv.Lexer import *
from src.main.org.apache.commons.csv.Token import *


class LexerTest(unittest.TestCase):

    __formatWithEscaping: CSVFormat = None


    @pytest.mark.test
    def testReadEscapeFF(self) -> None:
        
        with self.__createLexer("f", self.__formatWithEscaping.withEscape0('\f')) as lexer:
            ch = lexer.readEscape()
            self.assertEqual(ch, ord(FF))

    @pytest.mark.test
    def testReadEscapeBackspace(self) -> None:
        
        with self.__createLexer("b", self.__formatWithEscaping.withEscape0('\\')) as lexer:
            ch = lexer.readEscape()
            self.assertEqual(BACKSPACE, ch)

    @pytest.mark.test
    def testIsMetaCharCommentStart(self) -> None:
        
        with self.__createLexer("#", CSVFormat.DEFAULT.withCommentMarker0('#')) as lexer:
            ch = lexer.readEscape()
            self.assertEqual('#', chr(ch))

    @pytest.mark.test
    def testEscapingAtEOF(self) -> None:
        
        code = "escaping at EOF is evil\\"
        with self.__createLexer(code, self.__formatWithEscaping) as lexer:
            with pytest.raises(IOError):
                lexer.nextToken(Token())
    def setUp(self) -> None:
         self.__formatWithEscaping = CSVFormat.DEFAULT.withEscape0('\\')
    def __createLexer(self, input: str, format: CSVFormat) -> Lexer:
         return Lexer(format, ExtendedBufferedReader(io.StringIO(input)))
