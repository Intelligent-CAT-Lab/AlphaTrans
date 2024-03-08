package org.apache.commons.codec.language.bm;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.codec.ContextInitializer;
import org.apache.commons.codec.ExceptionHandler;
import org.apache.commons.codec.IntegrationUtils;

public enum RuleType {
    APPROX("approx"),
    EXACT("exact"),
    RULES("rules");

    private Value clz = ContextInitializer.getPythonClass("/language/bm/RuleType.py", "RuleType");
    private Value obj;

    RuleType(Value obj) {
        this.obj = obj;
    }

    public Value getPythonObject() {
        return obj;
    }

    public String getName() {
        //
        // return this.name;
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("getName").as(String.class);
    }

    RuleType(final String name) {
        //
        // this.name = name;
        //

        this.obj = clz.invokeMember("__init__", name);
    }
}
