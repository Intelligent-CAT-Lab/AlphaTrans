from __future__ import annotations
import io
from src.main.org.apache.commons.pool2.impl.DefaultPooledObject import *


class TestDefaultPooledObject:

    def testGetIdleTimeMillis(self) -> None:

        dpo = DefaultPooledObject(object())
        negativeIdleTimeReturned = AtomicBoolean(False)
        executor = Executors.newFixedThreadPool(
            Runtime.getRuntime().availableProcessors() * 3
        )

        def allocateAndDeallocateTask():
            for i1 in range(10000):
                if dpo.getIdleDuration().isNegative() or dpo.getIdleTime().isNegative():
                    negativeIdleTimeReturned.set(True)
                    break
                if dpo.getIdleDuration().isNegative() or dpo.getIdleTime().isNegative():
                    negativeIdleTimeReturned.set(True)
                    break
            dpo.allocate()
            for i2 in range(10000):
                if dpo.getIdleDuration().isNegative() or dpo.getIdleTime().isNegative():
                    negativeIdleTimeReturned.set(True)
                    break
            dpo.deallocate()

        def getIdleTimeTask():
            for i in range(10000):
                if dpo.getIdleDuration().isNegative() or dpo.getIdleTime().isNegative():
                    negativeIdleTimeReturned.set(True)
                    break

        probabilityOfAllocationTask = 0.7
        futures = []
        for i in range(1, 10001):
            randomTask = (
                allocateAndDeallocateTask
                if random.random() < probabilityOfAllocationTask
                else getIdleTimeTask
            )
            futures.append(executor.submit(randomTask))

        for future in futures:
            future.get()

        assert (
            not negativeIdleTimeReturned.get()
        ), "DefaultPooledObject.getIdleTimeMillis() returned a negative value"
