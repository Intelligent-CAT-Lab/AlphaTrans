from __future__ import annotations

# Imports Begin
import os
import typing
from typing import *
import io
from abc import ABC

# Imports End


class SccAlgorithmSelector(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def applyingTarjan(self) -> typing.Set[typing.Set[typing.Any]]:
        pass

    def applyingKosarajuSharir1(self, source: typing.Any) -> typing.Set[typing.Any]:
        pass

    def applyingKosarajuSharir0(self) -> typing.Set[typing.Set[typing.Any]]:
        pass

    def applyingCheriyanMehlhornGabow(self) -> typing.Set[typing.Set[typing.Any]]:
        pass

    # Class Methods End
