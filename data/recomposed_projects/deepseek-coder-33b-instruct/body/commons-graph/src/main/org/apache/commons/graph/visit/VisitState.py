from __future__ import annotations
import re
import io


class VisitState:

    SKIP: VisitState = None

    CONTINUE: VisitState = None

    ABORT: VisitState = None
