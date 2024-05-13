# Imports Begin
from src.main.org.apache.commons.csv.IOUtils import *
import unittest
# Imports End

class new Executable(...) { ... }(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def execute(self) -> None:

            try:
                IOUtils.rethrow(IOException())
            except IOException as e:
                self.assertTrue(isinstance(e, IOException))

    # Class Methods End


class IOUtilsTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testRethrow(self) -> None:

            with self.assertRaises(IOException):
                IOUtils.rethrow(IOException())

    # Class Methods End


