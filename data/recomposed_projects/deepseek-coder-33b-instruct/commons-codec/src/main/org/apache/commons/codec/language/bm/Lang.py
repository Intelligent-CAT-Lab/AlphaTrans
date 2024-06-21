from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.Resources import *
from src.main.org.apache.commons.codec.language.bm.Languages import *
from src.main.org.apache.commons.codec.language.bm.NameType import *
from src.main.org.apache.commons.codec.language.bm.ResourceConstants import *


class LangRule:

    __pattern: re.Pattern = None
    __languages: typing.Set[str] = None
    __acceptOnMatch: bool = None

    def matches(self, txt: str) -> bool:

        return bool(self.__pattern.search(txt))

    def __init__(
        self, pattern: re.Pattern, languages: typing.Set[str], acceptOnMatch: bool
    ) -> None:

        self.__pattern = pattern
        self.__languages = languages
        self.__acceptOnMatch = acceptOnMatch


class Lang:

    __rules: typing.List[LangRule] = None
    __languages: Languages = None

    __LANGUAGE_RULES_RN: str = "org/apache/commons/codec/language/bm/%s_lang.txt"

    __Langs: Dict[NameType, Lang] = {}

    def guessLanguages(self, input: str) -> LanguageSet:

        pass  # LLM could not translate this method

    def guessLanguage(self, text: str) -> str:

        ls = self.guessLanguages(text)
        return ls.getAny() if ls.isSingleton() else Languages.ANY

    @staticmethod
    def loadFromResource(languageRulesResourceName: str, languages: Languages) -> Lang:

        rules = []
        inExtendedComment = False

        with io.open(
            Resources.getInputStream(languageRulesResourceName),
            "r",
            encoding=ResourceConstants.ENCODING,
        ) as scanner:
            for rawLine in scanner:
                line = rawLine
                if inExtendedComment:
                    if line.endswith(ResourceConstants.EXT_CMT_END):
                        inExtendedComment = False
                elif line.startswith(ResourceConstants.EXT_CMT_START):
                    inExtendedComment = True
                else:
                    cmtI = line.find(ResourceConstants.CMT)
                    if cmtI >= 0:
                        line = line[:cmtI]

                    line = line.strip()

                    if not line:
                        continue  # empty lines can be safely skipped

                    parts = line.split()

                    if len(parts) != 3:
                        raise ValueError(
                            f"Malformed line '{rawLine}' in language resource '{languageRulesResourceName}'"
                        )

                    pattern = re.compile(parts[0])
                    langs = parts[1].split("+")
                    accept = parts[2] == "true"

                    rules.append(LangRule(pattern, set(langs), accept))

        return Lang(rules, languages)

    @staticmethod
    def instance(nameType: NameType) -> Lang:

        return Langs.get(nameType)

    def __init__(self, rules: typing.List[LangRule], languages: Languages) -> None:

        self.__rules = rules
        self.__languages = languages
