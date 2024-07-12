from __future__ import annotations
import time
import re
import mock
import collections
import os
import typing
from typing import *
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.pool2.PooledObject import *
from src.main.org.apache.commons.pool2.impl.BaseGenericObjectPool import *

# from src.test.org.apache.commons.pool2.impl.BaseGenericObjectPool_ESTest_scaffolding import *
from src.main.org.apache.commons.pool2.impl.DefaultEvictionPolicy import *

# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class BaseGenericObjectPool_ESTest(unittest.TestCase):

    def test7(self) -> None:

        baseGenericObjectPool_IdentityWrapper0 = BaseGenericObjectPool.IdentityWrapper(
            ""
        )
        string0 = baseGenericObjectPool_IdentityWrapper0.__str__()
        self.assertEqual("IdentityWrapper [instance=]", string0)

    def test6(self) -> None:

        baseGenericObjectPool0 = unittest.mock.Mock(spec=BaseGenericObjectPool)
        arrayDeque0 = collections.deque()
        baseGenericObjectPool_EvictionIterator0 = EvictionIterator(arrayDeque0)
        deque0 = baseGenericObjectPool_EvictionIterator0.getIdleObjects()
        self.assertEqual(0, len(deque0))

    def test5(self) -> None:

        baseGenericObjectPool0 = unittest.mock.Mock(spec=BaseGenericObjectPool)
        arrayDeque0 = collections.deque()
        baseGenericObjectPool_EvictionIterator0 = EvictionIterator(arrayDeque0)
        boolean0 = baseGenericObjectPool_EvictionIterator0.hasNext()
        self.assertFalse(boolean0)

    def test4(self) -> None:

        baseGenericObjectPool_IdentityWrapper0 = BaseGenericObjectPool.IdentityWrapper(
            ""
        )
        boolean0 = baseGenericObjectPool_IdentityWrapper0.equals("")
        self.assertFalse(boolean0)

    def test3(self) -> None:

        defaultEvictionPolicy0 = DefaultEvictionPolicy()
        baseGenericObjectPool_IdentityWrapper0 = BaseGenericObjectPool.IdentityWrapper(
            defaultEvictionPolicy0
        )
        baseGenericObjectPool_IdentityWrapper1 = BaseGenericObjectPool.IdentityWrapper(
            baseGenericObjectPool_IdentityWrapper0
        )
        boolean0 = baseGenericObjectPool_IdentityWrapper1.equals(
            baseGenericObjectPool_IdentityWrapper0
        )
        self.assertFalse(boolean0)

    def test2(self) -> None:

        long0 = Long(0)
        baseGenericObjectPool_IdentityWrapper0 = IdentityWrapper(long0)
        baseGenericObjectPool_IdentityWrapper1 = IdentityWrapper(
            baseGenericObjectPool_IdentityWrapper0
        )
        object0 = baseGenericObjectPool_IdentityWrapper1.getObject()
        boolean0 = baseGenericObjectPool_IdentityWrapper0.equals(object0)
        self.assertTrue(boolean0)

    def test1(self) -> None:

        baseGenericObjectPool0 = unittest.mock.Mock(spec=BaseGenericObjectPool)
        arrayDeque0 = collections.deque()
        pooledObject0 = unittest.mock.Mock(spec=PooledObject)
        pooledObject0.toString.return_value = None
        arrayDeque0.append(pooledObject0)
        baseGenericObjectPool_EvictionIterator0 = (
            baseGenericObjectPool0.EvictionIterator(arrayDeque0)
        )
        baseGenericObjectPool_EvictionIterator0.next()
        baseGenericObjectPool_EvictionIterator0.remove()

    def test0(self) -> None:

        baseGenericObjectPool0 = unittest.mock.Mock(spec=BaseGenericObjectPool)
        baseGenericObjectPool_Evictor0 = baseGenericObjectPool0.Evictor()
        scheduledFuture0 = unittest.mock.Mock(spec=ScheduledFuture)
        scheduledFuture0.cancel.return_value = False
        baseGenericObjectPool_Evictor0.setScheduledFuture(scheduledFuture0)
        baseGenericObjectPool_Evictor0.cancel()
