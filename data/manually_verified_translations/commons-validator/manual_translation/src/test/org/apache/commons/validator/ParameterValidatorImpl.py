from __future__ import annotations
import locale
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.apache.commons.validator.Field import *
from src.main.org.apache.commons.validator.Form import *
from src.main.org.apache.commons.validator.Validator import *
from src.main.org.apache.commons.validator.ValidatorAction import *
from src.main.org.apache.commons.validator.ValidatorResults import *


class ParameterValidatorImpl:

    @staticmethod
    def validateParameter(
        bean: typing.Any,
        form: Form,
        field: typing.Any,
        validator: Validator,
        action: ValidatorAction,
        results: ValidatorResults,
        locale: typing.Any,
    ) -> bool:

        return True
