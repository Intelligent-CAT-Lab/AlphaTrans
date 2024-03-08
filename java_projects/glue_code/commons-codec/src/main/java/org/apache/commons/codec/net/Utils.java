package org.apache.commons.codec.net;

import org.apache.commons.codec.ContextInitializer;
import org.apache.commons.codec.DecoderException;
import org.apache.commons.codec.ExceptionHandler;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

class Utils {
  private static final int RADIX = 16;
  private static Value clz = ContextInitializer.getPythonClass("/net/Utils.py", "Utils");
  private Value obj;

  public Utils(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  static char hexDigit(final int b) {
    //
    // return Character.toUpperCase(Character.forDigit(b & 0xF, RADIX));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("hexDigit", b).as(char.class);
  }

  static int digit16(final byte b) throws DecoderException {
    try {
      //
      // final int i = Character.digit((char) b, RADIX);
      // if (i == -1) {
      // throw new DecoderException(
      // "Invalid URL encoding: not a valid digit (radix " + RADIX + "): " + b, null);
      // }
      // return i;
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("digit16", b).as(int.class);
    } catch (PolyglotException e) {
      // TODO: Handle DecoderException
      throw (DecoderException) ExceptionHandler.handle(e, "Utils.digit16");
    }
  }
}
