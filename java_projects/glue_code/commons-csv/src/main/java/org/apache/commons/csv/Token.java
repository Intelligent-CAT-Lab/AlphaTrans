package org.apache.commons.csv;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.csv.ContextInitializer;
import org.apache.commons.csv.ExceptionHandler;
import org.apache.commons.csv.IntegrationUtils;
import static org.apache.commons.csv.Token.Type.INVALID;
final class Token {
    final StringBuilder content = new StringBuilder(INITIAL_TOKEN_LENGTH);
    private static final int INITIAL_TOKEN_LENGTH = 50;
    private static Value clz = ContextInitializer.getPythonClass("/Token.py", "Token");
    private Value obj;
    public Token(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public String toString() {
// 
// return type.name() + " [" + content.toString() + "]";
// 


// TODO: Check the type mapping below!
return obj.invokeMember("toString").as(String.class);
}
    void reset() {
// 
// content.setLength(0);
// type = INVALID;
// isReady = false;
// isQuoted = false;
// 

obj.invokeMember("reset");
}
    enum Type {
    private static Value clz = ContextInitializer.getPythonClass("/Token.py", "Type");
    private Value obj;
    public Type(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
}
}
