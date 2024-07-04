from __future__ import annotations
import time
import re
import datetime
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.pool2.impl.EvictionConfig import *


class TestEvictionConfig(unittest.TestCase):

    def testConstructorZerosMillis(self) -> None:

        config = EvictionConfig.EvictionConfig0(0, 0, 0)

        self.assertEqual(
            float("inf"), config.getIdleEvictDuration().total_seconds() * 1000
        )
        self.assertEqual(float("inf"), config.getIdleEvictTime())
        self.assertEqual(
            float("inf"), config.getIdleEvictTimeDuration().total_seconds() * 1000
        )
        self.assertEqual(
            float("inf"), config.getIdleSoftEvictDuration().total_seconds() * 1000
        )
        self.assertEqual(float("inf"), config.getIdleSoftEvictTime())
        self.assertEqual(
            float("inf"), config.getIdleSoftEvictTimeDuration().total_seconds() * 1000
        )
        self.assertEqual(0, config.getMinIdle())

    def testConstructorZerosDurations(self) -> None:

        config = EvictionConfig(datetime.timedelta(0), datetime.timedelta(0), 0)

        self.assertEqual(
            float("inf"), config.getIdleEvictDuration().total_seconds() * 1000
        )
        self.assertEqual(float("inf"), config.getIdleEvictTime())
        self.assertEqual(
            float("inf"), config.getIdleEvictTimeDuration().total_seconds() * 1000
        )
        self.assertEqual(
            float("inf"), config.getIdleSoftEvictDuration().total_seconds() * 1000
        )
        self.assertEqual(float("inf"), config.getIdleSoftEvictTime())
        self.assertEqual(
            float("inf"), config.getIdleSoftEvictTimeDuration().total_seconds() * 1000
        )
        self.assertEqual(0, config.getMinIdle())

    def testConstructor1s(self) -> None:

        config = EvictionConfig(
            datetime.timedelta(milliseconds=1), datetime.timedelta(milliseconds=1), 1
        )

        self.assertEqual(1, config.getIdleEvictDuration().total_seconds() * 1000)
        self.assertEqual(1, config.getIdleEvictTime())
        self.assertEqual(1, config.getIdleEvictTimeDuration().total_seconds() * 1000)
        self.assertEqual(1, config.getIdleSoftEvictDuration().total_seconds() * 1000)
        self.assertEqual(1, config.getIdleSoftEvictTime())
        self.assertEqual(
            1, config.getIdleSoftEvictTimeDuration().total_seconds() * 1000
        )
        self.assertEqual(1, config.getMinIdle())
