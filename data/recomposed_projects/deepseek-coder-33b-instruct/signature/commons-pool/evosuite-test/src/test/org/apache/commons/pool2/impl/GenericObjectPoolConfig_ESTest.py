from __future__ import annotations
import time
import re
import os
from io import StringIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.pool2.impl.GenericObjectPoolConfig import *

# from src.test.org.apache.commons.pool2.impl.GenericObjectPoolConfig_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class GenericObjectPoolConfig_ESTest(unittest.TestCase):

    def test28(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        self.assertEqual(0, genericObjectPoolConfig0.getMinIdle())

        genericObjectPoolConfig0.setMinIdle(8)
        int0 = genericObjectPoolConfig0.getMinIdle()
        self.assertEqual(8, int0)

    def test27(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig[int]()
        int0 = genericObjectPoolConfig0.getMaxIdle()
        self.assertEqual(0, genericObjectPoolConfig0.getMinIdle())
        self.assertEqual(8, int0)
        self.assertEqual(8, genericObjectPoolConfig0.getMaxTotal())

    def test26(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig[
            GenericObjectPoolConfig[object]
        ]()
        int0 = genericObjectPoolConfig0.getMaxTotal()
        self.assertEqual(8, genericObjectPoolConfig0.getMaxIdle())
        self.assertEqual(8, int0)
        self.assertEqual(0, genericObjectPoolConfig0.getMinIdle())

    def test25(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig[
            GenericObjectPoolConfig[object]
        ]()
        int0 = genericObjectPoolConfig0.getMinIdle()
        self.assertEqual(0, int0)
        self.assertEqual(8, genericObjectPoolConfig0.getMaxTotal())
        self.assertEqual(8, genericObjectPoolConfig0.getMaxIdle())

    def test24(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig[int]()
        genericObjectPoolConfig0.setMaxIdle(-1485)
        genericObjectPoolConfig0.clone()
        self.assertEqual(-1485, genericObjectPoolConfig0.getMaxIdle())

    def test23(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig[int]()
        try:
            genericObjectPoolConfig0.toStringAppendFields(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.pool2.impl.BaseObjectPoolConfig", e)

    def test22(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        genericObjectPoolConfig0.setBlockWhenExhausted(False)
        genericObjectPoolConfig1 = genericObjectPoolConfig0.clone()
        self.assertEqual(8, genericObjectPoolConfig1.getMaxIdle())
        self.assertEqual(0, genericObjectPoolConfig1.getMinIdle())
        self.assertEqual(8, genericObjectPoolConfig1.getMaxTotal())

    def test21(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig[int]()
        genericObjectPoolConfig0.setFairness(True)
        genericObjectPoolConfig1 = genericObjectPoolConfig0.clone()
        self.assertEqual(8, genericObjectPoolConfig1.getMaxIdle())
        self.assertEqual(0, genericObjectPoolConfig1.getMinIdle())
        self.assertEqual(8, genericObjectPoolConfig1.getMaxTotal())

    def test20(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig[int]()
        genericObjectPoolConfig0.setJmxEnabled(False)
        genericObjectPoolConfig1 = genericObjectPoolConfig0.clone()
        self.assertEqual(8, genericObjectPoolConfig1.getMaxIdle())
        self.assertEqual(0, genericObjectPoolConfig1.getMinIdle())
        self.assertEqual(8, genericObjectPoolConfig1.getMaxTotal())

    def test19(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        genericObjectPoolConfig0.setLifo(False)
        genericObjectPoolConfig1 = genericObjectPoolConfig0.clone()
        self.assertEqual(8, genericObjectPoolConfig1.getMaxIdle())
        self.assertEqual(0, genericObjectPoolConfig1.getMinIdle())
        self.assertEqual(8, genericObjectPoolConfig1.getMaxTotal())

    def test18(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        self.assertEqual(8, genericObjectPoolConfig0.getMaxIdle())

        genericObjectPoolConfig0.setMaxIdle(0)
        genericObjectPoolConfig0.clone()
        self.assertEqual(0, genericObjectPoolConfig0.getMaxIdle())

    def test17(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        genericObjectPoolConfig0.setMaxTotal(-1757)
        genericObjectPoolConfig0.clone()
        self.assertEqual(-1757, genericObjectPoolConfig0.getMaxTotal())

    def test16(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig[int]()
        self.assertEqual(8, genericObjectPoolConfig0.getMaxTotal())

        genericObjectPoolConfig0.setMaxTotal(0)
        genericObjectPoolConfig0.clone()
        self.assertEqual(0, genericObjectPoolConfig0.getMaxTotal())

    def test15(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        genericObjectPoolConfig0.setMinIdle(-1464)
        genericObjectPoolConfig0.clone()
        self.assertEqual(-1464, genericObjectPoolConfig0.getMinIdle())

    def test14(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig[int]()
        genericObjectPoolConfig0.setMinIdle(125)
        genericObjectPoolConfig0.clone()
        self.assertEqual(125, genericObjectPoolConfig0.getMinIdle())

    def test13(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        genericObjectPoolConfig0.setNumTestsPerEvictionRun(-899)
        genericObjectPoolConfig1 = genericObjectPoolConfig0.clone()
        self.assertEqual(8, genericObjectPoolConfig1.getMaxIdle())
        self.assertEqual(0, genericObjectPoolConfig1.getMinIdle())
        self.assertEqual(8, genericObjectPoolConfig1.getMaxTotal())

    def test12(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig[
            GenericObjectPoolConfig[object]
        ]()
        genericObjectPoolConfig0.setNumTestsPerEvictionRun(0)
        genericObjectPoolConfig1 = genericObjectPoolConfig0.clone()
        self.assertEqual(0, genericObjectPoolConfig1.getMinIdle())
        self.assertEqual(8, genericObjectPoolConfig1.getMaxTotal())
        self.assertEqual(8, genericObjectPoolConfig1.getMaxIdle())

    def test11(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        genericObjectPoolConfig0.setTestOnBorrow(True)
        genericObjectPoolConfig1 = genericObjectPoolConfig0.clone()

        self.assertEqual(8, genericObjectPoolConfig1.getMaxIdle())
        self.assertEqual(0, genericObjectPoolConfig1.getMinIdle())
        self.assertEqual(8, genericObjectPoolConfig1.getMaxTotal())

    def test10(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        genericObjectPoolConfig0.setTestOnCreate(True)
        genericObjectPoolConfig1 = genericObjectPoolConfig0.clone()

        self.assertEqual(8, genericObjectPoolConfig1.getMaxTotal())
        self.assertEqual(0, genericObjectPoolConfig1.getMinIdle())
        self.assertEqual(8, genericObjectPoolConfig1.getMaxIdle())

    def test09(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig[
            GenericObjectPoolConfig[int]
        ]()
        genericObjectPoolConfig0.setTestOnReturn(True)
        genericObjectPoolConfig1 = genericObjectPoolConfig0.clone()

        self.assertEqual(8, genericObjectPoolConfig1.getMaxIdle())
        self.assertEqual(8, genericObjectPoolConfig1.getMaxTotal())
        self.assertEqual(0, genericObjectPoolConfig1.getMinIdle())

    def test08(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        genericObjectPoolConfig0.setTestWhileIdle(True)
        genericObjectPoolConfig1 = genericObjectPoolConfig0.clone()
        self.assertEqual(8, genericObjectPoolConfig1.getMaxIdle())
        self.assertEqual(0, genericObjectPoolConfig1.getMinIdle())
        self.assertEqual(8, genericObjectPoolConfig1.getMaxTotal())

    def test07(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig[int]()
        genericObjectPoolConfig0.setMaxIdle(-1485)
        int0 = genericObjectPoolConfig0.getMaxIdle()
        self.assertEqual(-1485, int0)

    def test06(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        self.assertEqual(8, genericObjectPoolConfig0.getMaxIdle())

        genericObjectPoolConfig0.setMaxIdle(0)
        int0 = genericObjectPoolConfig0.getMaxIdle()
        self.assertEqual(0, int0)

    def test05(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        genericObjectPoolConfig0.setMaxTotal(-1299)
        int0 = genericObjectPoolConfig0.getMaxTotal()
        self.assertEqual(-1299, int0)

    def test04(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        self.assertEqual(8, genericObjectPoolConfig0.getMaxTotal())

        genericObjectPoolConfig0.setMaxTotal(0)
        int0 = genericObjectPoolConfig0.getMaxTotal()
        self.assertEqual(0, int0)

    def test03(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig[
            GenericObjectPoolConfig[object]
        ]()
        genericObjectPoolConfig0.setMinIdle(-1050)
        int0 = genericObjectPoolConfig0.getMinIdle()
        self.assertEqual(-1050, int0)

    def test02(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        genericObjectPoolConfig0.setMaxTotal(1)
        stringBuilder0 = StringBuilder(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy"
        )
        genericObjectPoolConfig0.toStringAppendFields(stringBuilder0)
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicylifo=true, fairness=false, maxWaitDuration=PT-0.001S, minEvictableIdleTime=PT30M, softMinEvictableIdleTime=PT-0.001S, numTestsPerEvictionRun=3, evictionPolicyClassName=org.apache.commons.pool2.impl.DefaultEvictionPolicy, testOnCreate=false, testOnBorrow=false, testOnReturn=false, testWhileIdle=false, timeBetweenEvictionRuns=PT-0.001S, blockWhenExhausted=true, jmxEnabled=true, jmxNamePrefix=pool, jmxNameBase=null, maxTotal=1, maxIdle=8, minIdle=0",
            stringBuilder0.toString(),
        )

    def test01(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        stringBuilder0 = StringBuilder("}PZkZWT;")
        genericObjectPoolConfig0.setMaxIdle(467)
        genericObjectPoolConfig0.toStringAppendFields(stringBuilder0)
        self.assertEqual(467, genericObjectPoolConfig0.getMaxIdle())

    def test00(self) -> None:

        stringBuilder0 = io.StringIO(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy"
        )
        genericObjectPoolConfig0 = GenericObjectPoolConfig[int]()
        genericObjectPoolConfig0.setMinIdle(-1)
        genericObjectPoolConfig0.toStringAppendFields(stringBuilder0)
        self.assertEqual(-1, genericObjectPoolConfig0.getMinIdle())
