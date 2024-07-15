from __future__ import annotations
import time
import re
import random
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.pool2.impl.DefaultPooledObject import *


class TestDefaultPooledObject(unittest.TestCase):

    def testGetIdleTimeMillis(self) -> None:
        dpo = DefaultPooledObject(Object())
        negativeIdleTimeReturned = AtomicBoolean(False)
        executor = Executors.newFixedThreadPool(
            Runtime.getRuntime().availableProcessors() * 3
        )
        allocateAndDeallocateTask = lambda: [
            dpo.allocate() if i1 < 10000 else dpo.deallocate()
            for i1 in range(10000)
            if not (
                dpo.getIdleDuration().isNegative() or dpo.getIdleTime().isNegative()
            )
        ]
        getIdleTimeTask = lambda: [
            dpo.getIdleDuration() if i < 10000 else dpo.getIdleTime()
            for i in range(10000)
            if not (
                dpo.getIdleDuration().isNegative() or dpo.getIdleTime().isNegative()
            )
        ]
        probabilityOfAllocationTask = 0.7
        futures = []
        for i in range(1, 10001):
            randomTask = (
                allocateAndDeallocateTask
                if random() < probabilityOfAllocationTask
                else getIdleTimeTask
            )
            futures.append(executor.submit(randomTask))
        for future in futures:
            future.get()
        self.assertFalse(
            negativeIdleTimeReturned.get(),
            "DefaultPooledObject.getIdleTimeMillis() returned a negative value",
        )
