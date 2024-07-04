from __future__ import annotations
import time
import re
import mock
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.fileupload.DefaultFileItemFactory import *

# from src.test.org.apache.commons.fileupload.DefaultFileItemFactory_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class DefaultFileItemFactory_ESTest(unittest.TestCase):

    def test1(self) -> None:
        defaultFileItemFactory0 = DefaultFileItemFactory.DefaultFileItemFactory1()
        self.assertEqual(0, defaultFileItemFactory0.getSizeThreshold())

    def test0(self) -> None:
        mockFile0 = MockFile("C5AWUwSj8ab#HRV;P", "V_rMYkO'#++=toF5an6")
        defaultFileItemFactory0 = DefaultFileItemFactory(2515, mockFile0)
        self.assertEqual("ISO-8859-1", defaultFileItemFactory0.getDefaultCharset())
