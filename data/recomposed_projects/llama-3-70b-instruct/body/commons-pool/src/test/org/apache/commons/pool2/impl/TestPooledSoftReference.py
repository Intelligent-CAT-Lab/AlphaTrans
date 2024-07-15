from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.pool2.impl.PooledSoftReference import *


class TestPooledSoftReference(unittest.TestCase):

    __REFERENT2: str = "test2"
    __REFERENT: str = "test"
    ref: PooledSoftReference[str] = None

    def testToString(self) -> None:
        expected = "Referenced Object: test, State: IDLE"
        self.assertEqual(expected, self.ref.toString())

    def testPooledSoftReference(self) -> None:
        self.assertEqual(self.__REFERENT, self.ref.getObject())

        softRef: SoftReference[str] = self.ref.getReference()
        self.assertEqual(self.__REFERENT, softRef.get())
        softRef.clear()

        softRef = SoftReference(self.__REFERENT2)
        self.ref.setReference(softRef)

        self.assertEqual(self.__REFERENT2, self.ref.getObject())

        softRef = self.ref.getReference()
        self.assertEqual(self.__REFERENT2, softRef.get())
        softRef.clear()

    def setUp(self) -> None:
        softRef = SoftReference(REFERENT)
        ref = PooledSoftReference(softRef)
