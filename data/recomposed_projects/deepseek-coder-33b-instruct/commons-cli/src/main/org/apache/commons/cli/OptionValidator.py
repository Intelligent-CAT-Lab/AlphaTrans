from __future__ import annotations
import io


class OptionValidator:

    @staticmethod
    def validate(option: str) -> str:

        if option is None:
            return None

        if len(option) == 1:
            ch = option[0]

            if not OptionValidator.__isValidOpt(ch):
                raise ValueError("Illegal option name '" + ch + "'")
        else:
            for ch in option:
                if not OptionValidator.__isValidChar(ch):
                    raise ValueError(
                        "The option '"
                        + option
                        + "' contains an illegal "
                        + "character : '"
                        + ch
                        + "'"
                    )
        return option

    @staticmethod
    def __isValidOpt(c: str) -> bool:

        return OptionValidator.__isValidChar(c) or c == "?" or c == "@"

    @staticmethod
    def __isValidChar(c: str) -> bool:

        # Python's str.isidentifier() method is equivalent to Java's Character.isJavaIdentifierPart()
        # It checks if a string is a valid identifier in Python.
        # It returns True if the string is a valid identifier, and False otherwise.
        return c.isidentifier()
