from __future__ import annotations
import time
import re
import mock
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.pool2.PooledObject import *
from src.main.org.apache.commons.pool2.impl.DefaultEvictionPolicy import *

# from src.test.org.apache.commons.pool2.impl.DefaultEvictionPolicy_ESTest_scaffolding import *
from src.main.org.apache.commons.pool2.impl.EvictionConfig import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.System import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class DefaultEvictionPolicy_ESTest(unittest.TestCase):

    def test1(self) -> None:

        defaultEvictionPolicy0 = DefaultEvictionPolicy()
        chronoUnit0 = ChronoUnit.NANOS
        duration0 = chronoUnit0.getDuration()
        evictionConfig0 = EvictionConfig(duration0, duration0, -19)
        chronoUnit1 = ChronoUnit.MILLIS
        duration1 = chronoUnit1.getDuration()
        pooledObject0 = mock(PooledObject)
        when(pooledObject0).getIdleDuration().thenReturn(duration1)
        boolean0 = defaultEvictionPolicy0.evict(evictionConfig0, pooledObject0, 1)
        assert boolean0

    def test0(self) -> None:

        defaultEvictionPolicy0 = DefaultEvictionPolicy[int]()
        chronoUnit0 = ChronoUnit.NANOS
        duration0 = chronoUnit0.getDuration()
        evictionConfig0 = EvictionConfig(duration0, duration0, 7)
        pooledObject0 = mock(PooledObject[int], ViolatedAssumptionAnswer())
        doReturn(duration0, duration0).when(pooledObject0).getIdleDuration()
        defaultEvictionPolicy0.evict(evictionConfig0, pooledObject0, 1)
        defaultEvictionPolicy1 = DefaultEvictionPolicy[object]()
        defaultEvictionPolicy2 = DefaultEvictionPolicy[int]()
        chronoUnit1 = ChronoUnit.MILLIS
        duration1 = chronoUnit1.getDuration()
        pooledObject1 = mock(PooledObject[int], ViolatedAssumptionAnswer())
        doReturn(duration1, duration0).when(pooledObject1).getIdleDuration()
        defaultEvictionPolicy3 = DefaultEvictionPolicy[ChronoLocalDate]()
        pooledObject2 = mock(PooledObject[ChronoLocalDate], ViolatedAssumptionAnswer())
        doReturn(duration1, duration1).when(pooledObject2).getIdleDuration()
        defaultEvictionPolicy3.evict(evictionConfig0, pooledObject2, 7)
        defaultEvictionPolicy4 = DefaultEvictionPolicy[int]()
        defaultEvictionPolicy2.evict(evictionConfig0, pooledObject1, 1)
        System.setCurrentTimeMillis(7)
        pooledObject3 = mock(PooledObject[int], ViolatedAssumptionAnswer())
        doReturn(None).when(pooledObject3).getIdleDuration()
        try:
            defaultEvictionPolicy0.evict(evictionConfig0, pooledObject3, 7)
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            verifyException("java.time.Duration", e)
