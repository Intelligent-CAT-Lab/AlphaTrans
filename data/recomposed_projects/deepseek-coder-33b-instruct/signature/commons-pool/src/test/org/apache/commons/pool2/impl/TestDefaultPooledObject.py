from __future__ import annotations
import re
import random
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.pool2.impl.DefaultPooledObject import *


class TestDefaultPooledObject(unittest.TestCase):

    def testGetIdleTimeMillis(self) -> None:

        dpo = DefaultPooledObject(object())
        negativeIdleTimeReturned = [False]
        executor = ThreadPoolExecutor(max_workers=(os.cpu_count() * 3))

        def allocateAndDeallocateTask():
            for _ in range(10000):
                if dpo.getIdleDuration().isNegative() or dpo.getIdleTime().isNegative():
                    negativeIdleTimeReturned[0] = True
                    break
            dpo.allocate()
            for _ in range(10000):
                if dpo.getIdleDuration().isNegative() or dpo.getIdleTime().isNegative():
                    negativeIdleTimeReturned[0] = True
                    break
            dpo.deallocate()

        def getIdleTimeTask():
            for _ in range(10000):
                if dpo.getIdleDuration().isNegative() or dpo.getIdleTime().isNegative():
                    negativeIdleTimeReturned[0] = True
                    break

        probabilityOfAllocationTask = 0.7
        futures = []
        for _ in range(10000):
            randomTask = (
                allocateAndDeallocateTask
                if random.random() < probabilityOfAllocationTask
                else getIdleTimeTask
            )
            futures.append(executor.submit(randomTask))

        for future in futures:
            future.result()

        self.assertFalse(
            negativeIdleTimeReturned[0],
            "DefaultPooledObject.getIdleTimeMillis() returned a negative value",
        )
