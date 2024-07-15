from __future__ import annotations
import time
import re
import mock
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.fileupload.DefaultFileItem import *

# from src.test.org.apache.commons.fileupload.DefaultFileItem_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class DefaultFileItem_ESTest(unittest.TestCase):

    def test0(self) -> None:

        mockFile0 = MockFile(None, "`abs4bMIr@1s")
        defaultFileItem0 = DefaultFileItem(")(", ")(", True, ")(", 3626, mockFile0)
        self.assertEqual(")(", defaultFileItem0.getFieldName())
