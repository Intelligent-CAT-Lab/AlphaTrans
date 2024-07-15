from __future__ import annotations
import re
from io import StringIO
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
        if not self.__cachedString:
            self.__cachedString = self.__builder
        return self.__cachedString

    def hashCode(self) -> int:
        return hash(self.toString())

    def equals(self, other: typing.Any) -> bool:
        if self is other:
            return True
        if not isinstance(other, Branch):
            return False
        return self.toString() == other.toString()

    def processNextReplacement(self, replacement: str, forceAppend: bool) -> None:

        append = (
            self.__lastReplacement == ""
            or not self.__lastReplacement.endswith(replacement)
            or forceAppend
        )

        if append and len(self.__builder) < MAX_LENGTH:
            self.__builder += replacement
            if len(self.__builder) > MAX_LENGTH:
                self.__builder = self.__builder[:MAX_LENGTH]
            self.__cachedString = ""

        self.__lastReplacement = replacement

    def finish(self) -> None:
        while len(self.__builder) < MAX_LENGTH:
            self.__builder += "0"
            self.__cachedString = None

    def createBranch(self) -> Branch:
        branch = Branch()
        branch.__builder = self.__builder
        branch.__lastReplacement = self.__lastReplacement
        return branch

    def __init__(self) -> None:
        self.__builder = io.StringIO()
        self.__lastReplacement = None
        self.__cachedString = None


class Rule:

    __replacementDefault: typing.List[str] = None

    __replacementBeforeVowel: typing.List[str] = None

    __replacementAtStart: typing.List[str] = None

    __pattern: str = ""

    def toString(self) -> str:
        return "{}=({},{},{})".format(
            self.__pattern,
            str(self.__replacementAtStart),
            str(self.__replacementBeforeVowel),
            str(self.__replacementDefault),
        )

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
        return ch.lower() in ["a", "e", "i", "o", "u"]


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
    def run_static_init():

        try:
            with Resources.getInputStream(
                DaitchMokotoffSoundex.__RESOURCE_FILE
            ) as scanner:
                DaitchMokotoffSoundex.__parseRules(
                    scanner,
                    DaitchMokotoffSoundex.__RESOURCE_FILE,
                    DaitchMokotoffSoundex.__RULES,
                    DaitchMokotoffSoundex.__FOLDINGS,
                )
        except Exception as e:
            print(f"Error in static initializer: {e}")

        for rule in DaitchMokotoffSoundex.__RULES.values():
            rule.sort(key=lambda r: r.getPatternLength(), reverse=True)

    def soundex0(self, source: str) -> str:

        branches = self.__soundex1(source, True)
        sb = ""
        index = 0
        for branch in branches:
            sb += branch
            if index < len(branches) - 1:
                sb += "|"
            index += 1
        return sb

    def encode1(self, source: str) -> str:
        if source is None:
            return None
        return self.__soundex1(source, False)[0]

    def encode0(self, obj: typing.Any) -> typing.Any:

        if not isinstance(obj, str):
            raise EncoderException(
                "Parameter supplied to DaitchMokotoffSoundex encode is not of type"
                + " java.lang.String",
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

        current_branches: typing.Set[Branch] = set()
        current_branches.add(Branch())

        last_char = "\0"
        for index in range(len(input)):
            ch = input[index]

            if ch.isspace():
                continue

            input_context = input[index:]
            rules = self.__RULES.get(ch)
            if rules is None:
                continue

            next_branches: typing.List[Branch] = [] if branching else []

            for rule in rules:
                if rule.matches(input_context):
                    if branching:
                        next_branches.clear()
                    replacements = rule.getReplacements(
                        input_context, last_char == "\0"
                    )
                    branching_required = len(replacements) > 1 and branching

                    for branch in current_branches:
                        for next_replacement in replacements:
                            next_branch = (
                                branch.createBranch() if branching_required else branch
                            )

                            force = (last_char == "m" and ch == "n") or (
                                last_char == "n" and ch == "m"
                            )

                            next_branch.processNextReplacement(next_replacement, force)

                            if not branching:
                                break
                            next_branches.append(next_branch)

                    if branching:
                        current_branches.clear()
                        current_branches.update(next_branches)
                    index += rule.getPatternLength() - 1
                    break

            last_char = ch

        result: typing.List[str] = [None] * len(current_branches)
        index = 0
        for branch in current_branches:
            branch.finish()
            result[index] = branch.toString()
            index += 1

        return result

    def __cleanup(self, input: str) -> str:

        sb = []
        for ch in input:
            if ch.isspace():
                continue

            ch = ch.lower()
            if self.__folding and ch in self.__FOLDINGS:
                ch = self.__FOLDINGS[ch]
            sb.append(ch)
        return "".join(sb)

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

        currentLine = 0
        inMultilineComment = False

        while scanner.hasNextLine():
            currentLine += 1
            rawLine = scanner.nextLine()
            line = rawLine

            if inMultilineComment:
                if line.endswith(DaitchMokotoffSoundex.__MULTILINE_COMMENT_END):
                    inMultilineComment = False
                continue

            if line.startswith(DaitchMokotoffSoundex.__MULTILINE_COMMENT_START):
                inMultilineComment = True
            else:
                cmtI = line.find(DaitchMokotoffSoundex.__COMMENT)
                if cmtI >= 0:
                    line = line[:cmtI]

                line = line.strip()

                if not line:
                    continue

                if "=" in line:
                    parts = line.split("=")
                    if len(parts) != 2:
                        raise ValueError(
                            "Malformed folding statement split into "
                            + str(len(parts))
                            + " parts: "
                            + rawLine
                            + " in "
                            + location
                        )
                    leftCharacter = parts[0]
                    rightCharacter = parts[1]

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
                    parts = line.split()
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
                        pattern = DaitchMokotoffSoundex.__stripQuotes(parts[0])
                        replacement1 = DaitchMokotoffSoundex.__stripQuotes(parts[1])
                        replacement2 = DaitchMokotoffSoundex.__stripQuotes(parts[2])
                        replacement3 = DaitchMokotoffSoundex.__stripQuotes(parts[3])

                        r = Rule(pattern, replacement1, replacement2, replacement3)
                        patternKey = r.pattern[0]
                        rules = ruleMapping.get(patternKey)
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


DaitchMokotoffSoundex.run_static_init()
