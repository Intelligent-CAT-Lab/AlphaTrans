# Imports Begin
from src.main.org.apache.commons.pool2.impl.EvictionConfig import *
import unittest
import os
import datetime

# Imports End


class TestEvictionConfig(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testConstructorZerosMillis(self) -> None:

        config = EvictionConfig.EvictionConfig0(0, 0, 0)
        self.assertEqual(config.getIdleEvictDuration().total_seconds(), 0)
        self.assertEqual(config.getIdleEvictTime(), 0)
        self.assertEqual(config.getIdleEvictTimeDuration().total_seconds(), 0)
        self.assertEqual(config.getIdleSoftEvictDuration().total_seconds(), 0)
        self.assertEqual(config.getIdleSoftEvictTime(), 0)
        self.assertEqual(config.getIdleSoftEvictTimeDuration().total_seconds(), 0)
        self.assertEqual(config.getMinIdle(), 0)

    def testConstructorZerosDurations(self) -> None:

        config = EvictionConfig(datetime.timedelta(0), datetime.timedelta(0), 0)
        assert config.getIdleEvictDuration().total_seconds() == float("inf")
        assert config.getIdleEvictTime() == float("inf")
        assert config.getIdleEvictTimeDuration().total_seconds() == float("inf")
        assert config.getIdleSoftEvictDuration().total_seconds() == float("inf")
        assert config.getIdleSoftEvictTime() == float("inf")
        assert config.getIdleSoftEvictTimeDuration().total_seconds() == float("inf")
        assert config.getMinIdle() == 0

    def testConstructor1s(self) -> None:

        config = EvictionConfig(
            datetime.timedelta(milliseconds=1), datetime.timedelta(milliseconds=1), 1
        )
        self.assertEqual(1, config.getIdleEvictDuration().total_seconds())
        self.assertEqual(1, config.getIdleEvictTime())
        self.assertEqual(1, config.getIdleEvictTimeDuration().total_seconds())
        self.assertEqual(1, config.getIdleSoftEvictDuration().total_seconds())
        self.assertEqual(1, config.getIdleSoftEvictTime())
        self.assertEqual(1, config.getIdleSoftEvictTimeDuration().total_seconds())
        self.assertEqual(1, config.getMinIdle())

    # Class Methods End
