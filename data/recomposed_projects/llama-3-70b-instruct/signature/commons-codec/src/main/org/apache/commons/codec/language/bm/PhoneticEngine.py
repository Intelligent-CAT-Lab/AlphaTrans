from __future__ import annotations
import re
import os
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.language.bm.Lang import *
from src.main.org.apache.commons.codec.language.bm.Languages import *
from src.main.org.apache.commons.codec.language.bm.NameType import *
from src.main.org.apache.commons.codec.language.bm.Rule import *
from src.main.org.apache.commons.codec.language.bm.RuleType import *


class PhonemeBuilder:

    __phonemes: typing.Set[Phoneme] = None

    def makeString(self) -> str:
        sb = StringBuilder()

        for ph in self.phonemes:
            if len(sb) > 0:
                sb.append("|")
            sb.append(ph.getPhonemeText())

        return sb.toString()

    def getPhonemes(self) -> typing.Set[Phoneme]:
        return self.__phonemes

    def apply(self, phonemeExpr: PhonemeExpr, maxPhonemes: int) -> None:
        newPhonemes: typing.Set[Phoneme] = set()
        for left in self.__phonemes:
            for right in phonemeExpr.getPhonemes():
                languages: LanguageSet = left.getLanguages().restrictTo(
                    right.getLanguages()
                )
                if not languages.isEmpty():
                    join: Phoneme = Phoneme.Phoneme1(left, right, languages)
                    if len(newPhonemes) < maxPhonemes:
                        newPhonemes.add(join)
                        if len(newPhonemes) >= maxPhonemes:
                            break
        self.__phonemes.clear()
        self.__phonemes.update(newPhonemes)

    def append(self, str: str) -> None:
        for ph in self.__phonemes:
            ph.append(str)

    def __init__(
        self, constructorId: int, phonemes: typing.Set[Phoneme], phoneme: Phoneme
    ) -> None:
        if constructorId == 0:
            self.__phonemes = phonemes
        else:
            self.__phonemes = set()
            self.__phonemes.add(phoneme)

    @staticmethod
    def empty(languages: LanguageSet) -> PhonemeBuilder:
        return PhonemeBuilder(3, None, Phoneme(2, "", languages, None))


class RulesApplication:

    __found: bool = False

    __maxPhonemes: int = 0

    __i: int = 0

    __phonemeBuilder: PhonemeBuilder = None

    __input: str = ""

    __finalRules: typing.Dict[str, typing.List[Rule]] = None

    def isFound(self) -> bool:
        return self.__found

    def invoke(self) -> RulesApplication:
        self.__found = False
        patternLength = 1
        rules = self.__finalRules.get(self.__input[self.__i : self.__i + patternLength])
        if rules is not None:
            for rule in rules:
                pattern = rule.getPattern()
                patternLength = len(pattern)
                if rule.patternAndContextMatches(self.__input, self.__i):
                    self.__phonemeBuilder.apply(rule.getPhoneme(), self.__maxPhonemes)
                    self.__found = True
                    break
        if not self.__found:
            patternLength = 1
        self.__i += patternLength
        return self

    def getPhonemeBuilder(self) -> PhonemeBuilder:
        return self.__phonemeBuilder

    def getI(self) -> int:
        return self.__i

    def __init__(
        self,
        finalRules: typing.Dict[str, typing.List[Rule]],
        input: str,
        phonemeBuilder: PhonemeBuilder,
        i: int,
        maxPhonemes: int,
    ) -> None:

        pass  # LLM could not translate this method


