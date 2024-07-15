from __future__ import annotations
import re
import io
import typing
import locale
from typing import *
import logging

# from src.main.org.apache.commons.logging.Log import *
# from src.main.org.apache.commons.logging.LogFactory import *
from src.main.org.apache.commons.validator.FormSet import *


class ValidatorResources:

    _defaultFormSet: FormSet = None

    _defaultLocale: typing.Any = locale.getdefaultlocale()
    __ARGS_PATTERN: str = "form-validation/formset/form/field/arg"
    __log: logging.Logger = None
    __REGISTRATIONS: typing.List[str] = [
        "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.0//EN",
        "/org/apache/commons/validator/resources/validator_1_0.dtd",
        "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.0.1//EN",
        "/org/apache/commons/validator/resources/validator_1_0_1.dtd",
        "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.1//EN",
        "/org/apache/commons/validator/resources/validator_1_1.dtd",
        "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.1.3//EN",
        "/org/apache/commons/validator/resources/validator_1_1_3.dtd",
        "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.2.0//EN",
        "/org/apache/commons/validator/resources/validator_1_2_0.dtd",
        "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.3.0//EN",
        "/org/apache/commons/validator/resources/validator_1_3_0.dtd",
        "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.4.0//EN",
        "/org/apache/commons/validator/resources/validator_1_4_0.dtd",
    ]
    __VALIDATOR_RULES: str = "digester-rules.xml"
    __serialVersionUID: int = -8203745881446239554

    @staticmethod
    def initialize_fields() -> None:
        ValidatorResources.__log: logging.Logger = logging.getLogger(
            ValidatorResources.__name__
        )

    def _buildKey(self, fs: FormSet) -> str:
        return self.__buildLocale(fs.getLanguage(), fs.getCountry(), fs.getVariant())

    def __init__(self) -> None:

        self._defaultFormSet = None
        self._defaultLocale = None
        self.__ARGS_PATTERN = "form-validation/formset/form/field/arg"
        self.__log = LogFactory.getLog(ValidatorResources)
        self.__REGISTRATIONS = [
            "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.0//EN",
            "/org/apache/commons/validator/resources/validator_1_0.dtd",
            "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.0.1//EN",
            "/org/apache/commons/validator/resources/validator_1_0_1.dtd",
            "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.1//EN",
            "/org/apache/commons/validator/resources/validator_1_1.dtd",
            "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.1.3//EN",
            "/org/apache/commons/validator/resources/validator_1_1_3.dtd",
            "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.2.0//EN",
            "/org/apache/commons/validator/resources/validator_1_2_0.dtd",
            "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.3.0//EN",
            "/org/apache/commons/validator/resources/validator_1_3_0.dtd",
            "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.4.0//EN",
            "/org/apache/commons/validator/resources/validator_1_4_0.dtd",
        ]
        self.__VALIDATOR_RULES = "digester-rules.xml"
        self.__serialVersionUID = -8203745881446239554

    def __getLog(self) -> logging.Logger:
        if self.__log is None:
            self.__log = LogFactory.getLog(ValidatorResources)
        return self.__log

    def __buildLocale(self, lang: str, country: str, variant: str) -> str:

        key = lang if lang is not None and len(lang) > 0 else ""
        key += "_" + country if country is not None and len(country) > 0 else ""
        key += "_" + variant if variant is not None and len(variant) > 0 else ""

        return key


ValidatorResources.initialize_fields()
