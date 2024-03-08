package org.apache.commons.graph.elo;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.ExceptionHandler;
import org.apache.commons.graph.IntegrationUtils;
public enum GameResult {
    private static Value clz = ContextInitializer.getPythonClass("/elo/GameResult.py", "GameResult");
    private Value obj;
    public GameResult(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
}
