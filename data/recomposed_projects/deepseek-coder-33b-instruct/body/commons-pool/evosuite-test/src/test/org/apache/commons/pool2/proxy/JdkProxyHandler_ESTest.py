from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.pool2.UsageTracking import *
from src.main.org.apache.commons.pool2.proxy.JdkProxyHandler import *

# from src.test.org.apache.commons.pool2.proxy.JdkProxyHandler_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class JdkProxyHandler_ESTest(unittest.TestCase):

    def test1(self) -> None:

        objectArray0 = [None] * 9
        jdkProxyHandler0 = JdkProxyHandler(None, None)

        try:
            jdkProxyHandler0.invoke(None, None, objectArray0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # This object may no longer be used as it has been returned to the Object Pool.
            self.verifyException("org.apache.commons.pool2.proxy.BaseProxyHandler", e)

    def test0(self) -> None:

        objectArray0 = [None] * 9
        integer0 = -733
        jdkProxyHandler0 = JdkProxyHandler(integer0, None)

        try:
            jdkProxyHandler0.invoke(integer0, None, objectArray0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("org.apache.commons.pool2.proxy.BaseProxyHandler", e)
