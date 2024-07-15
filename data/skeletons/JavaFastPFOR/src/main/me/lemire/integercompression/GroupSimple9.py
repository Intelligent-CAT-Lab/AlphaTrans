from __future__ import annotations

# Imports Begin
from src.main.me.lemire.integercompression.Util import *
from src.main.me.lemire.integercompression.SkippableIntegerCODEC import *
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.main.me.lemire.integercompression.IntWrapper import *
import os
import typing
from typing import *
import io

# Imports End


class GroupSimple9(IntegerCODEC, SkippableIntegerCODEC):

    # Class Fields Begin
    __M: typing.List[typing.List[int]] = None
    __bitLength: typing.List[int] = None
    __codeNum: typing.List[int] = None
    # Class Fields End

    # Class Methods Begin
    def headlessUncompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
        num: int,
    ) -> None:
        pass

    def headlessCompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        pass

    def toString(self) -> str:
        pass

    def uncompress0(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        pass

    def compress0(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        pass

    def __decode0(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode1(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode2(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode3(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode4(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode5(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode6(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode7(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode8(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode9(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode10(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode11(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode12(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode13(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode14(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode15(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode16(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode17(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode18(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode19(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode20(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode21(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode22(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode23(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode24(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode25(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode26(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode27(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode28(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode29(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode30(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode31(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode32(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode33(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode34(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode35(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode36(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode37(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode38(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode39(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode40(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode41(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode42(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode43(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode44(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode45(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode46(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode47(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode48(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode49(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode50(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode51(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode52(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode53(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode54(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode55(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode56(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode57(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode58(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode59(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode60(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode61(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode62(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode63(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode64(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode65(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode66(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode67(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode68(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode69(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode70(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode71(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode72(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode73(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode74(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode75(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode76(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode77(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode78(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode79(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __decode80(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        pass

    def __encode80(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode79(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode78(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode77(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode76(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode75(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode74(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode73(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode72(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode71(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode70(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode69(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode68(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode67(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode66(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode65(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode64(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode63(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode62(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode61(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode60(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode59(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode58(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode57(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode56(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode55(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode54(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode53(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode52(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode51(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode50(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode49(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode48(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode47(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode46(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode45(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode44(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode43(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode42(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode41(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode40(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode39(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode38(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode37(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode36(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode35(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode34(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode33(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode32(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode31(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode30(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode29(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode28(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode27(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode26(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode25(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode24(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode23(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode22(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode21(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode20(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode19(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode18(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode17(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode16(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode15(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode14(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode13(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode12(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode11(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode10(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode9(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode8(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode7(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode6(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode5(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode4(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode3(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode2(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode1(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    def __encode0(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        pass

    # Class Methods End
