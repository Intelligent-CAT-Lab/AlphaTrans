from __future__ import annotations
import re
from io import StringIO
from abc import ABC
import io


class BaseObject(ABC):

    def toString(self) -> str:

        builder = io.StringIO()
        builder.write(self.__class__.__name__)
        builder.write(" [")
        self._toStringAppendFields(builder)
        builder.write("]")
        return builder.getvalue()

    def _toStringAppendFields(self, builder: str) -> None:

        # The Java method is empty, so there's no translation needed.
        # If there was code in the method, it would be translated here.
        pass
