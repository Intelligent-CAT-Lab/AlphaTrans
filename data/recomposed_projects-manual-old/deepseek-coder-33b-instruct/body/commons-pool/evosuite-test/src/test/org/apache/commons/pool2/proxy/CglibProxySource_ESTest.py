from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.pool2.proxy.CglibProxySource import *

# from src.test.org.apache.commons.pool2.proxy.CglibProxySource_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class CglibProxySource_ESTest(unittest.TestCase):

    def test0(self) -> None:

        class0 = object
        cglibProxySource0 = CglibProxySource(class0)
        string0 = cglibProxySource0.__str__()
        self.assertEqual(
            "CglibProxySource [superclass=class java.lang.Object]", string0
        )
