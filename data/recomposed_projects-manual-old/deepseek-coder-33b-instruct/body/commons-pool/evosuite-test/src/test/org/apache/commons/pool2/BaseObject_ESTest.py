from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.pool2.BaseObject import *

# from src.test.org.apache.commons.pool2.BaseObject_ESTest_scaffolding import *
from src.main.org.apache.commons.pool2.impl.GenericObjectPoolConfig import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class BaseObject_ESTest(unittest.TestCase):

    def test1(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        string0 = genericObjectPoolConfig0.toString()
        expected_string = "GenericObjectPoolConfig [lifo=true, fairness=false, maxWaitDuration=PT-0.001S, minEvictableIdleTime=PT30M, softMinEvictableIdleTime=PT-0.001S, numTestsPerEvictionRun=3, evictionPolicyClassName=org.apache.commons.pool2.impl.DefaultEvictionPolicy, testOnCreate=false, testOnBorrow=false, testOnReturn=false, testWhileIdle=false, timeBetweenEvictionRuns=PT-0.001S, blockWhenExhausted=true, jmxEnabled=true, jmxNamePrefix=pool, jmxNameBase=null, maxTotal=8, maxIdle=8, minIdle=0]"
        self.assertEqual(string0, expected_string)

    def test0(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        try:
            genericObjectPoolConfig0._toStringAppendFields(None)
            self.fail("Expecting exception: RuntimeError")
        except Exception as e:
            self.verifyException(
                "org.apache.commons.pool2.impl.BaseObjectPoolConfig", e
            )
