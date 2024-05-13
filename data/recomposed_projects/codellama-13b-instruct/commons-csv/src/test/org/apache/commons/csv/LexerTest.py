# Imports Begin
from src.main.org.apache.commons.csv.Token import *
from src.main.org.apache.commons.csv.Lexer import *
from src.main.org.apache.commons.csv.ExtendedBufferedReader import *
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.CSVFormat import *
import unittest
import os
# Imports End

class new Executable(...) { ... }(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def execute(self) -> None:

            self.assertRaises(IOException, lexer.nextToken, Token())

    # Class Methods End


class LexerTest(unittest.TestCase):

    # Class Fields Begin
    __formatWithEscaping: CSVFormat = None
    # Class Fields End

    # Class Methods Begin
    def testReadEscapeFF(self) -> None:

            try:
                lexer = self.__createLexer("f", CSVFormat.DEFAULT.withEscape0('\f'))
                ch = lexer.readEscape()
                self.assertEqual(FF, ch)
            except Exception as e:
                self.fail(f"Unexpected exception: {e}")

    def testReadEscapeBackspace(self) -> None:

            try:
                lexer = self.__createLexer("b", CSVFormat.DEFAULT.withEscape0('\b'))
                ch = lexer.readEscape()
                self.assertEqual(BACKSPACE, ch)
            except Exception as e:
                self.fail(f"Unexpected exception: {e}")

    def testIsMetaCharCommentStart(self) -> None:

            lexer = self.__createLexer("#", CSVFormat.DEFAULT.withCommentMarker0('#'))
            try:
                ch = lexer.readEscape()
                self.assertEqual('#', ch)
            finally:
                lexer.close()

    def testEscapingAtEOF(self) -> None:

            code = "escaping at EOF is evil\\"
            try:
                lexer = self.__createLexer(code, self.__formatWithEscaping)
                self.assertRaises(Exception, lexer.nextToken, Token())
            finally:
                lexer.close()

    def setUp(self) -> None:

            self.formatWithEscaping = CSVFormat.DEFAULT.withEscape0('\\')

    def __createLexer(self, input: str, format: CSVFormat) -> Lexer:

            return Lexer(format, ExtendedBufferedReader(StringReader(input)))

    # Class Methods End


