from __future__ import annotations
import re
import os
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.Resources import *
from src.main.org.apache.commons.codec.language.bm.Languages import *
from src.main.org.apache.commons.codec.language.bm.NameType import *
from src.main.org.apache.commons.codec.language.bm.ResourceConstants import *
from src.main.org.apache.commons.codec.language.bm.RuleType import *


class PhonemeExpr(ABC):

    def getPhonemes(self) -> typing.Iterable[Phoneme]:
        return self.phonemes


class RPattern(ABC):

    def isMatch(self, input: str) -> bool:
        return self.regex().matcher(input).matches()


class Phoneme(PhonemeExpr):

    COMPARATOR: typing.Callable[[Phoneme, Phoneme], int] = lambda o1, o2: 0
    __languages: LanguageSet = None

    __phonemeText: str = ""

    def toString(self) -> str:
        return self.__phonemeText + "[" + self.__languages + "]"

    def join(self, right: Phoneme) -> Phoneme:
        return Phoneme(
            2,
            self.phonemeText + right.phonemeText,
            self.languages.restrictTo(right.languages),
            None,
        )

    def getPhonemes(self) -> typing.Iterable[Phoneme]:
        return [self]

    def mergeWithLanguage(self, lang: LanguageSet) -> Phoneme:
        return Phoneme(2, self.__phonemeText, self.__languages.merge(lang), None)

    def getPhonemeText(self) -> str:
        return self.__phonemeText

    def getLanguages(self) -> LanguageSet:
        return self.__languages

    def append(self, str: str) -> Phoneme:
        self.__phonemeText += str
        return self

    @staticmethod
    def Phoneme1(
        phonemeLeft: Phoneme, phonemeRight: Phoneme, languages: LanguageSet
    ) -> Phoneme:
        return Phoneme(1, phonemeLeft.phonemeText, languages, phonemeRight)

    @staticmethod
    def Phoneme0(phonemeLeft: Phoneme, phonemeRight: Phoneme) -> Phoneme:
        return Phoneme(0, phonemeLeft.phonemeText, phonemeLeft.languages, phonemeRight)

    def __init__(
        self,
        constructorId: int,
        phonemeText: str,
        languages: LanguageSet,
        phonemeRight: Phoneme,
    ) -> None:

        pass  # LLM could not translate this method


class PhonemeList(PhonemeExpr):

    __phonemes: typing.List[Phoneme] = None

    def getPhonemes(self) -> typing.List[Phoneme]:
        return self.__phonemes

    def __init__(self, phonemes: typing.List[Phoneme]) -> None:
        self.__phonemes = phonemes


