package org.apache.commons.graph.visit;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.ExceptionHandler;
import org.apache.commons.graph.IntegrationUtils;
public enum VisitState {
    private static Value clz = ContextInitializer.getPythonClass("/visit/VisitState.py", "VisitState");
    private Value obj;
    public VisitState(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
}
