from __future__ import annotations
import re
import io


class DestroyMode:

    ABANDONED: DestroyMode = None
    NORMAL: DestroyMode = None

    @staticmethod
    def initialize_fields() -> None:
        DestroyMode.ABANDONED: DestroyMode = None
        DestroyMode.NORMAL: DestroyMode = None


DestroyMode.initialize_fields()
