from __future__ import annotations
import re
import io


class GameResult:

    DRAW: GameResult = None
    WIN: GameResult = None

    @staticmethod
    def initialize_fields() -> None:
        GameResult.DRAW: GameResult = None
        GameResult.WIN: GameResult = None


GameResult.initialize_fields()
