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
        self.assertEqual(expected, ref.toString())

    def testPooledSoftReference(self) -> None:

        self.assertEqual(self.__REFERENT, ref.getObject())

        softRef = ref.getReference()
        self.assertEqual(self.__REFERENT, softRef.get())
        softRef.clear()

        softRef = SoftReference(self.__REFERENT2)
        ref.setReference(softRef)

        self.assertEqual(self.__REFERENT2, ref.getObject())

        softRef = ref.getReference()
        self.assertEqual(self.__REFERENT2, softRef.get())
        softRef.clear()

    def setUp(self) -> None:

        softRef = SoftReference(self.__REFERENT)
        self.ref = PooledSoftReference(softRef)
