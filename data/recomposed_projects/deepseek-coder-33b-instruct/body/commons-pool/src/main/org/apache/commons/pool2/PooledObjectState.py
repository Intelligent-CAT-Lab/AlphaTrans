from __future__ import annotations
import re
import io


class PooledObjectState:

    RETURNING: PooledObjectState = None

    ABANDONED: PooledObjectState = None

    INVALID: PooledObjectState = None

    VALIDATION_RETURN_TO_HEAD: PooledObjectState = None

    VALIDATION_PREALLOCATED: PooledObjectState = None

    VALIDATION: PooledObjectState = None

    EVICTION_RETURN_TO_HEAD: PooledObjectState = None

    EVICTION: PooledObjectState = None

    ALLOCATED: PooledObjectState = None

    IDLE: PooledObjectState = None
