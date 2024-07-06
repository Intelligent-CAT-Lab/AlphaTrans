from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.Resources import *
from src.main.org.apache.commons.codec.language.bm.Languages import *
from src.main.org.apache.commons.codec.language.bm.NameType import *
from src.main.org.apache.commons.codec.language.bm.ResourceConstants import *
from src.main.org.apache.commons.codec.language.bm.Rule1 import *
from src.main.org.apache.commons.codec.language.bm.RuleType import *
from src.main.org.apache.commons.codec.CharEncoding import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *


class Branch:

    __lastReplacement: str = ""

    __cachedString: str = ""

    __builder: str = ""

    def toString(self) -> str:
        if self.__cachedString == "":
            self.__cachedString = self.__builder
        return self.__cachedString

    def hashCode(self) -> int:
        return self.toString().hashCode()

    def equals(self, other: typing.Any) -> bool:
        if self == other:
            return True
        if not isinstance(other, Branch):
            return False
        return self.toString() == other.toString()

    def processNextReplacement(self, replacement: str, forceAppend: bool) -> None:
        append = (
            self.__lastReplacement is None
            or not self.__lastReplacement.endswith(replacement)
            or forceAppend
        )
        if append and len(self.__builder) < MAX_LENGTH:
            self.__builder.append(replacement)
            if len(self.__builder) > MAX_LENGTH:
                self.__builder.delete(MAX_LENGTH, len(self.__builder))
            self.__cachedString = None
        self.__lastReplacement = replacement

    def finish(self) -> None:
        while len(self.__builder) < MAX_LENGTH:
            self.__builder += "0"
            self.__cachedString = None

    def createBranch(self) -> Branch:
        branch = Branch()
        branch.__builder.append(self.toString())
        branch.__lastReplacement = self.__lastReplacement
        return branch

    def __init__(self) -> None:
        self.__builder = StringBuilder()
        self.__lastReplacement = ""
        self.__cachedString = ""


class Rule:

    __replacementDefault: typing.List[str] = None

    __replacementBeforeVowel: typing.List[str] = None

    __replacementAtStart: typing.List[str] = None

    __pattern: str = ""

    def toString(self) -> str:
        return f"{self.__pattern}=({self.__replacementAtStart},{self.__replacementBeforeVowel},{self.__replacementDefault})"

    def matches(self, context: str) -> bool:
        return context.startswith(self.__pattern)

    def getReplacements(self, context: str, atStart: bool) -> typing.List[str]:
        if atStart:
            return self.__replacementAtStart

        nextIndex = self.getPatternLength()
        nextCharIsVowel = nextIndex < len(context) and self.__isVowel(
            context[nextIndex]
        )
        if nextCharIsVowel:
            return self.__replacementBeforeVowel

        return self.__replacementDefault

    def getPatternLength(self) -> int:
        return len(self.__pattern)

    def __init__(
        self,
        pattern: str,
        replacementAtStart: str,
        replacementBeforeVowel: str,
        replacementDefault: str,
    ) -> None:
        self.__pattern = pattern
        self.__replacementAtStart = replacementAtStart.split("|")
        self.__replacementBeforeVowel = replacementBeforeVowel.split("|")
        self.__replacementDefault = replacementDefault.split("|")

    def __isVowel(self, ch: str) -> bool:
        return ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u"


