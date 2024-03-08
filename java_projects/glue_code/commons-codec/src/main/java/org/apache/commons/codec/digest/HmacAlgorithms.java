package org.apache.commons.codec.digest;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.codec.ContextInitializer;
import org.apache.commons.codec.ExceptionHandler;
import org.apache.commons.codec.IntegrationUtils;

public enum HmacAlgorithms {
    HMAC_MD5("HmacMD5"),

    HMAC_SHA_1("HmacSHA1"),

    HMAC_SHA_224("HmacSHA224"),

    HMAC_SHA_256("HmacSHA256"),

    HMAC_SHA_384("HmacSHA384"),

    HMAC_SHA_512("HmacSHA512");

    private Value clz = ContextInitializer.getPythonClass("/digest/HmacAlgorithms.py", "HmacAlgorithms");
    private Value obj;

    HmacAlgorithms(Value obj) {
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
