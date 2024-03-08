package org.apache.commons.csv;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.csv.ContextInitializer;
import org.apache.commons.csv.ExceptionHandler;
import org.apache.commons.csv.IntegrationUtils;
public enum QuoteMode {
    private static Value clz = ContextInitializer.getPythonClass("/QuoteMode.py", "QuoteMode");
    private Value obj;
    public QuoteMode(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
}
