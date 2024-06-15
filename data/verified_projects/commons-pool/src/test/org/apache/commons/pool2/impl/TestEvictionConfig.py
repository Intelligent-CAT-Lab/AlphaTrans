import pytest

import unittest
from datetime import timedelta
from src.main.org.apache.commons.pool2.impl.EvictionConfig import *
import sys

class TestEvictionConfig(unittest.TestCase):

    @pytest.mark.test
    def testConstructor1s(self) -> None:
        config = EvictionConfig(
            timedelta(milliseconds=1),
            timedelta(milliseconds=1),
            1
        )

        self.assertEqual(
            config.getIdleEvictDuration().total_seconds() * 1000,
            1
        )
        self.assertEqual(
            config.getIdleEvictTime(),
            1
        )
        self.assertEqual(
            config.getIdleEvictTimeDuration().total_seconds() * 1000,
            1
        )
        self.assertEqual(
            config.getIdleSoftEvictDuration().total_seconds() * 1000,
            1
        )
        self.assertEqual(
            config.getIdleSoftEvictTime(),
            1
        )
        self.assertEqual(
            config.getIdleSoftEvictTimeDuration().total_seconds() * 1000,
            1
        )
        self.assertEqual(
            config.getMinIdle(),
            1
        )

    
    @pytest.mark.test
    def testConstructorZerosDurations(self) -> None:
        config = EvictionConfig(timedelta(0), timedelta(0), 0)

        self.assertEqual(
            config.getIdleEvictDuration().total_seconds() * 1000,
            sys.maxsize
        )
        self.assertEqual(
            config.getIdleEvictTime(),
            sys.maxsize
        )
        self.assertEqual(
            config.getIdleEvictTimeDuration().total_seconds() * 1000,
            sys.maxsize
        )
        self.assertEqual(
            config.getIdleSoftEvictDuration().total_seconds() * 1000,
            sys.maxsize
        )
        self.assertEqual(
            config.getIdleSoftEvictTime(),
            sys.maxsize
        )
        self.assertEqual(
            config.getIdleSoftEvictTimeDuration().total_seconds() * 1000,
            sys.maxsize
        )
        self.assertEqual(
            config.getMinIdle(),
            0
        )

    
    @pytest.mark.test
    def testConstructorZerosMillis(self) -> None:
        config = EvictionConfig.EvictionConfig0(0, 0, 0)

        self.assertEqual(
            config.getIdleEvictDuration().total_seconds() * 1000,
            sys.maxsize
        )
        self.assertEqual(
            config.getIdleEvictTime(),
            sys.maxsize
        )
        self.assertEqual(
            config.getIdleEvictTimeDuration().total_seconds() * 1000,
            sys.maxsize
        )
        self.assertEqual(
            config.getIdleSoftEvictDuration().total_seconds() * 1000,
            sys.maxsize
        )
        self.assertEqual(
            config.getIdleSoftEvictTime(),
            sys.maxsize
        )
        self.assertEqual(
            config.getIdleSoftEvictTimeDuration().total_seconds() * 1000,
            sys.maxsize
        )
        self.assertEqual(
            config.getMinIdle(),
            0
        )
