# Imports Begin
from src.main.org.joda.money.Money import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.BigMoney import *
import typing

# Imports End


class Ser(Externalizable):

    # Class Fields Begin
    BIG_MONEY: int = None
    MONEY: int = None
    CURRENCY_UNIT: int = None
    __type: int = None
    __object: typing.Any = None
    # Class Fields End

    # Class Methods Begin
    def readExternal(self, in_: pickle.Unpickler) -> None:
        pass

    def writeExternal(self, out: pickle.Pickler) -> None:
        pass

    def __init__(self, constructorId: int, object: typing.Any, type: int) -> None:
        pass

    def __readResolve(self) -> typing.Any:
        pass

    def __readCurrency(self, in_: pickle.Unpickler) -> CurrencyUnit:
        pass

    def __readBigMoney(self, in_: pickle.Unpickler) -> BigMoney:
        pass

    def __writeCurrency(self, out: pickle.Pickler, obj: CurrencyUnit) -> None:
        pass

    def __writeBigMoney(self, out: pickle.Pickler, obj: BigMoney) -> None:
        pass

    # Class Methods End
