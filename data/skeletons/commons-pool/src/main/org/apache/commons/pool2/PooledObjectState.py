from __future__ import annotations

# Imports Begin
import io

# Imports End


class PooledObjectState:

    # Class Fields Begin
    IDLE: PooledObjectState = None
    ALLOCATED: PooledObjectState = None
    EVICTION: PooledObjectState = None
    EVICTION_RETURN_TO_HEAD: PooledObjectState = None
    VALIDATION: PooledObjectState = None
    VALIDATION_PREALLOCATED: PooledObjectState = None
    VALIDATION_RETURN_TO_HEAD: PooledObjectState = None
    INVALID: PooledObjectState = None
    ABANDONED: PooledObjectState = None
    RETURNING: PooledObjectState = None
    # Class Fields End

    # Class Methods Begin
    # Class Methods End
