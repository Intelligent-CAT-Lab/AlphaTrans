from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.digest.Md5Crypt import *

# from src.test.org.apache.commons.codec.digest.Md5Crypt_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Md5Crypt_ESTest(unittest.TestCase):

    def test0(self) -> None:
        md5Crypt0 = Md5Crypt()
