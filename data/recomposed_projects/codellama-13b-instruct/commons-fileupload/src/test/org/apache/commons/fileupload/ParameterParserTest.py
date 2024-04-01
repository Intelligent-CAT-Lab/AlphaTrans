# Imports Begin
from src.main.org.apache.commons.fileupload.ParameterParser import *
import unittest
import os
import typing
from typing import *

# Imports End


class ParameterParserTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def fileUpload199(self) -> None:

        parser = ParameterParser()
        s = 'Content-Disposition: form-data; name="file"; filename="=?ISO-8859-1?B?SWYgeW91IGNhbiByZWFkIHRoaXMgeW8=?= =?ISO-8859-2?B?dSB1bmRlcnN0YW5kIHRoZSBleGFtcGxlLg==?="\r\n'
        params = parser.parse0(s, [",", ";"])
        assert params["filename"] == "If you can read this you understand the example."

    def testFileUpload139(self) -> None:

        parser = ParameterParser()
        s = "Content-type: multipart/form-data , boundary=AaB03x"
        params = parser.parse0(s, [",", ";"])
        assert params["boundary"] == "AaB03x"
        s = "Content-type: multipart/form-data, boundary=AaB03x"
        params = parser.parse0(s, [";", ","])
        assert params["boundary"] == "AaB03x"
        s = "Content-type: multipart/mixed, boundary=BbC04y"
        params = parser.parse0(s, [",", ";"])
        assert params["boundary"] == "BbC04y"

    def testParsingEscapedChars(self) -> None:

        s = 'param = "stuff\\"; more stuff"'
        params = self.parse1(s, ";")
        self.assertEqual(len(params), 1)
        self.assertEqual(params["param"], 'stuff\\"; more stuff')
        s = 'param = "stuff\\\\"; anotherparam'
        params = self.parse1(s, ";")
        self.assertEqual(len(params), 2)
        self.assertEqual(params["param"], "stuff\\\\")
        self.assertIsNone(params.get("anotherparam"))

    def testContentTypeParsing(self) -> None:

        s = "text/plain; Charset=UTF-8"
        parser = ParameterParser()
        parser.setLowerCaseNames(True)
        params = parser.parse1(s, ";")
        assert params["charset"] == "UTF-8"

    def testParsing(self) -> None:

        s = 'test; test1 =  stuff   ; test2 =  "stuff; stuff"; test3="stuff'
        parser = ParameterParser()
        params = parser.parse1(s, ";")
        assert params["test1"] == "stuff"
        assert params["test2"] == "stuff; stuff"
        assert params["test3"] == '"stuff'
        params = parser.parse0(s, [",", ";"])
        assert params["test1"] == "stuff"
        assert params["test2"] == "stuff; stuff"
        assert params["test3"] == '"stuff'
        s = "  test  , test1=stuff   ,  , test2=, test3, "
        params = parser.parse1(s, ",")
        assert params["test1"] == "stuff"
        assert params["test2"] == None
        assert params["test3"] == None
        s = "  test"
        params = parser.parse1(s, ";")
        assert params["test"] == None
        s = "  "
        params = parser.parse1(s, ";")
        assert len(params) == 0
        s = " = stuff "
        params = parser.parse1(s, ";")
        assert len(params) == 0

    # Class Methods End
