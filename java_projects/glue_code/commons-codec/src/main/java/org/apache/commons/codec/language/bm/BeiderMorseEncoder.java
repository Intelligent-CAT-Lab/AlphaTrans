package org.apache.commons.codec.language.bm;

import org.apache.commons.codec.ContextInitializer;
import org.apache.commons.codec.EncoderException;
import org.apache.commons.codec.ExceptionHandler;
import org.apache.commons.codec.StringEncoder;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class BeiderMorseEncoder implements StringEncoder {
  private PhoneticEngine engine =
      PhoneticEngine.PhoneticEngine0(NameType.GENERIC, RuleType.APPROX, true);
  private static Value clz =
      ContextInitializer.getPythonClass("/language/bm/BeiderMorseEncoder.py", "BeiderMorseEncoder");
  private Value obj;

  public BeiderMorseEncoder(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String encode(final String source) throws EncoderException {
    try {
      //
      // return encode1(source);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode", source).as(String.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "BeiderMorseEncoder.encode");
    }
  }

  public Object encode(final Object source) throws EncoderException {
    try {
      //
      // return encode0(source);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode", source).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "BeiderMorseEncoder.encode");
    }
  }

  public void setMaxPhonemes(final int maxPhonemes) {
    //
    // this.engine =
    // new PhoneticEngine(
    // this.engine.getNameType(),
    // this.engine.getRuleType(),
    // this.engine.isConcat(),
    // maxPhonemes);
    //

    obj.invokeMember("setMaxPhonemes", maxPhonemes);
  }

  public void setRuleType(final RuleType ruleType) {
    //
    // this.engine =
    // new PhoneticEngine(
    // this.engine.getNameType(),
    // ruleType,
    // this.engine.isConcat(),
    // this.engine.getMaxPhonemes());
    //

    obj.invokeMember("setRuleType", ruleType);
  }

  public void setNameType(final NameType nameType) {
    //
    // this.engine =
    // new PhoneticEngine(
    // nameType,
    // this.engine.getRuleType(),
    // this.engine.isConcat(),
    // this.engine.getMaxPhonemes());
    //

    obj.invokeMember("setNameType", nameType);
  }

  public void setConcat(final boolean concat) {
    //
    // this.engine =
    // new PhoneticEngine(
    // this.engine.getNameType(),
    // this.engine.getRuleType(),
    // concat,
    // this.engine.getMaxPhonemes());
    //

    obj.invokeMember("setConcat", concat);
  }

  public boolean isConcat() {
    //
    // return this.engine.isConcat();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isConcat").as(boolean.class);
  }

  public RuleType getRuleType() {
    //
    // return this.engine.getRuleType();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getRuleType").as(RuleType.class);
  }

  public NameType getNameType() {
    //
    // return this.engine.getNameType();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getNameType").as(NameType.class);
  }

  public String encode1(final String source) throws EncoderException {
    try {
      //
      // if (source == null) {
      // return null;
      // }
      // return this.engine.encode0(source);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode1", source).as(String.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "BeiderMorseEncoder.encode1");
    }
  }

  public Object encode0(final Object source) throws EncoderException {
    try {
      //
      // if (!(source instanceof String)) {
      // throw new EncoderException(
      // "BeiderMorseEncoder encode parameter is not of type String", null);
      // }
      // return encode1((String) source);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode0", source).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "BeiderMorseEncoder.encode0");
    }
  }
}
