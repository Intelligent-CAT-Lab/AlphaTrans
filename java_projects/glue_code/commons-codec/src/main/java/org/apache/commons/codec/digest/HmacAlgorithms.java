package org.apache.commons.codec.digest;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.codec.ContextInitializer;
import org.apache.commons.codec.ExceptionHandler;
import org.apache.commons.codec.IntegrationUtils;
public enum HmacAlgorithms {
    private static Value clz = ContextInitializer.getPythonClass("/digest/HmacAlgorithms.py", "HmacAlgorithms");
    private Value obj;
    public HmacAlgorithms(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public String toString() {
// 
// return name;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("toString").as(String.class);
}
    public String getName() {
// 
// return name;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getName").as(String.class);
}
    HmacAlgorithms(final String algorithm) {
// 
// this.name = algorithm;
// 

this.obj = clz.invokeMember("__init__", algorithm);
}
}
