from __future__ import annotations
import re
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
        return c.isalnum() or c == "-" or c == "_"
