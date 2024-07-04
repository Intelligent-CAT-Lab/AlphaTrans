from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
import os


class SccAlgorithmSelector(ABC):

    def applyingTarjan(self) -> typing.Set[typing.Set[typing.Any]]:

        pass

    def applyingKosarajuSharir1(self, source: typing.Any) -> typing.Set[typing.Any]:

        pass

    def applyingKosarajuSharir0(self) -> typing.Set[typing.Set[typing.Any]]:

        pass

    def applyingCheriyanMehlhornGabow(self) -> typing.Set[typing.Set[typing.Any]]:
        pass
