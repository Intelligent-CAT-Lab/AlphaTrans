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

        with self.__createLexer("b", CSVFormat.DEFAULT.withEscape0("\b")) as lexer:
            ch = lexer.readEscape()
            self.assertEqual(ord(Constants.BACKSPACE), ch)

    def testIsMetaCharCommentStart(self) -> None:

        with self.__createLexer(
            "#", CSVFormat.DEFAULT.withCommentMarker0("#")
        ) as lexer:
            ch = lexer.readEscape()
            self.assertEqual(ord("#"), ch)

    def testEscapingAtEOF(self) -> None:

        code = "escaping at EOF is evil\\"
        with self.__createLexer(code, self.__formatWithEscaping) as lexer:
            with pytest.raises(IOError):
                lexer.nextToken(Token())

    def setUp(self) -> None:
        self.__formatWithEscaping = CSVFormat.DEFAULT.withEscape0("\\")

    def __createLexer(self, input_: str, format_: CSVFormat) -> Lexer:

        return Lexer(format_, ExtendedBufferedReader(io.StringIO(input_)))
