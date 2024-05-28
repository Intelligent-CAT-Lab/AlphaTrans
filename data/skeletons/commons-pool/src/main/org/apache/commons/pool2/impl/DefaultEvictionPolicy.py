from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.impl.EvictionPolicy import *
from src.main.org.apache.commons.pool2.impl.EvictionConfig import *
from src.main.org.apache.commons.pool2.PooledObject import *
import typing
from typing import *
import io

# Imports End


class DefaultEvictionPolicy(EvictionPolicy):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def evict(
        self,
        config: EvictionConfig,
        underTest: PooledObject[typing.Any],
        idleCount: int,
    ) -> bool:
        pass

    # Class Methods End
