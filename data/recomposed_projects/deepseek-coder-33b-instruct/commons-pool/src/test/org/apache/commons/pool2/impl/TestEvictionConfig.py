from __future__ import annotations
import io
import os
from src.main.org.apache.commons.pool2.impl.EvictionConfig import *


class TestEvictionConfig:

    def testConstructorZerosMillis(self) -> None:

        config = EvictionConfig.EvictionConfig0(0, 0, 0)

        assert Long.MAX_VALUE == config.getIdleEvictDuration().toMillis()
        assert Long.MAX_VALUE == config.getIdleEvictTime()
        assert Long.MAX_VALUE == config.getIdleEvictTimeDuration().toMillis()
        assert Long.MAX_VALUE == config.getIdleSoftEvictDuration().toMillis()
        assert Long.MAX_VALUE == config.getIdleSoftEvictTime()
        assert Long.MAX_VALUE == config.getIdleSoftEvictTimeDuration().toMillis()
        assert 0 == config.getMinIdle()

    def testConstructorZerosDurations(self) -> None:

        config = EvictionConfig(Duration.ZERO, Duration.ZERO, 0)

        self.assertEqual(float("inf"), config.getIdleEvictDuration().toMillis())
        self.assertEqual(float("inf"), config.getIdleEvictTime())
        self.assertEqual(float("inf"), config.getIdleEvictTimeDuration().toMillis())
        self.assertEqual(float("inf"), config.getIdleSoftEvictDuration().toMillis())
        self.assertEqual(float("inf"), config.getIdleSoftEvictTime())
        self.assertEqual(float("inf"), config.getIdleSoftEvictTimeDuration().toMillis())
        self.assertEqual(0, config.getMinIdle())

    def testConstructor1s(self) -> None:

        config = EvictionConfig(Duration.ofMillis(1), Duration.ofMillis(1), 1)

        self.assertEqual(1, config.getIdleEvictDuration().toMillis())
        self.assertEqual(1, config.getIdleEvictTime())
        self.assertEqual(1, config.getIdleEvictTimeDuration().toMillis())
        self.assertEqual(1, config.getIdleSoftEvictDuration().toMillis())
        self.assertEqual(1, config.getIdleSoftEvictTime())
        self.assertEqual(1, config.getIdleSoftEvictTimeDuration().toMillis())
        self.assertEqual(1, config.getMinIdle())
