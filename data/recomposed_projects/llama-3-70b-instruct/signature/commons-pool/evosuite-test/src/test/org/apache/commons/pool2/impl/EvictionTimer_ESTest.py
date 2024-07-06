from __future__ import annotations
import time
import re
import mock
import os
import datetime
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.pool2.impl.BaseGenericObjectPool import *
from src.main.org.apache.commons.pool2.impl.EvictionTimer import *

# from src.test.org.apache.commons.pool2.impl.EvictionTimer_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class EvictionTimer_ESTest(unittest.TestCase):

    def test3(self) -> None:
        int0 = EvictionTimer.getNumTasks()
        self.assertEqual(0, int0)

    def test2(self) -> None:

        duration0 = datetime.timedelta(0)
        EvictionTimer.cancel(None, duration0, False)

    def test1(self) -> None:

        baseGenericObjectPool0 = unittest.mock.Mock(spec=BaseGenericObjectPool)
        baseGenericObjectPool_Evictor0 = baseGenericObjectPool0.Evictor()
        duration0 = datetime.timedelta(milliseconds=-1)

        try:
            EvictionTimer.cancel(baseGenericObjectPool_Evictor0, duration0, False)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertIsInstance(e, RuntimeError)
            self.assertIsNone(e.getMessage())

    def test0(self) -> None:

        baseGenericObjectPool0 = mock(BaseGenericObjectPool, ViolatedAssumptionAnswer())
        baseGenericObjectPool_Evictor0 = baseGenericObjectPool0.new_Evictor()
        duration0 = Duration.ofMillis(100)
        scheduledFuture0 = mock(ScheduledFuture, ViolatedAssumptionAnswer())
        when(scheduledFuture0).cancel(any_bool()).thenReturn(False)
        baseGenericObjectPool_Evictor0.setScheduledFuture(scheduledFuture0)
        EvictionTimer.cancel(baseGenericObjectPool_Evictor0, duration0, True)
