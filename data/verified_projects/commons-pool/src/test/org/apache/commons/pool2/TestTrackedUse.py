import pytest

import unittest
from datetime import datetime, timezone
from src.main.org.apache.commons.pool2.TrackedUse import *

class TestTrackedUse(unittest.TestCase):

    class DefaultTrackedUse(TrackedUse):

        def getLastUsed(self) -> int:
            return 1

    
    @pytest.mark.test
    def testDefaultGetLastUsedInstant(self) -> None:
        expected = datetime.fromtimestamp(1 / 1000, tz=timezone.utc)
        self.assertEqual(
            expected,
            TestTrackedUse.DefaultTrackedUse().getLastUsedInstant()
        )
