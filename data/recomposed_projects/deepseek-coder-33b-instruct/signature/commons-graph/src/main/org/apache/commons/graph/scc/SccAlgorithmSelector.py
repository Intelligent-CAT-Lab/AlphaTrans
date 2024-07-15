from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
import os


class SccAlgorithmSelector(ABC):

    def applyingTarjan(self) -> typing.Set[typing.Set[typing.Any]]:

        # Implement the method here
        pass

    def applyingKosarajuSharir1(self, source: typing.Any) -> typing.Set[typing.Any]:

        # Implement the Kosaraju-Sharir algorithm here
        # This is a placeholder and will need to be replaced with the actual implementation
        pass

    def applyingKosarajuSharir0(self) -> typing.Set[typing.Set[typing.Any]]:

        # Implementation of the Kosaraju-Sharir algorithm goes here
        # This is a placeholder, as the actual implementation is not provided in the Java code
        pass

    def applyingCheriyanMehlhornGabow(self) -> typing.Set[typing.Set[typing.Any]]:
        pass