class Rule:

    ALL: str = "ALL"
    ALL_STRINGS_RMATCHER: RPattern = None
    __rContext: RPattern = None

    __phoneme: PhonemeExpr = None

    __pattern: str = ""

    __lContext: RPattern = None

    __RULES: typing.Dict[
        NameType,
        typing.Dict[RuleType, typing.Dict[str, typing.Dict[str, typing.List[Rule]]]],
    ] = {}

    __HASH_INCLUDE_LENGTH: int = 0
    __HASH_INCLUDE: str = "#include"
    __DOUBLE_QUOTE: str = '"'

    @staticmethod
    def initialize_fields() -> None:
        Rule.ALL_STRINGS_RMATCHER: RPattern = RPattern()

    @staticmethod
    def run_static_init():
        for s in NameType:
            rts = {}
            for rt in RuleType:
                rs = {}
                ls = Languages.getInstance0(s)
                for l in ls.getLanguages():
                    try:
                        scanner = Rule.__createScanner0(s, rt, l)
                        rs[l] = Rule.__parseRules(
                            scanner, Rule.__createResourceName(s, rt, l)
                        )
                    except RuntimeError as e:
                        raise RuntimeError(
                            "Problem processing " + Rule.__createResourceName(s, rt, l),
                            e,
                        )
                if rt != RuleType.RULES:
                    try:
                        scanner = Rule.__createScanner0(s, rt, "common")
                        rs["common"] = Rule.__parseRules(
                            scanner, Rule.__createResourceName(s, rt, "common")
                        )
                    except RuntimeError as e:
                        raise RuntimeError(
                            "Problem processing "
                            + Rule.__createResourceName(s, rt, "common"),
                            e,
                        )
                rts[rt] = rs
            Rule.__RULES[s] = rts

    def patternAndContextMatches(self, input: str, i: int) -> bool:
        if i < 0:
            raise IndexError("Can not match pattern at negative indexes")

        patternLength = len(self.__pattern)
        ipl = i + patternLength

        if ipl > len(input):
            return False

        if input[i:ipl] != self.__pattern:
            return False
        if not self.__rContext.isMatch(input[ipl:]):
            return False
        return self.__lContext.isMatch(input[:i])

    def getRContext(self) -> RPattern:
        return self.__rContext

    def getPhoneme(self) -> PhonemeExpr:
        return self.__phoneme

    def getPattern(self) -> str:
        return self.__pattern

    def getLContext(self) -> RPattern:
        return self.__lContext

    def __init__(
        self, pattern: str, lContext: str, rContext: str, phoneme: PhonemeExpr
    ) -> None:
        self.__pattern = pattern
        self.__lContext = self.__pattern(lContext + "$")
        self.__rContext = self.__pattern("^" + rContext)
        self.__phoneme = phoneme

    @staticmethod
    def getInstanceMap1(
        nameType: NameType, rt: RuleType, lang: str
    ) -> typing.Dict[str, typing.List[Rule]]:
        rules: typing.Dict[str, typing.List[Rule]] = (
            Rule.__RULES.get(nameType).get(rt).get(lang)
        )

        if rules is None:
            raise ValueError(
                String.format(
                    "No rules found for %s, %s, %s.",
                    nameType.getName(),
                    rt.getName(),
                    lang,
                )
            )

        return rules

    @staticmethod
    def getInstanceMap0(
        nameType: NameType, rt: RuleType, langs: LanguageSet
    ) -> typing.Dict[str, typing.List[Rule]]:
        return (
            Rule.getInstanceMap1(nameType, rt, langs.getAny())
            if langs.isSingleton()
            else Rule.getInstanceMap1(nameType, rt, Languages.ANY)
        )

    @staticmethod
    def getInstance1(nameType: NameType, rt: RuleType, lang: str) -> typing.List[Rule]:
        return Rule.getInstance0(nameType, rt, LanguageSet.from_(set([lang])))

    @staticmethod
    def getInstance0(
        nameType: NameType, rt: RuleType, langs: LanguageSet
    ) -> typing.List[Rule]:
        ruleMap: typing.Dict[str, typing.List[Rule]] = Rule.getInstanceMap0(
            nameType, rt, langs
        )
        allRules: typing.List[Rule] = []
        for rules in ruleMap.values():
            allRules.extend(rules)
        return allRules

    @staticmethod
    def __stripQuotes(str: str) -> str:
        if str.startswith(Rule.__DOUBLE_QUOTE):
            str = str[1:]

        if str.endswith(Rule.__DOUBLE_QUOTE):
            str = str[:-1]

        return str

    @staticmethod
    def __startsWith(input: str, prefix: str) -> bool:
        if len(prefix) > len(input):
            return False
        for i in range(len(prefix)):
            if input[i] != prefix[i]:
                return False
        return True

    @staticmethod
    def __pattern(regex: str) -> RPattern:

        pass  # LLM could not translate this method

    @staticmethod
    def __parseRules(
        scanner: typing.Any, location: str
    ) -> typing.Dict[str, typing.List[Rule]]:
        lines: typing.Dict[str, typing.List[Rule]] = {}
        currentLine: int = 0

        inMultilineComment: bool = False
        while scanner.hasNextLine():
            currentLine += 1
            rawLine: str = scanner.nextLine()
            line: str = rawLine

            if inMultilineComment:
                if line.endswith(ResourceConstants.EXT_CMT_END):
                    inMultilineComment = False
            elif line.startswith(ResourceConstants.EXT_CMT_START):
                inMultilineComment = True
            else:
                cmtI: int = line.indexOf(ResourceConstants.CMT)
                if cmtI >= 0:
                    line = line.substring(0, cmtI)

                line = line.trim()

                if line.isEmpty():
                    continue  # empty lines can be safely skipped

                if line.startsWith(HASH_INCLUDE):
                    incl: str = line.substring(HASH_INCLUDE_LENGTH).trim()
                    if incl.contains(" "):
                        raise ValueError(
                            "Malformed import statement '"
                            + rawLine
                            + "' in "
                            + location
                        )
                    try:
                        hashIncludeScanner: typing.Any = Rule.__createScanner1(incl)
                        lines.putAll(
                            Rule.__parseRules(
                                hashIncludeScanner, location + "->" + incl
                            )
                        )
                    finally:
                        hashIncludeScanner.close()
                else:
                    parts: typing.List[str] = line.split("\\s+")
                    if len(parts) != 4:
                        raise ValueError(
                            "Malformed rule statement split into "
                            + str(len(parts))
                            + " parts: "
                            + rawLine
                            + " in "
                            + location
                        )
                    try:
                        pat: str = Rule.__stripQuotes(parts[0])
                        lCon: str = Rule.__stripQuotes(parts[1])
                        rCon: str = Rule.__stripQuotes(parts[2])
                        ph: PhonemeExpr = Rule.__parsePhonemeExpr(stripQuotes(parts[3]))
                        cLine: int = currentLine
                        r: Rule1 = Rule1(pat, lCon, rCon, ph, cLine, location)
                        patternKey: str = r.pattern.substring(0, 1)
                        rules: typing.List[Rule] = lines.get(patternKey)
                        if rules is None:
                            rules = []
                            lines.put(patternKey, rules)
                        rules.add(r)
                    except ValueError as e:
                        raise RuntimeError(
                            "Problem parsing line '"
                            + str(currentLine)
                            + "' in "
                            + location,
                            e,
                        )
        return lines

    @staticmethod
    def __parsePhonemeExpr(ph: str) -> PhonemeExpr:

        pass  # LLM could not translate this method

    @staticmethod
    def __parsePhoneme(ph: str) -> Phoneme:
        open = ph.find("[")
        if open >= 0:
            if not ph.endswith("]"):
                raise ValueError(
                    "Phoneme expression contains a '[' but does not end in ']'"
                )
            before = ph[0:open]
            in_ = ph[open + 1 : ph.length() - 1]
            langs = set(in_.split("+"))
            return Phoneme(2, before, LanguageSet.from_(langs), None)
        return Phoneme(2, ph, Languages.ANY_LANGUAGE, None)

    @staticmethod
    def __endsWith(input: str, suffix: str) -> bool:
        suffixLength = len(suffix)
        inputLength = len(input)

        if suffixLength > inputLength:
            return False
        for i, j in zip(
            range(inputLength - 1, -1, -1), range(suffixLength - 1, -1, -1)
        ):
            if input[i] != suffix[j]:
                return False
        return True

    @staticmethod
    def __createScanner1(lang: str) -> typing.Any:
        resName = f"org/apache/commons/codec/language/bm/{lang}.txt"
        return Scanner(Resources.getInputStream(resName), ResourceConstants.ENCODING)

    @staticmethod
    def __createScanner0(nameType: NameType, rt: RuleType, lang: str) -> typing.Any:
        resName = Rule.__createResourceName(nameType, rt, lang)
        return Scanner(Resources.getInputStream(resName), ResourceConstants.ENCODING)

    @staticmethod
    def __createResourceName(nameType: NameType, rt: RuleType, lang: str) -> str:
        return f"org/apache/commons/codec/language/bm/{nameType.getName()}_{rt.getName()}_{lang}.txt"

    @staticmethod
    def __contains(chars: str, input: str) -> bool:

        pass  # LLM could not translate this method


Rule.initialize_fields()

Rule.run_static_init()
