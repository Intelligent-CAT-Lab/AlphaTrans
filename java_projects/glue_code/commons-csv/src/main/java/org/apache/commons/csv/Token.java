package org.apache.commons.csv;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.csv.ContextInitializer;
import org.apache.commons.csv.ExceptionHandler;
import org.apache.commons.csv.IntegrationUtils;

final class Token {
    final StringBuilder content = new StringBuilder(INITIAL_TOKEN_LENGTH);
    private static final int INITIAL_TOKEN_LENGTH = 50;
    private static Value clz = ContextInitializer.getPythonClass("/Token.py", "Token");
    private Value obj;

    public Token(Value obj) {
        this.obj = obj;
    }

    public Token() {
        this.obj = clz.newInstance();
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
        /** Token has no valid content, i.e. is in its initialized state. */
        INVALID,

        /** Token with content, at beginning or in the middle of a line. */
        TOKEN,

        /** Token (which can have content) when the end of file is reached. */
        EOF,

        /** Token with content when the end of a line is reached. */
        EORECORD,

        /** Token is a comment line. */
        COMMENT
    }
}
