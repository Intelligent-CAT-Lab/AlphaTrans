package org.apache.commons.codec;

import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import org.graalvm.polyglot.Value;

public class Charsets {
  @Deprecated public static final Charset UTF_8 = StandardCharsets.UTF_8;
  @Deprecated public static final Charset UTF_16LE = StandardCharsets.UTF_16LE;
  @Deprecated public static final Charset UTF_16BE = StandardCharsets.UTF_16BE;
  @Deprecated public static final Charset UTF_16 = StandardCharsets.UTF_16;
  @Deprecated public static final Charset US_ASCII = StandardCharsets.US_ASCII;
  @Deprecated public static final Charset ISO_8859_1 = StandardCharsets.ISO_8859_1;
  private static Value clz = ContextInitializer.getPythonClass("/Charsets.py", "Charsets");
  private Value obj;

  public Charsets(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public static Charset toCharset1(final String charset) {
    //
    // return charset == null ? Charset.defaultCharset() : Charset.forName(charset);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("toCharset1", charset).as(Charset.class);
  }

  public static Charset toCharset0(final Charset charset) {
    //
    // return charset == null ? Charset.defaultCharset() : charset;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("toCharset0", charset).as(Charset.class);
  }
}
