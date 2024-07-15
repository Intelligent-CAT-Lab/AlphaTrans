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
        pass


class RPattern(ABC):

    def isMatch(self, input: str) -> bool:
        pass


class Phoneme(PhonemeExpr):

    __languages: LanguageSet = None

    __phonemeText: str = ""

    COMPARATOR: typing.Callable[[Phoneme, Phoneme], int] = None

    @staticmethod
    def initialize_fields() -> None:
        Phoneme.COMPARATOR: typing.Callable[[Phoneme, Phoneme], int] = lambda o1, o2: (
            (
                lambda o1Length=len(o1.__phonemeText), o2Length=len(o2.__phonemeText): (
                    next(
                        (
                            (
                                o1.__phonemeText[i] - o2.__phonemeText[i]
                                if i < o2Length
                                else (+1 if i >= o2Length else -1)
                            )
                            for i in range(o1Length)
                        ),
                        -1 if o1Length < o2Length else 0,
                    )
                )
            )()
        )

    def toString(self) -> str:
        return self.__phonemeText + "[" + str(self.__languages) + "]"

    def join(self, right: Phoneme) -> Phoneme:
        return Phoneme(
            2,
            self.__phonemeText + right.__phonemeText,
            self.__languages.restrictTo(right.__languages),
            None,
        )

    def getPhonemes(self) -> typing.Iterable[Phoneme]:
        return [self]

    def mergeWithLanguage(self, lang: LanguageSet) -> Phoneme:
        return Phoneme(2, str(self.__phonemeText), self.__languages.merge(lang), None)

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
        return Phoneme(1, phonemeLeft._Phoneme__phonemeText, languages, phonemeRight)

    @staticmethod
    def Phoneme0(phonemeLeft: Phoneme, phonemeRight: Phoneme) -> Phoneme:
        return Phoneme(
            0,
            phonemeLeft._Phoneme__phonemeText,
            phonemeLeft._Phoneme__languages,
            phonemeRight,
        )

    def __init__(
        self,
        constructorId: int,
        phonemeText: str,
        languages: LanguageSet,
        phonemeRight: Phoneme,
    ) -> None:

        if constructorId == 0 or constructorId == 1:
            self.__languages = languages
            self.__phonemeText = StringBuilder(phonemeText)
            self.__phonemeText.append(phonemeRight.phonemeText)
        else:
            self.__phonemeText = StringBuilder(phonemeText)
            self.__languages = languages


class PhonemeList(PhonemeExpr):

    __phonemes: typing.List[Phoneme] = None

    def getPhonemes(self) -> typing.List[Phoneme]:
        return self.__phonemes

    def __init__(self, phonemes: typing.List[Phoneme]) -> None:
        self.__phonemes = phonemes


