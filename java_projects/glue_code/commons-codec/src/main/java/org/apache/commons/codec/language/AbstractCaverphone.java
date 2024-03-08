package org.apache.commons.codec.language;

import org.apache.commons.codec.ContextInitializer;
import org.apache.commons.codec.EncoderException;
import org.apache.commons.codec.ExceptionHandler;
import org.apache.commons.codec.StringEncoder;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public abstract class AbstractCaverphone implements StringEncoder {
  private static Value clz =
      ContextInitializer.getPythonClass("/language/AbstractCaverphone.py", "AbstractCaverphone");
  private Value obj;

  public AbstractCaverphone(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public Object encode(final Object source) throws EncoderException {
    try {
      //
      // if (!(source instanceof String)) {
      // throw new EncoderException(
      // "Parameter supplied to Caverphone encode is not of type java.lang.String",
      // null);
      // }
      // return this.encode((String) source);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode", source).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "AbstractCaverphone.encode");
    }
  }

  public boolean isEncodeEqual(final String str1, final String str2) throws EncoderException {
    try {
      //
      // return this.encode(str1).equals(this.encode(str2));
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("isEncodeEqual", str1, str2).as(boolean.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "AbstractCaverphone.isEncodeEqual");
    }
  }

  public AbstractCaverphone() {
    //

    this.obj = clz.invokeMember("__init__");
  }
}
