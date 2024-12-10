from __future__ import annotations
import re
import os
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.fileupload.ParameterParser import *


class ParameterParserTest(unittest.TestCase):

    def testfileUpload199(self) -> None:

        parser = ParameterParser()
        s = (
            'Content-Disposition: form-data; name="file";'
            + ' filename="=?ISO-8859-1?B?SWYgeW91IGNhbiByZWFkIHRoaXMgeW8=?='
            + ' =?ISO-8859-2?B?dSB1bmRlcnN0YW5kIHRoZSBleGFtcGxlLg==?="\r\n'
        )
        params = parser.parse0(s, [",", ";"])
        self.assertEqual(
            "If you can read this you understand the example.", params.get("filename")
        )

    def testFileUpload139(self) -> None:

        parser = ParameterParser()
        s = "Content-type: multipart/form-data , boundary=AaB03x"
        params = parser.parse0(s, [",", ";"])
        self.assertEqual("AaB03x", params.get("boundary"))

        s = "Content-type: multipart/form-data, boundary=AaB03x"
        params = parser.parse0(s, [";", ","])
        self.assertEqual("AaB03x", params.get("boundary"))

        s = "Content-type: multipart/mixed, boundary=BbC04y"
        params = parser.parse0(s, [",", ";"])
        self.assertEqual("BbC04y", params.get("boundary"))

    def testParsingEscapedChars(self) -> None:

        s = 'param = "stuff\\"; more stuff"'
        parser = ParameterParser()
        params = parser.parse1(s, ";")
        self.assertEqual(1, len(params))
        self.assertEqual('stuff\\"; more stuff', params.get("param"))

        s = 'param = "stuff\\\\"; anotherparam'
        params = parser.parse1(s, ";")
        self.assertEqual(2, len(params))
        self.assertEqual("stuff\\\\", params.get("param"))
        self.assertIsNone(params.get("anotherparam"))

    def testContentTypeParsing(self) -> None:

        s = "text/plain; Charset=UTF-8"
        parser = ParameterParser()
        parser.setLowerCaseNames(True)
        params = parser.parse1(s, ";")
        self.assertEqual("UTF-8", params.get("charset"))

    def testParsing(self) -> None:

        s = 'test; test1 =  stuff   ; test2 =  "stuff; stuff"; test3="stuff'
        parser = ParameterParser()
        params = parser.parse1(s, ";")
        self.assertEqual(None, params.get("test"))
        self.assertEqual("stuff", params.get("test1"))
        self.assertEqual("stuff; stuff", params.get("test2"))
        self.assertEqual('"stuff', params.get("test3"))

        params = parser.parse0(s, [",", ";"])
        self.assertEqual(None, params.get("test"))
        self.assertEqual("stuff", params.get("test1"))
        self.assertEqual("stuff; stuff", params.get("test2"))
        self.assertEqual('"stuff', params.get("test3"))

        s = "  test  , test1=stuff   ,  , test2=, test3, "
        params = parser.parse1(s, ",")
        self.assertEqual(None, params.get("test"))
        self.assertEqual("stuff", params.get("test1"))
        self.assertEqual(None, params.get("test2"))
        self.assertEqual(None, params.get("test3"))

        s = "  test"
        params = parser.parse1(s, ";")
        self.assertEqual(None, params.get("test"))

        s = "  "
        params = parser.parse1(s, ";")
        self.assertEqual(0, len(params))

        s = " = stuff "
        params = parser.parse1(s, ";")
        self.assertEqual(0, len(params))