class DaitchMokotoffSoundex(StringEncoder):

    __folding: bool = False

    __FOLDINGS: typing.Dict[str, str] = {}

    __RULES: typing.Dict[str, typing.List[Rule]] = {}
    __MAX_LENGTH: int = 6
    __RESOURCE_FILE: str = "org/apache/commons/codec/language/dmrules.txt"
    __MULTILINE_COMMENT_START: str = "/*"
    __MULTILINE_COMMENT_END: str = "*/"
    __DOUBLE_QUOTE: str = '"'
    __COMMENT: str = "//"

    @staticmethod
    def initialize_fields() -> None:
        DaitchMokotoffSoundex.__RULES: typing.Dict[str, typing.List[Rule]] = {}

    def soundex0(self, source: str) -> str:
        branches = self.__soundex1(source, True)
        sb = StringBuilder()
        index = 0
        for branch in branches:
            sb.append(branch)
            if index + 1 < len(branches):
                sb.append("|")
            index += 1
        return sb.toString()

    def encode1(self, source: str) -> str:
        if source is None:
            return None

        input = self.__cleanup(source)

        currentBranches = set()
        currentBranches.add(Branch())

        lastChar = "\0"
        for index in range(len(input)):
            ch = input[index]

            if Character.isWhitespace(ch):
                continue

            inputContext = input[index:]
            rules = self.__RULES.get(ch)
            if rules is None:
                continue

            nextBranches = [] if branching else []

            for rule in rules:
                if rule.matches(inputContext):
                    if branching:
                        nextBranches.clear()

                    replacements = rule.getReplacements(inputContext, lastChar == "\0")
                    branchingRequired = len(replacements) > 1 and branching

                    for branch in currentBranches:
                        for nextReplacement in replacements:
                            nextBranch = (
                                branch.createBranch() if branchingRequired else branch
                            )

                            force = (lastChar == "m" and ch == "n") or (
                                lastChar == "n" and ch == "m"
                            )

                            nextBranch.processNextReplacement(nextReplacement, force)

                            if not branching:
                                break

                            nextBranches.append(nextBranch)

                    if branching:
                        currentBranches.clear()
                        currentBranches.update(nextBranches)

                    index += rule.getPatternLength() - 1
                    break

            lastChar = ch

        result = [None] * len(currentBranches)
        index = 0
        for branch in currentBranches:
            branch.finish()
            result[index] = branch.toString()
            index += 1

        return result[0]

    def encode0(self, obj: typing.Any) -> typing.Any:
        if not isinstance(obj, str):
            raise EncoderException(
                "Parameter supplied to DaitchMokotoffSoundex encode is not of type"
                " java.lang.String",
                None,
            )
        return self.encode1(obj)

    @staticmethod
    def DaitchMokotoffSoundex1() -> DaitchMokotoffSoundex:
        return DaitchMokotoffSoundex(True)

    def __init__(self, folding: bool) -> None:
        self.__folding = folding

    def __soundex1(self, source: str, branching: bool) -> typing.List[str]:
        if source is None:
            return None

        input = self.__cleanup(source)

        currentBranches = set()
        currentBranches.add(Branch())

        lastChar = "\0"
        for index in range(len(input)):
            ch = input[index]

            if Character.isWhitespace(ch):
                continue

            inputContext = input[index:]
            rules = self.__RULES.get(ch)
            if rules is None:
                continue

            nextBranches = [] if branching else []

            for rule in rules:
                if rule.matches(inputContext):
                    if branching:
                        nextBranches.clear()

                    replacements = rule.getReplacements(inputContext, lastChar == "\0")
                    branchingRequired = len(replacements) > 1 and branching

                    for branch in currentBranches:
                        for nextReplacement in replacements:
                            nextBranch = (
                                branch.createBranch() if branchingRequired else branch
                            )

                            force = (lastChar == "m" and ch == "n") or (
                                lastChar == "n" and ch == "m"
                            )

                            nextBranch.processNextReplacement(nextReplacement, force)

                            if not branching:
                                break

                            nextBranches.append(nextBranch)

                    if branching:
                        currentBranches.clear()
                        currentBranches.update(nextBranches)

                    index += rule.getPatternLength() - 1
                    break

            lastChar = ch

        result = [None] * len(currentBranches)
        index = 0
        for branch in currentBranches:
            branch.finish()
            result[index] = branch.toString()
            index += 1

        return result

    def __cleanup(self, input: str) -> str:
        sb = StringBuilder()
        for ch in input.toCharArray():
            if Character.isWhitespace(ch):
                continue

            ch = Character.toLowerCase(ch)
            if self.__folding and self.__FOLDINGS.containsKey(ch):
                ch = self.__FOLDINGS.get(ch)
            sb.append(ch)
        return sb.toString()

    @staticmethod
    def __stripQuotes(str: str) -> str:
        if str.startswith(DaitchMokotoffSoundex.__DOUBLE_QUOTE):
            str = str[1:]

        if str.endswith(DaitchMokotoffSoundex.__DOUBLE_QUOTE):
            str = str[:-1]

        return str

    @staticmethod
    def __parseRules(
        scanner: typing.Any,
        location: str,
        ruleMapping: typing.Dict[str, typing.List[Rule]],
        asciiFoldings: typing.Dict[str, str],
    ) -> None:
        currentLine: int = 0
        inMultilineComment: bool = False

        while scanner.hasNextLine():
            currentLine += 1
            rawLine: str = scanner.nextLine()
            line: str = rawLine

            if inMultilineComment:
                if line.endswith(DaitchMokotoffSoundex.__MULTILINE_COMMENT_END):
                    inMultilineComment = False
                continue

            if line.startswith(DaitchMokotoffSoundex.__MULTILINE_COMMENT_START):
                inMultilineComment = True
            else:
                cmtI: int = line.index(DaitchMokotoffSoundex.__COMMENT)
                if cmtI >= 0:
                    line = line[:cmtI]

                line = line.strip()

                if line == "":
                    continue  # empty lines can be safely skipped

                if "=" in line:
                    parts: typing.List[str] = line.split("=")
                    if len(parts) != 2:
                        raise ValueError(
                            "Malformed folding statement split into "
                            + str(len(parts))
                            + " parts: "
                            + rawLine
                            + " in "
                            + location
                        )
                    leftCharacter: str = parts[0]
                    rightCharacter: str = parts[1]

                    if len(leftCharacter) != 1 or len(rightCharacter) != 1:
                        raise ValueError(
                            "Malformed folding statement - "
                            + "patterns are not single characters: "
                            + rawLine
                            + " in "
                            + location
                        )

                    asciiFoldings[leftCharacter[0]] = rightCharacter[0]
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
                        pattern: str = DaitchMokotoffSoundex.__stripQuotes(parts[0])
                        replacement1: str = DaitchMokotoffSoundex.__stripQuotes(
                            parts[1]
                        )
                        replacement2: str = DaitchMokotoffSoundex.__stripQuotes(
                            parts[2]
                        )
                        replacement3: str = DaitchMokotoffSoundex.__stripQuotes(
                            parts[3]
                        )

                        r: Rule = Rule(
                            pattern, replacement1, replacement2, replacement3
                        )
                        patternKey: str = r.pattern[0]
                        rules: typing.List[Rule] = ruleMapping.get(patternKey)
                        if rules is None:
                            rules = []
                            ruleMapping[patternKey] = rules
                        rules.append(r)
                    except ValueError as e:
                        raise RuntimeError(
                            "Problem parsing line '"
                            + str(currentLine)
                            + "' in "
                            + location,
                            e,
                        )


DaitchMokotoffSoundex.initialize_fields()

DaitchMokotoffSoundex.run_static_init()
