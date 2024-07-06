from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.pool2.impl.SecurityManagerCallStack import *

# from src.test.org.apache.commons.pool2.impl.SecurityManagerCallStack_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class SecurityManagerCallStack_ESTest(unittest.TestCase):

    def test0(self) -> None:
        securityManagerCallStack0 = SecurityManagerCallStack()
        securityManagerCallStack0.clear()
