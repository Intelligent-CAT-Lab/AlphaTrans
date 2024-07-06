from __future__ import annotations
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

    def testJiraCsv248(self) -> None:
        with self.__getTestInput() as in_:
            with ObjectInputStream(in_) as ois:
                object_ = ois.readObject()
                self.assertTrue(isinstance(object_, CSVRecord))
                rec = typing.cast(CSVRecord, object_)
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
                with self.assertRaises(RuntimeError):
                    rec.get2("A")

    @staticmethod
    def __getTestInput() -> typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]:
        return ClassLoader.getSystemClassLoader().getResourceAsStream(
            "org/apache/commons/csv/CSV-248/csvRecord.bin"
        )
