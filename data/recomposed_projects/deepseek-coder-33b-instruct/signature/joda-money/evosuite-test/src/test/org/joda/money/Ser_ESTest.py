from __future__ import annotations
import time
import re
import mock
import pickle
import os
import typing
from typing import *
from io import BytesIO
import unittest
import pytest
import io
import unittest

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.Ser import *

# from src.test.org.joda.money.Ser_ESTest_scaffolding import *


class Ser_ESTest(unittest.TestCase):

    def test6(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        byteArrayOutputStream0 = io.BytesIO()
        objectOutputStream0 = pickle.Pickler(byteArrayOutputStream0)
        objectOutputStream0.dump(currencyUnit0)
        # Unstable assertion: self.assertEqual("\uFFFD\uFFFD\u0000\u0005sr\u0000\u0012org.joda.money.Ser\uFFFD\u0019\n)\uFFFD#\uFFFD4\f\u0000\u0000xpw\nC\u0000\u0003AUD\u0000$\u0000\u0002x", byteArrayOutputStream0.getvalue().decode())

    def test5(self) -> None:

        ser0 = Ser(14, None, 14)

        try:
            ser0.readExternal(None)
            self.fail("Expecting exception: RuntimeError")

        except TypeError as e:
            self.assertEqual(str(e), "argument of type 'NoneType' is not iterable")

    def test4(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        ser0 = Ser(14, currencyUnit0, -78)
        byteArrayOutputStream0 = io.BytesIO()
        objectOutputStream0 = pickle.Pickler(byteArrayOutputStream0)
        try:
            ser0.writeExternal(objectOutputStream0)
            self.fail("Expecting exception: InvalidClassException")

        except pickle.PicklingError as e:
            #
            # Joda-Money bug: Serialization broken
            #
            self.verifyException("org.joda.money.Ser", e)

    def test3(self) -> None:

        ser0 = Ser(0, None, 67)
        mockFileOutputStream0 = io.BytesIO()
        objectOutputStream0 = pickle.Pickler(mockFileOutputStream0)
        mockFileInputStream0 = io.BytesIO()
        bufferedInputStream0 = io.BufferedReader(
            io.BytesIO(mockFileInputStream0.getvalue())
        )
        objectInputStream0 = pickle.Unpickler(bufferedInputStream0)
        try:
            ser0.readExternal(objectInputStream0)
            self.fail("Expecting exception: EOFError")

        except EOFError as e:
            # no message in exception (str(e) returned '')
            self.assertIsInstance(e, EOFError)

    def test2(self) -> None:

        object0 = object()
        ser0 = Ser(0, object0, 67)
        mockFileOutputStream0 = io.BytesIO()
        objectOutputStream0 = pickle.Pickler(mockFileOutputStream0)

        try:
            ser0.writeExternal(objectOutputStream0)
            self.fail("Expecting exception: TypeError")

        except pickle.PicklingError as e:
            self.verifyException("org.joda.money.Ser", e)

    def test1(self) -> None:

        object0 = object()
        ser0 = Ser(-25, object0, -25)

        try:
            ser0.writeExternal(None)
            self.fail("Expecting exception: RuntimeError")

        except TypeError as e:
            self.verifyException("org.joda.money.Ser", e)

    def test0(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        ser0 = Ser(0, currencyUnit0, -1)
