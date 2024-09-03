import pytest

from src.main.org.apache.commons.csv.Token import *
from src.main.org.apache.commons.csv.Lexer import *
from src.main.org.apache.commons.csv.ExtendedBufferedReader import *
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.CSVFormat import *
import unittest
import io


class LexerTest(unittest.TestCase):

    __formatWithEscaping = None

    
    def __createLexer(self, input, format) -> Lexer:
        return Lexer(format, ExtendedBufferedReader(io.StringIO(input)))

    
    def setUp(self) -> None:
        self.__formatWithEscaping = CSVFormat.DEFAULT.withEscape0('\\')

    
    @pytest.mark.test
    def testEscapingAtEOF(self) -> None:
        try:
            code = "escaping at EOF is evil\\"
            lexer = self.__createLexer(code, self.__formatWithEscaping)
            try:
                with self.assertRaises((IOError, OSError)):
                    lexer.nextToken(Token())
            finally:
                lexer.close()
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testIsMetaCharCommentStart(self) -> None:
        try:
            lexer = self.__createLexer("#", CSVFormat.DEFAULT.withCommentMarker0('#'))
            try:
                ch = lexer.readEscape()
                self.assertEqual('#', chr(ch))
            finally:
                lexer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testReadEscapeBackspace(self) -> None:
        try:
            lexer = self.__createLexer("b", CSVFormat.DEFAULT.withEscape0('\b'))
            try:
                ch = lexer.readEscape()
                self.assertEqual(Constants.BACKSPACE, chr(ch))
            finally:
                lexer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testReadEscapeFF(self) -> None:
        try:
            lexer = self.__createLexer("f", CSVFormat.DEFAULT.withEscape0('\f'))
            try:
                ch = lexer.readEscape()
                self.assertEqual(Constants.FF, chr(ch))
            finally:
                lexer.close()
        except (IOError, OSError) as e:
            self.fail(f"An unexpected exception occurred: {e}")
