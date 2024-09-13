from __future__ import annotations
import copy
import re
import os
import io
import typing
from typing import *
import logging

# from src.main.org.apache.commons.logging.Log import *
# from src.main.org.apache.commons.logging.LogFactory import *
from src.main.org.apache.commons.validator.Arg import *
from src.main.org.apache.commons.validator.Msg import *
from src.main.org.apache.commons.validator.Var import *


class ValidatorUtils:

    __LOG: logging.Logger = logging.getLogger(__name__)

    @staticmethod
    def copyMap(map_: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:

        results = {}

        for key, value in map_.items():
            if isinstance(value, Msg):
                results[key] = value.clone()
            elif isinstance(value, Arg):
                results[key] = value.clone()
            elif isinstance(value, Var):
                results[key] = value.clone()
            else:
                results[key] = value

        return results

    @staticmethod
    def replace(value: str, key: str, replaceValue: str) -> str:

        if value is None or key is None or replaceValue is None:
            return value

        pos = value.find(key)

        if pos < 0:
            return value

        length = len(value)
        start = pos
        end = pos + len(key)

        if length == len(key):
            value = replaceValue

        elif end == length:
            value = value[:start] + replaceValue

        else:
            value = (
                value[:start]
                + replaceValue
                + ValidatorUtils.replace(value[end:], key, replaceValue)
            )

        return value
