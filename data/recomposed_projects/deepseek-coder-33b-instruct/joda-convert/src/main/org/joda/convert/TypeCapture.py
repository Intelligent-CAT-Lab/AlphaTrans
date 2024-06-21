from __future__ import annotations
from abc import ABC
import io
import typing
from typing import *
from src.main.org.joda.convert.Types import *


class TypeCapture(ABC):

    def capture(self) -> typing.Type:

        superclass = self.__class__.__bases__[0].__mro__[1]
        Types.checkArgument2(
            isinstance(superclass, typing._GenericAlias),
            "%s isn't parameterized" % superclass,
        )
        return superclass.__args__[0]
