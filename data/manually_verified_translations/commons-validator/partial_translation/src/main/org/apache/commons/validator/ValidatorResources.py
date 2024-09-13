from __future__ import annotations
import re
import io
import typing
from typing import *
import logging

# from src.main.org.apache.commons.logging.Log import *
# from src.main.org.apache.commons.logging.LogFactory import *
from src.main.org.apache.commons.validator.FormSet import *


class ValidatorResources:

    _defaultFormSet: FormSet = None

    _defaultLocale: typing.Any = None  # LLM could not translate this field

    __ARGS_PATTERN: str = "form-validation/formset/form/field/arg"
    __log: logging.Logger = logging.getLogger(__name__)
    __REGISTRATIONS: typing.List[typing.List[str]] = [
        [
            "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.0//EN",
            "/org/apache/commons/validator/resources/validator_1_0.dtd",
        ],
        [
            "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.0.1//EN",
            "/org/apache/commons/validator/resources/validator_1_0_1.dtd",
        ],
        [
            "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.1//EN",
            "/org/apache/commons/validator/resources/validator_1_1.dtd",
        ],
        [
            "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.1.3//EN",
            "/org/apache/commons/validator/resources/validator_1_1_3.dtd",
        ],
        [
            "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.2.0//EN",
            "/org/apache/commons/validator/resources/validator_1_2_0.dtd",
        ],
        [
            "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.3.0//EN",
            "/org/apache/commons/validator/resources/validator_1_3_0.dtd",
        ],
        [
            "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.4.0//EN",
            "/org/apache/commons/validator/resources/validator_1_4_0.dtd",
        ],
    ]
    __VALIDATOR_RULES: str = "digester-rules.xml"
    __serialVersionUID: int = -8203745881446239554

    def _buildKey(self, fs: FormSet) -> str:
        return self.__buildLocale(fs.getLanguage(), fs.getCountry(), fs.getVariant())

    def __init__(self) -> None:
        super().__init__()

    def __getLog(self) -> logging.Logger:
        return self.__log

    def __buildLocale(self, lang: str, country: str, variant: str) -> str:

        key = lang if lang and len(lang) > 0 else ""
        key += "_" + country if country and len(country) > 0 else ""
        key += "_" + variant if variant and len(variant) > 0 else ""

        return key
