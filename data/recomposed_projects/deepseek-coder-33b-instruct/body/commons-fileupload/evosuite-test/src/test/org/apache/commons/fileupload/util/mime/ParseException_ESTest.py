from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.fileupload.util.mime.ParseException import *

# from src.test.org.apache.commons.fileupload.util.mime.ParseException_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class ParseException_ESTest(unittest.TestCase):

    def test0(self) -> None:
        parseException0 = ParseException(None)
