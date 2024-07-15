from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.fileupload.util.Streams import *

# from src.test.org.apache.commons.fileupload.util.Streams_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Streams_ESTest(unittest.TestCase):

    def test2(self) -> None:
        string0 = Streams.checkFileName(None)
        self.assertIsNone(string0)

    def test1(self) -> None:
        string0 = Streams.checkFileName("")
        self.assertEqual("", string0)

    def test0(self) -> None:
        string0 = Streams.checkFileName("org.apache.commons.fileupload.util.Streams")
        self.assertEqual("org.apache.commons.fileupload.util.Streams", string0)