class Rule:

    ALL: str = "ALL"
    ALL_STRINGS_RMATCHER: RPattern = None  # LLM could not translate this field

    __rContext: RPattern = None

    __phoneme: PhonemeExpr = None

    __pattern: str = ""

    __lContext: RPattern = None

    __RULES: typing.Dict[
        NameType,
        typing.Dict[RuleType, typing.Dict[str, typing.Dict[str, typing.List[Rule]]]],
    ] = {}

    __HASH_INCLUDE: str = "#include"
    __DOUBLE_QUOTE: str = '"'

    @staticmethod
    def run_static_init():

        for s in NameType:
            rts = {rt: {} for rt in RuleType}

            ls = Languages.getInstance0(s)
            for l in ls.getLanguages():
                try:
                    scanner = Rule.__createScanner0(s, rt, l)
                    for rt in RuleType:
                        rs = Rule.__parseRules(
                            scanner, Rule.__createResourceName(s, rt, l)
                        )
                        rts[rt][l] = rs
                except RuntimeError as e:
                    raise RuntimeError(
                        f"Problem processing {Rule.__createResourceName(s, rt, l)}", e
                    )
                finally:
                    scanner.close()

                if not rt.equals(RuleType.RULES):
                    try:
                        scanner = Rule.__createScanner0(s, rt, "common")
                        rs = Rule.__parseRules(
                            scanner, Rule.__createResourceName(s, rt, "common")
                        )
                        rts[rt]["common"] = rs
                    except RuntimeError as e:
                        raise RuntimeError(
                            f"Problem processing {Rule.__createResourceName(s, rt, 'common')}",
                            e,
                        )
                    finally:
                        scanner.close()

            Rule.__RULES[s] = {
                k: {
                    inner_k: Collections.unmodifiableMap(inner_v)
                    for inner_k, inner_v in v.items()
                }
                for k, v in rts.items()
            }

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

        rules = Rule.__RULES.get(nameType).get(rt).get(lang)

        if rules is None:
            raise ValueError(
                f"No rules found for {nameType.getName()}, {rt.getName()}, {lang}."
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

        langs = LanguageSet.from_(set([lang]))
        return Rule.getInstance0(nameType, rt, langs)

    @staticmethod
    def getInstance0(
        nameType: NameType, rt: RuleType, langs: LanguageSet
    ) -> typing.List[Rule]:

        ruleMap = Rule.getInstanceMap0(nameType, rt, langs)
        allRules = []
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

        starts_with = regex.startswith("^")
        ends_with = regex.endswith("$")
        content = regex[1:-1] if starts_with and ends_with else regex
        boxes = "[" in content

        if not boxes:
            if starts_with and ends_with:
                if not content:
                    return RPattern(lambda input: len(input) == 0)
                return RPattern(lambda input: input == content)
            if (starts_with or ends_with) and not content:
                return Rule.ALL_STRINGS_RMATCHER
            if starts_with:
                return RPattern(lambda input: input.startswith(content))
            if ends_with:
                return RPattern(lambda input: input.endswith(content))
        else:
            starts_with_box = content.startswith("[")
            ends_with_box = content.endswith("]")

            if starts_with_box and ends_with_box:
                box_content = content[1:-1]
                if "[" not in box_content:
                    negate = box_content.startswith("^")
                    box_content = box_content[1:] if negate else box_content
                    should_match = not negate

                    if starts_with and ends_with:
                        return RPattern(
                            lambda input: len(input) == 1
                            and (input[0] in box_content) == should_match
                        )
                    if starts_with:
                        return RPattern(
                            lambda input: len(input) > 0
                            and (input[0] in box_content) == should_match
                        )
                    if ends_with:
                        return RPattern(
                            lambda input: len(input) > 0
                            and (input[-1] in box_content) == should_match
                        )

        return RPattern(lambda input: re.search(regex, input) is not None)

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
                cmtI: int = line.find(ResourceConstants.CMT)
                if cmtI >= 0:
                    line = line[:cmtI]

                line = line.strip()

                if not line:
                    continue

                if line.startswith(Rule.__HASH_INCLUDE):
                    incl: str = line[Rule.__HASH_INCLUDE_LENGTH :].strip()
                    if " " in incl:
                        raise ValueError(
                            f"Malformed import statement '{rawLine}' in {location}"
                        )
                    try:
                        hashIncludeScanner: typing.Any = Rule.__createScanner1(incl)
                        lines.update(
                            Rule.__parseRules(hashIncludeScanner, f"{location}->{incl}")
                        )
                    finally:
                        hashIncludeScanner.close()
                else:
                    parts: typing.List[str] = line.split()
                    if len(parts) != 4:
                        raise ValueError(
                            f"Malformed rule statement split into {len(parts)} parts: {rawLine} in {location}"
                        )
                    try:
                        pat: str = Rule.__stripQuotes(parts[0])
                        lCon: str = Rule.__stripQuotes(parts[1])
                        rCon: str = Rule.__stripQuotes(parts[2])
                        ph: PhonemeExpr = Rule.__parsePhonemeExpr(
                            Rule.__stripQuotes(parts[3])
                        )
                        r: Rule1 = Rule1(pat, lCon, rCon, ph, currentLine, location)
                        patternKey: str = r.pattern[0]
                        rules: typing.List[Rule] = lines.get(patternKey, [])
                        rules.append(r)
                        lines[patternKey] = rules
                    except ValueError as e:
                        raise RuntimeError(
                            f"Problem parsing line '{currentLine}' in {location}", e
                        )

        return lines

    @staticmethod
    def __parsePhonemeExpr(ph: str) -> PhonemeExpr:

        if ph.startswith("("):  # we have a bracketed list of options
            if not ph.endswith(")"):
                raise ValueError("Phoneme starts with '(' so must end with ')'")

            phs = []
            body = ph[1:-1]
            for part in body.split("|"):
                phs.append(Rule.__parsePhoneme(part))
            if body.startswith("|") or body.endswith("|"):
                phs.append(Phoneme(2, "", ANY_LANGUAGE, None))

            return PhonemeList(phs)
        return Rule.__parsePhoneme(ph)

    @staticmethod
    def __parsePhoneme(ph: str) -> Phoneme:

        open_ = ph.find("[")
        if open_ >= 0:
            if not ph.endswith("]"):
                raise ValueError(
                    "Phoneme expression contains a '[' but does not end in ']'"
                )
            before = ph[:open_]
            in_ = ph[open_ + 1 : -1]
            langs = set(in_.split("+"))

            return Phoneme(2, before, LanguageSet.from_(langs), None)
        return Phoneme(2, ph, ANY_LANGUAGE, None)

    @staticmethod
    def __endsWith(input: str, suffix: str) -> bool:

        suffix_length = len(suffix)
        input_length = len(input)

        if suffix_length > input_length:
            return False
        for i, j in zip(
            range(input_length - 1, input_length - suffix_length - 1, -1),
            range(suffix_length - 1, -1, -1),
        ):
            if input[i] != suffix[j]:
                return False
        return True

    @staticmethod
    def __createScanner1(lang: str) -> typing.Any:

        resName = "org/apache/commons/codec/language/bm/{}.txt".format(lang)
        return Resources.getInputStream(resName)

    @staticmethod
    def __createScanner0(nameType: NameType, rt: RuleType, lang: str) -> typing.Any:

        resName = Rule.__createResourceName(nameType, rt, lang)
        return Scanner(Resources.getInputStream(resName), ResourceConstants.ENCODING)

    @staticmethod
    def __createResourceName(nameType: NameType, rt: RuleType, lang: str) -> str:
        return "org/apache/commons/codec/language/bm/{}_{}_{}.txt".format(
            nameType.getName(), rt.getName(), lang
        )

    @staticmethod
    def __contains(chars: str, input: str) -> bool:
        for i in range(len(chars)):
            if chars[i] == input:
                return True
        return False


Phoneme.initialize_fields()

Rule.run_static_init()
