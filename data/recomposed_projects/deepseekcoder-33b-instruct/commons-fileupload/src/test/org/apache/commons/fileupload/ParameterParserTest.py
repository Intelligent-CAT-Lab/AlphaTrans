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
        s = (
            'Content-Disposition: form-data; name="file";'
            + ' filename="=?ISO-8859-1?B?SWYgeW91IGNhbiByZWFkIHRoaXMgeW8=?='
            + ' =?ISO-8859-2?B?dSB1bmRlcnN0YW5kIHRoZSBleGFtcGxlLg==?="\r\n'
        )
        params = parser.parse0(s, [",", ";"])
        self.assertTrue(
            params.get("filename") == "If you can read this you understand the example."
        )

    def testFileUpload139(self) -> None:

        parser = ParameterParser()
        s = "Content-type: multipart/form-data , boundary=AaB03x"
        params = parser.parse0(s, [",", ";"])
        self.assertTrue(params.get("boundary") == "AaB03x")
        s = "Content-type: multipart/form-data, boundary=AaB03x"
        params = parser.parse0(s, [";", ","])
        self.assertTrue(params.get("boundary") == "AaB03x")
        s = "Content-type: multipart/mixed, boundary=BbC04y"
        params = parser.parse0(s, [",", ";"])
        self.assertTrue(params.get("boundary") == "BbC04y")

    def testParsingEscapedChars(self) -> None:

        s = 'param = "stuff\\"; more stuff"'
        parser = ParameterParser()
        params = parser.parse1(s, ";")
        self.assertEqual(1, len(params))
        self.assertEqual('stuff\\"; more stuff', params["param"])
        s = 'param = "stuff\\\\"; anotherparam'
        params = parser.parse1(s, ";")
        self.assertEqual(2, len(params))
        self.assertEqual("stuff\\\\", params["param"])
        self.assertIsNone(params.get("anotherparam"))

    def testContentTypeParsing(self) -> None:

        s = "text/plain; Charset=UTF-8"
        parser = ParameterParser()
        parser.setLowerCaseNames(True)
        params = parser.parse1(s, ";")
        self.assertTrue(params.get("charset") == "UTF-8")

    def testParsing(self) -> None:

        s = 'test; test1 =  stuff   ; test2 =  "stuff; stuff"; test3="stuff'
        parser = ParameterParser()
        params = parser.parse1(s, ";")
        self.assertTrue(params.get("test") is None)
        self.assertTrue(params.get("test1") == "stuff")
        self.assertTrue(params.get("test2") == "stuff; stuff")
        self.assertTrue(params.get("test3") == '"stuff')
        params = parser.parse0(s, [",", ";"])
        self.assertTrue(params.get("test") is None)
        self.assertTrue(params.get("test1") == "stuff")
        self.assertTrue(params.get("test2") == "stuff; stuff")
        self.assertTrue(params.get("test3") == '"stuff')
        s = "  test  , test1=stuff   ,  , test2=, test3, "
        params = parser.parse1(s, ",")
        self.assertTrue(params.get("test") is None)
        self.assertTrue(params.get("test1") == "stuff")
        self.assertTrue(params.get("test2") is None)
        self.assertTrue(params.get("test3") is None)
        s = "  test"
        params = parser.parse1(s, ";")
        self.assertTrue(params.get("test") is None)
        s = "  "
        params = parser.parse1(s, ";")
        self.assertTrue(len(params) == 0)
        s = " = stuff "
        params = parser.parse1(s, ";")
        self.assertTrue(len(params) == 0)

    # Class Methods End
