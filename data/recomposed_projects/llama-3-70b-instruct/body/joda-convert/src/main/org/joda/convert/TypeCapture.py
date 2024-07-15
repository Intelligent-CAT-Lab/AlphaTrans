from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.joda.convert.Types import *


class TypeCapture(ABC):

    def capture(self) -> typing.Type:
        superclass = self.__class__.getGenericSuperclass()
        Types.checkArgument2(
            isinstance(superclass, ParameterizedType),
            "%s isn't parameterized",
            superclass,
        )
        return superclass.getActualTypeArguments()[0]
