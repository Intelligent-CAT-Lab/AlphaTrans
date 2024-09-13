from __future__ import annotations
import time
import re
from io import StringIO
import io
import typing
from typing import *
import os


class Arg:

    _resource: bool = True
    _position: int = -1
    _name: str = ""
    _key: str = None
    _bundle: str = None
    __serialVersionUID: int = -8922606779669839294

    def toString(self) -> str:

        results = io.StringIO()

        results.write("Arg: name=")
        results.write(self._name)
        results.write("  key=")
        results.write(self._key)
        results.write("  position=")
        results.write(str(self._position))
        results.write("  bundle=")
        results.write(self._bundle)
        results.write("  resource=")
        results.write(str(self._resource))
        results.write("\n")

        return results.getvalue()

    def clone(self) -> typing.Any:

        try:
            return super().clone()

        except Exception as e:
            raise RuntimeError(str(e))

    def setResource(self, resource: bool) -> None:
        self._resource = resource

    def setPosition(self, position: int) -> None:
        self._position = position

    def setName(self, name: str) -> None:
        self._name = name

    def setKey(self, key: str) -> None:
        self._key = key

    def setBundle(self, bundle: str) -> None:
        self._bundle = bundle

    def isResource(self) -> bool:
        return self._resource

    def getPosition(self) -> int:
        return self._position

    def getName(self) -> str:
        return self._name

    def getKey(self) -> str:
        return self._key

    def getBundle(self) -> str:
        return self._bundle
