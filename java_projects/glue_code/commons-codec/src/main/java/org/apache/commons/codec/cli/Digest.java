package org.apache.commons.codec.cli;

import org.apache.commons.codec.ContextInitializer;
import org.graalvm.polyglot.Value;

public class Digest {
  private static Value clz = ContextInitializer.getPythonClass("/cli/Digest.py", "Digest");
  private Value obj;

  public Digest(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // return String.format("%s %s", super.toString(), Arrays.toString(args));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  private void println1(final String prefix, final byte[] digest, final String fileName) {
    //
    // System.out.println(
    // prefix + Hex.encodeHexString0(digest) + (fileName != null ? "  " + fileName : ""));
    //

    obj.invokeMember("println1", prefix, digest, fileName);
  }

  private void println0(final String prefix, final byte[] digest) {
    //
    // println1(prefix, digest, null);
    //

    obj.invokeMember("println0", prefix, digest);
  }

  private Digest(final String[] args) {
    //
    // if (args == null) {
    // throw new IllegalArgumentException("args");
    // }
    // final int argsLength = args.length;
    // if (argsLength == 0) {
    // throw new IllegalArgumentException(
    // String.format(
    // "Usage: java %s [algorithm] [FILE|DIRECTORY|string] ...",
    // Digest.class.getName()));
    // }
    // this.args = args;
    // algorithm = args[0];
    // if (argsLength <= 1) {
    // inputs = null;
    // } else {
    // inputs = new String[argsLength - 1];
    // System.arraycopy(args, 1, inputs, 0, inputs.length);
    // }
    //

    this.obj = clz.invokeMember("__init__", args);
  }
}
