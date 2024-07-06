from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.ExtendedBufferedReader import *
from src.main.org.apache.commons.csv.Lexer import *
from src.main.org.apache.commons.csv.Token import *


class LexerTest(unittest.TestCase):

    __formatWithEscaping: CSVFormat = None

    def testReadEscapeFF(self) -> None:
        with Lexer(
            self.__createLexer("f", CSVFormat.DEFAULT.withEscape0("\f"))
        ) as lexer:
            ch = lexer.readEscape()
            self.assertEqual(FF, ch)

    def testReadEscapeBackspace(self) -> None:
        with Lexer(
            self.__createLexer("b", CSVFormat.DEFAULT.withEscape0("\b"))
        ) as lexer:
            ch = lexer.readEscape()
            self.assertEqual(BACKSPACE, ch)

    def testIsMetaCharCommentStart(self) -> None:
        with Lexer(
            self.__createLexer("#", CSVFormat.DEFAULT.withCommentMarker0("#"))
        ) as lexer:
            ch = lexer.readEscape()
            self.assertEqual("#", ch)

    def testEscapingAtEOF(self) -> None:
        code = "escaping at EOF is evil\\"
        with self.__createLexer(code, self.__formatWithEscaping) as lexer:
            with self.assertRaises(Exception):
                lexer.nextToken(Token())

    def setUp(self) -> None:
        self.__formatWithEscaping = CSVFormat.DEFAULT.withEscape0("\\")

    def __createLexer(self, input: str, format: CSVFormat) -> Lexer:
        return Lexer(format, ExtendedBufferedReader(StringReader(input)))
