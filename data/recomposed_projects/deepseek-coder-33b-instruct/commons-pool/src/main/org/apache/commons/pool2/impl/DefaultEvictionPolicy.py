from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.apache.commons.pool2.PooledObject import *
from src.main.org.apache.commons.pool2.impl.EvictionConfig import *
from src.main.org.apache.commons.pool2.impl.EvictionPolicy import *


class DefaultEvictionPolicy(EvictionPolicy):

    def evict(
        self,
        config: EvictionConfig,
        underTest: PooledObject[typing.Any],
        idleCount: int,
    ) -> bool:

        return (
            config.getIdleSoftEvictDuration().compareTo(underTest.getIdleDuration()) < 0
            and config.getMinIdle() < idleCount
        ) or config.getIdleEvictDuration().compareTo(underTest.getIdleDuration()) < 0
