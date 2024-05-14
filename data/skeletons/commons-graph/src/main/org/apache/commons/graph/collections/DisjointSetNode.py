# Imports Begin
import typing

# Imports End


class DisjointSetNode(Comparable, DisjointSetNode):

    # Class Fields Begin
    __element: typing.Any = None
    __parent: DisjointSetNode = None
    __rank: int = None
    # Class Fields End

    # Class Methods Begin
    def setRank(self, rank: int) -> None:
        pass

    def setParent(self, parent: DisjointSetNode) -> None:
        pass

    def increaseRank(self) -> None:
        pass

    def getRank(self) -> int:
        pass

    def getParent(self) -> "DisjointSetNode":
        pass

    def getElement(self) -> typing.Any:
        pass

    def compareTo(self, o: DisjointSetNode) -> int:
        pass

    def __init__(self, element: typing.Any) -> None:
        pass

    # Class Methods End
