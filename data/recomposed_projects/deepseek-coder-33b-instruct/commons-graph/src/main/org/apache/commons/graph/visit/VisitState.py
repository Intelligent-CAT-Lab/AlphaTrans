from __future__ import annotations
import io


class VisitState:

    SKIP: VisitState = None
    CONTINUE: VisitState = None
    ABORT: VisitState = None
