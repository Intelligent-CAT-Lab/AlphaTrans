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

    __acceptOnMatch: bool = False

    def matches(self, txt: str) -> bool:
        return self.__pattern.search(txt) is not None

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
    __Langs: typing.Dict[NameType, Lang] = {}

    @staticmethod
    def run_static_init():
        for s in NameType.values():
            Langs.put(
                s,
                loadFromResource(
                    String.format(LANGUAGE_RULES_RN, s.getName()),
                    Languages.getInstance0(s),
                ),
            )

    def guessLanguages(self, input: str) -> LanguageSet:
        text = input.lower()
        langs = set(self.__languages.getLanguages())
        for rule in self.__rules:
            if rule.matches(text):
                if rule.__acceptOnMatch:
                    langs.intersection_update(rule.__languages)
                else:
                    langs.difference_update(rule.__languages)
        ls = LanguageSet.from_(langs)
        return ls if ls != Languages.NO_LANGUAGES else Languages.ANY_LANGUAGE

    def guessLanguage(self, text: str) -> str:
        ls = self.guessLanguages(text)
        return ls.getAny() if ls.isSingleton() else Languages.ANY

    @staticmethod
    def loadFromResource(languageRulesResourceName: str, languages: Languages) -> Lang:
        rules: typing.List[LangRule] = []
        with Resources.getInputStream(languageRulesResourceName) as scanner:
            inExtendedComment: bool = False
            while scanner.hasNextLine():
                rawLine: str = scanner.nextLine()
                line: str = rawLine
                if inExtendedComment:
                    if line.endswith(ResourceConstants.EXT_CMT_END):
                        inExtendedComment = False
                else:
                    if line.startswith(ResourceConstants.EXT_CMT_START):
                        inExtendedComment = True
                    else:
                        cmtI: int = line.index(ResourceConstants.CMT)
                        if cmtI >= 0:
                            line = line.substring(0, cmtI)
                        line = line.trim()
                        if line.isEmpty():
                            continue  # empty lines can be safely skipped
                        parts: typing.List[str] = line.split("\\s+")
                        if len(parts) != 3:
                            raise ValueError(
                                "Malformed line '"
                                + rawLine
                                + "' in language resource '"
                                + languageRulesResourceName
                                + "'"
                            )
                        pattern: re.Pattern = re.compile(parts[0])
                        langs: typing.List[str] = parts[1].split("\\+")
                        accept: bool = parts[2].equals("true")
                        rules.append(LangRule(pattern, set(langs), accept))
        return Lang(rules, languages)

    @staticmethod
    def instance(nameType: NameType) -> Lang:
        return Lang.__Langs.get(nameType)

    def __init__(self, rules: typing.List[LangRule], languages: Languages) -> None:
        self.__rules = rules
        self.__languages = languages


Lang.run_static_init()
