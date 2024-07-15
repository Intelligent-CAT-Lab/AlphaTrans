from __future__ import annotations
import time
import re
import os
from io import StringIO
import unittest
import pytest
import io
import unittest

# from src.test.org.apache.commons.pool2.impl.BaseObjectPoolConfig_ESTest_scaffolding import *
from src.main.org.apache.commons.pool2.impl.DefaultEvictionPolicy import *
from src.main.org.apache.commons.pool2.impl.EvictionPolicy import *
from src.main.org.apache.commons.pool2.impl.GenericKeyedObjectPoolConfig import *
from src.main.org.apache.commons.pool2.impl.GenericObjectPoolConfig import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class BaseObjectPoolConfig_ESTest(unittest.TestCase):

    def test75(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        boolean0 = genericObjectPoolConfig0.getBlockWhenExhausted()
        assert not genericObjectPoolConfig0.getTestOnBorrow()
        assert genericObjectPoolConfig0.getJmxNamePrefix() == "pool"
        assert not genericObjectPoolConfig0.getTestOnCreate()
        assert (
            genericObjectPoolConfig0.getEvictionPolicyClassName()
            == "org.apache.commons.pool2.impl.DefaultEvictionPolicy"
        )
        assert not genericObjectPoolConfig0.getFairness()
        assert genericObjectPoolConfig0.getJmxEnabled()
        assert boolean0
        assert genericObjectPoolConfig0.getLifo()
        assert genericObjectPoolConfig0.getNumTestsPerEvictionRun() == 3
        assert not genericObjectPoolConfig0.getTestOnReturn()
        assert not genericObjectPoolConfig0.getTestWhileIdle()

    def test74(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[
            DefaultEvictionPolicy[object]
        ]()
        int0 = genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun()
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle())
        self.assertFalse(genericKeyedObjectPoolConfig0.getFairness())
        self.assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted())
        self.assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericKeyedObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate())
        self.assertEqual("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix())
        self.assertTrue(genericKeyedObjectPoolConfig0.getLifo())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow())
        self.assertEqual(3, int0)
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn())

    def test73(self) -> None:

        generic_keyed_object_pool_config0 = GenericKeyedObjectPoolConfig(
            DefaultEvictionPolicy()
        )
        self.assertFalse(generic_keyed_object_pool_config0.getTestOnCreate())

        generic_keyed_object_pool_config0.setTestOnCreate(True)
        boolean0 = generic_keyed_object_pool_config0.getTestOnCreate()
        self.assertTrue(boolean0)

    def test72(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        genericObjectPoolConfig0.getDurationBetweenEvictionRuns()
        self.assertEqual(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertFalse(genericObjectPoolConfig0.getTestOnBorrow())
        self.assertEqual("pool", genericObjectPoolConfig0.getJmxNamePrefix())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertTrue(genericObjectPoolConfig0.getJmxEnabled())
        self.assertFalse(genericObjectPoolConfig0.getFairness())
        self.assertFalse(genericObjectPoolConfig0.getTestOnReturn())
        self.assertFalse(genericObjectPoolConfig0.getTestWhileIdle())
        self.assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted())
        self.assertFalse(genericObjectPoolConfig0.getTestOnCreate())
        self.assertTrue(genericObjectPoolConfig0.getLifo())

    def test71(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        long0 = genericObjectPoolConfig0.getMaxWaitMillis()
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted())
        self.assertFalse(genericObjectPoolConfig0.getFairness())
        self.assertTrue(genericObjectPoolConfig0.getJmxEnabled())
        self.assertEqual(-1, long0)
        self.assertEqual("pool", genericObjectPoolConfig0.getJmxNamePrefix())
        self.assertFalse(genericObjectPoolConfig0.getTestOnBorrow())
        self.assertFalse(genericObjectPoolConfig0.getTestOnCreate())
        self.assertTrue(genericObjectPoolConfig0.getLifo())
        self.assertEqual(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertFalse(genericObjectPoolConfig0.getTestOnReturn())
        self.assertFalse(genericObjectPoolConfig0.getTestWhileIdle())

    def test70(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        long0 = genericObjectPoolConfig0.getMinEvictableIdleTimeMillis()
        self.assertFalse(genericObjectPoolConfig0.getTestWhileIdle())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertTrue(genericObjectPoolConfig0.getJmxEnabled())
        self.assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted())
        self.assertFalse(genericObjectPoolConfig0.getFairness())
        self.assertEqual(1800000, long0)
        self.assertEqual("pool", genericObjectPoolConfig0.getJmxNamePrefix())
        self.assertFalse(genericObjectPoolConfig0.getTestOnCreate())
        self.assertFalse(genericObjectPoolConfig0.getTestOnBorrow())
        self.assertTrue(genericObjectPoolConfig0.getLifo())
        self.assertEqual(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertFalse(genericObjectPoolConfig0.getTestOnReturn())

    def test69(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig()
        boolean0 = genericKeyedObjectPoolConfig0.getLifo()
        self.assertEqual(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate())
        self.assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericKeyedObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow())
        self.assertEqual("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix())
        self.assertFalse(genericKeyedObjectPoolConfig0.getFairness())
        self.assertTrue(boolean0)
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle())

    def test68(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig()
        genericKeyedObjectPoolConfig0.getMinEvictableIdleTime()
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle())
        self.assertFalse(genericKeyedObjectPoolConfig0.getFairness())
        self.assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled())
        self.assertEqual("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericKeyedObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate())
        self.assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn())
        self.assertTrue(genericKeyedObjectPoolConfig0.getLifo())
        self.assertEqual(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun())

    def test67(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        string0 = genericObjectPoolConfig0.getEvictionPolicyClassName()
        self.assertEqual("org.apache.commons.pool2.impl.DefaultEvictionPolicy", string0)
        self.assertFalse(genericObjectPoolConfig0.getTestOnReturn())
        self.assertFalse(genericObjectPoolConfig0.getTestWhileIdle())
        self.assertEqual(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertTrue(genericObjectPoolConfig0.getJmxEnabled())
        self.assertIsNotNone(string0)
        self.assertTrue(genericObjectPoolConfig0.getLifo())
        self.assertFalse(genericObjectPoolConfig0.getTestOnCreate())
        self.assertEqual("pool", genericObjectPoolConfig0.getJmxNamePrefix())
        self.assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted())
        self.assertFalse(genericObjectPoolConfig0.getTestOnBorrow())
        self.assertFalse(genericObjectPoolConfig0.getFairness())

    def test66(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig()
        long0 = genericKeyedObjectPoolConfig0.getEvictorShutdownTimeoutMillis()
        self.assertEqual(10000, long0)
        self.assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate())
        self.assertTrue(genericKeyedObjectPoolConfig0.getLifo())
        self.assertEqual(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericKeyedObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled())
        self.assertFalse(genericKeyedObjectPoolConfig0.getFairness())
        self.assertEqual("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix())

    def test65(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        genericObjectPoolConfig0.setMaxWait(
            genericObjectPoolConfig0.DEFAULT_MIN_EVICTABLE_IDLE_DURATION
        )
        genericObjectPoolConfig0.getMaxWaitDuration()
        self.assertFalse(genericObjectPoolConfig0.getFairness())
        self.assertFalse(genericObjectPoolConfig0.getTestWhileIdle())
        self.assertFalse(genericObjectPoolConfig0.getTestOnReturn())
        self.assertTrue(genericObjectPoolConfig0.getLifo())
        self.assertEqual(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertFalse(genericObjectPoolConfig0.getTestOnCreate())
        self.assertFalse(genericObjectPoolConfig0.getTestOnBorrow())
        self.assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertEqual("pool", genericObjectPoolConfig0.getJmxNamePrefix())
        self.assertTrue(genericObjectPoolConfig0.getJmxEnabled())

    def test64(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        genericObjectPoolConfig0.setTestOnBorrow(False)
        self.assertTrue(genericObjectPoolConfig0.getJmxEnabled())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted())
        self.assertEqual(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertFalse(genericObjectPoolConfig0.getFairness())
        self.assertFalse(genericObjectPoolConfig0.getTestOnBorrow())
        self.assertTrue(genericObjectPoolConfig0.getLifo())
        self.assertFalse(genericObjectPoolConfig0.getTestOnCreate())
        self.assertEqual("pool", genericObjectPoolConfig0.getJmxNamePrefix())
        self.assertFalse(genericObjectPoolConfig0.getTestOnReturn())
        self.assertFalse(genericObjectPoolConfig0.getTestWhileIdle())

    def test63(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        boolean0 = genericObjectPoolConfig0.getJmxEnabled()
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertFalse(genericObjectPoolConfig0.getTestWhileIdle())
        self.assertTrue(boolean0)
        self.assertFalse(genericObjectPoolConfig0.getTestOnReturn())
        self.assertEqual("pool", genericObjectPoolConfig0.getJmxNamePrefix())
        self.assertEqual(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertTrue(genericObjectPoolConfig0.getLifo())
        self.assertFalse(genericObjectPoolConfig0.getFairness())
        self.assertFalse(genericObjectPoolConfig0.getTestOnCreate())
        self.assertFalse(genericObjectPoolConfig0.getTestOnBorrow())
        self.assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted())

    def test62(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        boolean0 = genericObjectPoolConfig0.getTestOnBorrow()
        self.assertFalse(genericObjectPoolConfig0.getTestWhileIdle())
        self.assertFalse(genericObjectPoolConfig0.getFairness())
        self.assertFalse(genericObjectPoolConfig0.getTestOnReturn())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted())
        self.assertEqual(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertFalse(boolean0)
        self.assertTrue(genericObjectPoolConfig0.getJmxEnabled())
        self.assertEqual("pool", genericObjectPoolConfig0.getJmxNamePrefix())
        self.assertTrue(genericObjectPoolConfig0.getLifo())
        self.assertFalse(genericObjectPoolConfig0.getTestOnCreate())

    def test61(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[
            DefaultEvictionPolicy[object]
        ]()
        genericKeyedObjectPoolConfig0.setTestWhileIdle(False)

        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericKeyedObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted())
        self.assertFalse(genericKeyedObjectPoolConfig0.getFairness())
        self.assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled())
        self.assertEqual("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix())
        self.assertTrue(genericKeyedObjectPoolConfig0.getLifo())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle())
        self.assertEqual(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn())

    def test60(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig[int]()
        boolean0 = genericObjectPoolConfig0.getFairness()
        self.assertFalse(genericObjectPoolConfig0.getTestOnBorrow())
        self.assertFalse(genericObjectPoolConfig0.getTestOnCreate())
        self.assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted())
        self.assertFalse(boolean0)
        self.assertEqual(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertFalse(genericObjectPoolConfig0.getTestOnReturn())
        self.assertTrue(genericObjectPoolConfig0.getLifo())
        self.assertFalse(genericObjectPoolConfig0.getTestWhileIdle())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertEqual("pool", genericObjectPoolConfig0.getJmxNamePrefix())
        self.assertTrue(genericObjectPoolConfig0.getJmxEnabled())

    def test59(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        genericObjectPoolConfig0.setMaxWaitMillis(0)
        long0 = genericObjectPoolConfig0.getMaxWaitMillis()
        self.assertEqual(0, long0)
        self.assertEqual(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertTrue(genericObjectPoolConfig0.getJmxEnabled())
        self.assertEqual("pool", genericObjectPoolConfig0.getJmxNamePrefix())
        self.assertTrue(genericObjectPoolConfig0.getLifo())
        self.assertFalse(genericObjectPoolConfig0.getTestOnBorrow())
        self.assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted())
        self.assertFalse(genericObjectPoolConfig0.getTestOnCreate())
        self.assertFalse(genericObjectPoolConfig0.getFairness())
        self.assertFalse(genericObjectPoolConfig0.getTestWhileIdle())
        self.assertFalse(genericObjectPoolConfig0.getTestOnReturn())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericObjectPoolConfig0.getEvictionPolicyClassName(),
        )

    def test58(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig[int]()
        genericObjectPoolConfig0.setBlockWhenExhausted(True)
        self.assertFalse(genericObjectPoolConfig0.getTestOnReturn())
        self.assertEqual("pool", genericObjectPoolConfig0.getJmxNamePrefix())
        self.assertFalse(genericObjectPoolConfig0.getTestWhileIdle())
        self.assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted())
        self.assertTrue(genericObjectPoolConfig0.getJmxEnabled())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertEqual(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertTrue(genericObjectPoolConfig0.getLifo())
        self.assertFalse(genericObjectPoolConfig0.getTestOnBorrow())
        self.assertFalse(genericObjectPoolConfig0.getFairness())
        self.assertFalse(genericObjectPoolConfig0.getTestOnCreate())

    def test57(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        boolean0 = genericObjectPoolConfig0.getTestOnCreate()
        self.assertEqual(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertEqual("pool", genericObjectPoolConfig0.getJmxNamePrefix())
        self.assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted())
        self.assertFalse(genericObjectPoolConfig0.getTestOnBorrow())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertTrue(genericObjectPoolConfig0.getJmxEnabled())
        self.assertFalse(genericObjectPoolConfig0.getTestOnReturn())
        self.assertFalse(genericObjectPoolConfig0.getFairness())
        self.assertFalse(genericObjectPoolConfig0.getTestWhileIdle())
        self.assertFalse(boolean0)
        self.assertTrue(genericObjectPoolConfig0.getLifo())

    def test56(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[int]()
        long0 = genericKeyedObjectPoolConfig0.getSoftMinEvictableIdleTimeMillis()
        self.assertEqual(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertTrue(genericKeyedObjectPoolConfig0.getLifo())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn())
        self.assertFalse(genericKeyedObjectPoolConfig0.getFairness())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle())
        self.assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled())
        self.assertEqual(-1, long0)
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericKeyedObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted())
        self.assertEqual("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix())

    def test55(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[
            DefaultEvictionPolicy[int]
        ]()
        genericKeyedObjectPoolConfig0.setFairness(False)
        self.assertFalse(genericKeyedObjectPoolConfig0.getFairness())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericKeyedObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow())
        self.assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled())
        self.assertEqual("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix())
        self.assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate())
        self.assertTrue(genericKeyedObjectPoolConfig0.getLifo())
        self.assertEqual(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn())

    def test54(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[int]()
        boolean0 = genericKeyedObjectPoolConfig0.getTestOnReturn()
        self.assertEqual(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow())
        self.assertEqual("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix())
        self.assertFalse(boolean0)
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericKeyedObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled())
        self.assertFalse(genericKeyedObjectPoolConfig0.getFairness())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle())
        self.assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate())
        self.assertTrue(genericKeyedObjectPoolConfig0.getLifo())

    def test53(self) -> None:

        generic_keyed_object_pool_config0 = GenericKeyedObjectPoolConfig()
        generic_keyed_object_pool_config0.set_evictor_shutdown_timeout_millis(0)
        long0 = generic_keyed_object_pool_config0.get_evictor_shutdown_timeout_millis()
        self.assertEqual(
            3, generic_keyed_object_pool_config0.get_num_tests_per_eviction_run()
        )
        self.assertEqual(
            "pool", generic_keyed_object_pool_config0.get_jmx_name_prefix()
        )
        self.assertFalse(generic_keyed_object_pool_config0.get_test_on_create())
        self.assertTrue(generic_keyed_object_pool_config0.get_lifo())
        self.assertTrue(generic_keyed_object_pool_config0.get_block_when_exhausted())
        self.assertTrue(generic_keyed_object_pool_config0.get_jmx_enabled())
        self.assertFalse(generic_keyed_object_pool_config0.get_test_on_borrow())
        self.assertFalse(generic_keyed_object_pool_config0.get_fairness())
        self.assertFalse(generic_keyed_object_pool_config0.get_test_while_idle())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            generic_keyed_object_pool_config0.get_eviction_policy_class_name(),
        )
        self.assertEqual(0, long0)
        self.assertFalse(generic_keyed_object_pool_config0.get_test_on_return())

    def test52(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[int]()
        genericKeyedObjectPoolConfig0.setJmxEnabled(True)
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericKeyedObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted())
        self.assertFalse(genericKeyedObjectPoolConfig0.getFairness())
        self.assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled())
        self.assertEqual("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle())
        self.assertEqual(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertTrue(genericKeyedObjectPoolConfig0.getLifo())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn())

    def test51(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig()
        genericKeyedObjectPoolConfig0.getEvictionPolicy()
        self.assertEqual("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix())
        self.assertTrue(genericKeyedObjectPoolConfig0.getLifo())
        self.assertEqual(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow())
        self.assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted())
        self.assertFalse(genericKeyedObjectPoolConfig0.getFairness())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericKeyedObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn())

    def test50(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        boolean0 = genericObjectPoolConfig0.getTestWhileIdle()
        self.assertFalse(genericObjectPoolConfig0.getFairness())
        self.assertFalse(boolean0)
        self.assertFalse(genericObjectPoolConfig0.getTestOnReturn())
        self.assertTrue(genericObjectPoolConfig0.getJmxEnabled())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertEqual(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertFalse(genericObjectPoolConfig0.getTestOnBorrow())
        self.assertTrue(genericObjectPoolConfig0.getLifo())
        self.assertEqual("pool", genericObjectPoolConfig0.getJmxNamePrefix())
        self.assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted())
        self.assertFalse(genericObjectPoolConfig0.getTestOnCreate())

    def test49(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        string0 = genericObjectPoolConfig0.getJmxNameBase()
        self.assertFalse(genericObjectPoolConfig0.getTestOnCreate())
        self.assertFalse(genericObjectPoolConfig0.getTestOnBorrow())
        self.assertFalse(genericObjectPoolConfig0.getTestWhileIdle())
        self.assertIsNone(string0)
        self.assertFalse(genericObjectPoolConfig0.getTestOnReturn())
        self.assertTrue(genericObjectPoolConfig0.getLifo())
        self.assertEqual(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted())
        self.assertFalse(genericObjectPoolConfig0.getFairness())
        self.assertEqual("pool", genericObjectPoolConfig0.getJmxNamePrefix())
        self.assertTrue(genericObjectPoolConfig0.getJmxEnabled())

    def test48(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig[int]()
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericObjectPoolConfig0.getEvictionPolicyClassName(),
        )

        genericObjectPoolConfig0.setEvictionPolicyClassName(None)
        string0 = genericObjectPoolConfig0.getEvictionPolicyClassName()
        self.assertFalse(genericObjectPoolConfig0.getFairness())
        self.assertFalse(genericObjectPoolConfig0.getTestWhileIdle())
        self.assertTrue(genericObjectPoolConfig0.getLifo())
        self.assertEqual(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertFalse(genericObjectPoolConfig0.getTestOnReturn())
        self.assertIsNone(string0)
        self.assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted())
        self.assertFalse(genericObjectPoolConfig0.getTestOnCreate())
        self.assertFalse(genericObjectPoolConfig0.getTestOnBorrow())
        self.assertTrue(genericObjectPoolConfig0.getJmxEnabled())
        self.assertEqual("pool", genericObjectPoolConfig0.getJmxNamePrefix())

    def test47(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        genericObjectPoolConfig0.getMaxWaitDuration()
        self.assertFalse(genericObjectPoolConfig0.getTestOnReturn())
        self.assertEqual("pool", genericObjectPoolConfig0.getJmxNamePrefix())
        self.assertFalse(genericObjectPoolConfig0.getTestOnCreate())
        self.assertFalse(genericObjectPoolConfig0.getFairness())
        self.assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted())
        self.assertFalse(genericObjectPoolConfig0.getTestOnBorrow())
        self.assertTrue(genericObjectPoolConfig0.getJmxEnabled())
        self.assertEqual(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertTrue(genericObjectPoolConfig0.getLifo())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertFalse(genericObjectPoolConfig0.getTestWhileIdle())

    def test46(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        genericObjectPoolConfig0.getMinEvictableIdleDuration()
        self.assertFalse(genericObjectPoolConfig0.getTestWhileIdle())
        self.assertFalse(genericObjectPoolConfig0.getFairness())
        self.assertFalse(genericObjectPoolConfig0.getTestOnReturn())
        self.assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted())
        self.assertFalse(genericObjectPoolConfig0.getTestOnCreate())
        self.assertEqual(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertTrue(genericObjectPoolConfig0.getLifo())
        self.assertFalse(genericObjectPoolConfig0.getTestOnBorrow())
        self.assertEqual("pool", genericObjectPoolConfig0.getJmxNamePrefix())
        self.assertTrue(genericObjectPoolConfig0.getJmxEnabled())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericObjectPoolConfig0.getEvictionPolicyClassName(),
        )

    def test45(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[
            DefaultEvictionPolicy[int]
        ]()
        string0 = genericKeyedObjectPoolConfig0.getJmxNamePrefix()
        assert genericKeyedObjectPoolConfig0.getBlockWhenExhausted()
        assert string0 is not None
        assert not genericKeyedObjectPoolConfig0.getTestOnBorrow()
        assert string0 == "pool"
        assert not genericKeyedObjectPoolConfig0.getFairness()
        assert (
            genericKeyedObjectPoolConfig0.getEvictionPolicyClassName()
            == "org.apache.commons.pool2.impl.DefaultEvictionPolicy"
        )
        assert genericKeyedObjectPoolConfig0.getJmxEnabled()
        assert not genericKeyedObjectPoolConfig0.getTestOnReturn()
        assert not genericKeyedObjectPoolConfig0.getTestOnCreate()
        assert genericKeyedObjectPoolConfig0.getLifo()
        assert not genericKeyedObjectPoolConfig0.getTestWhileIdle()
        assert genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun() == 3

    def test44(self) -> None:

        pass  # LLM could not translate this method

    def test43(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[int]()
        self.assertEqual(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun())

        genericKeyedObjectPoolConfig0.setNumTestsPerEvictionRun(0)
        int0 = genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun()
        self.assertEqual(0, int0)

    def test42(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        genericObjectPoolConfig0.setJmxNameBase("")
        string0 = genericObjectPoolConfig0.getJmxNameBase()
        self.assertFalse(genericObjectPoolConfig0.getFairness())
        self.assertEqual("", genericObjectPoolConfig0.getJmxNameBase())
        self.assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertEqual(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertIsNotNone(string0)
        self.assertFalse(genericObjectPoolConfig0.getTestOnCreate())
        self.assertFalse(genericObjectPoolConfig0.getTestOnReturn())
        self.assertFalse(genericObjectPoolConfig0.getTestWhileIdle())
        self.assertTrue(genericObjectPoolConfig0.getJmxEnabled())
        self.assertEqual("pool", genericObjectPoolConfig0.getJmxNamePrefix())
        self.assertTrue(genericObjectPoolConfig0.getLifo())
        self.assertFalse(genericObjectPoolConfig0.getTestOnBorrow())

    def test41(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        long0 = genericObjectPoolConfig0.getTimeBetweenEvictionRunsMillis()
        self.assertEqual("pool", genericObjectPoolConfig0.getJmxNamePrefix())
        self.assertFalse(genericObjectPoolConfig0.getTestOnCreate())
        self.assertEqual(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertTrue(genericObjectPoolConfig0.getLifo())
        self.assertEqual(-1, long0)
        self.assertFalse(genericObjectPoolConfig0.getTestOnReturn())
        self.assertFalse(genericObjectPoolConfig0.getTestWhileIdle())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertTrue(genericObjectPoolConfig0.getJmxEnabled())
        self.assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted())
        self.assertFalse(genericObjectPoolConfig0.getFairness())
        self.assertFalse(genericObjectPoolConfig0.getTestOnBorrow())

    def test40(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[int]()
        genericObjectPoolConfig0 = GenericObjectPoolConfig[object]()
        genericObjectPoolConfig0.setTimeBetweenEvictionRuns(
            genericKeyedObjectPoolConfig0.DEFAULT_SOFT_MIN_EVICTABLE_IDLE_TIME
        )
        genericObjectPoolConfig0.getDurationBetweenEvictionRuns()
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertTrue(genericObjectPoolConfig0.getJmxEnabled())
        self.assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted())
        self.assertFalse(genericObjectPoolConfig0.getTestWhileIdle())
        self.assertFalse(genericObjectPoolConfig0.getFairness())
        self.assertFalse(genericObjectPoolConfig0.getTestOnBorrow())
        self.assertEqual("pool", genericObjectPoolConfig0.getJmxNamePrefix())
        self.assertFalse(genericObjectPoolConfig0.getTestOnReturn())
        self.assertEqual(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertFalse(genericObjectPoolConfig0.getTestOnCreate())
        self.assertTrue(genericObjectPoolConfig0.getLifo())

    def test39(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        try:
            genericObjectPoolConfig0.toStringAppendFields(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.pool2.impl.BaseObjectPoolConfig", e)

    def test38(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        self.assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted())

        genericObjectPoolConfig0.setBlockWhenExhausted(False)
        boolean0 = genericObjectPoolConfig0.getBlockWhenExhausted()
        self.assertFalse(boolean0)

    def test37(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig()
        defaultEvictionPolicy0 = DefaultEvictionPolicy()
        genericKeyedObjectPoolConfig0.setEvictionPolicy(defaultEvictionPolicy0)
        genericKeyedObjectPoolConfig0.getEvictionPolicy()
        assert genericKeyedObjectPoolConfig0.getJmxEnabled()
        assert genericKeyedObjectPoolConfig0.getBlockWhenExhausted()
        assert not genericKeyedObjectPoolConfig0.getTestWhileIdle()
        assert genericKeyedObjectPoolConfig0.getLifo()
        assert genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun() == 3
        assert not genericKeyedObjectPoolConfig0.getTestOnReturn()
        assert not genericKeyedObjectPoolConfig0.getTestOnBorrow()
        assert not genericKeyedObjectPoolConfig0.getTestOnCreate()
        assert not genericKeyedObjectPoolConfig0.getFairness()
        assert genericKeyedObjectPoolConfig0.getJmxNamePrefix() == "pool"
        assert (
            genericKeyedObjectPoolConfig0.getEvictionPolicyClassName()
            == "org.apache.commons.pool2.impl.DefaultEvictionPolicy"
        )

    def test36(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericObjectPoolConfig0.getEvictionPolicyClassName(),
        )

        genericObjectPoolConfig0.setEvictionPolicyClassName("")
        string0 = genericObjectPoolConfig0.getEvictionPolicyClassName()
        self.assertIsNotNone(string0)
        self.assertEqual("", genericObjectPoolConfig0.getEvictionPolicyClassName())

    def test35(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig()
        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        genericKeyedObjectPoolConfig0.setEvictorShutdownTimeout(
            genericObjectPoolConfig0.DEFAULT_SOFT_MIN_EVICTABLE_IDLE_TIME
        )
        long0 = genericKeyedObjectPoolConfig0.getEvictorShutdownTimeoutMillis()
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle())
        self.assertFalse(genericKeyedObjectPoolConfig0.getFairness())
        self.assertEqual((-1), long0)
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn())
        self.assertEqual(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow())
        self.assertTrue(genericKeyedObjectPoolConfig0.getLifo())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate())
        self.assertEqual("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix())
        self.assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericKeyedObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled())

    def test34(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        self.assertFalse(genericObjectPoolConfig0.getFairness())

        genericObjectPoolConfig0.setFairness(True)
        boolean0 = genericObjectPoolConfig0.getFairness()
        self.assertTrue(boolean0)

    def test33(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        self.assertTrue(genericObjectPoolConfig0.getJmxEnabled())

        genericObjectPoolConfig0.setJmxEnabled(False)
        boolean0 = genericObjectPoolConfig0.getJmxEnabled()
        self.assertFalse(boolean0)

    def test32(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig()
        genericKeyedObjectPoolConfig0.setJmxNameBase("%&]X")
        string0 = genericKeyedObjectPoolConfig0.getJmxNameBase()
        self.assertEqual("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix())
        self.assertTrue(genericKeyedObjectPoolConfig0.getLifo())
        self.assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted())
        self.assertFalse(genericKeyedObjectPoolConfig0.getFairness())
        self.assertEqual("%&]X", genericKeyedObjectPoolConfig0.getJmxNameBase())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle())
        self.assertEqual(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericKeyedObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertIsNotNone(string0)

    def test31(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig()
        self.assertEqual("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix())

        genericKeyedObjectPoolConfig0.setJmxNamePrefix("")
        string0 = genericKeyedObjectPoolConfig0.getJmxNamePrefix()
        self.assertEqual("", genericKeyedObjectPoolConfig0.getJmxNamePrefix())
        self.assertIsNotNone(string0)

    def test30(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        self.assertEqual("pool", genericObjectPoolConfig0.getJmxNamePrefix())

        genericObjectPoolConfig0.setJmxNamePrefix(None)
        string0 = genericObjectPoolConfig0.getJmxNamePrefix()
        self.assertFalse(genericObjectPoolConfig0.getTestOnBorrow())
        self.assertTrue(genericObjectPoolConfig0.getLifo())
        self.assertEqual(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertFalse(genericObjectPoolConfig0.getTestOnReturn())
        self.assertFalse(genericObjectPoolConfig0.getFairness())
        self.assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted())
        self.assertFalse(genericObjectPoolConfig0.getTestOnCreate())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertFalse(genericObjectPoolConfig0.getTestWhileIdle())
        self.assertTrue(genericObjectPoolConfig0.getJmxEnabled())
        self.assertIsNone(string0)

    def test29(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig()
        self.assertTrue(genericKeyedObjectPoolConfig0.getLifo())

        genericKeyedObjectPoolConfig0.setLifo(False)
        boolean0 = genericKeyedObjectPoolConfig0.getLifo()
        self.assertFalse(boolean0)

    def test28(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig[int]()
        genericObjectPoolConfig0.setMaxWait(
            genericObjectPoolConfig0.DEFAULT_EVICTOR_SHUTDOWN_TIMEOUT
        )
        long0 = genericObjectPoolConfig0.getMaxWaitMillis()
        self.assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted())
        self.assertFalse(genericObjectPoolConfig0.getTestOnCreate())
        self.assertEqual(10000, long0)
        self.assertTrue(genericObjectPoolConfig0.getLifo())
        self.assertEqual(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertFalse(genericObjectPoolConfig0.getTestOnReturn())
        self.assertFalse(genericObjectPoolConfig0.getFairness())
        self.assertFalse(genericObjectPoolConfig0.getTestWhileIdle())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertFalse(genericObjectPoolConfig0.getTestOnBorrow())
        self.assertEqual("pool", genericObjectPoolConfig0.getJmxNamePrefix())
        self.assertTrue(genericObjectPoolConfig0.getJmxEnabled())

    def test27(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig()
        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        genericObjectPoolConfig0.setSoftMinEvictableIdleTime(
            genericKeyedObjectPoolConfig0.DEFAULT_MIN_EVICTABLE_IDLE_DURATION
        )
        long0 = genericObjectPoolConfig0.getSoftMinEvictableIdleTimeMillis()
        self.assertFalse(genericObjectPoolConfig0.getTestOnReturn())
        self.assertFalse(genericObjectPoolConfig0.getFairness())
        self.assertFalse(genericObjectPoolConfig0.getTestOnBorrow())
        self.assertEqual("pool", genericObjectPoolConfig0.getJmxNamePrefix())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted())
        self.assertTrue(genericObjectPoolConfig0.getJmxEnabled())
        self.assertEqual(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertFalse(genericObjectPoolConfig0.getTestWhileIdle())
        self.assertFalse(genericObjectPoolConfig0.getTestOnCreate())
        self.assertEqual(1800000, long0)
        self.assertTrue(genericObjectPoolConfig0.getLifo())

    def test26(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig[int]()
        chronoUnit0 = ChronoUnit.MICROS
        duration0 = Duration.of(-1, chronoUnit0)
        genericObjectPoolConfig0.setSoftMinEvictableIdleTime(duration0)
        long0 = genericObjectPoolConfig0.getSoftMinEvictableIdleTimeMillis()
        self.assertTrue(genericObjectPoolConfig0.getJmxEnabled())
        self.assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertFalse(genericObjectPoolConfig0.getTestWhileIdle())
        self.assertEqual("pool", genericObjectPoolConfig0.getJmxNamePrefix())
        self.assertFalse(genericObjectPoolConfig0.getTestOnReturn())
        self.assertFalse(genericObjectPoolConfig0.getFairness())
        self.assertEqual(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertTrue(genericObjectPoolConfig0.getLifo())
        self.assertFalse(genericObjectPoolConfig0.getTestOnBorrow())
        self.assertEqual(0, long0)
        self.assertFalse(genericObjectPoolConfig0.getTestOnCreate())

    def test25(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        self.assertFalse(genericObjectPoolConfig0.getTestOnBorrow())

        genericObjectPoolConfig0.setTestOnBorrow(True)
        boolean0 = genericObjectPoolConfig0.getTestOnBorrow()
        self.assertTrue(boolean0)

    def test24(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[int]()
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn())

        genericKeyedObjectPoolConfig0.setTestOnReturn(True)
        boolean0 = genericKeyedObjectPoolConfig0.getTestOnReturn()
        self.assertTrue(boolean0)

    def test23(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        self.assertFalse(genericObjectPoolConfig0.getTestWhileIdle())

        genericObjectPoolConfig0.setTestWhileIdle(True)
        boolean0 = genericObjectPoolConfig0.getTestWhileIdle()
        self.assertTrue(boolean0)

    def test22(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig[int]()
        genericObjectPoolConfig0.setTimeBetweenEvictionRunsMillis(187)
        long0 = genericObjectPoolConfig0.getTimeBetweenEvictionRunsMillis()
        self.assertFalse(genericObjectPoolConfig0.getTestOnReturn())
        self.assertFalse(genericObjectPoolConfig0.getTestOnBorrow())
        self.assertFalse(genericObjectPoolConfig0.getFairness())
        self.assertEqual("pool", genericObjectPoolConfig0.getJmxNamePrefix())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertEqual(187, long0)
        self.assertTrue(genericObjectPoolConfig0.getJmxEnabled())
        self.assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted())
        self.assertFalse(genericObjectPoolConfig0.getTestWhileIdle())
        self.assertFalse(genericObjectPoolConfig0.getTestOnCreate())
        self.assertEqual(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertTrue(genericObjectPoolConfig0.getLifo())

    def test21(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig[int]()
        genericObjectPoolConfig0.setTimeBetweenEvictionRunsMillis(0)
        long0 = genericObjectPoolConfig0.getTimeBetweenEvictionRunsMillis()
        self.assertFalse(genericObjectPoolConfig0.getTestWhileIdle())
        self.assertTrue(genericObjectPoolConfig0.getJmxEnabled())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertEqual(0, long0)
        self.assertFalse(genericObjectPoolConfig0.getTestOnReturn())
        self.assertFalse(genericObjectPoolConfig0.getTestOnCreate())
        self.assertTrue(genericObjectPoolConfig0.getLifo())
        self.assertEqual("pool", genericObjectPoolConfig0.getJmxNamePrefix())
        self.assertFalse(genericObjectPoolConfig0.getTestOnBorrow())
        self.assertEqual(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertFalse(genericObjectPoolConfig0.getFairness())
        self.assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted())

    def test20(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        stringBuilder0 = io.StringIO()
        genericObjectPoolConfig0.toStringAppendFields(stringBuilder0)
        self.assertEqual(
            "lifo=true, fairness=false, maxWaitDuration=PT-0.001S, minEvictableIdleTime=PT30M, softMinEvictableIdleTime=PT-0.001S, numTestsPerEvictionRun=3, evictionPolicyClassName=org.apache.commons.pool2.impl.DefaultEvictionPolicy, testOnCreate=false, testOnBorrow=false, testOnReturn=false, testWhileIdle=false, timeBetweenEvictionRuns=PT-0.001S, blockWhenExhausted=true, jmxEnabled=true, jmxNamePrefix=pool, jmxNameBase=null, maxTotal=8, maxIdle=8, minIdle=0",
            stringBuilder0.getvalue(),
        )

    def test19(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        genericObjectPoolConfig0.setEvictorShutdownTimeoutMillis1(2488)
        genericObjectPoolConfig0.getEvictorShutdownTimeout()
        self.assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted())
        self.assertEqual(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertTrue(genericObjectPoolConfig0.getLifo())
        self.assertFalse(genericObjectPoolConfig0.getTestOnCreate())
        self.assertFalse(genericObjectPoolConfig0.getTestWhileIdle())
        self.assertFalse(genericObjectPoolConfig0.getTestOnReturn())
        self.assertFalse(genericObjectPoolConfig0.getTestOnBorrow())
        self.assertEqual("pool", genericObjectPoolConfig0.getJmxNamePrefix())
        self.assertFalse(genericObjectPoolConfig0.getFairness())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertTrue(genericObjectPoolConfig0.getJmxEnabled())

    def test18(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[int]()
        genericKeyedObjectPoolConfig0.setEvictorShutdownTimeoutMillis1(-1)
        genericKeyedObjectPoolConfig0.getEvictorShutdownTimeoutDuration()
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn())
        self.assertFalse(genericKeyedObjectPoolConfig0.getFairness())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow())
        self.assertEqual("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericKeyedObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled())
        self.assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted())
        self.assertEqual(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate())
        self.assertTrue(genericKeyedObjectPoolConfig0.getLifo())

    def test17(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig[
            DefaultEvictionPolicy[object]
        ]()
        genericObjectPoolConfig1 = GenericObjectPoolConfig[object]()
        genericObjectPoolConfig1.setMinEvictableIdleTime(
            genericObjectPoolConfig0.DEFAULT_MIN_EVICTABLE_IDLE_DURATION
        )
        genericObjectPoolConfig1.getMinEvictableIdleDuration()
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericObjectPoolConfig1.getEvictionPolicyClassName(),
        )
        self.assertTrue(genericObjectPoolConfig1.getBlockWhenExhausted())
        self.assertTrue(genericObjectPoolConfig1.getJmxEnabled())
        self.assertFalse(genericObjectPoolConfig1.getFairness())
        self.assertEqual(3, genericObjectPoolConfig1.getNumTestsPerEvictionRun())
        self.assertTrue(genericObjectPoolConfig1.getLifo())
        self.assertFalse(genericObjectPoolConfig1.getTestOnCreate())
        self.assertFalse(genericObjectPoolConfig1.getTestOnBorrow())
        self.assertEqual("pool", genericObjectPoolConfig1.getJmxNamePrefix())
        self.assertFalse(genericObjectPoolConfig1.getTestOnReturn())
        self.assertFalse(genericObjectPoolConfig1.getTestWhileIdle())

    def test16(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig()
        genericKeyedObjectPoolConfig0.setMinEvictableIdleTime(
            genericKeyedObjectPoolConfig0.DEFAULT_EVICTOR_SHUTDOWN_TIMEOUT
        )
        genericKeyedObjectPoolConfig0.getMinEvictableIdleTime()
        self.assertEqual(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertEqual("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow())
        self.assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericKeyedObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle())
        self.assertFalse(genericKeyedObjectPoolConfig0.getFairness())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn())
        self.assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted())
        self.assertTrue(genericKeyedObjectPoolConfig0.getLifo())

    def test15(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[int]()
        genericKeyedObjectPoolConfig0.setSoftMinEvictableIdleTimeMillis(0)
        genericKeyedObjectPoolConfig0.getSoftMinEvictableIdleDuration()
        self.assertEqual("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn())
        self.assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericKeyedObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle())
        self.assertFalse(genericKeyedObjectPoolConfig0.getFairness())
        self.assertEqual(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertTrue(genericKeyedObjectPoolConfig0.getLifo())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate())

    def test14(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        genericObjectPoolConfig0.setSoftMinEvictableIdleTimeMillis(9223372036854775807)
        genericObjectPoolConfig0.getSoftMinEvictableIdleTime()
        self.assertFalse(genericObjectPoolConfig0.getTestWhileIdle())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertFalse(genericObjectPoolConfig0.getTestOnReturn())
        self.assertEqual(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertFalse(genericObjectPoolConfig0.getTestOnCreate())
        self.assertEqual("pool", genericObjectPoolConfig0.getJmxNamePrefix())
        self.assertTrue(genericObjectPoolConfig0.getLifo())
        self.assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted())
        self.assertTrue(genericObjectPoolConfig0.getJmxEnabled())
        self.assertFalse(genericObjectPoolConfig0.getFairness())
        self.assertFalse(genericObjectPoolConfig0.getTestOnBorrow())

    def test13(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[int]()
        genericKeyedObjectPoolConfig0.setTimeBetweenEvictionRunsMillis(-1)
        genericKeyedObjectPoolConfig0.getTimeBetweenEvictionRuns()
        assert genericKeyedObjectPoolConfig0.getJmxEnabled()
        assert genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun() == 3
        assert genericKeyedObjectPoolConfig0.getLifo()
        assert (
            genericKeyedObjectPoolConfig0.getEvictionPolicyClassName()
            == "org.apache.commons.pool2.impl.DefaultEvictionPolicy"
        )
        assert not genericKeyedObjectPoolConfig0.getTestOnCreate()
        assert genericKeyedObjectPoolConfig0.getJmxNamePrefix() == "pool"
        assert not genericKeyedObjectPoolConfig0.getFairness()
        assert not genericKeyedObjectPoolConfig0.getTestOnBorrow()
        assert genericKeyedObjectPoolConfig0.getBlockWhenExhausted()
        assert not genericKeyedObjectPoolConfig0.getTestOnReturn()
        assert not genericKeyedObjectPoolConfig0.getTestWhileIdle()

    def test12(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        genericObjectPoolConfig0.setEvictorShutdownTimeoutMillis0(None)
        self.assertFalse(genericObjectPoolConfig0.getTestOnReturn())
        self.assertTrue(genericObjectPoolConfig0.getLifo())
        self.assertEqual("pool", genericObjectPoolConfig0.getJmxNamePrefix())
        self.assertFalse(genericObjectPoolConfig0.getTestOnCreate())
        self.assertFalse(genericObjectPoolConfig0.getFairness())
        self.assertFalse(genericObjectPoolConfig0.getTestOnBorrow())
        self.assertTrue(genericObjectPoolConfig0.getJmxEnabled())
        self.assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertEqual(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertFalse(genericObjectPoolConfig0.getTestWhileIdle())

    def test11(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[int]()
        genericKeyedObjectPoolConfig0.setLifo(True)
        assert genericKeyedObjectPoolConfig0.getJmxEnabled()
        assert (
            genericKeyedObjectPoolConfig0.getEvictionPolicyClassName()
            == "org.apache.commons.pool2.impl.DefaultEvictionPolicy"
        )
        assert not genericKeyedObjectPoolConfig0.getTestWhileIdle()
        assert not genericKeyedObjectPoolConfig0.getTestOnReturn()
        assert genericKeyedObjectPoolConfig0.getLifo()
        assert genericKeyedObjectPoolConfig0.getJmxNamePrefix() == "pool"
        assert genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun() == 3
        assert not genericKeyedObjectPoolConfig0.getFairness()
        assert not genericKeyedObjectPoolConfig0.getTestOnCreate()
        assert not genericKeyedObjectPoolConfig0.getTestOnBorrow()
        assert genericKeyedObjectPoolConfig0.getBlockWhenExhausted()

    def test10(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig()
        genericKeyedObjectPoolConfig0.setTestOnCreate(False)
        self.assertEqual(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn())
        self.assertEqual("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix())
        self.assertTrue(genericKeyedObjectPoolConfig0.getLifo())
        self.assertFalse(genericKeyedObjectPoolConfig0.getFairness())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow())
        self.assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericKeyedObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle())

    def test09(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig()
        genericKeyedObjectPoolConfig0.setTestOnReturn(False)
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle())
        self.assertEqual(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun())
        self.assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled())
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericKeyedObjectPoolConfig0.getEvictionPolicyClassName(),
        )
        self.assertTrue(genericKeyedObjectPoolConfig0.getLifo())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate())
        self.assertEqual("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix())
        self.assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow())
        self.assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted())
        self.assertFalse(genericKeyedObjectPoolConfig0.getFairness())

    def test08(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        genericObjectPoolConfig0.setLifo(False)
        genericObjectPoolConfig0.toString()
        self.assertFalse(genericObjectPoolConfig0.getLifo())

    def test07(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig[
            DefaultEvictionPolicy[int]
        ]()
        assert not genericKeyedObjectPoolConfig0.getFairness()

        genericKeyedObjectPoolConfig0.setFairness(True)
        genericKeyedObjectPoolConfig0.toString()
        assert genericKeyedObjectPoolConfig0.getFairness()

    def test06(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        genericObjectPoolConfig0.setMaxWait(
            genericObjectPoolConfig0.DEFAULT_EVICTOR_SHUTDOWN_TIMEOUT
        )
        string0 = genericObjectPoolConfig0.toString()
        self.assertEqual(
            string0,
            "GenericObjectPoolConfig [lifo=true, fairness=false, maxWaitDuration=PT10S, minEvictableIdleTime=PT30M, softMinEvictableIdleTime=PT-0.001S, numTestsPerEvictionRun=3, evictionPolicyClassName=org.apache.commons.pool2.impl.DefaultEvictionPolicy, testOnCreate=false, testOnBorrow=false, testOnReturn=false, testWhileIdle=false, timeBetweenEvictionRuns=PT-0.001S, blockWhenExhausted=true, jmxEnabled=true, jmxNamePrefix=pool, jmxNameBase=null, maxTotal=8, maxIdle=8, minIdle=0]",
        )

    def test05(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig()
        genericKeyedObjectPoolConfig0.setMinEvictableIdleTimeMillis(995)
        stringBuilder0 = io.StringIO()
        genericKeyedObjectPoolConfig0.toStringAppendFields(stringBuilder0)
        self.assertEqual(
            "lifo=true, fairness=false, maxWaitDuration=PT-0.001S, minEvictableIdleTime=PT0.995S, softMinEvictableIdleTime=PT-0.001S, numTestsPerEvictionRun=3, evictionPolicyClassName=org.apache.commons.pool2.impl.DefaultEvictionPolicy, testOnCreate=false, testOnBorrow=false, testOnReturn=false, testWhileIdle=false, timeBetweenEvictionRuns=PT-0.001S, blockWhenExhausted=true, jmxEnabled=true, jmxNamePrefix=pool, jmxNameBase=null, minIdlePerKey=0, maxIdlePerKey=8, maxTotalPerKey=8, maxTotal=-1",
            stringBuilder0.getvalue(),
        )
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericKeyedObjectPoolConfig0.getEvictionPolicyClassName(),
        )

    def test04(self) -> None:

        genericKeyedObjectPoolConfig0 = GenericKeyedObjectPoolConfig()
        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        genericObjectPoolConfig0.setSoftMinEvictableIdleTime(
            genericKeyedObjectPoolConfig0.DEFAULT_MIN_EVICTABLE_IDLE_DURATION
        )
        string0 = genericObjectPoolConfig0.toString()
        self.assertEqual(
            string0,
            "GenericObjectPoolConfig [lifo=true, fairness=false, maxWaitDuration=PT-0.001S, minEvictableIdleTime=PT30M, softMinEvictableIdleTime=PT30M, numTestsPerEvictionRun=3, evictionPolicyClassName=org.apache.commons.pool2.impl.DefaultEvictionPolicy, testOnCreate=false, testOnBorrow=false, testOnReturn=false, testWhileIdle=false, timeBetweenEvictionRuns=PT-0.001S, blockWhenExhausted=true, jmxEnabled=true, jmxNamePrefix=pool, jmxNameBase=null, maxTotal=8, maxIdle=8, minIdle=0]",
        )

    def test03(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        self.assertEqual(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun())

        genericObjectPoolConfig0.setNumTestsPerEvictionRun(0)
        genericObjectPoolConfig0.toString()
        self.assertEqual(0, genericObjectPoolConfig0.getNumTestsPerEvictionRun())

    def test02(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        self.assertEqual(
            "org.apache.commons.pool2.impl.DefaultEvictionPolicy",
            genericObjectPoolConfig0.getEvictionPolicyClassName(),
        )

        genericObjectPoolConfig0.setEvictionPolicyClassName(", testOnCreate=")
        genericObjectPoolConfig0.toString()
        self.assertEqual(
            ", testOnCreate=", genericObjectPoolConfig0.getEvictionPolicyClassName()
        )

    def test01(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        genericObjectPoolConfig0.setTestOnCreate(True)
        genericObjectPoolConfig0.toString()
        self.assertTrue(genericObjectPoolConfig0.getTestOnCreate())

    def test00(self) -> None:

        genericObjectPoolConfig0 = GenericObjectPoolConfig()
        self.assertFalse(genericObjectPoolConfig0.getTestOnBorrow())

        genericObjectPoolConfig0.setTestOnBorrow(True)
        genericObjectPoolConfig0.toString()
        self.assertTrue(genericObjectPoolConfig0.getTestOnBorrow())
