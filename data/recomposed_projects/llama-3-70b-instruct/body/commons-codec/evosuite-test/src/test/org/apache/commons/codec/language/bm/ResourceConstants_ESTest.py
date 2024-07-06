from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.language.bm.ResourceConstants import *

# from src.test.org.apache.commons.codec.language.bm.ResourceConstants_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class ResourceConstants_ESTest(unittest.TestCase):

    def test0(self) -> None:
        resourceConstants0 = ResourceConstants()