class PhoneticEngine:

    __maxPhonemes: int = 0

    __concat: bool = False

    __ruleType: RuleType = None

    __nameType: NameType = None

    __lang: Lang = None

    __DEFAULT_MAX_PHONEMES: int = 20
    __NAME_PREFIXES: typing.Dict[NameType, typing.Set[str]] = {}

    @staticmethod
    def run_static_init():
        PhoneticEngine.__NAME_PREFIXES[NameType.ASHKENAZI] = frozenset(
            {"bar", "ben", "da", "de", "van", "von"}
        )
        PhoneticEngine.__NAME_PREFIXES[NameType.SEPHARDIC] = frozenset(
            {
                "al",
                "el",
                "da",
                "dal",
                "de",
                "del",
                "dela",
                "de la",
                "della",
                "des",
                "di",
                "do",
                "dos",
                "du",
                "van",
                "von",
            }
        )
        PhoneticEngine.__NAME_PREFIXES[NameType.GENERIC] = frozenset(
            {
                "da",
                "dal",
                "de",
                "del",
                "dela",
                "de la",
                "della",
                "des",
                "di",
                "do",
                "dos",
                "du",
                "van",
                "von",
            }
        )

    def getMaxPhonemes(self) -> int:
        return self.__maxPhonemes

    def isConcat(self) -> bool:
        return self.__concat

    def getRuleType(self) -> RuleType:
        return self.__ruleType

    def getNameType(self) -> NameType:
        return self.__nameType

    def getLang(self) -> Lang:
        return self.__lang

    def encode1(self, input: str, languageSet: LanguageSet) -> str:
        rules = Rule.getInstanceMap0(self.nameType, RuleType.RULES, languageSet)
        finalRules1 = Rule.getInstanceMap1(self.nameType, self.ruleType, "common")
        finalRules2 = Rule.getInstanceMap0(self.nameType, self.ruleType, languageSet)

        input = input.lower().replace("-", " ").strip()

        if self.nameType == NameType.GENERIC:
            if len(input) >= 2 and input[0:2] == "d'":  # check for d'
                remainder = input[2:]
                combined = "d" + remainder
                return (
                    "(" + self.encode0(remainder) + ")-(" + self.encode0(combined) + ")"
                )
            for l in PhoneticEngine.NAME_PREFIXES[self.nameType]:
                if input.startswith(l + " "):
                    remainder = input[len(l) + 1 :]  # input without the prefix
                    combined = l + remainder  # input with prefix without space
                    return (
                        "("
                        + self.encode0(remainder)
                        + ")-("
                        + self.encode0(combined)
                        + ")"
                    )

        words = input.split("\\s+")
        words2 = []

        if self.nameType == NameType.SEPHARDIC:
            for aWord in words:
                parts = aWord.split("'")
                lastPart = parts[len(parts) - 1]
                words2.append(lastPart)
            words2 = [
                x
                for x in words2
                if x not in PhoneticEngine.NAME_PREFIXES[self.nameType]
            ]
        elif self.nameType == NameType.ASHKENAZI:
            words2 = words
            words2 = [
                x
                for x in words2
                if x not in PhoneticEngine.NAME_PREFIXES[self.nameType]
            ]
        elif self.nameType == NameType.GENERIC:
            words2 = words
        else:
            raise Exception("Unreachable case: " + self.nameType)

        if self.concat:
            input = self.__join(words2, " ")
        elif len(words2) == 1:
            input = words[0]
        else:
            result = ""
            for word in words2:
                result += "-" + self.encode0(word)
            return result[1:]

        phonemeBuilder = PhonemeBuilder.empty(languageSet)

        i = 0
        while i < len(input):
            rulesApplication = RulesApplication(
                finalRules, input, phonemeBuilder, i, self.maxPhonemes
            ).invoke()
            i = rulesApplication.getI()
            phonemeBuilder = rulesApplication.getPhonemeBuilder()

        phonemeBuilder = self.__applyFinalRules(phonemeBuilder, finalRules1)
        phonemeBuilder = self.__applyFinalRules(phonemeBuilder, finalRules2)

        return phonemeBuilder.makeString()

    def encode0(self, input: str) -> str:
        languageSet: LanguageSet = self.lang.guessLanguages(input)
        return self.encode1(input, languageSet)

    def __init__(
        self, nameType: NameType, ruleType: RuleType, concat: bool, maxPhonemes: int
    ) -> None:
        if ruleType == RuleType.RULES:
            raise ValueError("ruleType must not be " + RuleType.RULES)
        self.__nameType = nameType
        self.__ruleType = ruleType
        self.__concat = concat
        self.__lang = Lang.instance(nameType)
        self.__maxPhonemes = maxPhonemes

    @staticmethod
    def PhoneticEngine0(
        nameType: NameType, ruleType: RuleType, concat: bool
    ) -> PhoneticEngine:
        return PhoneticEngine(nameType, ruleType, concat, DEFAULT_MAX_PHONEMES)

    def __applyFinalRules(
        self,
        phonemeBuilder: PhonemeBuilder,
        finalRules: typing.Dict[str, typing.List[Rule]],
    ) -> PhonemeBuilder:
        if finalRules is None:
            raise TypeError("finalRules")
        if not finalRules:
            return phonemeBuilder
        phonemes: typing.Dict[Phoneme, Phoneme] = {}
        for phoneme in phonemeBuilder.getPhonemes():
            subBuilder = PhonemeBuilder.empty(phoneme.getLanguages())
            phonemeText = phoneme.getPhonemeText()
            i = 0
            while i < len(phonemeText):
                rulesApplication = RulesApplication(
                    finalRules, phonemeText, subBuilder, i, self.__maxPhonemes
                ).invoke()
                found = rulesApplication.isFound()
                subBuilder = rulesApplication.getPhonemeBuilder()
                if not found:
                    subBuilder.append(phonemeText[i])
                i = rulesApplication.getI()
            for newPhoneme in subBuilder.getPhonemes():
                if newPhoneme in phonemes:
                    oldPhoneme = phonemes[newPhoneme]
                    mergedPhoneme = oldPhoneme.mergeWithLanguage(
                        newPhoneme.getLanguages()
                    )
                    phonemes[mergedPhoneme] = mergedPhoneme
                else:
                    phonemes[newPhoneme] = newPhoneme
        return PhonemeBuilder(0, phonemes.keys(), None)

    @staticmethod
    def __join(strings: typing.Iterable[str], sep: str) -> str:
        sb = ""
        for s in strings:
            sb += s
            sb += sep
        return sb


PhoneticEngine.run_static_init()
