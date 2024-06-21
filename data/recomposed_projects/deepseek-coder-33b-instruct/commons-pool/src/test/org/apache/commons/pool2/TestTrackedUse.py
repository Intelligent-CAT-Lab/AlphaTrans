from __future__ import annotations
import io
from src.main.org.apache.commons.pool2.TrackedUse import *


class DefaultTrackedUse(TrackedUse):

    def getLastUsed(self) -> int:

        return 1


class TestTrackedUse:

    def testDefaultGetLastUsedInstant(self) -> None:

        class DefaultTrackedUse(TrackedUse):
            def getLastUsedInstant(self) -> Instant:
                return Instant.ofEpochMilli(1)

        assert Instant.ofEpochMilli(1) == DefaultTrackedUse().getLastUsedInstant()
