from src.main.org.apache.commons.pool2.impl.DefaultPooledObject import *
from concurrent.futures import ThreadPoolExecutor
from threading import Event
import unittest
import multiprocessing
import datetime
import random

class TestDefaultPooledObject(unittest.TestCase):

    def testGetIdleTimeMillis(self) -> None:
        try:
            dpo = DefaultPooledObject(object())
            negativeIdleTimeReturned = Event()
            executor = ThreadPoolExecutor(max_workers=multiprocessing.cpu_count() * 3)

            def allocateAndDeallocateTask():
                for i1 in range(10000):
                    if (dpo.getIdleDuration() < datetime.timedelta(0) or
                        dpo.getIdleTime() < datetime.timedelta(0)):
                        negativeIdleTimeReturned.set()
                        break
                    if (dpo.getIdleDuration() < datetime.timedelta(0) or
                        dpo.getIdleTime() < datetime.timedelta(0)):
                        negativeIdleTimeReturned.set()
                        break
                dpo.allocate()
                for i2 in range(10000):
                    if (dpo.getIdleDuration() < datetime.timedelta(0) or 
                        dpo.getIdleTime() < datetime.timedelta(0)):
                        negativeIdleTimeReturned.set()
                        break
                dpo.deallocate()

            def getIdleTimeTask():
                for i in range(10000):
                    if (dpo.getIdleDuration() < datetime.timedelta(0) or
                        dpo.getIdleTime() < datetime.timedelta(0)):
                        negativeIdleTimeReturned.set()
                        break

            probabilityOfAllocationTask = 0.7
            futures = []
            for i in range(1, 10001):
                if random.random() < probabilityOfAllocationTask:
                    randomTask = allocateAndDeallocateTask
                else:
                    randomTask = getIdleTimeTask
                futures.append(executor.submit(randomTask))

            for future in futures:
                future.result()

            self.assertFalse(
                negativeIdleTimeReturned.is_set(),
                "DefaultPooledObject.getIdleTimeMillis() returned a negative value"
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
