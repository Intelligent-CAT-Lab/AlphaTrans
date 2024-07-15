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

        pass  # LLM could not translate this method

    def testConstructorZerosDurations(self) -> None:
        config = EvictionConfig(datetime.timedelta(0), datetime.timedelta(0), 0)

        self.assertEqual(
            9223372036854775807, config.getIdleEvictDuration().total_seconds() * 1000
        )
        self.assertEqual(9223372036854775807, config.getIdleEvictTime())
        self.assertEqual(
            9223372036854775807,
            config.getIdleEvictTimeDuration().total_seconds() * 1000,
        )
        self.assertEqual(
            9223372036854775807,
            config.getIdleSoftEvictDuration().total_seconds() * 1000,
        )
        self.assertEqual(9223372036854775807, config.getIdleSoftEvictTime())
        self.assertEqual(
            9223372036854775807,
            config.getIdleSoftEvictTimeDuration().total_seconds() * 1000,
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
