# Imports Begin
from src.main.org.apache.commons.pool2.impl.EvictionConfig import *
from src.main.org.apache.commons.pool2.PooledObject import *
import typing
from abc import ABC

# Imports End


class EvictionPolicy(ABC):

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
