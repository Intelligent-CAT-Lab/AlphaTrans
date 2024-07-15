from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.digest.Crypt import *

# from src.test.org.apache.commons.codec.digest.Crypt_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Crypt_ESTest(unittest.TestCase):

    def test0(self) -> None:
        crypt0 = Crypt()
