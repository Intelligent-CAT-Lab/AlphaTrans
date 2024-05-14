# Imports Begin
from src.main.org.apache.commons.graph.GraphException import *
import typing

# Imports End


class NotEnoughColorsException(GraphException):

    # Class Fields Begin
    __serialVersionUID: int = None
    # Class Fields End

    # Class Methods Begin
    def __init__(self, colors: typing.Set[typing.Any]) -> None:
        pass

    # Class Methods End
