from __future__ import annotations
import time
import re
import mock
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.pool2.impl.InterruptibleReentrantLock import *

# from src.test.org.apache.commons.pool2.impl.InterruptibleReentrantLock_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *


class InterruptibleReentrantLock_ESTest(unittest.TestCase):

    def test3(self) -> None:

        interruptibleReentrantLock0 = InterruptibleReentrantLock(True)
        condition0 = interruptibleReentrantLock0.newCondition()

        try:
            interruptibleReentrantLock0.interruptWaiters(condition0)
            self.fail("Expecting exception: IllegalMonitorStateException")

        except IllegalMonitorStateException as e:
            verifyException(
                "java.util.concurrent.locks.AbstractQueuedSynchronizer$ConditionObject",
                e,
            )

    def test2(self) -> None:

        pass  # LLM could not translate this method

    def test1(self) -> None:

        interruptibleReentrantLock0 = InterruptibleReentrantLock(True)

        try:
            interruptibleReentrantLock0.interruptWaiters(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")
            self.assertEqual(type(e), RuntimeError)

    def test0(self) -> None:

        interruptibleReentrantLock0 = InterruptibleReentrantLock(True)
        interruptibleReentrantLock0.tryLock()
        condition0 = interruptibleReentrantLock0.newCondition()
        interruptibleReentrantLock0.interruptWaiters(condition0)
