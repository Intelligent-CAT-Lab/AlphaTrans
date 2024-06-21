from __future__ import annotations
import io
from src.test.org.joda.convert.SuperFactorySuper import *


class SuperFactorySub(SuperFactorySuper):

    def __init__(self, amount: int) -> None:

        # Calling the SuperFactorySuper class method
        super().SuperFactorySuper(amount)
