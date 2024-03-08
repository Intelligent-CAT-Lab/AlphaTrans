package org.apache.commons.codec;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.codec.ContextInitializer;
import org.apache.commons.codec.ExceptionHandler;
import org.apache.commons.codec.IntegrationUtils;
public enum CodecPolicy {
    private static Value clz = ContextInitializer.getPythonClass("/CodecPolicy.py", "CodecPolicy");
    private Value obj;
    public CodecPolicy(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
}
