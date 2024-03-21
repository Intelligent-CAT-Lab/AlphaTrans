package org.apache.commons.csv;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.csv.ContextInitializer;
import org.apache.commons.csv.ExceptionHandler;
import org.apache.commons.csv.IntegrationUtils;
public enum DuplicateHeaderMode {
    /** Allows all duplicate headers. */
    ALLOW_ALL,

    /** Allows duplicate headers only if they're empty, blank, or null strings. */
    ALLOW_EMPTY,

    /** Disallows duplicate headers entirely. */
    DISALLOW;

    // private static Value clz = ContextInitializer.getPythonClass("/DuplicateHeaderMode.py", "DuplicateHeaderMode");
    // private Value obj;
    // public DuplicateHeaderMode(Value obj) {
    //     this.obj = obj;
    // }
    // public Value getPythonObject() {
    //     return obj;
    // }
}
