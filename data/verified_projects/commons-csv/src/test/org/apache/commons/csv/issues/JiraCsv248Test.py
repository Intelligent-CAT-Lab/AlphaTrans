import pytest

from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.CSVParser import *
import pickle
import unittest
import io
from pathlib import Path

class JiraCsv248Test(unittest.TestCase):

    @staticmethod
    def __getTestInput() -> io.BufferedReader:
        resourcePath = Path(__file__).resolve()\
        .parent.parent.parent.parent.parent.parent \
        / 'resources' / 'org' / 'apache' / 'commons' / 'csv' / 'CSV-248' / 'csvRecord.bin'
        return resourcePath.open('rb')

    
    @pytest.mark.test
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
