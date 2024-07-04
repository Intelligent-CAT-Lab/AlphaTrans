from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.pool2.PooledObject import *
from src.main.org.apache.commons.pool2.impl.EvictionConfig import *


class EvictionPolicy(ABC):

    def evict(
        self,
        config: EvictionConfig,
        underTest: PooledObject[typing.Any],
        idleCount: int,
    ) -> bool:

        # Your implementation here
        pass
