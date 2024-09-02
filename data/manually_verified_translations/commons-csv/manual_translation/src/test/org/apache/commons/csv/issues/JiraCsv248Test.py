from __future__ import annotations
import pickle
import re
import os
import numbers
import unittest
import pytest
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
import unittest
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVRecord import *


class JiraCsv248Test(unittest.TestCase):

    @staticmethod
    def __getTestInput() -> io.BufferedReader:
        resourcePath = Path(__file__).resolve()\
        .parent.parent.parent.parent.parent.parent \
        / 'resources' / 'org' / 'apache' / 'commons' / 'csv' / 'CSV-248' / 'csvRecord.bin'
        return resourcePath.open('rb')

    
    def testJiraCsv248(self) -> None:
        obj = CSVRecord(None, ["One", "Two"], "my comment", 1, 4)
        pythonResourcePath = Path(__file__).resolve()\
                .parent.parent.parent.parent.parent.parent \
                / 'resources' / 'org' / 'apache' / 'commons' / 'csv' / 'CSV-248' / 'csvRecordPython.bin'
        with open(pythonResourcePath, 'wb') as file:
            pickle.dump(obj, file)
        inStream = pythonResourcePath.open('rb')
        try:
            ois = pickle.load(inStream)
            self.assertTrue(isinstance(ois, CSVRecord))
            rec = ois
            self.assertEqual(1, rec.getRecordNumber())
            self.assertEqual("One", rec.get1(0))
            self.assertEqual("Two", rec.get1(1))
            self.assertEqual(2, rec.size())
            self.assertEqual(4, rec.getCharacterPosition())
            self.assertEqual("my comment", rec.getComment())
            self.assertIsNone(rec.getParser())
            self.assertTrue(rec.isConsistent())
            self.assertFalse(rec.isMapped("A"))
            self.assertFalse(rec.isSet1("A"))
            self.assertEqual(0, len(rec.toMap()))
            try:
                rec.get2("A")
                self.fail("Access by name is not expected after deserialisation")
            except RuntimeError as expected:
                pass
        finally:
            inStream.close()
            if pythonResourcePath.exists() and pythonResourcePath.is_file():
                pythonResourcePath.unlink()

    # def testJiraCsv248(self) -> None:

    #     with self.__getTestInput() as inp:
    #         ois = ObjectInputStream(inp)
    #         object = ois.readObject()
    #         self.assertTrue(isinstance(object, CSVRecord))
    #         rec = object
    #         self.assertEqual(1, rec.getRecordNumber())
    #         self.assertEqual("One", rec.get1(0))
    #         self.assertEqual("Two", rec.get1(1))
    #         self.assertEqual(2, rec.size())
    #         self.assertEqual(4, rec.getCharacterPosition())
    #         self.assertEqual("my comment", rec.getComment())
    #         self.assertIsNone(rec.getParser())
    #         self.assertTrue(rec.isConsistent())
    #         self.assertFalse(rec.isMapped("A"))
    #         self.assertFalse(rec.isSet1("A"))
    #         self.assertEqual(0, len(rec.toMap()))
    #         try:
    #             rec.get2("A")
    #             self.fail("Access by name is not expected after deserialisation")
    #         except RuntimeError:
    #             pass

    # @staticmethod
    # def __getTestInput() -> typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]:
    #     resourcePath = Path(__file__).resolve()\
    #     .parent.parent.parent.parent.parent.parent \
    #     / 'resources' / 'org' / 'apache' / 'commons' / 'csv' / 'CSV-248' / 'csvRecord.bin'
    #     return resourcePath.open('rb')
