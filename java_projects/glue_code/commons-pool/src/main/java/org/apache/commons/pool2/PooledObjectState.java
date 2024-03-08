package org.apache.commons.pool;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.pool.ContextInitializer;
import org.apache.commons.pool.ExceptionHandler;
import org.apache.commons.pool.IntegrationUtils;
public enum PooledObjectState {
    private static Value clz = ContextInitializer.getPythonClass("/PooledObjectState.py", "PooledObjectState");
    private Value obj;
    public PooledObjectState(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
}
