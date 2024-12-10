from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.PooledObject import *
from src.main.org.apache.commons.pool2.BasePooledObjectFactory import *
from src.main.org.apache.commons.pool2.impl.PoolImplUtils import *
import unittest
import os
import datetime
import typing
from typing import *
import io
from abc import ABC

# Imports End


class SimpleFactory(BasePooledObjectFactory):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def wrap(self, obj: str) -> PooledObject[str]:
        pass

    def create(self) -> str:
        pass

    # Class Methods End


class FactoryAB(BasePooledObjectFactory, ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    # Class Methods End

    pass


class FactoryBA(FactoryAB, ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    # Class Methods End

    pass


class FactoryC(FactoryBA, ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    # Class Methods End

    pass


class FactoryDE(FactoryC, ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    # Class Methods End

    pass


class FactoryF(FactoryDE, ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    # Class Methods End

    pass


class NotSimpleFactory(FactoryF):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def wrap(self, obj: int) -> PooledObject[int]:
        pass

    def create(self) -> int:
        pass

    # Class Methods End


class TestPoolImplUtils(unittest.TestCase):

    # Class Fields Begin
    __INSTANT_1: datetime.datetime = None
    __INSTANT_0: datetime.datetime = None
    # Class Fields End

    # Class Methods Begin
    def testToDuration_test0_decomposed(self) -> None:
        pass

    def testToChronoUnit_test0_decomposed(self) -> None:
        pass

    def testMinInstants_test0_decomposed(self) -> None:
        pass

    def testMaxInstants_test0_decomposed(self) -> None:
        pass

    def testFactoryTypeSimple_test1_decomposed(self) -> None:
        pass

    def testFactoryTypeSimple_test0_decomposed(self) -> None:
        pass

    def testFactoryTypeNotSimple_test1_decomposed(self) -> None:
        pass

    def testFactoryTypeNotSimple_test0_decomposed(self) -> None:
        pass

    # Class Methods End
