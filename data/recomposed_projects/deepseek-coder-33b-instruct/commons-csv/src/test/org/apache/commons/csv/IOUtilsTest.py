from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.apache.commons.csv.IOUtils import *


class IOUtilsTest(unittest.TestCase):

    @pytest.mark.test
    def testRethrow(self) -> None:

        with pytest.raises(IOError):
            IOUtils.rethrow(IOError())
