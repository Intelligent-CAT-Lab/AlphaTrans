from __future__ import annotations
import io
from src.main.org.apache.commons.pool2.impl.PooledSoftReference import *


class TestPooledSoftReference:

    __REFERENT2: str = "test2"

    __REFERENT: str = "test"

    def testToString(self) -> None:

        expected = "Referenced Object: test, State: IDLE"
        assert expected == ref.toString()

    def testPooledSoftReference(self) -> None:

        assert self.__REFERENT == ref.getObject()

        softRef = ref.getReference()
        assert self.__REFERENT == softRef.get()
        softRef.clear()

        softRef = SoftReference(self.__REFERENT2)
        ref.setReference(softRef)

        assert self.__REFERENT2 == ref.getObject()

        softRef = ref.getReference()
        assert self.__REFERENT2 == softRef.get()
        softRef.clear()

    def setUp(self) -> None:

        softRef = SoftReference(self.__REFERENT)
        self.ref = PooledSoftReference(softRef)
