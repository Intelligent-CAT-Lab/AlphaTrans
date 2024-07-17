import pytest

from src.main.org.apache.commons.csv.IOUtils import *
import unittest

class IOUtilsTest(unittest.TestCase):

    @pytest.mark.test
    def testRethrow(self) -> None:
        with self.assertRaises((IOError, OSError)):
            IOUtils.rethrow(IOError())
