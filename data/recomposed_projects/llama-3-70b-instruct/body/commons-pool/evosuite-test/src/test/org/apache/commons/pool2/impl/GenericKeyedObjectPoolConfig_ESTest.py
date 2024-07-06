from __future__ import annotations
import time
import re
import os
from io import StringIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.pool2.impl.GenericKeyedObjectPoolConfig import *

# from src.test.org.apache.commons.pool2.impl.GenericKeyedObjectPoolConfig_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class GenericKeyedObjectPoolConfig_ESTest(unittest.TestCase):

    def test34(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[int]()
        self.assertEqual(-1, genericKeyedObjectPoolConfig0.getMaxTotal())

        genericKeyedObjectPoolConfig0.setMaxTotal(0)
        genericKeyedObjectPoolConfig0.clone()
        self.assertEqual(0, genericKeyedObjectPoolConfig0.getMaxTotal())

    def test33(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[int]()
        int0 = genericKeyedObjectPoolConfig0.getMaxTotal()
        self.assertEqual(8, genericKeyedObjectPoolConfig0.getMaxIdlePerKey())
        self.assertEqual(8, genericKeyedObjectPoolConfig0.getMaxTotalPerKey())
        self.assertEqual(-1, int0)
        self.assertEqual(0, genericKeyedObjectPoolConfig0.getMinIdlePerKey())

    def test32(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[int]()
        int0 = genericKeyedObjectPoolConfig0.getMaxTotalPerKey()
        self.assertEqual(0, genericKeyedObjectPoolConfig0.getMinIdlePerKey())
        self.assertEqual(-1, genericKeyedObjectPoolConfig0.getMaxTotal())
        self.assertEqual(8, int0)
        self.assertEqual(8, genericKeyedObjectPoolConfig0.getMaxIdlePerKey())

    def test31(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig()
        genericKeyedObjectPoolConfig0.setMinIdlePerKey(-1)
        genericKeyedObjectPoolConfig0.clone()
        self.assertEqual(-1, genericKeyedObjectPoolConfig0.getMinIdlePerKey())

    def test30(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig()
        int0 = genericKeyedObjectPoolConfig0.getMaxIdlePerKey()
        self.assertEqual(0, genericKeyedObjectPoolConfig0.getMinIdlePerKey())
        self.assertEqual(-1, genericKeyedObjectPoolConfig0.getMaxTotal())
        self.assertEqual(8, int0)
        self.assertEqual(8, genericKeyedObjectPoolConfig0.getMaxTotalPerKey())

    def test29(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig()
        int0 = genericKeyedObjectPoolConfig0.getMinIdlePerKey()
        self.assertEqual(-1, genericKeyedObjectPoolConfig0.getMaxTotal())
        self.assertEqual(8, genericKeyedObjectPoolConfig0.getMaxTotalPerKey())
        self.assertEqual(8, genericKeyedObjectPoolConfig0.getMaxIdlePerKey())
        self.assertEqual(0, int0)

    def test28(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig()

        try:
            genericKeyedObjectPoolConfig0.toStringAppendFields(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.pool2.impl.BaseObjectPoolConfig", e)

    def test27(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig()
        genericKeyedObjectPoolConfig0.setBlockWhenExhausted(False)
        genericKeyedObjectPoolConfig1 = genericKeyedObjectPoolConfig0.clone()

        self.assertEqual(0, genericKeyedObjectPoolConfig1.getMinIdlePerKey())
        self.assertEqual(-1, genericKeyedObjectPoolConfig1.getMaxTotal())
        self.assertEqual(8, genericKeyedObjectPoolConfig1.getMaxTotalPerKey())
        self.assertEqual(8, genericKeyedObjectPoolConfig1.getMaxIdlePerKey())

    def test26(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig()
        genericKeyedObjectPoolConfig0.setFairness(True)
        genericKeyedObjectPoolConfig1 = genericKeyedObjectPoolConfig0.clone()

        self.assertEqual(8, genericKeyedObjectPoolConfig1.getMaxTotalPerKey())
        self.assertEqual(8, genericKeyedObjectPoolConfig1.getMaxIdlePerKey())
        self.assertEqual(-1, genericKeyedObjectPoolConfig1.getMaxTotal())
        self.assertEqual(0, genericKeyedObjectPoolConfig1.getMinIdlePerKey())

    def test25(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig()
        genericKeyedObjectPoolConfig0.setJmxEnabled(False)
        genericKeyedObjectPoolConfig1 = genericKeyedObjectPoolConfig0.clone()

        self.assertEqual(0, genericKeyedObjectPoolConfig1.getMinIdlePerKey())
        self.assertEqual(8, genericKeyedObjectPoolConfig1.getMaxIdlePerKey())
        self.assertEqual(8, genericKeyedObjectPoolConfig1.getMaxTotalPerKey())
        self.assertEqual(-1, genericKeyedObjectPoolConfig1.getMaxTotal())

    def test24(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig()
        genericKeyedObjectPoolConfig0.setLifo(False)
        genericKeyedObjectPoolConfig1 = genericKeyedObjectPoolConfig0.clone()

        self.assertEqual(8, genericKeyedObjectPoolConfig1.getMaxTotalPerKey())
        self.assertEqual(8, genericKeyedObjectPoolConfig1.getMaxIdlePerKey())
        self.assertEqual(-1, genericKeyedObjectPoolConfig1.getMaxTotal())
        self.assertEqual(0, genericKeyedObjectPoolConfig1.getMinIdlePerKey())

    def test23(self) -> None:

        generic_keyed_object_pool_config0 = GenericKeyedObjectPoolConfig()
        self.assertEqual(8, generic_keyed_object_pool_config0.getMaxIdlePerKey())

        generic_keyed_object_pool_config0.setMaxIdlePerKey(-1)
        generic_keyed_object_pool_config0.clone()
        self.assertEqual(-1, generic_keyed_object_pool_config0.getMaxIdlePerKey())

    def test22(self) -> None:

        generic_keyed_object_pool_config0 = GenericKeyedObjectPoolConfig()
        self.assertEqual(8, generic_keyed_object_pool_config0.getMaxIdlePerKey())

        generic_keyed_object_pool_config0.setMaxIdlePerKey(0)
        generic_keyed_object_pool_config0.clone()
        self.assertEqual(0, generic_keyed_object_pool_config0.getMaxIdlePerKey())

    def test21(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[int]()
        genericKeyedObjectPoolConfig0.setMaxTotal(8)
        genericKeyedObjectPoolConfig0.clone()
        self.assertEqual(8, genericKeyedObjectPoolConfig0.getMaxTotal())

    def test20(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig()
        genericKeyedObjectPoolConfig0.setMaxTotalPerKey(-487)
        genericKeyedObjectPoolConfig0.clone()
        self.assertEqual(-487, genericKeyedObjectPoolConfig0.getMaxTotalPerKey())

    def test19(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig()
        self.assertEqual(8, genericKeyedObjectPoolConfig0.getMaxTotalPerKey())

        genericKeyedObjectPoolConfig0.setMaxTotalPerKey(0)
        genericKeyedObjectPoolConfig0.clone()
        self.assertEqual(0, genericKeyedObjectPoolConfig0.getMaxTotalPerKey())

    def test18(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[int]()
        genericKeyedObjectPoolConfig0.setMinIdlePerKey(8)
        genericKeyedObjectPoolConfig0.clone()
        self.assertEqual(8, genericKeyedObjectPoolConfig0.getMinIdlePerKey())

    def test17(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[int]()
        genericKeyedObjectPoolConfig0.setNumTestsPerEvictionRun(-1801)
        genericKeyedObjectPoolConfig1 = genericKeyedObjectPoolConfig0.clone()
        self.assertEqual(8, genericKeyedObjectPoolConfig1.getMaxIdlePerKey())
        self.assertEqual(8, genericKeyedObjectPoolConfig1.getMaxTotalPerKey())
        self.assertEqual(0, genericKeyedObjectPoolConfig1.getMinIdlePerKey())
        self.assertEqual(-1, genericKeyedObjectPoolConfig1.getMaxTotal())

    def test16(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[int]()
        genericKeyedObjectPoolConfig0.setNumTestsPerEvictionRun(0)
        genericKeyedObjectPoolConfig1 = genericKeyedObjectPoolConfig0.clone()

        self.assertEqual(8, genericKeyedObjectPoolConfig1.getMaxTotalPerKey())
        self.assertEqual(-1, genericKeyedObjectPoolConfig1.getMaxTotal())
        self.assertEqual(0, genericKeyedObjectPoolConfig1.getMinIdlePerKey())
        self.assertEqual(8, genericKeyedObjectPoolConfig1.getMaxIdlePerKey())

    def test15(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig()
        genericKeyedObjectPoolConfig0.setTestOnBorrow(True)
        genericKeyedObjectPoolConfig1 = genericKeyedObjectPoolConfig0.clone()

        self.assertEqual(8, genericKeyedObjectPoolConfig1.getMaxIdlePerKey())
        self.assertEqual(0, genericKeyedObjectPoolConfig1.getMinIdlePerKey())
        self.assertEqual(-1, genericKeyedObjectPoolConfig1.getMaxTotal())
        self.assertEqual(8, genericKeyedObjectPoolConfig1.getMaxTotalPerKey())

    def test14(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig()
        genericKeyedObjectPoolConfig0.setTestOnCreate(True)
        genericKeyedObjectPoolConfig1 = genericKeyedObjectPoolConfig0.clone()

        self.assertEqual(0, genericKeyedObjectPoolConfig1.getMinIdlePerKey())
        self.assertEqual(-1, genericKeyedObjectPoolConfig1.getMaxTotal())
        self.assertEqual(8, genericKeyedObjectPoolConfig1.getMaxTotalPerKey())
        self.assertEqual(8, genericKeyedObjectPoolConfig1.getMaxIdlePerKey())

    def test13(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[int]()
        genericKeyedObjectPoolConfig0.setTestOnReturn(True)
        genericKeyedObjectPoolConfig1 = genericKeyedObjectPoolConfig0.clone()
        self.assertEqual(0, genericKeyedObjectPoolConfig1.getMinIdlePerKey())
        self.assertEqual(-1, genericKeyedObjectPoolConfig1.getMaxTotal())
        self.assertEqual(8, genericKeyedObjectPoolConfig1.getMaxTotalPerKey())
        self.assertEqual(8, genericKeyedObjectPoolConfig1.getMaxIdlePerKey())

    def test12(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[int]()
        genericKeyedObjectPoolConfig0.setTestWhileIdle(True)
        genericKeyedObjectPoolConfig1 = genericKeyedObjectPoolConfig0.clone()

        self.assertEqual(0, genericKeyedObjectPoolConfig1.getMinIdlePerKey())
        self.assertEqual(-1, genericKeyedObjectPoolConfig1.getMaxTotal())
        self.assertEqual(8, genericKeyedObjectPoolConfig1.getMaxIdlePerKey())
        self.assertEqual(8, genericKeyedObjectPoolConfig1.getMaxTotalPerKey())

    def test11(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig()
        genericKeyedObjectPoolConfig0.setMaxIdlePerKey(-3951)
        int0 = genericKeyedObjectPoolConfig0.getMaxIdlePerKey()
        self.assertEqual(-3951, int0)

    def test10(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[
            GenericKeyedObjectPoolConfig[object]
        ]()
        self.assertEqual(8, genericKeyedObjectPoolConfig0.getMaxIdlePerKey())

        genericKeyedObjectPoolConfig0.setMaxIdlePerKey(0)
        int0 = genericKeyedObjectPoolConfig0.getMaxIdlePerKey()
        self.assertEqual(0, int0)

    def test09(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[int]()
        self.assertEqual(-1, genericKeyedObjectPoolConfig0.getMaxTotal())

        genericKeyedObjectPoolConfig0.setMaxTotal(8)
        int0 = genericKeyedObjectPoolConfig0.getMaxTotal()
        self.assertEqual(8, int0)

    def test08(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig()
        self.assertEqual(-1, genericKeyedObjectPoolConfig0.getMaxTotal())

        genericKeyedObjectPoolConfig0.setMaxTotal(0)
        int0 = genericKeyedObjectPoolConfig0.getMaxTotal()
        self.assertEqual(0, int0)

    def test07(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[
            GenericKeyedObjectPoolConfig[object]
        ]()
        self.assertEqual(8, genericKeyedObjectPoolConfig0.getMaxTotalPerKey())

        genericKeyedObjectPoolConfig0.setMaxTotalPerKey(-1)
        int0 = genericKeyedObjectPoolConfig0.getMaxTotalPerKey()
        self.assertEqual(-1, int0)

    def test06(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[int]()
        self.assertEqual(8, genericKeyedObjectPoolConfig0.getMaxTotalPerKey())

        genericKeyedObjectPoolConfig0.setMaxTotalPerKey(0)
        int0 = genericKeyedObjectPoolConfig0.getMaxTotalPerKey()
        self.assertEqual(0, int0)

    def test05(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig()
        self.assertEqual(0, genericKeyedObjectPoolConfig0.getMinIdlePerKey())

        genericKeyedObjectPoolConfig0.setMinIdlePerKey(-1)
        int0 = genericKeyedObjectPoolConfig0.getMinIdlePerKey()
        self.assertEqual(-1, int0)

    def test04(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[int]()
        self.assertEqual(0, genericKeyedObjectPoolConfig0.getMinIdlePerKey())

        genericKeyedObjectPoolConfig0.setMinIdlePerKey(8)
        int0 = genericKeyedObjectPoolConfig0.getMinIdlePerKey()
        self.assertEqual(8, int0)

    def test03(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[object]()
        genericKeyedObjectPoolConfig0.setMinIdlePerKey(-1)
        genericKeyedObjectPoolConfig0.toString()
        self.assertEqual(-1, genericKeyedObjectPoolConfig0.getMinIdlePerKey())

    def test02(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig()
        genericKeyedObjectPoolConfig0.setMaxIdlePerKey(-196)
        stringBuilder0 = io.StringIO()
        genericKeyedObjectPoolConfig0.toStringAppendFields(stringBuilder0)
        self.assertEqual(
            "lifo=true, fairness=false, maxWaitDuration=PT-0.001S, minEvictableIdleTime=PT30M, softMinEvictableIdleTime=PT-0.001S, numTestsPerEvictionRun=3, evictionPolicyClassName=org.apache.commons.pool2.impl.DefaultEvictionPolicy, testOnCreate=false, testOnBorrow=false, testOnReturn=false, testWhileIdle=false, timeBetweenEvictionRuns=PT-0.001S, blockWhenExhausted=true, jmxEnabled=true, jmxNamePrefix=pool, jmxNameBase=null, minIdlePerKey=0, maxIdlePerKey=-196, maxTotalPerKey=8, maxTotal=-1",
            stringBuilder0.getvalue(),
        )
        self.assertEqual(-196, genericKeyedObjectPoolConfig0.getMaxIdlePerKey())

    def test01(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[object]()
        self.assertEqual(8, genericKeyedObjectPoolConfig0.getMaxTotalPerKey())

        genericKeyedObjectPoolConfig0.setMaxTotalPerKey(0)
        genericKeyedObjectPoolConfig0.toString()
        self.assertEqual(0, genericKeyedObjectPoolConfig0.getMaxTotalPerKey())

    def test00(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[int]()
        genericKeyedObjectPoolConfig0.setMaxTotal(8)
        genericKeyedObjectPoolConfig0.toString()
        self.assertEqual(8, genericKeyedObjectPoolConfig0.getMaxTotal())
