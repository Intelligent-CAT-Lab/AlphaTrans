import pytest

from src.main.org.apache.commons.pool2.impl.PooledSoftReference import *
import unittest
import weakref


class TestPooledSoftReference(unittest.TestCase):

    __REFERENT = "test"
    __REFERENT2 = "test2"

    def __init__(self) -> None:
        self.ref = None
    

    def setUp(self) -> None:
        referentWrapper = ReferenceWrapper(TestPooledSoftReference.__REFERENT)
        softRef = weakref.ref(referentWrapper)
        self.ref = PooledSoftReference(softRef)
    
    
    @pytest.mark.test
    def testPooledSoftReference(self) -> None:
        self.assertEqual(
            TestPooledSoftReference.__REFERENT,
            self.ref.getObject().obj
        )

        softRef = self.ref.getReference()
        self.assertEqual(
            TestPooledSoftReference.__REFERENT,
            softRef().obj
        )
        softRef = None

        referent2Wrapper = ReferenceWrapper(TestPooledSoftReference.__REFERENT2)
        softRef = weakref.ref(referent2Wrapper)
        self.ref.setReference(softRef)

        self.assertEqual(
            TestPooledSoftReference.__REFERENT2,
            self.ref.getObject().obj
        )

        softRef = self.ref.getReference()
        self.assertEqual(
            TestPooledSoftReference.__REFERENT2,
            softRef().obj
        )
        softRef = None

    
    @pytest.mark.test
    def testToString(self) -> None:
        expected = "Referenced Object: test, State: IDLE"
        self.assertEqual(expected, self.ref.toString())



class ReferenceWrapper:
    def __init__(self, obj):
        self.obj = obj
