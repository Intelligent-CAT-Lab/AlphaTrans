from __future__ import annotations
import re
import os
from io import StringIO
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

        try:
            lexer = self.__createLexer("f", CSVFormat.DEFAULT.withEscape0("\f"))
            ch = lexer.readEscape()
            self.assertEqual(ch, ord("\f"))
        finally:
            lexer.close()

    def testReadEscapeBackspace(self) -> None:

        lexer = self.__createLexer("b", CSVFormat.DEFAULT.withEscape0("\b"))
        try:
            ch = lexer.readEscape()
            self.assertEqual(ord(Constants.BACKSPACE), ch)
        finally:
            lexer.close()

    def testIsMetaCharCommentStart(self) -> None:

        lexer = self.__createLexer(
            "#", CSVFormat.DEFAULT.withCommentMarker0("#")
        )
        try:
            ch = lexer.readEscape()
            self.assertEqual(ord("#"), ch)
        finally:
            lexer.close()

    def testEscapingAtEOF(self) -> None:

        code = "escaping at EOF is evil\\"
        lexer = self.__createLexer(code, self.__formatWithEscaping)
        try:
            with pytest.raises(IOError):
                lexer.nextToken(Token())
        finally:
            lexer.close()

    def setUp(self) -> None:
        self.__formatWithEscaping = CSVFormat.DEFAULT.withEscape0("\\")

    def __createLexer(self, input_: str, format_: CSVFormat) -> Lexer:

        return Lexer(format_, ExtendedBufferedReader(io.StringIO(input_)))
