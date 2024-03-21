package org.apache.commons.csv;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.csv.ContextInitializer;
import org.apache.commons.csv.ExceptionHandler;
import org.apache.commons.csv.IntegrationUtils;
public enum QuoteMode {

    /** Quotes all fields. */
    ALL,

    /** Quotes all non-null fields. */
    ALL_NON_NULL,

    /**
     * Quotes fields which contain special characters such as a the field delimiter, quote character
     * or any of the characters in the line separator string.
     */
    MINIMAL,

    /** Quotes all non-numeric fields. */
    NON_NUMERIC,

    /**
     * Never quotes fields. When the delimiter occurs in data, the printer prefixes it with the
     * escape character. If the escape character is not set, format validation throws an exception.
     */
    NONE
    // private static Value clz = ContextInitializer.getPythonClass("/QuoteMode.py", "QuoteMode");
    // private Value obj;
    // public QuoteMode(Value obj) {
    //     this.obj = obj;
    // }
    // public Value getPythonObject() {
    //     return obj;
    // }
}
